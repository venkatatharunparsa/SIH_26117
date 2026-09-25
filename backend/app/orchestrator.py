"""Workbench conductor (orchestrator) — Session → Grant → Orch → Pack → Gateway.

Desk turns enter here. Orch decides the next step (chat / extract / retrieve /
HITL ask / PPTX draft). Packed prompts leave **only** through gateway.chat_completions.
Fail-closed on missing grant / disabled card.

Conversation context (org / Workbench layer)
--------------------------------------------
No multi-tenant ``org_id`` exists in this demo. Organisation-level context is the
single Workbench boundary ``DEFAULT_ORG_ID``, scoped per task session.

Storage key: ``{DEFAULT_ORG_ID}/{grant_id}`` (implemented as ``_STATE[grant_id]``
with ``OrchState.org_id``). ``grant_id`` is the Workbench session id for the open
task grant. Rolling window = last ``CHAT_HISTORY_WINDOW`` role+content messages
(not N exchanges), packed into Gateway→Ollama on every conversational turn.
"""

from __future__ import annotations

import re
import threading
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import artefacts, cards, gateway, grants, mcp_host, pptx_draft, retrieve, roles, secrets, skills, specialists, word_draft
from .audit import log_event
from .config import ARTIFACTS_DIR, ROOT

_lock = threading.Lock()
# Workbench session store: grant_id -> conductor state (org = DEFAULT_ORG_ID)
_STATE: dict[str, "OrchState"] = {}

# Single-tenant Workbench org boundary until multi-tenant org_id lands.
DEFAULT_ORG_ID = "kwb-workbench"

# Rolling window: last N user/assistant/system transcript messages (not N exchanges).
# Cap applies to OrchState.chat_history and to messages packed for the LLM.
CHAT_HISTORY_WINDOW = 10

# Cursor-like workspace file read (whitelist under repo ROOT only).
FILE_READ_MAX_BYTES = 48 * 1024
_ALLOWED_FILE_EXTS = {".md", ".txt", ".py", ".ts", ".tsx", ".json", ".yaml", ".yml"}
_README_DEFAULTS = (
    "README.md",
    "data/fixtures/README_attach_demo.md",
    "apps/kwb-app/README.md",
)
_READ_INTENT_RE = re.compile(
    r"(?i)\b(?:read|summarize|summarise|open|show|inspect|cat)\b|"
    r"\bwhat(?:'s| is)\s+in\b|"
    r"@"
)
_PATH_TOKEN_RE = re.compile(
    r"(?i)(?:@)?("
    r"(?:[\w./\\-]+[/\\])?[\w.-]+\.(?:md|txt|py|tsx?|json|ya?ml)"
    r"|README(?:\.md)?"
    r")"
)


@dataclass
class OrchState:
    grant_id: str
    task_id: str
    task_type: str
    org_id: str = DEFAULT_ORG_ID
    phase: str = "idle"
    extract: str = ""
    extract_bullets: list[str] = field(default_factory=list)
    query: str = ""
    findings: str = ""
    cites: list[dict[str, Any]] = field(default_factory=list)
    match_notes: list[str] = field(default_factory=list)
    h1_acked: bool = False
    h7_acked: bool = False
    h2_ok: bool = False
    draft_filename: str | None = None
    artefact_version: str | None = None
    draft_format: str = "docx"
    attached_name: str | None = None
    pending_ask: dict[str, Any] | None = None
    # Server SoT (org/workbench): last CHAT_HISTORY_WINDOW messages for Pack→Gateway
    chat_history: list[dict[str, str]] = field(default_factory=list)

    @property
    def context_key(self) -> str:
        """Organisation-scoped session key: {org_id}/{grant_id}."""
        return f"{self.org_id}/{self.grant_id}"


def _get_state(grant_id: str) -> OrchState | None:
    with _lock:
        return _STATE.get(grant_id)


def _put_state(st: OrchState) -> None:
    with _lock:
        _STATE[st.grant_id] = st


def _normalize_msg(role: str | None, content: str | None) -> dict[str, str] | None:
    text = (content or "").strip()
    if not text:
        return None
    r = role or "user"
    if r not in ("user", "assistant", "system"):
        r = "user"
    return {"role": r, "content": text[:4000]}


def _append_chat(st: OrchState, role: str, content: str) -> None:
    """Append one transcript message; keep rolling window of CHAT_HISTORY_WINDOW."""
    msg = _normalize_msg(role, content)
    if not msg:
        return
    st.chat_history.append(msg)
    if len(st.chat_history) > CHAT_HISTORY_WINDOW:
        st.chat_history = st.chat_history[-CHAT_HISTORY_WINDOW:]


def _seed_history_from_client(
    st: OrchState, messages: list[dict[str, str]] | None
) -> None:
    """Bootstrap server history from client only when store is empty (reconnect/demo)."""
    if st.chat_history or not messages:
        return
    for m in messages:
        norm = _normalize_msg(m.get("role"), m.get("content"))
        if norm:
            st.chat_history.append(norm)
    if len(st.chat_history) > CHAT_HISTORY_WINDOW:
        st.chat_history = st.chat_history[-CHAT_HISTORY_WINDOW:]


def _resolve_pack_messages(
    st: OrchState,
    *,
    text: str,
    client_messages: list[dict[str, str]] | None,
) -> list[dict[str, str]]:
    """Build the conversation slice sent to the model (server history + current user)."""
    _seed_history_from_client(st, client_messages)
    hist = list(st.chat_history)
    if text:
        # Drop trailing duplicate of current user line if client already seeded it
        if (
            hist
            and hist[-1].get("role") == "user"
            and hist[-1].get("content") == text
        ):
            pass
        else:
            hist = hist + [{"role": "user", "content": text[:4000]}]
    return hist[-CHAT_HISTORY_WINDOW:]


