"""Endpoint + URL validation matrix for SIH26117 KWB.
Run with API up: python backend/scripts/validate_endpoints.py
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE = "http://127.0.0.1:8080"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "eval" / "evidence" / "ENDPOINT_VALIDATE.json"


def req(method: str, path: str, body: dict | None = None, binary: bool = False) -> tuple[int, dict | str]:
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    r = urllib.request.Request(f"{BASE}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as res:
            raw = res.read()
            if binary:
                return res.status, f"bytes:{len(raw)}"
            try:
                return res.status, json.loads(raw.decode())
            except json.JSONDecodeError:
                return res.status, raw[:200].decode(errors="replace")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw.decode())
        except Exception:
            return e.code, raw[:200].decode(errors="replace")
    except Exception as e:
        return 0, str(e)


def main() -> int:
    rows: list[dict] = []

    def add(name: str, method: str, path: str, expect: str, body=None, check=None, binary=False):
        code, data = req(method, path, body, binary=binary)
        ok = False
        note = ""
        if expect == "2xx":
            ok = 200 <= code < 300
        elif expect == "4xx":
            ok = 400 <= code < 500
        if check and ok:
            try:
                ok = bool(check(data))
            except Exception as e:
                ok = False
                note = str(e)
        rows.append(
            {
                "name": name,
                "method": method,
                "url": f"{BASE}{path}",
                "status": code,
                "expect": expect,
                "ok": ok,
                "note": note or (str(data)[:120] if not ok else ""),
            }
        )
        print(f"{'PASS' if ok else 'FAIL'} {method} {path} -> {code}")

    # Discovery
    add("root", "GET", "/", "2xx", check=lambda d: d.get("primary_desk", "").startswith("apps/kwb-app"))
    add("health", "GET", "/health", "2xx", check=lambda d: d.get("ok") is True and "kwb-app" in str(d.get("desk", "")))
    add("cards", "GET", "/cards", "2xx")
    add("runtime", "GET", "/runtime/status", "2xx")
    add("audit_recent", "GET", "/audit/recent?limit=5", "2xx")
    add("mcp_status", "GET", "/mcp/status", "2xx")

    # Happy path slice
    code, start = req("POST", "/task/start", {"task_type": "inspection", "user_id": "validate"})
    rows.append({"name": "task_start", "method": "POST", "url": f"{BASE}/task/start", "status": code, "expect": "2xx", "ok": 200 <= code < 300})
    print(f"{'PASS' if 200 <= code < 300 else 'FAIL'} POST /task/start -> {code}")
    gid = (start or {}).get("grant_id") if isinstance(start, dict) else None

    if gid:
        add("h1", "POST", "/task/h1-confirm", "2xx", {"grant_id": gid, "extract_text": "FX validate", "h1_acked": True})
        add("retrieve", "POST", "/task/retrieve", "2xx", {"grant_id": gid, "query": "thickness", "k": 3})
        add("h7", "POST", "/task/h7-ack", "2xx", {"grant_id": gid, "h7_acked": True})
        code, draft = req(
            "POST",
            "/task/inspect-draft",
            {
                "grant_id": gid,
                "title": "Validate DRAFT",
                "findings": "Measured 7.6 mm below 8.0 mm. Confidential synthetic.",
                "query_for_cites": "thickness",
                "h7_acked": True,
            },
        )
        ok = 200 <= code < 300
        rows.append({"name": "inspect_draft", "method": "POST", "url": f"{BASE}/task/inspect-draft", "status": code, "expect": "2xx", "ok": ok})
        print(f"{'PASS' if ok else 'FAIL'} POST /task/inspect-draft -> {code}")
        fn = (draft or {}).get("filename") if isinstance(draft, dict) else None
        ver = (draft or {}).get("artefact_version") if isinstance(draft, dict) else None
        if fn:
            add("artifacts", "GET", f"/artifacts/{fn}?grant_id={gid}", "2xx", binary=True)
            add("h2", "POST", "/task/h2-ack", "2xx", {"grant_id": gid, "draft_filename": fn, "artefact_version": ver})
            add(
                "export",
                "POST",
                "/task/export",
                "2xx",
                {"grant_id": gid, "draft_filename": fn, "h2_acked": True, "artefact_version": ver},
            )
            add("leave_pack", "GET", f"/task/leave-pack?grant_id={gid}&draft_filename={fn}", "2xx", binary=True)

    # Fail-closed samples
    add("g8_deny", "POST", "/gateway/chat", "4xx", {"grant_id": gid or "x", "model": "gpt-4o", "messages": [{"role": "user", "content": "ping"}]})
    add("g9_deny", "POST", "/task/export-check", "4xx", {"text": "api_key=AKIAIOSFODNN7EXAMPLE"})
    add("mon_a_start", "POST", "/monitor-a/start", "2xx", {})

    passed = sum(1 for r in rows if r["ok"])
    total = len(rows)
    report = {
        "ok": passed == total,
        "passed": passed,
        "total": total,
        "api_base": BASE,
        "primary_desk": "apps/kwb-app",
        "rows": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\n{passed}/{total} -> {OUT}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
