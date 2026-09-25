"""Knowledge Work Bench — FastAPI entry (demo spine · post REAL red-team).

HITL gates (H1/H2/H9) follow an interrupt/resume *pattern* documented in
KWB/from_langgraph_web — implemented here as explicit endpoints, not LangGraph.
"""

from __future__ import annotations

import hashlib
import io
import json
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import (
    artefacts,
    cards,
    gateway,
    grants,
    mcp_mock,
    monitor_a,
    ocr_extract,
    orchestrator,
    pptx_draft,
    retrieve,
    sandbox,
    secrets,
    word_draft,
)
from .audit import log_event, recent, subscribe, unsubscribe, verify_chain
from .config import ARTIFACTS_DIR, ROOT, TEMPLATES_DIR, ensure_dirs, get_settings, load_yaml

_ALLOWED_ARTIFACT_SUFFIXES = {".docx", ".pptx", ".json"}
_DOCX_MEDIA = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
_PPTX_MEDIA = (
    "application/vnd.openxmlformats-officedocument.presentationml.presentation"
)


def _safe_artifact_path(filename: str) -> Path:
    """Basename-only resolve under ARTIFACTS_DIR (path-traversal safe)."""
    name = Path(filename).name
    if not name or name in (".", ".."):
        raise HTTPException(
            status_code=400,
            detail={"error": "invalid_filename", "filename": filename},
        )
    root = ARTIFACTS_DIR.resolve()
    path = (ARTIFACTS_DIR / name).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail={"error": "path_traversal", "filename": name},
        ) from exc
    return path