def _orch_context_block(st: OrchState) -> str:
    """Task context the LLM should see alongside chat (extract / cites / findings)."""
    parts: list[str] = []
    if st.extract:
        parts.append(f"Prior extract summary:\n{st.extract[:800]}")
    if st.match_notes:
        notes = "\n".join(f"- {n}" for n in st.match_notes[:5])
        parts.append(f"Company-doc cite notes:\n{notes}")
    if st.findings and st.findings.strip() and st.findings.strip() != (st.extract or "").strip():
        parts.append(f"Human/findings notes:\n{st.findings[:800]}")
    if st.attached_name:
        parts.append(f"Attached: {st.attached_name}")
    if st.draft_filename:
        parts.append(f"Current DRAFT: {st.draft_filename}")
    return "\n\n".join(parts)


def _detect_file_read_hint(text: str) -> str | None:
    """If user asks to read/summarize a workspace file, return the path hint."""
    raw = (text or "").strip()
    if not raw:
        return None
    if not _READ_INTENT_RE.search(raw):
        return None
    m = _PATH_TOKEN_RE.search(raw)
    if not m:
        return None
    return m.group(1).replace("\\", "/").strip()


def _under_repo(path: Path) -> bool:
    try:
        path.resolve().relative_to(ROOT.resolve())
        return True
    except ValueError:
        return False


def _candidate_rel_paths(hint: str) -> list[str]:
    h = hint.strip().lstrip("./").replace("\\", "/")
    low = h.lower()
    out: list[str] = []
    if low in {"readme", "readme.md"}:
        out.extend(_README_DEFAULTS)
    else:
        out.append(h)
        if low.endswith("readme") and not low.endswith(".md"):
            out.append(f"{h}.md")
        # Bare filename → try common roots
        if "/" not in h:
            out.extend(
                [
                    f"data/fixtures/{h}",
                    f"apps/kwb-app/{h}",
                    f"workspace/knowledge/{h}",
                ]
            )
    # de-dupe preserve order
    seen: set[str] = set()
    uniq: list[str] = []
    for p in out:
        key = p.lower()
        if key not in seen:
            seen.add(key)
            uniq.append(p)
    return uniq


def _resolve_workspace_file(hint: str) -> tuple[Path | None, str | None]:
    """Resolve hint to a readable text file under ROOT. Returns (path, error)."""
    for rel in _candidate_rel_paths(hint):
        cand = (ROOT / rel).resolve()
        if not _under_repo(cand):
            continue
        if not cand.is_file():
            continue
        if cand.suffix.lower() not in _ALLOWED_FILE_EXTS:
            return None, (
                f"File type not allowed for chat read ({cand.suffix or 'no ext'}). "
                f"Allowed: {', '.join(sorted(_ALLOWED_FILE_EXTS))}."
            )
        return cand, None
    allowed = ", ".join(_README_DEFAULTS)
    return None, (
        f"Could not resolve '{hint}' under the repo. "
        f"Try a path like README.md, data/fixtures/…, apps/kwb-app/…, "
        f"workspace/knowledge/… (text: {', '.join(sorted(_ALLOWED_FILE_EXTS))}), "
        f"or attach via ⌁. Known README defaults: {allowed}."
    )


def _load_workspace_file(path: Path) -> tuple[str | None, str | None]:
    """Load UTF-8 text capped at FILE_READ_MAX_BYTES. Returns (text, error)."""
    try:
        data = path.read_bytes()
    except OSError as e:
        return None, f"Failed to read {path.name}: {e}"
    if len(data) > FILE_READ_MAX_BYTES:
        data = data[:FILE_READ_MAX_BYTES]
        truncated = True
    else:
        truncated = False
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("utf-8", errors="replace")
    if truncated:
        text += f"\n\n… [truncated at {FILE_READ_MAX_BYTES} bytes]"
    return text, None


def _detect_mcp_tool(text: str) -> str | None:
    t = (text or "").strip().lower()
    if not t:
        return None
    if t.startswith("mcp:") or t.startswith("/mcp "):
        rest = t.split(":", 1)[-1].strip() if ":" in t else t[5:].strip()
        name = rest.split()[0] if rest else ""
        if name in mcp_host.DEFAULT_ALLOWLIST:
            return name
    if "list skills" in t or t in {"skills", "list_skills"}:
        return "list_skills"
    if "ping knowledge" in t or "ping_knowledge" in t:
        return "ping_knowledge"
    if t in {"time", "utc", "workspace clock", "clock"}:
        return "workspace_clock"
    return None


def _try_workspace_file_read(text: str) -> dict[str, Any] | None:
    """Detect read/summarize intent and load file. None = not a file-read turn."""
    hint = _detect_file_read_hint(text)
    if not hint:
        return None
    path, err = _resolve_workspace_file(hint)
    if err or path is None:
        return {"ok": False, "hint": hint, "error": err or "not_found"}
    body, load_err = _load_workspace_file(path)
    if load_err or body is None:
        return {"ok": False, "hint": hint, "error": load_err or "read_failed"}
    try:
        rel = path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        rel = path.name
    return {
        "ok": True,
        "hint": hint,
        "path": rel,
        "chars": len(body),
        "content": body,
    }


def _assistant_text(gw: dict[str, Any]) -> tuple[str | None, str | None]:
    model = gw.get("model") if isinstance(gw, dict) else None
    body = gw.get("body") if isinstance(gw, dict) else None
    if isinstance(body, dict):
        choices = body.get("choices")
        if isinstance(choices, list) and choices:
            msg = (choices[0] or {}).get("message") or {}
            content = msg.get("content")
            if isinstance(content, str) and content.strip():
                return content.strip(), model if isinstance(model, str) else None
        if isinstance(body.get("content"), str) and body["content"].strip():
            return body["content"].strip(), model if isinstance(model, str) else None
    return None, model if isinstance(model, str) else None


