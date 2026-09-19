"""Fail-closed inject demo — run with API up on 127.0.0.1:8080."""

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
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw": raw}


def main() -> int:
    print("=== start inspection task ===")
    st, start = post("/task/start", {"task_type": "inspection"})
    print(st, start)
    if st != 200:
        return 1
    gid = start["grant_id"]

    print("=== G8 deny public URL (via normalize — client override blocked) ===")
    # model not on card
    st, bad = post(
        "/gateway/chat",
        {
            "grant_id": gid,
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": "hi"}],
        },
    )
    print(st, bad)

    print("=== G9 secret deny ===")
    st, sec = post("/task/export-check", {"text": "api_key=sk-abcdefghijklmnopqrstuvwxyz"})
    print(st, sec)

    print("=== G7 revoke then retrieve ===")
    st, _ = post("/task/revoke", {"grant_id": gid})
    print("revoke", st)
    st, denied = post("/task/retrieve", {"grant_id": gid, "query": "thickness"})
    print(st, denied)

    print("=== audit verify ===")
    req = urllib.request.Request(BASE + "/audit/verify")
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(json.loads(resp.read().decode("utf-8")))

    print("OK — fail-closed script finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