def _newest_monitor_a_pack() -> tuple[Path | None, dict | None]:
    """Best-effort latest Monitor A evidence pack under artefacts dir."""
    packs = sorted(
        ARTIFACTS_DIR.glob("monitor-a-*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not packs:
        return None, None
    path = packs[0]
    try:
        raw = path.read_bytes()
        data = json.loads(raw.decode("utf-8"))
        sha = data.get("sha256") or hashlib.sha256(raw).hexdigest()
        return path, {"filename": path.name, "sha256": sha, "path": str(path)}
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return path, {"filename": path.name, "sha256": None, "path": str(path)}

ensure_dirs()
grants.init_db()
settings = get_settings()
DESK_DIR = ROOT / "desk"

app = FastAPI(
    title="Knowledge Work Bench",
    description="Offline industrial knowledge workbench — demo REAL spine (assist→export).",
    version="0.5.0",
)

# Local demo UI only — no file:// null origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8080",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://localhost:5173",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


class CalcRequest(BaseModel):
    expression: str = Field(..., examples=["(12.5 + 7.5) * 2"])
    grant_id: str


class PythonRequest(BaseModel):
    source: str
    grant_id: str
    prefer_docker: bool = False
    timeout_s: float | None = None


class ChatRequest(BaseModel):
    messages: list[dict[str, str]]
    grant_id: str
    model: str | None = None
    # Ignored when grant present — settings.llm_base_url only (red-team fix)


class OrchTurnRequest(BaseModel):
    """Desk → Session/Grant → Orchestrator (Pack→Gateway for model calls)."""

    grant_id: str | None = None
    task_type: str = "inspection"
    user_id: str = "kwb-desktop"
    message: str | None = None
    messages: list[dict[str, str]] | None = None
    attach_text: str | None = None
    attach_filename: str | None = None
    # Binary attach (png/jpg/pdf) — base64; orch runs pypdf / Tesseract ingest
    attach_b64: str | None = None
    attach_content_type: str | None = None
    intent: str = "auto"  # auto | message | attach | confirm | continue | cancel


class StartTaskRequest(BaseModel):
    task_type: str = Field(..., examples=["inspection", "coding"])
    user_id: str = "demo-operator"
    task_id: str | None = None


class RetrieveRequest(BaseModel):
    grant_id: str
    query: str
    k: int = 5


class InspectDraftRequest(BaseModel):
    grant_id: str
    title: str = "Inspection note (DRAFT)"
    findings: str
    query_for_cites: str | None = None
    # Client flag ignored for gate — server artefacts.h7_acked is SoT (M6)
    h7_acked: bool = False


class AttachExtractRequest(BaseModel):
    grant_id: str
    text: str | None = None
    filename: str | None = None
    # Optional binary ingest (same engines as /orch/turn attach_b64)
    file_b64: str | None = None
    content_type: str | None = None
    k: int = 5
    allow_fixture_fallback: bool = True


class PptxDraftRequest(BaseModel):
    grant_id: str
    title: str = "Integrity briefing (DRAFT)"
    findings: str
    bullets: list[str] | None = None
    query_for_cites: str | None = None
    template: str = "kwb_brief"
    h7_acked: bool = False


class H7AckRequest(BaseModel):
    grant_id: str


class ExportRequest(BaseModel):
    grant_id: str
    draft_filename: str
    h2_acked: bool = False
    artefact_version: str | None = None


class ExportCheckRequest(BaseModel):
    text: str


class RevokeRequest(BaseModel):
    grant_id: str


class H1ConfirmRequest(BaseModel):
    grant_id: str
    extract_text: str
    h1_acked: bool = False


class H2AckRequest(BaseModel):
    grant_id: str
    draft_filename: str
    artefact_version: str


class DraftEditRequest(BaseModel):
    grant_id: str
    draft_filename: str
    findings: str
    title: str | None = None


class H9AckRequest(BaseModel):
    grant_id: str
    accept: bool = True


class McpEchoRequest(BaseModel):
    text: str = "ping"


@app.on_event("startup")
def _startup() -> None:
    ensure_dirs()
    grants.init_db()
    # Seed PPTX templates once if missing (demo path)
    if not (TEMPLATES_DIR / "kwb_brief.pptx").is_file():
        try:
            pptx_draft.write_sample_templates()
        except Exception as exc:  # noqa: BLE001 — demo seed only
            log_event("pptx_templates_seed_failed", error=str(exc)[:200])
    log_event("app_start", bind=f"{settings.bind_host}:{settings.bind_port}")


@app.get("/")
def root() -> dict:
    """Primary product is Electron desk — HTML /desk/ is legacy only."""
    return {
        "ok": True,
        "product": "Knowledge Work Bench",
        "primary_desk": "apps/kwb-app (Electron) — npm run electron:dev",
        "api_base": f"http://{settings.bind_host}:{settings.bind_port}",
        "health": "/health",
        "legacy_html_desk": "/desk/",
        "rejected_web_desk": "apps/kwb-desk — do not demo",
    }


if DESK_DIR.is_dir():
    app.mount("/desk", StaticFiles(directory=str(DESK_DIR), html=True), name="desk")


@app.get("/health")
def health() -> dict:
    policy = {}
    if settings.models_config_path.exists():
        policy = (load_yaml(settings.models_config_path) or {}).get("policy") or {}
    target = gateway.inference_target()
    runtime = gateway.runtime_status()
    return {
        "ok": True,
        "product": "Knowledge Work Bench",
        "bind": f"{settings.bind_host}:{settings.bind_port}",
        "runtime": "Ollama = inference only (demo) · vLLM org — same /v1 contract",
        "llm_base_url": settings.llm_base_url,
        "inference_target": target,
        "inference_label": target.get("label"),
        "runtime_probe": {
            "reachable": runtime.get("reachable"),
            "base_url": runtime.get("base_url"),
            "denied": runtime.get("denied"),
        },
        "ollama_policy": {
            "inference_only": True,
            "no_pull": True,
            "no_registry": True,
            "adopt": "local_tags_only",
            **policy,
        },
        "boundary": "assist→export leave · no forward-accept · Monitor A ≠ CERT",
        "hitl": "self-HITL H1/H2/H3/H7/H9 · artefact_version stale · G10 sandbox-red",
        "ocr": ocr_extract.status(),
        "primary_desk": "apps/kwb-app",
        "legacy_html_desk": "/desk/",
        "desk": "apps/kwb-app",
        "version": "0.5.1",
    }


@app.get("/inference/status")
def inference_status() -> dict:
    """Explicit: which LLM host Gateway will call (local B vs Laptop-A)."""
    target = gateway.inference_target()
    probe = gateway.runtime_status()
    tags: list[str] = []
    try:
        import httpx

        base = target["llm_base_url"]
        with httpx.Client(timeout=3.0) as client:
            r = client.get(f"{base}/api/tags")
            if r.status_code == 200:
                tags = [
                    str(m.get("name"))
                    for m in (r.json() or {}).get("models") or []
                    if m.get("name")
                ]
    except Exception:
        pass
    return {
        "ok": True,
        **target,
        "runtime_reachable": probe.get("reachable"),
        "tags_on_target": tags,
        "how_to_use_laptop_a": (
            "On B: .\\scripts\\hotspot_link_workbench.ps1 -ServerIp <A-IP> "
            "then restart API in THAT same PowerShell window"
        ),
    }


_FIXTURES_ROOT = (ROOT / "data" / "fixtures").resolve()
_FIXTURE_TEXT = {
    ".txt",
    ".md",
    ".csv",
    ".json",
    ".log",
    ".py",
    ".yaml",
    ".yml",
}
_FIXTURE_IMAGE = {".png", ".jpg", ".jpeg", ".webp"}
_FIXTURE_PDF = {".pdf"}


def _fixture_kind(name: str) -> str:
    ext = Path(name).suffix.lower()
    if ext in _FIXTURE_TEXT:
        return "text"
    if ext in _FIXTURE_IMAGE:
        return "image"
    if ext in _FIXTURE_PDF:
        return "pdf"
    return "other"


def _safe_fixture_path(name: str) -> Path:
    base = Path(name).name
    if not base or base in (".", ".."):
        raise HTTPException(status_code=400, detail={"error": "invalid_filename"})
    path = (_FIXTURES_ROOT / base).resolve()
    try:
        path.relative_to(_FIXTURES_ROOT)
    except ValueError as exc:
        raise HTTPException(
            status_code=400, detail={"error": "path_traversal"}
        ) from exc
    return path


@app.get("/fixtures/catalog")
def fixtures_catalog() -> dict:
    """List demo fixtures under data/fixtures (browser + Electron fallback).

    Grouped into industrial folders so the desk tree can expand/collapse
    like a Cursor-style explorer (demo layout, not plant DMS).
    """
    groups: dict[str, list[dict]] = {
        "01_scans": [],
        "02_notes_pdf": [],
        "03_sop_kb": [],
        "04_templates": [],
        "05_other": [],
    }
    if _FIXTURES_ROOT.is_dir():
        for p in sorted(_FIXTURES_ROOT.iterdir()):
            if not p.is_file() or p.name.startswith("."):
                continue
            kind = _fixture_kind(p.name)
            item = {
                "name": p.name,
                "path": p.name,  # read still uses basename under fixtures root
                "kind": kind,
                "size": p.stat().st_size,
            }
            lower = p.name.lower()
            if kind == "image" or "scan" in lower:
                groups["01_scans"].append(item)
            elif kind == "pdf" or lower.endswith(".md") and "readme" in lower:
                groups["02_notes_pdf"].append(item)
            elif "sop" in lower or "extract" in lower:
                groups["03_sop_kb"].append(item)
            elif "tpl" in lower or "template" in lower:
                groups["04_templates"].append(item)
            else:
                groups["05_other"].append(item)

    tree: list[dict] = []
    labels = {
        "01_scans": "scans",
        "02_notes_pdf": "notes_pdf",
        "03_sop_kb": "sop_kb",
        "04_templates": "templates",
        "05_other": "other",
    }
    for key, kids in groups.items():
        if not kids:
            continue
        # Paths for children stay basename for /fixtures/file/{name}
        # but tree path uses folder/name for UI keys
        children = []
        for it in kids:
            children.append(
                {
                    **it,
                    "path": f"{labels[key]}/{it['name']}",
                }
            )
        tree.append(
            {
                "name": labels[key],
                "path": labels[key],
                "kind": "dir",
                "children": children,
            }
        )
    return {
        "ok": True,
        "root": str(_FIXTURES_ROOT),
        "rootName": "fixtures",
        "tree": tree,
        "note": "Demo fixtures grouped for tree UX · Open Folder in Electron for any project dir",
    }


@app.get("/fixtures/file/{name}")
def fixtures_file(name: str) -> dict:
    """Read one fixture as text or base64 (path-traversal safe)."""
    path = _safe_fixture_path(name)
    if not path.is_file():
        raise HTTPException(status_code=404, detail={"error": "not_found", "name": name})
    size = path.stat().st_size
    if size > 8 * 1024 * 1024:
        raise HTTPException(status_code=400, detail={"error": "file_too_large"})
    kind = _fixture_kind(path.name)
    if kind == "text":
        return {
            "ok": True,
            "name": path.name,
            "path": path.name,
            "kind": kind,
            "text": path.read_text(encoding="utf-8", errors="replace"),
            "size": size,
        }
    if kind in ("image", "pdf"):
        import base64

        data = path.read_bytes()
        ext = path.suffix.lower()
        types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
            ".pdf": "application/pdf",
        }
        return {
            "ok": True,
            "name": path.name,
            "path": path.name,
            "kind": kind,
            "b64": base64.b64encode(data).decode("ascii"),
            "contentType": types.get(ext, "application/octet-stream"),
            "size": size,
        }
    return {
        "ok": True,
        "name": path.name,
        "path": path.name,
        "kind": "other",
        "size": size,
        "note": "Preview not supported",
    }


@app.get("/audit/recent")
def audit_recent(limit: int = 50) -> dict:
    return {"events": recent(limit=limit)}


@app.get("/orch/events")
async def orch_events(grant_id: str | None = None):
    """SSE mid-turn phase stream (audit subscribers). Not token streaming."""
    import asyncio
    import queue as sync_queue

    q: sync_queue.Queue = sync_queue.Queue(maxsize=256)

    def _cb(event: dict) -> None:
        if grant_id:
            eg = event.get("grant_id")
            kind = str(event.get("kind") or "")
            # Always pass global inference markers; filter grant-scoped when set
            if eg and eg != grant_id:
                return
            if eg is None and kind not in (
                "gateway_chat_start",
                "gateway_chat",
                "gateway_deny",
                "orch_phase",
            ):
                return
        try:
            q.put_nowait(event)
        except sync_queue.Full:
            pass

    subscribe(_cb)

    async def gen():
        try:
            yield f"data: {json.dumps({'kind': 'orch_events_open', 'grant_id': grant_id})}\n\n"
            while True:
                def _pull():
                    try:
                        return q.get(timeout=15.0)
                    except sync_queue.Empty:
                        return None

                event = await asyncio.to_thread(_pull)
                if event is None:
                    yield ": ping\n\n"
                else:
                    yield f"data: {json.dumps(event, default=str)}\n\n"
        finally:
            unsubscribe(_cb)

    return StreamingResponse(
        gen(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/audit/verify")
def audit_verify() -> dict:
    return verify_chain()


@app.get("/runtime/status")
def runtime_status() -> dict:
    return gateway.runtime_status()


@app.get("/cards")
def list_cards() -> dict:
    return {"cards": cards.enabled_cards()}


@app.post("/task/start")
def task_start(body: StartTaskRequest) -> dict:
    routed = cards.route_task(body.task_type)
    if not routed.get("ok"):
        raise HTTPException(status_code=400, detail=routed)
    task_id = body.task_id or uuid.uuid4().hex[:12]
    g = grants.open_grant(
        task_id=task_id,
        user_id=body.user_id,
        model_card=routed["card_id"],
    )
    return {
        "ok": True,
        "task_id": task_id,
        "grant_id": g.id,
        "route": routed,
    }


@app.post("/orch/turn")
def orch_turn(body: OrchTurnRequest) -> dict:
    """Primary desk entry — Session/Grant → Orchestrator → Pack→Gateway when needed.

    Attach / Confirm extract / cite review / PPTX draft / free-text chat all share this spine.
    Do not call /gateway/chat from the desk for normal conversation.
    """
    out = orchestrator.turn(
        grant_id=body.grant_id,
        task_type=body.task_type,
        user_id=body.user_id,
        message=body.message,
        messages=body.messages,
        attach_text=body.attach_text,
        attach_filename=body.attach_filename,
        attach_b64=body.attach_b64,
        attach_content_type=body.attach_content_type,
        intent=body.intent,
    )
    if not out.get("ok"):
        err = out.get("error") or "orch_failed"
        if err in ("grant_inactive", "gateway_deny"):
            raise HTTPException(status_code=403, detail=out)
        if err in ("no_route", "card_disabled", "tag_not_adopted"):
            raise HTTPException(status_code=400, detail=out)
        raise HTTPException(status_code=400, detail=out)
    return out


@app.post("/task/revoke")
def task_revoke(body: RevokeRequest) -> dict:
    ok = grants.revoke(body.grant_id)
    if not ok:
        raise HTTPException(
            status_code=400,
            detail={"error": "revoke_failed", "grant_id": body.grant_id},
        )
    return {"ok": True, "grant_id": body.grant_id, "status": "revoked"}


@app.post("/task/retrieve")
def task_retrieve(body: RetrieveRequest) -> dict:
    err = grants.require_active(body.grant_id, "retrieve")
    if err:
        raise HTTPException(status_code=403, detail=err)
    g = grants.get(body.grant_id)
    assert g is not None
    return retrieve.retrieve(body.query, shelves=g.shelves, k=body.k)


@app.post("/task/h1-confirm")
def task_h1_confirm(body: H1ConfirmRequest) -> dict:
    """D — fixture/OCR extract confirm (B2). Same-user H1."""
    err = grants.require_active(body.grant_id, "word")
    if err:
        raise HTTPException(status_code=403, detail=err)
    out = artefacts.ack_h1(body.grant_id, body.extract_text, body.h1_acked)
    if not out.get("ok"):
        raise HTTPException(status_code=400, detail=out)
    return out


@app.post("/task/attach-extract")
def task_attach_extract(body: AttachExtractRequest) -> dict:
    """Attach README/txt/PDF/image → extract key points → match company knowledge (pre-H1).

    Binary via file_b64 uses the same OCR/PDF ingest as /orch/turn (honest engine labels).
    Prefer /orch/turn for the full Confirm extract spine.
    """
    err = grants.require_active(body.grant_id, "retrieve")
    if err:
        raise HTTPException(status_code=403, detail=err)
    g = grants.get(body.grant_id)
    assert g is not None

    ingest_meta: dict = {
        "engine": "plain",
        "degraded": False,
        "live_ocr": False,
        "message": "Plain text attach (no OCR)",
    }
    text = (body.text or "").strip()
    if body.file_b64 and str(body.file_b64).strip():
        import base64

        try:
            raw = base64.b64decode(body.file_b64, validate=False)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail={"error": "file_b64_invalid", "message": str(e)},
            ) from e
        ing = ocr_extract.ingest_bytes(
            raw,
            filename=body.filename,
            content_type=body.content_type,
            allow_fixture_fallback=body.allow_fixture_fallback,
        )
        ingest_meta = ing
        if not ing.get("ok"):
            raise HTTPException(status_code=400, detail=ing)
        text = (ing.get("text") or "").strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail={"error": "empty_attach", "message": "Attach text is empty"},
        )
    bullets = pptx_draft.extract_key_points(text)
    query = pptx_draft.build_retrieve_query(text, bullets)
    hit = retrieve.retrieve(query, shelves=g.shelves, k=body.k)
    cites = hit.get("cites") or []
    match_notes: list[str] = []
    for c in cites[:5]:
        match_notes.append(f"{c.get('path')}: {c.get('snippet')}")
    if not match_notes:
        match_notes.append("NOT FOUND under grant — abstain (fail closed)")
    findings = "\n".join(f"- {b}" for b in bullets) if bullets else text[:800]

    engine = ingest_meta.get("engine") or "plain"
    degraded = bool(ingest_meta.get("degraded"))
    live_ocr = bool(ingest_meta.get("live_ocr"))
    if live_ocr:
        source_line = f"Source: live OCR ({engine})."
    elif engine == "pypdf":
        source_line = "Source: PDF text layer (pypdf) — not OCR."
    elif engine == "fixture_stub" or degraded:
        source_line = "Source: fixture stub — NOT live OCR."
    else:
        source_line = f"Source: {engine}."

    log_event(
        "attach_extract",
        grant_id=body.grant_id,
        filename=body.filename,
        n_bullets=len(bullets),
        n_cites=len(cites),
        verdict=hit.get("verdict"),
        ingest_engine=engine,
        ingest_degraded=degraded,
        live_ocr=live_ocr,
    )
    return {
        "ok": True,
        "filename": body.filename,
        "extract_bullets": bullets,
        "extract_text": findings,
        "query": query,
        "cites": cites,
        "match_notes": match_notes,
        "verdict": hit.get("verdict"),
        "ingest_engine": engine,
        "ingest_degraded": degraded,
        "live_ocr": live_ocr,
        "ingest_message": ingest_meta.get("message"),
        "ask": {
            "kind": "confirm_extract",
            "prompt": (
                f"Confirm extract before we treat it as input. {source_line} "
                "Enter to accept, or paste a corrected extract."
            ),
            "context_preview": findings[:420],
        },
    }


@app.post("/task/h7-ack")
def task_h7_ack(body: H7AckRequest) -> dict:
    """M6 — server-side cite review ack; inspect-draft reads this, not client flag."""
    err = grants.require_active(body.grant_id, "retrieve")
    if err:
        raise HTTPException(status_code=403, detail=err)
    return artefacts.ack_h7(body.grant_id)


@app.post("/task/inspect-draft")
def task_inspect_draft(body: InspectDraftRequest) -> dict:
    err = grants.require_active(body.grant_id, "word")
    if err:
        raise HTTPException(status_code=403, detail=err)
    g = grants.get(body.grant_id)
    assert g is not None

    cites: list[str] = []
    verdict = "NOT FOUND"
    if body.query_for_cites:
        hit = retrieve.retrieve(body.query_for_cites, shelves=g.shelves, k=5)
        verdict = hit.get("verdict", "NOT FOUND")
        cites = [f"{c['path']}: {c['snippet']}" for c in hit.get("cites") or []]
        # Server H7 only — ignore client-only body.h7_acked theatre
        if cites and not artefacts.h7_acked(body.grant_id):
            log_event(
                "h7_required_deny",
                grant_id=body.grant_id,
                error="h7_required",
                cite_count=len(cites),
            )
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "h7_required",
                    "message": "Own-work cite review required before draft — POST /task/h7-ack",
                    "cites": cites,
                },
            )

    sec = secrets.scan_text(body.findings)
    if not sec.get("ok"):
        raise HTTPException(status_code=400, detail=sec)

    routed_model = None
    if g.model_card:
        card = cards.get_card(g.model_card)
        routed_model = (card or {}).get("model_id")

    ver = artefacts.fingerprint(body.title, body.findings, "|".join(cites))
    draft = word_draft.write_inspection_draft(
        title=body.title,
        findings=body.findings,
        cites=cites,
        model_id=routed_model,
        task_id=g.task_id,
        artefact_version=ver,
    )
    artefacts.register_draft(
        filename=draft["filename"],
        grant_id=body.grant_id,
        artefact_version=ver,
        findings=body.findings,
        title=body.title,
    )
    return {**draft, "cite_verdict": verdict, "cites": cites}


