"""Draft artefact registry — version fingerprint + HITL state (WP-05 B3/B4).

HITL interrupt / resume *pattern* (KWB/from_langgraph_web — notes only):
  LangGraph interrupt(payload) ≈ hard gate wait (H1 / H2 stale / H9)
  checkpointer + thread_id ≈ grant-scoped pending decision in this registry
  Command(resume=…) ≈ desk accept / edit / reject → continue
We own the thin loop; do not add LangGraph as a dependency or runtime owner.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .audit import log_event
from .config import ARTIFACTS_DIR, ensure_dirs

# filename -> meta
_DRAFTS: dict[str, dict[str, Any]] = {}
# grant_id -> last sandbox report
_SANDBOX: dict[str, dict[str, Any]] = {}
# grant_id -> H1 state
_H1: dict[str, dict[str, Any]] = {}
# grant_id -> H7 cite-review ack (server SoT; client body flag is ignored)
_H7: dict[str, dict[str, Any]] = {}


def fingerprint(*parts: str) -> str:
    raw = "\n".join(p or "" for p in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def _meta_path(filename: str) -> Path:
    ensure_dirs()
    return ARTIFACTS_DIR / f"{filename}.meta.json"


def register_draft(
    *,
    filename: str,
    grant_id: str,
    artefact_version: str,
    findings: str,
    title: str,
) -> dict[str, Any]:
    meta = {
        "filename": filename,
        "grant_id": grant_id,
        "artefact_version": artefact_version,
        "findings": findings,
        "title": title,
        "h2_acked_version": None,
        "h2_stale": False,
    }
    _DRAFTS[filename] = meta
    _meta_path(filename).write_text(json.dumps(meta, indent=2), encoding="utf-8")
    log_event("artefact_register", filename=filename, artefact_version=artefact_version)
    return dict(meta)


def get_draft(filename: str) -> dict[str, Any] | None:
    if filename in _DRAFTS:
        return dict(_DRAFTS[filename])
    path = _meta_path(filename)
    if path.is_file():
        meta = json.loads(path.read_text(encoding="utf-8"))
        _DRAFTS[filename] = meta
        return dict(meta)
    return None


def ack_h2(filename: str, artefact_version: str) -> dict[str, Any]:
    meta = get_draft(filename)
    if not meta:
        return {"ok": False, "error": "draft_not_found"}
    if meta["artefact_version"] != artefact_version:
        return {
            "ok": False,
            "error": "h2_stale",
            "message": "artefact_version mismatch — re-check after edit",
            "current": meta["artefact_version"],
            "provided": artefact_version,
        }
    meta["h2_acked_version"] = artefact_version
    meta["h2_stale"] = False
    _DRAFTS[filename] = meta
    _meta_path(filename).write_text(json.dumps(meta, indent=2), encoding="utf-8")
    log_event("h2_ack", filename=filename, artefact_version=artefact_version)
    return {"ok": True, **meta}


def mark_edit(filename: str, findings: str, title: str | None = None) -> dict[str, Any]:
    """Material edit → new artefact_version; H2 becomes stale."""
    meta = get_draft(filename)
    if not meta:
        return {"ok": False, "error": "draft_not_found"}
    title = title if title is not None else meta.get("title") or ""
    new_v = fingerprint(title, findings)
    meta["findings"] = findings
    meta["title"] = title
    meta["artefact_version"] = new_v
    meta["h2_stale"] = True
    meta["h2_acked_version"] = None
    _DRAFTS[filename] = meta
    _meta_path(filename).write_text(json.dumps(meta, indent=2), encoding="utf-8")
    log_event("artefact_edit_stale", filename=filename, artefact_version=new_v)
    return {"ok": True, **meta}


def h2_fresh(filename: str) -> tuple[bool, dict[str, Any] | None]:
    meta = get_draft(filename)
    if not meta:
        return False, None
    fresh = (
        not meta.get("h2_stale")
        and meta.get("h2_acked_version") == meta.get("artefact_version")
        and meta.get("h2_acked_version") is not None
    )
    return fresh, meta


def record_sandbox(grant_id: str, report: dict[str, Any]) -> dict[str, Any]:
    """Store sandbox observation for H9; audit carries 07-like stable fields."""
    packed = {
        "grant_id": grant_id,
        "ok": bool(report.get("ok")),
        "report": report,
        "h9_acked": False,
    }
    _SANDBOX[grant_id] = packed
    stderr = report.get("stderr") or ""
    if isinstance(stderr, str) and len(stderr) > 2000:
        stderr = stderr[:2000] + "\n… truncated"
    log_event(
        "sandbox_recorded",
        grant_id=grant_id,
        ok=packed["ok"],
        exit_code=report.get("exit_code"),
        duration_ms=report.get("duration_ms"),
        timeout_occurred=report.get("timeout_occurred"),
        mode=report.get("mode"),
        stderr=stderr,
    )
    return dict(packed)


def ack_h9(grant_id: str, accept: bool) -> dict[str, Any]:
    cur = _SANDBOX.get(grant_id)
    if not cur:
        return {"ok": False, "error": "sandbox_report_missing"}
    if not cur["ok"] and accept:
        return {
            "ok": False,
            "error": "sandbox_red",
            "message": "Cannot H9-accept a red sandbox report",
        }
    cur["h9_acked"] = True
    cur["h9_decision"] = "accept" if accept else "reject"
    _SANDBOX[grant_id] = cur
    log_event("h9_ack", grant_id=grant_id, decision=cur["h9_decision"])
    return {"ok": True, **cur}


def sandbox_state(grant_id: str) -> dict[str, Any] | None:
    cur = _SANDBOX.get(grant_id)
    return dict(cur) if cur else None


def export_sandbox_gate(grant_id: str) -> dict[str, Any] | None:
    """None = no sandbox used (inspection OK). Else error detail or ok."""
    cur = _SANDBOX.get(grant_id)
    if not cur:
        return None
    if not cur["ok"]:
        return {
            "error": "sandbox_red_export_denied",
            "message": "G10 — sandbox-red blocks export leave",
        }
    if cur.get("h9_decision") == "reject":
        return {
            "error": "h9_rejected_export_denied",
            "message": "H9 reject blocks export leave",
        }
    if not cur.get("h9_acked"):
        return {
            "error": "h9_required",
            "message": "H9 ack required after sandbox before export leave",
        }
    return {"ok": True}


def ack_h1(grant_id: str, extract_text: str, confirmed: bool) -> dict[str, Any]:
    if not confirmed:
        return {"ok": False, "error": "h1_not_confirmed"}
    ver = fingerprint(extract_text)
    meta = {"grant_id": grant_id, "extract_version": ver, "h1_acked": True}
    _H1[grant_id] = meta
    log_event("h1_ack", grant_id=grant_id, extract_version=ver)
    return {"ok": True, **meta}


def h1_state(grant_id: str) -> dict[str, Any] | None:
    cur = _H1.get(grant_id)
    return dict(cur) if cur else None


def ack_h7(grant_id: str) -> dict[str, Any]:
    """Own-work cite review — persist on grant registry (M6)."""
    meta = {"grant_id": grant_id, "h7_acked": True}
    _H7[grant_id] = meta
    log_event("h7_ack", grant_id=grant_id)
    return {"ok": True, **meta}


def h7_state(grant_id: str) -> dict[str, Any] | None:
    cur = _H7.get(grant_id)
    return dict(cur) if cur else None


def h7_acked(grant_id: str) -> bool:
    cur = _H7.get(grant_id)
    return bool(cur and cur.get("h7_acked"))
