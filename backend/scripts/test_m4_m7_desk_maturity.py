"""M4-M7 desk maturity — H7 server, audit denies, fail-closed injects.

Requires API on 127.0.0.1:8080 with latest code.
Run: python scripts/test_m4_m7_desk_maturity.py
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8080"


def post(path: str, body: dict) -> tuple[int, dict]:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        BASE + path,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw": raw}


def get(path: str) -> tuple[int, dict]:
    req = urllib.request.Request(BASE + path, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw": raw}


def detail_error(body: dict) -> str:
    d = body.get("detail") if isinstance(body, dict) else body
    if isinstance(d, dict):
        return str(d.get("error") or d)
    return str(d or body)


def main() -> int:
    print("=== M4-M7 desk maturity integration ===")

    st, start = post("/task/start", {"task_type": "inspection", "user_id": "m4m7-test"})
    assert st == 200, start
    gid = start["grant_id"]
    print(f"OK start grant={gid}")

    st, h1 = post(
        "/task/h1-confirm",
        {"grant_id": gid, "extract_text": "V-101 7.6mm FX-EXT-01", "h1_acked": True},
    )
    assert st == 200, h1
    print("OK h1")

    st, ret = post(
        "/task/retrieve",
        {"grant_id": gid, "query": "thickness vessel minimum", "k": 5},
    )
    assert st == 200, ret
    cites = ret.get("cites") or []
    assert cites, f"expected cites for H7 path, got {ret}"
    print(f"OK retrieve cites={len(cites)}")

    # M6 — client h7_acked theatre must NOT unlock draft
    st, denied = post(
        "/task/inspect-draft",
        {
            "grant_id": gid,
            "title": "M4-M7 draft (should deny)",
            "findings": "Measured 7.6 mm below 8.0 mm. Confidential synthetic.",
            "query_for_cites": "thickness vessel minimum",
            "h7_acked": True,
        },
    )
    assert st == 400, (st, denied)
    assert "h7_required" in detail_error(denied), denied
    print("PASS M6 inspect-draft without server h7-ack -> 400 h7_required")

    st, h7 = post("/task/h7-ack", {"grant_id": gid})
    assert st == 200 and h7.get("ok") and h7.get("h7_acked"), h7
    print("OK h7-ack server")

    st, draft = post(
        "/task/inspect-draft",
        {
            "grant_id": gid,
            "title": "M4-M7 draft OK",
            "findings": "Measured 7.6 mm below 8.0 mm. Confidential synthetic.",
            "query_for_cites": "thickness vessel minimum",
            "h7_acked": False,
        },
    )
    assert st == 200, draft
    assert draft.get("filename"), draft
    print(f"PASS M6 draft after h7-ack -> {draft['filename']}")

    # M5 — export-check secret
    st, sec = post(
        "/task/export-check",
        {"text": "api_key=sk-abcdefghijklmnopqrstuvwxyz"},
    )
    assert st == 200 and sec.get("ok") is False, sec
    assert sec.get("error") == "secret_in_draft" or "secret" in str(sec.get("error", "")), sec
    print(f"PASS M5 export-check secret ok=false error={sec.get('error')}")

    # M4 — audit recent after deny
    st, audit = get("/audit/recent?limit=80")
    assert st == 200, audit
    events = audit.get("events") or []
    kinds = {e.get("kind") for e in events}
    assert "secrets_deny" in kinds or any(
        e.get("error") == "secret_in_draft" or e.get("kind") == "secrets_deny" for e in events
    ), f"expected secrets_deny in audit, kinds={sorted(kinds)[-20:]}"
    print(f"PASS M4 audit/recent has deny event (secrets_deny) n={len(events)}")

    # M5 — gateway bad model
    st, bad = post(
        "/gateway/chat",
        {
            "grant_id": gid,
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": "hi"}],
        },
    )
    g8_ok = (st >= 400) or (
        isinstance(bad, dict)
        and (bad.get("ok") is False or bad.get("error") == "gateway_deny")
    )
    assert g8_ok, bad
    assert bad.get("error") == "gateway_deny" or st >= 400, bad
    print(f"PASS M5 gateway bad model -> gateway_deny status={st}")

    st, audit2 = get("/audit/recent?limit=80")
    assert st == 200, audit2
    ev2 = audit2.get("events") or []
    assert any(e.get("kind") == "gateway_deny" for e in ev2), [
        e.get("kind") for e in ev2[-15:]
    ]
    print("PASS M4 audit/recent includes gateway_deny after inject")

    # Leave-pack path still works without cites query (M1-M3 regression smoke)
    st, s2 = post("/task/start", {"task_type": "inspection", "user_id": "m4m7-leave"})
    assert st == 200, s2
    g2 = s2["grant_id"]
    st, _ = post(
        "/task/h1-confirm",
        {"grant_id": g2, "extract_text": "leave path", "h1_acked": True},
    )
    assert st == 200
    st, d2 = post(
        "/task/inspect-draft",
        {
            "grant_id": g2,
            "title": "Leave regression",
            "findings": "No cites query - H7 not required.",
        },
    )
    assert st == 200, d2
    print("PASS M1-M3 leave path still drafts without query_for_cites")

    print("PASS M4+M5+M6+M7 (API) - desk poll/locks/injects are UI; endpoints + H7 SoT wired.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as e:
        print("FAIL", e, file=sys.stderr)
        raise SystemExit(1)
    except urllib.error.URLError as e:
        print("FAIL API unreachable — start uvicorn on 127.0.0.1:8080:", e, file=sys.stderr)
        raise SystemExit(2)