@app.post("/task/pptx-draft")
def task_pptx_draft(body: PptxDraftRequest) -> dict:
    """Generate PowerPoint DRAFT from template + extract bullets (desk path)."""
    err = grants.require_active(body.grant_id, "word")
    if err:
        raise HTTPException(status_code=403, detail=err)
    g = grants.get(body.grant_id)
    assert g is not None

    cites: list[str] = []
    verdict = "NOT FOUND"
    if body.query_for_cites:
        hit = retrieve.retrieve(body.query_for_cites, shelves=g.shelves, k=5)
        verdict = hit.get("verdict", "NOT FOUND")
        cites = [f"{c['path']}: {c['snippet']}" for c in hit.get("cites") or []]
        if cites and not artefacts.h7_acked(body.grant_id):
            log_event(
                "h7_required_deny",
                grant_id=body.grant_id,
                error="h7_required",
                cite_count=len(cites),
                format="pptx",
            )
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "h7_required",
                    "message": "Own-work cite review required before PPTX draft — POST /task/h7-ack",
                    "cites": cites,
                },
            )

    sec = secrets.scan_text(body.findings)
    if not sec.get("ok"):
        raise HTTPException(status_code=400, detail=sec)

    routed_model = None
    if g.model_card:
        card = cards.get_card(g.model_card)
        routed_model = (card or {}).get("model_id")

    bullets = body.bullets or pptx_draft.extract_key_points(body.findings)
    ver = artefacts.fingerprint(
        body.title, body.findings, "|".join(cites), "pptx", *bullets
    )
    draft = pptx_draft.write_pptx_draft(
        title=body.title,
        findings=body.findings,
        bullets=bullets,
        cites=cites,
        match_notes=cites[:5],
        model_id=routed_model,
        task_id=g.task_id,
        artefact_version=ver,
        template=body.template or "kwb_brief",
    )
    artefacts.register_draft(
        filename=draft["filename"],
        grant_id=body.grant_id,
        artefact_version=ver,
        findings=body.findings,
        title=body.title,
    )
    return {**draft, "cite_verdict": verdict, "cites": cites, "bullets": bullets}


