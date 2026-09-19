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
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import (
    artefacts,
    cards,
    gateway,
    grants,
    mcp_mock,
    monitor_a,
    retrieve,
    sandbox,
    secrets,
    word_draft,
)
from .audit import log_event, recent, verify_chain
from .config import ARTIFACTS_DIR, ROOT, ensure_dirs, get_settings, load_yaml

_ALLOWED_ARTIFACT_SUFFIXES = {".docx", ".json"}
_DOCX_MEDIA = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
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
    log_event("app_start", bind=f"{settings.bind_host}:{settings.bind_port}")


@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/desk/")


if DESK_DIR.is_dir():
    app.mount("/desk", StaticFiles(directory=str(DESK_DIR), html=True), name="desk")


@app.get("/health")
def health() -> dict:
    policy = {}
    if settings.models_config_path.exists():
        policy = (load_yaml(settings.models_config_path) or {}).get("policy") or {}
    return {
        "ok": True,
        "product": "Knowledge Work Bench",
        "bind": f"{settings.bind_host}:{settings.bind_port}",
        "runtime": "Ollama = inference only (demo) · vLLM org — same /v1 contract",
        "llm_base_url": settings.llm_base_url,
        "ollama_policy": {
            "inference_only": True,
            "no_pull": True,
            "no_registry": True,
            "adopt": "local_tags_only",
            **policy,
        },
        "boundary": "assist→export leave · no forward-accept · Monitor A ≠ CERT",
        "hitl": "self-HITL H1/H2/H3/H7/H9 · artefact_version stale · G10 sandbox-red",
        "desk": "/desk/",
        "version": "0.5.0",
    }


@app.get("/audit/recent")
def audit_recent(limit: int = 50) -> dict:
    return {"events": recent(limit=limit)}


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
    if not path.is_file() or path.suffix.lower() != ".docx":
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
    return {
        "ok": True,
        "path": str(path),
        "filename": name,
        "status": "exported",
        "artefact_version": (meta or {}).get("artefact_version"),
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
    """M1 — serve DRAFT .docx (or Monitor A .json pack) from ARTIFACTS_DIR."""
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
    if grant_id and suffix == ".docx":
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
    media = _DOCX_MEDIA if suffix == ".docx" else "application/json"
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
    return secrets.scan_text(body.text)


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
    return gateway.chat_completions(
        messages=body.messages,
        model=model,
        allow_base_override=False,
        allowed_model_ids=allowed,
    )


@app.get("/mcp/status")
def mcp_status() -> dict:
    """MCP MOCK stub — default OFF (SOVEREIGN_MCP_MOCK=1 to enable echo)."""
    return mcp_mock.status()


@app.post("/mcp/echo")
def mcp_echo(body: McpEchoRequest) -> dict:
    """FastMCP-inspired echo behind feature flag; returns not-enabled when OFF."""
    return mcp_mock.echo_tool(body.text)