def _pack_chat(
    *,
    task_type: str,
    card_id: str | None,
    messages: list[dict[str, str]],
    phase: str,
    orch_context: str = "",
    file_context: str = "",
    file_path: str | None = None,
) -> list[dict[str, str]]:
    """Minimal trust-delimited pack — role + skills + orch/file context."""
    role = roles.role_for_task(task_type)
    sys = (
        f"{role['prompt']}"
        "You are inside an industrial evidence desk (Knowledge Work Bench).\n"
        "Stay concise. You assist; humans verify. Never claim CERT or plant authority.\n"
        f"role_id={role['id']} task_type={task_type} card={card_id or 'n/a'} phase={phase}\n"
    )
    skill_block = skills.skills_context_block(task_type)
    if skill_block:
        sys += skill_block + "\n"
    if file_context.strip():
        label = file_path or "workspace file"
        sys += (
            f"Workspace file content is loaded ({label}). "
            "Answer from that file body. Do not claim you only have task type, card, or phase — "
            "the file text is in trust:file below.\n"
        )
    if orch_context.strip():
        sys += f"--- trust:orch_context ---\n{orch_context.strip()}\n"
    if file_context.strip():
        sys += (
            f"--- trust:file path={file_path or 'unknown'} ---\n"
            f"{file_context.strip()}\n"
        )
    sys += "--- trust:system ---"
    packed: list[dict[str, str]] = [{"role": "system", "content": sys}]
    for m in messages[-CHAT_HISTORY_WINDOW:]:
        norm = _normalize_msg(m.get("role"), m.get("content"))
        if norm:
            packed.append(norm)
    return packed


def _ask(kind: str, prompt: str, *, preview: str | None = None, action: str) -> dict[str, Any]:
    return {
        "kind": kind,
        "prompt": prompt,
        "context_preview": preview,
        "confirm_action": action,
    }


def _gateway_reply(
    g: grants.Grant,
    packed: list[dict[str, str]],
    *,
    max_tokens: int = 512,
) -> dict[str, Any]:
    model = ""
    if g.model_card:
        card = cards.get_card(g.model_card)
        model = (card or {}).get("model_id") or ""
        # Coding card may bind a 2nd offline-staged tag when present
        if g.model_card == "code-assist":
            second = cards.adopt_second_chat_tag()
            if second:
                model = second
    if not model:
        return {"ok": False, "error": "model_required"}
    allowed = {model}
    return gateway.chat_completions(
        messages=packed,
        model=model,
        allow_base_override=False,
        allowed_model_ids=allowed,
        max_tokens=max_tokens,
        grant_id=g.id,
        phase="gateway_chat",
    )


def _try_vision_scan(
    g: grants.Grant,
    *,
    raw_b64: str,
    filename: str | None,
    content_type: str | None,
) -> dict[str, Any] | None:
    """Optional on-device vision (moondream) for image attaches. Fail → caller uses OCR framework."""
    routed = cards.route_task("vision")
    if not routed.get("ok"):
        return None
    model = str(routed.get("model_id") or "")
    tags = cards.local_chat_tags()
    # Accept moondream or moondream:latest
    if model and not any(model in t or t.startswith(model.split(":")[0]) for t in tags):
        # still try if model string matches a tag loosely
        if not any("moondream" in t.lower() for t in tags):
            return None
        for t in tags:
            if "moondream" in t.lower():
                model = t
                break
    if not model:
        return None

    ct = (content_type or "image/png").split(";")[0].strip() or "image/png"
    data_url = f"data:{ct};base64,{raw_b64}"
    prompt = (
        "You are an on-prem inspection vision helper. "
        "Read this industrial inspection image or scan. "
        "Extract asset tag, measured thickness (mm), location, and defects as short bullets. "
        "If unclear, say so. Confidential synthetic demos are OK."
    )
    messages: list[dict[str, Any]] = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": data_url}},
            ],
        }
    ]
    log_event(
        "orch_phase",
        grant_id=g.id,
        phase="vision_scan",
        label=f"Vision · {model}",
        model=model,
        filename=filename,
    )
    gw = gateway.chat_completions(
        messages=messages,
        model=model,
        allow_base_override=False,
        allowed_model_ids={model, model.split(":")[0], "moondream", "moondream:latest"},
        max_tokens=400,
        timeout_s=180.0,
        grant_id=g.id,
        phase="vision_scan",
    )
    if not gw.get("ok"):
        return None
    text, _ = _assistant_text(gw)
    if not (text or "").strip():
        return None
    return {
        "ok": True,
        "text": text.strip(),
        "engine": "moondream",
        "degraded": False,
        "live_ocr": True,
        "message": f"Vision model {model} (on-device via Gateway)",
        "model_id": model,
        "gateway": gw,
    }