@app.post("/task/h2-ack")
def task_h2_ack(body: H2AckRequest) -> dict:
    err = grants.require_active(body.grant_id, "word")
    if err:
        raise HTTPException(status_code=403, detail=err)
    name = Path(body.draft_filename).name
    meta = artefacts.get_draft(name)
    if not meta or meta.get("grant_id") != body.grant_id:
        raise HTTPException(status_code=404, detail={"error": "draft_not_found"})
    out = artefacts.ack_h2(name, body.artefact_version)
    if not out.get("ok"):
        raise HTTPException(status_code=400, detail=out)
    return out


@app.post("/task/draft-edit")
def task_draft_edit(body: DraftEditRequest) -> dict:
    """Material edit → stale H2 (B4)."""
    err = grants.require_active(body.grant_id, "word")
    if err:
        raise HTTPException(status_code=403, detail=err)
    name = Path(body.draft_filename).name
    meta = artefacts.get_draft(name)
    if not meta or meta.get("grant_id") != body.grant_id:
        raise HTTPException(status_code=404, detail={"error": "draft_not_found"})
    sec = secrets.scan_text(body.findings)
    if not sec.get("ok"):
        raise HTTPException(status_code=400, detail=sec)
    out = artefacts.mark_edit(name, body.findings, body.title)
    if not out.get("ok"):
        raise HTTPException(status_code=400, detail=out)
    return out


