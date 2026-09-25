"""Smoke: orch attach → confirm extract → confirm cites → LLM polish → Word .docx."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import httpx

BASE = "http://127.0.0.1:8080"
ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "data" / "fixtures" / "README_attach_demo.md"


def main() -> int:
    text = README.read_text(encoding="utf-8")
    c = httpx.Client(timeout=120.0)

    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "task_type": "inspection",
            "user_id": "smoke-word",
            "intent": "message",
            "message": "hi",
            "messages": [{"role": "user", "content": "hi"}],
        },
    )
    chat = r.json()
    print("CHAT", r.status_code, chat.get("grant_id"))
    gid = chat.get("grant_id")
    if not gid:
        print("FAIL: no grant")
        return 1

    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "grant_id": gid,
            "intent": "attach",
            "attach_text": text,
            "attach_filename": "README_attach_demo.md",
        },
    )
    att = r.json()
    print("ATTACH", r.status_code, att.get("phase"))
    assert r.status_code == 200, att

    r = c.post(f"{BASE}/orch/turn", json={"grant_id": gid, "intent": "confirm", "message": ""})
    h1 = r.json()
    print("CONFIRM_EXTRACT", r.status_code, h1.get("phase"))
    assert r.status_code == 200, h1

    r = c.post(f"{BASE}/orch/turn", json={"grant_id": gid, "intent": "confirm", "message": ""})
    draft = r.json()
    print("WORD", r.status_code)
    print(json.dumps({k: draft.get(k) for k in ("ok", "error", "phase", "draft", "polish")}, indent=2, default=str)[:2000])
    assert r.status_code == 200, draft
    assert draft.get("ok") is not False, draft
    d = draft.get("draft") or {}
    assert d.get("format") == "docx", d
    assert d.get("polished") is True, d
    fn = d.get("filename")
    assert fn and fn.endswith(".docx"), d
    path = ROOT / "workspace" / "artifacts" / fn
    assert path.is_file(), path
    print("WROTE", path)

    r = c.post(f"{BASE}/orch/turn", json={"grant_id": gid, "intent": "confirm", "message": ""})
    print("SELF_CHECK", r.status_code, r.json().get("phase"))
    r = c.post(f"{BASE}/orch/turn", json={"grant_id": gid, "intent": "confirm", "message": ""})
    leave = r.json()
    print("EXPORT", r.status_code, leave.get("leave_ready"), leave.get("grant_revoked"))
    assert leave.get("leave_ready") is True

    print("SMOKE_WORD OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except httpx.ConnectError:
        print("API not up — restart uvicorn to load word polish path", file=sys.stderr)
        raise SystemExit(2)
