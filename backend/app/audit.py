"""Append-only audit log with SHA-256 hash chain (jury-verifiable · not HMAC-CERT)."""

from __future__ import annotations

import hashlib
import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import AUDIT_DIR, ensure_dirs

_lock = threading.Lock()
_subscribers: list = []
_GENESIS = "0" * 64


def _path() -> Path:
    ensure_dirs()
    day = datetime.now(timezone.utc).strftime("%Y%m%d")
    return AUDIT_DIR / f"audit-{day}.jsonl"


def _chain_meta_path() -> Path:
    ensure_dirs()
    day = datetime.now(timezone.utc).strftime("%Y%m%d")
    return AUDIT_DIR / f"audit-{day}.chain.json"


def _last_hash() -> str:
    meta = _chain_meta_path()
    if meta.exists():
        try:
            tip = json.loads(meta.read_text(encoding="utf-8")).get("tip")
            if tip:
                return tip
        except json.JSONDecodeError:
            pass
    path = _path()
    if not path.exists():
        return _GENESIS
    tip = _GENESIS
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("hash"):
            tip = event["hash"]
    return tip


def subscribe(callback) -> None:
    _subscribers.append(callback)


def log_event(kind: str, **payload: Any) -> dict:
    with _lock:
        ensure_dirs()
        prev = _last_hash()
        event = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "kind": kind,
            "prev_hash": prev,
            **payload,
        }
        # Hash over canonical payload excluding hash field
        canonical = json.dumps(event, ensure_ascii=False, sort_keys=True, default=str)
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        event["hash"] = digest
        line = json.dumps(event, ensure_ascii=False, default=str)
        with open(_path(), "a", encoding="utf-8") as f:
            f.write(line + "\n")
        _chain_meta_path().write_text(
            json.dumps({"tip": digest, "updated": event["ts"]}),
            encoding="utf-8",
        )
    for cb in list(_subscribers):
        try:
            cb(event)
        except Exception:
            pass
    return event


def recent(limit: int = 100) -> list[dict]:
    ensure_dirs()
    path = _path()
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    out = []
    for line in lines[-limit:]:
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def verify_chain() -> dict[str, Any]:
    """Verify hash chain for today's audit file. Skips legacy lines without hash."""
    ensure_dirs()
    path = _path()
    if not path.exists():
        return {"ok": True, "entries": 0, "tip": _GENESIS, "note": "empty"}
    prev: str | None = None
    n = 0
    skipped_legacy = 0
    tip = _GENESIS
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            return {"ok": False, "error": "json_corrupt", "line": i + 1}
        if "hash" not in event or "prev_hash" not in event:
            skipped_legacy += 1
            continue
        got_prev = event.get("prev_hash")
        got_hash = event.get("hash")
        if prev is not None and got_prev != prev:
            return {
                "ok": False,
                "error": "prev_hash_mismatch",
                "line": i + 1,
                "expected_prev": prev,
            }
        check = {k: v for k, v in event.items() if k != "hash"}
        canonical = json.dumps(check, ensure_ascii=False, sort_keys=True, default=str)
        expect = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        if got_hash != expect:
            return {"ok": False, "error": "hash_mismatch", "line": i + 1}
        prev = got_hash
        tip = got_hash
        n += 1
    return {
        "ok": True,
        "entries": n,
        "skipped_legacy": skipped_legacy,
        "tip": tip,
        "not_cert": True,
    }