@app.post("/task/h9-ack")
def task_h9_ack(body: H9AckRequest) -> dict:
    err = grants.require_active(body.grant_id, "sandbox")
    if err:
        raise HTTPException(status_code=403, detail=err)
    out = artefacts.ack_h9(body.grant_id, body.accept)
    if not out.get("ok"):
        raise HTTPException(status_code=400, detail=out)
    return out


@app.post("/task/export")
def task_export(body: ExportRequest) -> dict:
    """I leave — H2 fresh + secrets on docx body + H9/G10 if sandbox used."""
    err = grants.require_active(body.grant_id, "word")
    if err:
        raise HTTPException(status_code=403, detail=err)
    if not body.h2_acked:
        raise HTTPException(
            status_code=400,
            detail={"error": "h2_required", "message": "Own-work H2 ack required before export leave"},
        )
    name = Path(body.draft_filename).name
    path = ARTIFACTS_DIR / name
    if not path.is_file() or path.suffix.lower() not in {".docx", ".pptx"}:
        raise HTTPException(status_code=404, detail={"error": "draft_not_found", "filename": name})

    fresh, meta = artefacts.h2_fresh(name)
    if not fresh:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "h2_stale",
                "message": "H2 must be fresh for current artefact_version — call /task/h2-ack",
                "meta": meta,
            },
        )
    if body.artefact_version and meta and body.artefact_version != meta.get("artefact_version"):
        raise HTTPException(
            status_code=400,
            detail={
                "error": "artefact_version_mismatch",
                "current": meta.get("artefact_version"),
                "provided": body.artefact_version,
            },
        )

    sb = artefacts.export_sandbox_gate(body.grant_id)
    if sb is not None and not sb.get("ok"):
        raise HTTPException(status_code=400, detail=sb)

    if path.suffix.lower() == ".pptx":
        body_text = pptx_draft.extract_pptx_text(path)
    else:
        body_text = word_draft.extract_docx_text(path)
    sec = secrets.scan_text(body_text + "\n" + name)
    if not sec.get("ok"):
        raise HTTPException(status_code=400, detail=sec)

    sb_state = artefacts.sandbox_state(body.grant_id)
    sb_obs: dict = {}
    if sb_state and isinstance(sb_state.get("report"), dict):
        r = sb_state["report"]
        stderr = r.get("stderr") or ""
        if isinstance(stderr, str) and len(stderr) > 2000:
            stderr = stderr[:2000] + "\n… truncated"
        sb_obs = {
            "ok": r.get("ok"),
            "exit_code": r.get("exit_code"),
            "duration_ms": r.get("duration_ms"),
            "stderr": stderr,
        }
    log_event(
        "export_leave",
        grant_id=body.grant_id,
        path=str(path),
        h2_acked=True,
        artefact_version=(meta or {}).get("artefact_version"),
        sandbox_gated=sb is not None,
        **({f"sandbox_{k}": v for k, v in sb_obs.items()} if sb_obs else {}),
    )
    # Optional revoke-on-export: shelf closes after leave (G7-ready grant hang fix).
    revoked = grants.revoke(body.grant_id)
    if revoked:
        log_event("export_leave_revoke", grant_id=body.grant_id)
    return {
        "ok": True,
        "path": str(path),
        "filename": name,
        "status": "exported",
        "artefact_version": (meta or {}).get("artefact_version"),
        "grant_revoked": revoked,
        "note": "Solution ends at export leave — no forward-accept",
        "downloads": {
            "draft": f"/artifacts/{name}?grant_id={body.grant_id}",
            "leave_pack": (
                f"/task/leave-pack?grant_id={body.grant_id}"
                f"&draft_filename={name}"
            ),
        },
    }