def _ensure_grant(
    *,
    grant_id: str | None,
    task_type: str,
    user_id: str,
) -> tuple[grants.Grant, OrchState, dict[str, Any]]:
    if grant_id:
        g = grants.get(grant_id)
        if not g or not g.active:
            raise PermissionError("grant_inactive")
        st = _get_state(grant_id)
        if st is None:
            st = OrchState(
                grant_id=g.id,
                task_id=g.task_id,
                task_type=task_type,
            )
            _put_state(st)
        card = cards.get_card(g.model_card) if g.model_card else None
        route = {
            "ok": True,
            "task_type": st.task_type,
            "card_id": g.model_card,
            "model_id": (card or {}).get("model_id"),
        }
        return g, st, route

    routed = cards.route_task(task_type)
    if not routed.get("ok"):
        raise ValueError(routed.get("error") or "no_route")
    task_id = uuid.uuid4().hex[:12]
    g = grants.open_grant(
        task_id=task_id,
        user_id=user_id,
        model_card=routed["card_id"],
    )
    st = OrchState(
        grant_id=g.id,
        task_id=task_id,
        task_type=task_type,
    )
    _put_state(st)
    log_event(
        "orch_session_open",
        grant_id=g.id,
        task_id=task_id,
        task_type=task_type,
        card_id=routed["card_id"],
    )
    return g, st, routed


