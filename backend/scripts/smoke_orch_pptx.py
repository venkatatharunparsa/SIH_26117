"""Smoke: orch attach → confirm extract → confirm cites → PPTX."""
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
    c = httpx.Client(timeout=60.0)

    # 1 chat via orch (not gateway)
    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "task_type": "inspection",
            "user_id": "smoke-orch",
            "intent": "message",
            "message": "hi",
            "messages": [{"role": "user", "content": "hi"}],
        },
    )
    print("CHAT", r.status_code)
    chat = r.json()
    print(json.dumps({k: chat.get(k) for k in (
        "ok", "grant_id", "phase", "orchestrator", "error", "note",
        "history_len", "history_window", "context_key",
    )}, indent=2))
    if r.status_code >= 400 and chat.get("error") not in (None, "gateway_deny"):
        # LLM may be down — still require orch spine + grant
        pass
    gid = chat.get("grant_id")
    if not gid:
        print("FAIL: no grant from orch chat")
        return 1
    assert chat.get("orchestrator") is True
    # Window semantics (server may still open grant even if LLM deny)
    if chat.get("history_window") is not None:
        assert chat["history_window"] == 10
    if chat.get("context_key"):
        assert str(chat["context_key"]).startswith("kwb-workbench/")

    # 2 attach
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
    print("ATTACH", r.status_code, att.get("phase"), "cites", len(att.get("cites") or []))
    assert r.status_code == 200, att
    assert att.get("ask", {}).get("confirm_action") == "confirm_extract"
    assert (att.get("cites") or att.get("match_notes")), "expected company doc hits"

    # 3 confirm extract
    r = c.post(
        f"{BASE}/orch/turn",
        json={"grant_id": gid, "intent": "confirm", "message": ""},
    )
    h1 = r.json()
    print("CONFIRM_EXTRACT", r.status_code, h1.get("phase"))
    assert r.status_code == 200, h1
    assert h1.get("ask", {}).get("confirm_action") == "confirm_cites"

    # 4 confirm cites → LLM polish → Word .docx (Expected Solution)
    r = c.post(
        f"{BASE}/orch/turn",
        json={"grant_id": gid, "intent": "confirm", "message": ""},
    )
    draft = r.json()
    print("WORD", r.status_code, draft.get("draft"))
    assert r.status_code == 200, draft
    assert (draft.get("draft") or {}).get("format") == "docx", draft
    fn = (draft.get("draft") or {}).get("filename")
    assert fn and fn.endswith(".docx"), draft
    path = ROOT / "workspace" / "artifacts" / fn
    assert path.is_file(), path
    print("WROTE", path)

    # 5 self-check + export
    r = c.post(
        f"{BASE}/orch/turn",
        json={"grant_id": gid, "intent": "confirm", "message": ""},
    )
    print("SELF_CHECK", r.status_code, r.json().get("phase"))
    r = c.post(
        f"{BASE}/orch/turn",
        json={"grant_id": gid, "intent": "confirm", "message": ""},
    )
    leave = r.json()
    print("EXPORT", r.status_code, leave.get("leave_ready"), leave.get("grant_revoked"))
    assert r.status_code == 200, leave
    assert leave.get("leave_ready") is True

    print("SMOKE OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except httpx.ConnectError:
        print("API not up — start uvicorn then re-run", file=sys.stderr)
        raise SystemExit(2)