@app.get("/artifacts/{filename}")
def get_artifact(filename: str, grant_id: str | None = None) -> FileResponse:
    """M1 — serve DRAFT .docx/.pptx only with matching grant_id; Monitor A .json packs OK."""
    path = _safe_artifact_path(filename)
    suffix = path.suffix.lower()
    if suffix not in _ALLOWED_ARTIFACT_SUFFIXES:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "unsupported_type",
                "allowed": sorted(_ALLOWED_ARTIFACT_SUFFIXES),
                "filename": path.name,
            },
        )
    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail={"error": "not_found", "filename": path.name},
        )
    # Red-team C2: drafts are grant-scoped — do not serve without grant_id
    if suffix in {".docx", ".pptx"}:
        if not grant_id:
            raise HTTPException(
                status_code=403,
                detail={
                    "error": "grant_required",
                    "filename": path.name,
                    "message": "DRAFT download requires grant_id query param",
                },
            )
        meta = artefacts.get_draft(path.name)
        if meta is not None and meta.get("grant_id") != grant_id:
            raise HTTPException(
                status_code=403,
                detail={
                    "error": "grant_mismatch",
                    "filename": path.name,
                    "grant_id": grant_id,
                },
            )
        # Unknown meta (legacy file): still require grant_id present (above) but
        # cannot prove ownership — allow only if grant is active (same session trust).
        if meta is None:
            g = grants.get(grant_id)
            if not g or not g.active:
                raise HTTPException(
                    status_code=403,
                    detail={
                        "error": "grant_inactive",
                        "filename": path.name,
                        "grant_id": grant_id,
                    },
                )
    if suffix == ".docx":
        media = _DOCX_MEDIA
    elif suffix == ".pptx":
        media = _PPTX_MEDIA
    else:
        media = "application/json"
    return FileResponse(
        path,
        media_type=media,
        filename=path.name,
        content_disposition_type="attachment",
    )