def _run_attach(
    g: grants.Grant,
    st: OrchState,
    text: str,
    filename: str | None,
    *,
    ingest_meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    ext = specialists.extract_specialist(text)
    bullets = ext.get("bullets") or []
    query = ext.get("query") or text[:200]
    cite = specialists.cite_specialist(query, g.shelves, k=5)
    cites = cite.get("cites") or []
    match_notes = cite.get("match_notes") or []
    if not match_notes:
        match_notes = ["NOT FOUND under grant — abstain (fail closed)"]
    findings = "\n".join(f"- {b}" for b in bullets) if bullets else text[:800]

    meta = ingest_meta or {}
    engine = meta.get("engine") or "plain"
    degraded = bool(meta.get("degraded"))
    live_ocr = bool(meta.get("live_ocr"))
    ingest_msg = (meta.get("message") or "").strip()

    st.extract = findings
    st.extract_bullets = bullets
    st.query = query
    st.findings = findings
    st.cites = list(cites)
    st.match_notes = match_notes
    st.attached_name = filename
    st.h1_acked = False
    st.h7_acked = False
    st.phase = "await_confirm_extract"
    log_event(
        "orch_phase",
        grant_id=g.id,
        phase="attach_extract",
        label=f"Extract · {engine}" + (" · live OCR" if live_ocr else ""),
        engine=engine,
        live_ocr=live_ocr,
    )

    if engine == "moondream":
        source_line = "Source: on-device vision model (moondream) via Gateway."
    elif live_ocr:
        source_line = f"Source: live OCR ({engine})."
    elif engine == "pypdf":
        source_line = "Source: PDF text layer (pypdf) — not OCR."
    elif engine == "fixture_stub" or degraded:
        source_line = "Source: fixture stub — NOT live OCR."
    elif engine == "plain":
        source_line = "Source: plain text attach."
    else:
        source_line = f"Source: {engine}."

    ask_prompt = (
        f"Confirm extract before we treat it as input. {source_line} "
        "Enter to accept, or paste a corrected extract."
    )
    ask = _ask(
        "confirm_extract",
        ask_prompt,
        preview=findings[:420],
        action="confirm_extract",
    )
    st.pending_ask = ask
    label = filename or "document"
    _append_chat(st, "user", f"[attach] {label}\n{text[:1200]}")
    assist = (
        f"Extract ready for confirm. {source_line}\n"
        + (f"{ingest_msg}\n" if ingest_msg else "")
        + (findings[:600] if findings else "(empty extract)")
        + "\nCite notes:\n"
        + "\n".join(match_notes[:3])
    )
    _append_chat(st, "assistant", assist)
    _put_state(st)
    log_event(
        "orch_attach_extract",
        grant_id=g.id,
        filename=filename,
        n_bullets=len(bullets),
        n_cites=len(cites),
        verdict=cite.get("verdict"),
        history_len=len(st.chat_history),
        ingest_engine=engine,
        ingest_degraded=degraded,
        live_ocr=live_ocr,
    )
    return {
        "tools": [
            {**ext},
            {**cite},
            {
                "name": "attach_extract",
                "ok": True,
                "extract_bullets": bullets,
                "query": query,
                "cites": cites,
                "match_notes": match_notes,
                "verdict": cite.get("verdict"),
                "ingest_engine": engine,
                "ingest_degraded": degraded,
                "live_ocr": live_ocr,
                "ingest_message": ingest_msg or None,
            }
        ],
        "ask": ask,
        "extract_bullets": bullets,
        "match_notes": match_notes,
        "cites": cites,
        "query": query,
        "extract_text": findings,
        "history_len": len(st.chat_history),
        "ingest_engine": engine,
        "ingest_degraded": degraded,
        "live_ocr": live_ocr,
        "ingest_message": ingest_msg or None,
    }


def _confirm_extract(g: grants.Grant, st: OrchState, correction: str | None) -> dict[str, Any]:
    if correction and correction.strip():
        st.extract = correction.strip()
        st.extract_bullets = pptx_draft.extract_key_points(st.extract)
        st.findings = st.extract
        st.query = pptx_draft.build_retrieve_query(st.extract, st.extract_bullets)

    out = artefacts.ack_h1(g.id, st.extract, True)
    if not out.get("ok"):
        return {"ok": False, "error": out.get("error") or "h1_failed"}
    st.h1_acked = True

    hit = retrieve.retrieve(st.query or st.extract[:200], shelves=g.shelves, k=5)
    cites = hit.get("cites") or []
    st.cites = list(cites)
    st.match_notes = [f"{c.get('path')}: {c.get('snippet')}" for c in cites[:5]] or [
        "NOT FOUND under grant — abstain (fail closed)"
    ]
    st.phase = "await_review_cites"
    ask = _ask(
        "review_cites",
        "Review citations vs company docs. Enter to LLM-polish then write DRAFT Word, or type notes for findings.",
        preview="\n".join(st.match_notes)[:420],
        action="confirm_cites",
    )
    st.pending_ask = ask
    _append_chat(
        st,
        "user",
        correction.strip() if correction and correction.strip() else "[confirmed extract]",
    )
    _append_chat(
        st,
        "assistant",
        "Extract confirmed. Company-doc cites for review:\n"
        + "\n".join(st.match_notes[:5]),
    )
    _put_state(st)
    return {
        "tools": [
            {"name": "h1_confirm", "ok": True, **out},
            {
                "name": "retrieve",
                "ok": True,
                "cites": cites,
                "verdict": hit.get("verdict"),
                "query": st.query,
            },
        ],
        "ask": ask,
        "cites": cites,
        "match_notes": st.match_notes,
        "history_len": len(st.chat_history),
    }


def _confirm_cites(g: grants.Grant, st: OrchState, notes: str | None) -> dict[str, Any]:
    """Cite confirm → Gateway LLM polish → proper Word DRAFT (.docx)."""
    if notes and notes.strip():
        st.findings = notes.strip()

    h7 = artefacts.ack_h7(g.id)
    st.h7_acked = True

    cite_lines = [f"{c.get('path')}: {c.get('snippet')}" for c in st.cites]
    sec = secrets.scan_text(st.findings)
    if not sec.get("ok"):
        return {"ok": False, **sec}

    routed_model = None
    if g.model_card:
        card = cards.get_card(g.model_card)
        routed_model = (card or {}).get("model_id")

    bullets = st.extract_bullets or pptx_draft.extract_key_points(st.findings)
    if st.query:
        hit = retrieve.retrieve(st.query, shelves=g.shelves, k=5)
        cite_lines = [f"{c['path']}: {c['snippet']}" for c in hit.get("cites") or []]
        st.cites = list(hit.get("cites") or [])

    if cite_lines and not artefacts.h7_acked(g.id):
        return {"ok": False, "error": "h7_required"}

    # LLM polish via Gateway (never invent cites; fail closed on gateway deny)
    log_event(
        "orch_phase",
        grant_id=g.id,
        phase="word_polish",
        label="Word polish via Gateway",
    )
    polish_msgs = word_draft.polish_prompt(
        extract=st.findings or st.extract or "",
        cites=cite_lines,
        task_type=st.task_type or g.task_type or "inspection",
    )
    gw = _gateway_reply(g, polish_msgs, max_tokens=900)
    if not gw.get("ok"):
        return {
            "ok": False,
            "error": gw.get("error") or "polish_gateway_failed",
            "gateway": gw,
            "message": "LLM polish via Gateway failed — Word DRAFT not written",
        }
    polish_text, _model = _assistant_text(gw)
    if not polish_text:
        return {
            "ok": False,
            "error": "polish_empty",
            "gateway": gw,
            "message": "LLM polish returned empty — Word DRAFT not written",
        }
    fields = word_draft.parse_polish_fields(polish_text)
    title = (fields.get("title") or "Inspection recommendation note (DRAFT)").strip()
    findings_body = (fields.get("findings") or st.findings or st.extract or "").strip()
    decision = (fields.get("decision") or "").strip()
    recommendation = (fields.get("recommendation") or "").strip()

    sec2 = secrets.scan_text(
        "\n".join(
            [
                title,
                decision,
                findings_body,
                recommendation,
                fields.get("actions") or "",
            ]
        )
    )
    if not sec2.get("ok"):
        return {"ok": False, **sec2}

    ver = artefacts.fingerprint(
        title,
        findings_body,
        "|".join(cite_lines),
        "docx",
        decision,
        recommendation,
        *bullets[:8],
    )
    draft = word_draft.write_inspection_draft(
        title=title,
        findings=findings_body,
        cites=cite_lines,
        model_id=routed_model,
        task_id=g.task_id,
        artefact_version=ver,
        grant_id=g.id,
        card_id=g.model_card,
        decision=decision or None,
        asset_id=fields.get("asset_id") or None,
        location=fields.get("location") or None,
        recommendation=recommendation or None,
        actions=fields.get("actions") or None,
        restrictions=fields.get("restrictions") or None,
        monitoring=fields.get("monitoring") or None,
        polished=True,
    )
    artefacts.register_draft(
        filename=draft["filename"],
        grant_id=g.id,
        artefact_version=ver,
        findings=findings_body,
        title=title,
    )
    st.findings = findings_body
    st.draft_filename = draft["filename"]
    st.artefact_version = ver
    st.draft_format = "docx"
    st.h2_ok = False
    st.phase = "await_self_check"
    ask = _ask(
        "self_check_draft",
        f"Self-check Word DRAFT ({draft['filename']}) before export leave. Enter to confirm, or type corrections.",
        preview=draft["filename"],
        action="confirm_self_check",
    )
    st.pending_ask = ask
    _append_chat(
        st,
        "user",
        notes.strip() if notes and notes.strip() else "[confirmed cites → LLM polish → Word DRAFT]",
    )
    _append_chat(
        st,
        "assistant",
        f"LLM-polished Word DRAFT ready: {draft['filename']}. Self-check before export leave.",
    )
    _append_chat(
        st,
        "system",
        f"polish_preview:\n{polish_text[:1200]}",
    )
    _put_state(st)
    log_event(
        "orch_word_draft",
        grant_id=g.id,
        filename=draft["filename"],
        artefact_version=ver,
        polished=True,
    )
    return {
        "tools": [
            {"name": "h7_ack", "ok": True, **h7},
            {
                "name": "llm_polish",
                "ok": True,
                "model": routed_model,
                "fields": {k: v for k, v in fields.items() if v},
            },
            {"name": "word_draft", "ok": True, **draft, "cites": cite_lines},
        ],
        "ask": ask,
        "draft": {
            "filename": draft["filename"],
            "path": draft["path"],
            "artefact_version": ver,
            "format": "docx",
            "polished": True,
            "download": f"/artifacts/{draft['filename']}?grant_id={g.id}",
        },
        "polish": {"fields": fields, "preview": polish_text[:800]},
        "history_len": len(st.chat_history),
    }


def _confirm_self_check(g: grants.Grant, st: OrchState, correction: str | None) -> dict[str, Any]:
    if correction and correction.strip() and st.draft_filename:
        st.findings = correction.strip()
        artefacts.mark_edit(
            st.draft_filename, st.findings, "Inspection recommendation note (DRAFT)"
        )
        return _confirm_cites(g, st, None)

    if not st.draft_filename or not st.artefact_version:
        return {"ok": False, "error": "draft_missing"}
    out = artefacts.ack_h2(st.draft_filename, st.artefact_version)
    if not out.get("ok"):
        return {"ok": False, **out}
    st.h2_ok = True
    st.phase = "await_export"
    ask = _ask(
        "confirm_export",
        "Export leave — soft-copy DRAFT (not CERT). Enter to export, or type cancel.",
        action="confirm_export",
    )
    st.pending_ask = ask
    _append_chat(
        st,
        "user",
        correction.strip()
        if correction and correction.strip()
        else "[self-check confirmed]",
    )
    _append_chat(
        st,
        "assistant",
        f"Self-check OK on {st.draft_filename}. Ready for export leave (DRAFT, not CERT).",
    )
    _put_state(st)
    return {
        "tools": [{"name": "h2_ack", "ok": True, **out}],
        "ask": ask,
        "history_len": len(st.chat_history),
    }


def _confirm_export(g: grants.Grant, st: OrchState) -> dict[str, Any]:
    if not st.draft_filename:
        return {"ok": False, "error": "draft_missing"}
    name = st.draft_filename
    path = ARTIFACTS_DIR / name
    if not path.is_file():
        return {"ok": False, "error": "draft_not_found"}

    fresh, meta = artefacts.h2_fresh(name)
    if not fresh:
        return {"ok": False, "error": "h2_stale", "meta": meta}

    sb = artefacts.export_sandbox_gate(g.id)
    if sb is not None and not sb.get("ok"):
        return {"ok": False, **sb}

    suffix = path.suffix.lower()
    if suffix == ".docx":
        body_text = word_draft.extract_docx_text(path)
    elif suffix == ".pptx":
        body_text = pptx_draft.extract_pptx_text(path)
    else:
        return {"ok": False, "error": "unsupported_type"}

    sec = secrets.scan_text(body_text + "\n" + name)
    if not sec.get("ok"):
        return {"ok": False, **sec}

    revoked = grants.revoke(g.id)
    st.phase = "done"
    st.pending_ask = None
    _append_chat(st, "user", "[export leave]")
    _append_chat(
        st,
        "assistant",
        f"Export leave complete for {name}. Grant revoked; shelf closed.",
    )
    _put_state(st)
    log_event(
        "export_leave",
        grant_id=g.id,
        path=str(path),
        h2_acked=True,
        artefact_version=st.artefact_version,
        format=suffix.lstrip("."),
        grant_revoked=revoked,
        history_len=len(st.chat_history),
    )
    return {
        "tools": [
            {
                "name": "export",
                "ok": True,
                "filename": name,
                "grant_revoked": revoked,
                "downloads": {"draft": f"/artifacts/{name}?grant_id={g.id}"},
            }
        ],
        "draft": {
            "filename": name,
            "artefact_version": st.artefact_version,
            "format": suffix.lstrip("."),
            "download": f"/artifacts/{name}?grant_id={g.id}",
        },
        "leave_ready": True,
        "grant_revoked": revoked,
        "history_len": len(st.chat_history),
    }


_AFFIRM = frozenset(
    {"", "y", "yes", "ok", "okay", "confirm", "continue", "proceed", "lgtm", "ack"}
)


def turn(
    *,
    grant_id: str | None = None,
    task_type: str = "inspection",
    user_id: str = "kwb-desktop",
    message: str | None = None,
    messages: list[dict[str, str]] | None = None,
    attach_text: str | None = None,
    attach_filename: str | None = None,
    attach_b64: str | None = None,
    attach_content_type: str | None = None,
    intent: str = "auto",
) -> dict[str, Any]:
    """Single desk entry: Grant → Orch decides → Pack→Gateway when model needed."""
    try:
        g, st, route = _ensure_grant(
            grant_id=grant_id, task_type=task_type, user_id=user_id
        )
    except PermissionError:
        return {"ok": False, "error": "grant_inactive"}
    except ValueError as e:
        return {"ok": False, "error": str(e)}

    text = (message or "").strip()
    intent_l = (intent or "auto").lower()

    log_event(
        "orch_phase",
        grant_id=g.id,
        phase="turn_start",
        label=f"Orch turn · {intent_l or 'auto'} · card {g.model_card or '?'}",
        intent=intent_l,
        task_type=task_type,
        model_id=(route or {}).get("model_id"),
    )

    result: dict[str, Any] = {
        "ok": True,
        "grant_id": g.id,
        "task_id": st.task_id,
        "route": route,
        "phase": st.phase,
        "orchestrator": True,
    }

    if intent_l == "cancel" or text.lower() in {"cancel", "reject", "no", "stop"}:
        if st.pending_ask:
            st.pending_ask = None
            _put_state(st)
            result["phase"] = st.phase
            result["note"] = "Ask cancelled"
            return result

    if attach_b64 is not None or attach_text is not None or intent_l == "attach":
        err = grants.require_active(g.id, "retrieve")
        if err:
            return {**result, "ok": False, **err}

        ingest_meta: dict[str, Any] | None = None
        body: str | None = None

        if attach_b64 is not None and str(attach_b64).strip():
            import base64

            from . import ocr_extract

            b64_str = str(attach_b64).strip()
            try:
                raw = base64.b64decode(b64_str, validate=False)
            except Exception:
                return {
                    **result,
                    "ok": False,
                    "error": "attach_b64_invalid",
                    "message": "attach_b64 is not valid base64",
                }

            suf = ocr_extract._suffix(attach_filename, attach_content_type)
            ct_l = (attach_content_type or "").lower()
            is_image = suf in ocr_extract.IMAGE_SUFFIXES or ct_l.startswith("image/")

            body = None
            ingest_meta = None
            if is_image:
                vis = _try_vision_scan(
                    g,
                    raw_b64=b64_str,
                    filename=attach_filename,
                    content_type=attach_content_type,
                )
                if vis and vis.get("ok") and (vis.get("text") or "").strip():
                    ingest_meta = vis
                    body = str(vis.get("text") or "").strip()

            if body is None:
                ing = ocr_extract.ingest_bytes(
                    raw,
                    filename=attach_filename,
                    content_type=attach_content_type,
                    allow_fixture_fallback=True,
                )
                ingest_meta = ing
                if not ing.get("ok"):
                    return {
                        **result,
                        "ok": False,
                        "error": ing.get("error") or "ingest_failed",
                        "message": ing.get("message"),
                        "ingest_engine": ing.get("engine"),
                        "ingest_degraded": ing.get("degraded"),
                        "live_ocr": ing.get("live_ocr"),
                    }
                body = (ing.get("text") or "").strip()
                if not body:
                    return {
                        **result,
                        "ok": False,
                        "error": "empty_attach",
                        "message": ing.get("message") or "Ingest produced empty text",
                        "ingest_engine": ing.get("engine"),
                    }
        else:
            body = attach_text if attach_text is not None else text
            if not (body or "").strip():
                return {**result, "ok": False, "error": "empty_attach"}
            ingest_meta = {
                "engine": "plain",
                "degraded": False,
                "live_ocr": False,
                "message": "Plain text attach (no OCR)",
            }

        out = _run_attach(
            g, st, body.strip(), attach_filename, ingest_meta=ingest_meta
        )
        result.update(out)
        result["phase"] = st.phase
        result["attached_name"] = attach_filename
        return result

    pending = st.pending_ask
    affirming = intent_l in {"confirm", "continue"} or text.lower() in _AFFIRM

    if pending and (intent_l in {"confirm", "continue"} or affirming or text):
        action = pending.get("confirm_action") or ""
        correction: str | None
        if affirming and (
            not text
            or text.lower() in _AFFIRM
            or intent_l in {"confirm", "continue"}
        ):
            correction = None
        else:
            correction = text or None

        err = grants.require_active(g.id, "retrieve")
        if err:
            return {**result, "ok": False, **err}

        if action == "confirm_extract":
            out = _confirm_extract(g, st, correction)
        elif action == "confirm_cites":
            out = _confirm_cites(g, st, correction)
        elif action == "confirm_self_check":
            out = _confirm_self_check(g, st, correction)
        elif action == "confirm_export":
            out = _confirm_export(g, st)
        else:
            out = {"ok": False, "error": "unknown_ask_action", "action": action}

        if out.get("ok") is False and out.get("error"):
            return {**result, **out, "ok": False}
        result.update(out)
        result["phase"] = st.phase
        return result

    if intent_l == "continue" and not pending:
        if not st.h1_acked and st.extract:
            st.phase = "await_confirm_extract"
            ask = _ask(
                "confirm_extract",
                "Confirm extract before we treat it as input. Enter to accept, or paste a corrected extract.",
                preview=st.extract[:420],
                action="confirm_extract",
            )
            st.pending_ask = ask
            _put_state(st)
            result["ask"] = ask
            result["phase"] = st.phase
            return result
        if st.h1_acked and not st.h7_acked:
            out = _confirm_extract(g, st, None)
            result.update(out)
            result["phase"] = st.phase
            return result
        if st.h7_acked and not st.draft_filename:
            out = _confirm_cites(g, st, None)
            result.update(out)
            result["phase"] = st.phase
            return result
        if st.draft_filename and not st.h2_ok:
            st.phase = "await_self_check"
            ask = _ask(
                "self_check_draft",
                f"Self-check DRAFT ({st.draft_filename}) before export leave. Enter to confirm.",
                preview=st.draft_filename,
                action="confirm_self_check",
            )
            st.pending_ask = ask
            _put_state(st)
            result["ask"] = ask
            return result
        if st.h2_ok and st.phase != "done":
            st.phase = "await_export"
            ask = _ask(
                "confirm_export",
                "Export leave — soft-copy DRAFT (not CERT). Enter to export, or type cancel.",
                action="confirm_export",
            )
            st.pending_ask = ask
            _put_state(st)
            result["ask"] = ask
            return result

    # Free-text chat — orchestrated Pack → Gateway (O3 spine)
    if not text and not (messages or []):
        result["note"] = "empty_turn"
        result["phase"] = st.phase
        result["history_len"] = len(st.chat_history)
        result["context_key"] = st.context_key
        return result

    err = grants.require_active(g.id, "gateway")
    if err:
        return {**result, "ok": False, **err}

    # Cursor-like: read/summarize workspace file when user asks (whitelist under ROOT)
    file_hit = _try_workspace_file_read(text) if text else None
    file_context = ""
    file_path: str | None = None
    if file_hit is not None and not file_hit.get("ok"):
        msg = file_hit.get("error") or "File not available for chat read."
        _append_chat(st, "user", text)
        _append_chat(st, "assistant", msg)
        _put_state(st)
        log_event(
            "orch_file_read_miss",
            grant_id=g.id,
            hint=file_hit.get("hint"),
            error=file_hit.get("error"),
        )
        result["phase"] = st.phase
        result["assistant"] = {"text": msg, "model": None}
        result["tools"] = [
            {
                "name": "read_workspace_file",
                "ok": False,
                "hint": file_hit.get("hint"),
                "error": file_hit.get("error"),
            }
        ]
        result["history_len"] = len(st.chat_history)
        result["context_key"] = st.context_key
        result["history_window"] = CHAT_HISTORY_WINDOW
        return result

    if file_hit and file_hit.get("ok"):
        file_context = str(file_hit.get("content") or "")
        file_path = str(file_hit.get("path") or "")
        # History keeps a short read marker + snippet (full body goes in pack system)
        snippet = file_context[:2800]
        _append_chat(
            st,
            "system",
            f"[read_file] {file_path} ({file_hit.get('chars')} chars)\n{snippet}",
        )

    # In-process MCP tools (allowlist) — before LLM when user asks for tools/skills
    mcp_tool = _detect_mcp_tool(text)
    if mcp_tool:
        tool_out = mcp_host.call_tool(mcp_tool, {"text": text}, grant_id=g.id)
        msg = (
            f"MCP tool `{mcp_tool}`: {tool_out}"
            if tool_out.get("ok")
            else f"MCP tool failed: {tool_out.get('error') or tool_out}"
        )
        _append_chat(st, "user", text)
        _append_chat(st, "assistant", msg[:2000])
        _put_state(st)
        result["phase"] = st.phase
        result["assistant"] = {"text": msg[:2000], "model": None}
        result["tools"] = [{"name": "mcp_host", "ok": bool(tool_out.get("ok")), **tool_out}]
        result["history_len"] = len(st.chat_history)
        result["context_key"] = st.context_key
        result["history_window"] = CHAT_HISTORY_WINDOW
        result["role"] = roles.role_for_task(st.task_type)
        result["skills"] = [s["id"] for s in skills.select_skills_for_task(st.task_type)]
        result["skill_plan"] = skills.recommend_plan(
            message=text or "",
            filename="",
            task_type=st.task_type,
        )
        return result

    # Server SoT: org/workbench rolling history (≤10), not bare latest line
    hist = _resolve_pack_messages(st, text=text, client_messages=messages)
    packed = _pack_chat(
        task_type=st.task_type,
        card_id=g.model_card,
        messages=hist,
        phase=st.phase,
        orch_context=_orch_context_block(st),
        file_context=file_context,
        file_path=file_path,
    )
    packed_roles = [m.get("role") for m in packed]
    gw = _gateway_reply(g, packed)
    if isinstance(gw, dict) and gw.get("ok") is False and gw.get("error") == "gateway_deny":
        log_event("orch_gateway_deny", grant_id=g.id, reason=gw.get("reason"))
        return {**result, "ok": False, "error": "gateway_deny", "gateway": gw}

    reply, model = _assistant_text(gw)
    # Persist this turn into workbench session store (attach path also appends; never wipe)
    if text:
        last = st.chat_history[-1] if st.chat_history else None
        if not (
            last
            and last.get("role") == "user"
            and last.get("content") == text[:4000]
        ):
            _append_chat(st, "user", text)
    if reply:
        _append_chat(st, "assistant", reply)

    log_event(
        "orch_chat",
        grant_id=g.id,
        org_id=st.org_id,
        context_key=st.context_key,
        model=model,
        has_reply=bool(reply),
        history_len=len(st.chat_history),
        packed_msg_count=max(0, len(packed) - 1),  # exclude system
        packed_roles=packed_roles,
        file_path=file_path,
    )
    result["phase"] = st.phase
    tools: list[dict[str, Any]] = []
    if file_path:
        tools.append(
            {
                "name": "read_workspace_file",
                "ok": True,
                "path": file_path,
                "chars": len(file_context),
            }
        )
    tools.append(
        {
            "name": "pack_gateway_chat",
            "ok": bool(gw.get("ok")),
            "model": model,
            "packed_msg_count": max(0, len(packed) - 1),
            "history_window": CHAT_HISTORY_WINDOW,
            "file_in_pack": bool(file_context),
            "role_id": roles.role_for_task(st.task_type)["id"],
            "skills_in_pack": bool(skills.skills_context_block(st.task_type)),
        }
    )
    result["tools"] = tools
    result["role"] = roles.role_for_task(st.task_type)
    result["skills"] = [s["id"] for s in skills.select_skills_for_task(st.task_type)]
    result["skill_plan"] = skills.recommend_plan(
        message=text or "",
        filename=file_path or "",
        task_type=st.task_type,
    )
    result["gateway"] = {
        "ok": gw.get("ok"),
        "model": model,
        "status": gw.get("status"),
        "base_url": gw.get("base_url"),
        "inference_host": gw.get("inference_host"),
        "inference_label": gw.get("inference_label"),
    }
    result["history_len"] = len(st.chat_history)
    result["context_key"] = st.context_key
    result["history_window"] = CHAT_HISTORY_WINDOW
    result["packed_preview"] = [
        {"role": m.get("role"), "chars": len(m.get("content") or "")}
        for m in packed
    ]
    if file_path:
        result["file_read"] = {"path": file_path, "chars": len(file_context)}
    if reply:
        result["assistant"] = {"text": reply, "model": model}
    else:
        result["assistant"] = None
        result["note"] = "no_assistant_text"
        if gw.get("ok") is False:
            result["gateway_error"] = gw.get("error") or gw.get("detail")
    _put_state(st)
    return result
