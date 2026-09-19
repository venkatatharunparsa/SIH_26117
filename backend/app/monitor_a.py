"""Monitor A — start/stop egress posture snapshots (G5). Persisted · not CERT."""

from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .audit import log_event
from .config import ARTIFACTS_DIR, ensure_dirs

_SESS_DIR: Path | None = None


def _sess_dir() -> Path:
    global _SESS_DIR
    ensure_dirs()
    d = ARTIFACTS_DIR / "monitor_a_sessions"
    d.mkdir(parents=True, exist_ok=True)
    _SESS_DIR = d
    return d


def _snapshot(label: str) -> dict[str, Any]:
    import socket

    probes = []
    for host, port in (("127.0.0.1", 8080), ("127.0.0.1", 11434)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        try:
            r = s.connect_ex((host, port))
            probes.append({"host": host, "port": port, "connect_ex": r, "local_ok": r == 0})
        except OSError as e:
            probes.append({"host": host, "port": port, "error": str(e)})
        finally:
            s.close()

    return {
        "label": label,
        "ts": datetime.now(timezone.utc).isoformat(),
        "scope": ["workbench", "ollama_loopback"],
        "claim": "default-deny intent; evidence artefact — not CERT / not accreditation",
        "local_probes": probes,
        "note": (
            "Demo Monitor A = start/stop loopback snapshot on workbench+Ollama. "
            "Evidence artefact — not CERT. Not OS/firewall WAN forensics "
            "(add host capture in jury runbook for full WP-13 D1)."
        ),
    }


def start() -> dict[str, Any]:
    sid = uuid.uuid4().hex[:12]
    snap = _snapshot("start")
    path = _sess_dir() / f"{sid}.json"
    path.write_text(json.dumps({"start": snap, "stop": None}, indent=2), encoding="utf-8")
    log_event("monitor_a_start", session_id=sid, path=str(path))
    return {"ok": True, "session_id": sid, "start": snap}


def stop(session_id: str) -> dict[str, Any]:
    path = _sess_dir() / f"{session_id}.json"
    if not path.exists():
        return {"ok": False, "error": "monitor_session_not_found", "session_id": session_id}
    sess = json.loads(path.read_text(encoding="utf-8"))
    snap = _snapshot("stop")
    sess["stop"] = snap
    pack = {
        "session_id": session_id,
        "start": sess["start"],
        "stop": snap,
        "not_cert": True,
    }
    raw = json.dumps(pack, sort_keys=True, ensure_ascii=False)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    pack["sha256"] = digest
    out_path = ARTIFACTS_DIR / f"monitor-a-{session_id}.json"
    out_path.write_text(json.dumps(pack, indent=2), encoding="utf-8")
    path.write_text(json.dumps(sess, indent=2), encoding="utf-8")
    log_event("monitor_a_stop", session_id=session_id, path=str(out_path), sha256=digest)
    return {"ok": True, "path": str(out_path), "pack": pack}