@app.get("/task/leave-pack")
def task_leave_pack(
    grant_id: str,
    draft_filename: str,
    audit_limit: int = 50,
) -> Response:
    """M2 — zip: DRAFT docx + audit slice + Monitor A pack (best-effort) + manifest."""
    name = Path(draft_filename).name
    draft_path = _safe_artifact_path(name)
    if draft_path.suffix.lower() != ".docx":
        raise HTTPException(
            status_code=400,
            detail={"error": "unsupported_type", "message": "leave-pack requires .docx draft"},
        )
    if not draft_path.is_file():
        raise HTTPException(
            status_code=404,
            detail={"error": "draft_not_found", "filename": name},
        )
    meta = artefacts.get_draft(name)
    if meta is not None and meta.get("grant_id") != grant_id:
        raise HTTPException(
            status_code=403,
            detail={"error": "grant_mismatch", "filename": name, "grant_id": grant_id},
        )

    limit = max(1, min(audit_limit, 500))
    events = recent(limit=max(limit * 4, 200))
    grant_events = [e for e in events if e.get("grant_id") == grant_id]
    audit_slice = grant_events[-limit:] if grant_events else events[-limit:]

    mon_path, mon_info = _newest_monitor_a_pack()
    exported_at = datetime.now(timezone.utc).isoformat()
    manifest = {
        "grant_id": grant_id,
        "draft": name,
        "exported_at": exported_at,
        "note": "export leave — no forward-accept — not CERT",
        "audit_events": len(audit_slice),
        "monitor_a": mon_info,
    }

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(name, draft_path.read_bytes())
        zf.writestr(
            "audit-slice.json",
            json.dumps(audit_slice, indent=2, ensure_ascii=False, default=str),
        )
        if mon_path is not None and mon_path.is_file():
            zf.writestr(mon_path.name, mon_path.read_bytes())
        zf.writestr(
            "manifest.json",
            json.dumps(manifest, indent=2, ensure_ascii=False),
        )

    log_event(
        "leave_pack",
        grant_id=grant_id,
        draft=name,
        audit_events=len(audit_slice),
        monitor_a=mon_info.get("filename") if mon_info else None,
    )
    zip_name = f"leave-pack-{grant_id[:12]}.zip"
    return Response(
        content=buf.getvalue(),
        media_type="application/zip",
        headers={
            "Content-Disposition": f'attachment; filename="{zip_name}"',
        },
    )


