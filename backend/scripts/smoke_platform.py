"""Smoke: skills · roles · MCP host · specialists wiring."""
from __future__ import annotations

import json
import sys

import httpx

BASE = "http://127.0.0.1:8080"


def main() -> int:
    c = httpx.Client(timeout=60.0)
    s = c.get(f"{BASE}/skills").json()
    print("SKILLS", len(s.get("skills") or []), [x["id"] for x in s.get("skills") or []])
    assert len(s.get("skills") or []) >= 2

    r = c.get(f"{BASE}/roles").json()
    print("ROLES", [x["id"] for x in r.get("roles") or []])
    assert any(x.get("id") == "inspection_analyst" for x in r.get("roles") or [])

    m = c.get(f"{BASE}/mcp/status").json()
    print("MCP", json.dumps(m))
    assert m.get("enabled") is True, m

    # MCP tools require active grant (red-team H2)
    start = c.post(
        f"{BASE}/task/start",
        json={"task_type": "inspection", "user_id": "smoke-plat-mcp"},
    ).json()
    gid_mcp = start.get("grant_id")
    assert gid_mcp, start
    call = c.post(
        f"{BASE}/mcp/call",
        json={"name": "list_skills", "arguments": {}, "grant_id": gid_mcp},
    ).json()
    print("MCP_CALL", call.get("ok"), "n=", len(call.get("skills") or []))
    assert call.get("ok") is True

    # ungated call must fail
    bad = c.post(f"{BASE}/mcp/call", json={"name": "list_skills", "arguments": {}})
    assert bad.status_code == 403, bad.status_code

    chat = c.post(
        f"{BASE}/orch/turn",
        json={
            "task_type": "inspection",
            "user_id": "smoke-plat",
            "intent": "message",
            "message": "list skills",
        },
    ).json()
    print("ORCH_MCP", chat.get("ok"), (chat.get("assistant") or {}).get("text", "")[:120])
    assert chat.get("grant_id")
    tools = chat.get("tools") or []
    assert any(t.get("name") == "mcp_host" for t in tools), tools

    chat2 = c.post(
        f"{BASE}/orch/turn",
        json={
            "grant_id": chat["grant_id"],
            "intent": "message",
            "message": "hi",
        },
    ).json()
    print(
        "ORCH_CHAT",
        chat2.get("role", {}).get("id"),
        chat2.get("skills"),
        (chat2.get("tools") or [{}])[-1].get("skills_in_pack"),
    )
    assert chat2.get("role", {}).get("id") == "inspection_analyst"
    assert "inspection-note" in (chat2.get("skills") or [])

    print("SMOKE_PLATFORM OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except httpx.ConnectError:
        print("API not up", file=sys.stderr)
        raise SystemExit(2)