@app.post("/task/export-check")
def task_export_check(body: ExportCheckRequest) -> dict:
    """G9 — scan arbitrary text (fail-closed inject demo)."""
    out = secrets.scan_text(body.text)
    if not out.get("ok"):
        raise HTTPException(status_code=400, detail=out)
    return out


@app.post("/monitor-a/start")
def mon_start() -> dict:
    return monitor_a.start()


@app.post("/monitor-a/stop")
def mon_stop(session_id: str) -> dict:
    out = monitor_a.stop(session_id)
    if not out.get("ok"):
        raise HTTPException(status_code=404, detail=out)
    return out


@app.post("/sandbox/calc")
def sandbox_calc(body: CalcRequest) -> dict:
    err = grants.require_active(body.grant_id, "sandbox")
    if err:
        raise HTTPException(status_code=403, detail=err)
    result = sandbox.run_calc(body.expression).as_dict()
    artefacts.record_sandbox(body.grant_id, result)
    return result


@app.post("/sandbox/python")
def sandbox_python(body: PythonRequest) -> dict:
    err = grants.require_active(body.grant_id, "sandbox")
    if err:
        raise HTTPException(status_code=403, detail=err)
    result = sandbox.run_python(
        body.source,
        timeout_s=body.timeout_s,
        prefer_docker=body.prefer_docker,
    ).as_dict()
    artefacts.record_sandbox(body.grant_id, result)
    return result


@app.post("/gateway/chat")
def gateway_chat(body: ChatRequest) -> dict:
    """Low-level gateway (scripts / deny demos). Desk conversation must use POST /orch/turn."""
    err = grants.require_active(body.grant_id, "gateway")
    if err:
        raise HTTPException(status_code=403, detail=err)
    g = grants.get(body.grant_id)
    assert g is not None
    allowed = cards.model_ids_for_card(g.model_card)
    model = body.model
    if not model:
        # Default to card model
        if g.model_card:
            card = cards.get_card(g.model_card)
            model = (card or {}).get("model_id") or ""
    if not model:
        raise HTTPException(status_code=400, detail={"error": "model_required"})
    out = gateway.chat_completions(
        messages=body.messages,
        model=model,
        allow_base_override=False,
        allowed_model_ids=allowed,
    )
    # Fail-closed: surface gateway_deny as HTTP 403 (not 200 + ok:false)
    if isinstance(out, dict) and out.get("ok") is False and out.get("error") == "gateway_deny":
        raise HTTPException(status_code=403, detail=out)
    return out


@app.get("/mcp/status")
def mcp_status() -> dict:
    """In-process MCP-shaped tool host status (default ON; SOVEREIGN_MCP_HOST=0 to disable)."""
    return mcp_mock.status()


@app.get("/mcp/tools")
def mcp_tools() -> dict:
    return {"ok": True, "tools": mcp_mock.list_tools(), **mcp_mock.status()}


@app.post("/mcp/echo")
def mcp_echo(body: McpEchoRequest) -> dict:
    """Allowlisted echo tool — requires active grant via query/body not in model; use /mcp/call."""
    # Red-team H2: ungated echo removed from anonymous surface
    raise HTTPException(
        status_code=403,
        detail={
            "error": "grant_required",
            "message": "Use POST /mcp/call with grant_id for echo_tool",
        },
    )


@app.post("/mcp/call")
def mcp_call(body: dict) -> dict:
    """Call an allowlisted in-process tool: {name, arguments?, grant_id}."""
    name = str((body or {}).get("name") or "")
    args = (body or {}).get("arguments") or {}
    gid = (body or {}).get("grant_id")
    if not gid:
        raise HTTPException(
            status_code=403,
            detail={"error": "grant_required", "message": "mcp/call requires grant_id"},
        )
    g = grants.get(str(gid))
    if not g or not g.active:
        raise HTTPException(
            status_code=403,
            detail={"error": "grant_inactive", "grant_id": gid},
        )
    if not isinstance(args, dict):
        args = {}
    out = mcp_mock.call_tool(name, args, grant_id=str(gid))
    if isinstance(out, dict) and out.get("ok") is False:
        # Keep 200 + ok:false for allowlist miss (H1), or 403 for host off
        if out.get("error") == "mcp_host_not_enabled":
            raise HTTPException(status_code=403, detail=out)
    return out


@app.get("/skills")
def skills_list() -> dict:
    from . import skills as skills_mod

    return {"ok": True, "skills": skills_mod.list_skills()}


class SkillRecommendRequest(BaseModel):
    message: str = ""
    filename: str = ""
    task_type: str = ""


@app.post("/skills/recommend")
def skills_recommend(body: SkillRecommendRequest) -> dict:
    """Skill-authored plan for the current input (not a fixed menu, not an LLM)."""
    from . import skills as skills_mod

    return skills_mod.recommend_plan(
        message=body.message or "",
        filename=body.filename or "",
        task_type=body.task_type or "",
    )


@app.get("/roles")
def roles_list() -> dict:
    from . import roles as roles_mod

    return {"ok": True, "roles": roles_mod.list_roles()}
