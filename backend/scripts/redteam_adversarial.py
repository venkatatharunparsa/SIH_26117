#!/usr/bin/env python3
"""Adversarial / red-team suite for KWB API (localhost attack surface).

Expect: denials and safe failures. Unexpected PASS = vulnerability finding.
Writes eval/evidence/REDTEAM_ADV_REPORT.md + REDTEAM_ADV.json

  python backend/scripts/redteam_adversarial.py
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "http://127.0.0.1:8080"
ROOT = Path(__file__).resolve().parents[2]
OUT_JSON = ROOT / "eval" / "evidence" / "REDTEAM_ADV.json"
OUT_MD = ROOT / "eval" / "evidence" / "REDTEAM_ADV_REPORT.md"


def req(method: str, path: str, body: dict | None = None, timeout: float = 60.0):
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    r = urllib.request.Request(
        f"{BASE}{path}", data=data, headers=headers, method=method
    )
    try:
        with urllib.request.urlopen(r, timeout=timeout) as res:
            raw = res.read()
            try:
                return res.status, json.loads(raw.decode())
            except Exception:
                return res.status, {"bytes": len(raw), "raw_head": raw[:80].decode(errors="replace")}
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw.decode())
        except Exception:
            return e.code, {"raw": raw[:300].decode(errors="replace")}
    except Exception as e:
        return 0, {"error": str(e)}


def main() -> int:
    findings: list[dict] = []
    meta = {"ts": datetime.now(timezone.utc).isoformat(), "base": BASE}

    def expect_deny(aid: str, name: str, st: int, data, *, ok_statuses=(400, 403, 404, 422)):
        """Attack should be blocked."""
        blocked = st in ok_statuses or (
            isinstance(data, dict) and data.get("ok") is False
        )
        sev = "ok" if blocked else "HIGH"
        findings.append(
            {
                "id": aid,
                "name": name,
                "expect": "deny",
                "status": st,
                "blocked": blocked,
                "severity": sev if not blocked else "info",
                "detail": str(data)[:220],
            }
        )
        mark = "BLOCKED" if blocked else "OPEN"
        print(f"{mark} [{aid}] {name} -> {st}")
        return blocked

    def expect_safe(aid: str, name: str, ok: bool, detail: str = "", sev_if_bad="HIGH"):
        findings.append(
            {
                "id": aid,
                "name": name,
                "expect": "safe",
                "status": 0,
                "blocked": ok,
                "severity": "info" if ok else sev_if_bad,
                "detail": detail[:220],
            }
        )
        print(f"{'OK' if ok else 'OPEN'} [{aid}] {name}")
        return ok

    # Setup: real grant + maybe a draft name from artifacts dir
    st, start = req("POST", "/task/start", {"task_type": "inspection", "user_id": "redteam"})
    gid = (start or {}).get("grant_id")
    if not gid:
        print("FATAL: cannot open grant")
        return 2

    # ── A. Gateway / egress ───────────────────────────────────
    st, d = req(
        "POST",
        "/gateway/chat",
        {
            "grant_id": gid,
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": "leak"}],
        },
    )
    expect_deny("A1", "public model gpt-4o", st, d)

    st, d = req(
        "POST",
        "/gateway/chat",
        {
            "grant_id": gid,
            "model": "claude-3-opus",
            "messages": [{"role": "user", "content": "x"}],
        },
    )
    expect_deny("A2", "public model claude", st, d)

    # Try override base_url if API accepts extra fields (should ignore / deny)
    st, d = req(
        "POST",
        "/gateway/chat",
        {
            "grant_id": gid,
            "model": "llama3.2:3b",
            "base_url": "https://api.openai.com",
            "messages": [{"role": "user", "content": "x"}],
        },
    )
    # Either 403 deny or 200 to local only — must NOT succeed against openai
    leaked = st == 200 and isinstance(d, dict) and "openai" in str(d.get("base_url", "")).lower()
    expect_safe(
        "A3",
        "base_url override to openai ignored",
        not leaked,
        f"st={st} base={d.get('base_url') if isinstance(d, dict) else d}",
    )

    # ── B. Grant / ACL ────────────────────────────────────────
    st, d = req("POST", "/task/retrieve", {"grant_id": "deadbeef", "query": "x", "k": 3})
    expect_deny("B1", "fake grant retrieve", st, d)

    st, d = req(
        "POST",
        "/sandbox/calc",
        {"grant_id": "000000000000", "expression": "1+1"},
    )
    expect_deny("B2", "fake grant sandbox", st, d)

    req("POST", "/task/revoke", {"grant_id": gid})
    st, d = req("POST", "/task/retrieve", {"grant_id": gid, "query": "thickness", "k": 3})
    expect_deny("B3", "revoked grant retrieve", st, d, ok_statuses=(403,))

    st, d = req(
        "POST",
        "/orch/turn",
        {"grant_id": gid, "task_type": "inspection", "intent": "message", "message": "hi"},
    )
    expect_deny("B4", "revoked grant orch", st, d, ok_statuses=(403, 400))

    # new grant for further tests
    st, start2 = req("POST", "/task/start", {"task_type": "inspection", "user_id": "redteam2"})
    gid2 = (start2 or {}).get("grant_id")

    # ── C. Path traversal / artifacts ─────────────────────────
    for trav in (
        "..%2F..%2F..%2Fwindows%2Fwin.ini",
        "../../../etc/passwd",
        "..\\..\\..\\windows\\win.ini",
        "....//....//....//windows/win.ini",
    ):
        st, d = req("GET", f"/artifacts/{trav}")
        expect_deny(f"C1-{trav[:12]}", f"path traversal {trav[:40]}", st, d)

    # List any draft and try download WITHOUT grant_id
    arts = list((ROOT / "workspace" / "artifacts").glob("draft-*.docx"))
    if arts:
        name = arts[0].name
        st, d = req("GET", f"/artifacts/{name}")
        # Finding: if 200 without grant — OPEN (we will fix to require grant)
        open_dl = st == 200
        findings.append(
            {
                "id": "C2",
                "name": "artifact download without grant_id",
                "expect": "deny",
                "status": st,
                "blocked": not open_dl,
                "severity": "HIGH" if open_dl else "info",
                "detail": f"file={name} st={st}",
            }
        )
        print(f"{'OPEN' if open_dl else 'BLOCKED'} [C2] artifact without grant -> {st}")

        st, d = req("GET", f"/artifacts/{name}?grant_id=wronggrant")
        expect_deny("C3", "artifact wrong grant_id", st, d, ok_statuses=(403, 404))
    else:
        expect_safe("C2", "no draft to test ungated download", True, "skipped")

    # ── D. Secrets / export ───────────────────────────────────
    st, d = req(
        "POST",
        "/task/export-check",
        {"text": "aws_access_key_id=AKIAIOSFODNN7EXAMPLE\npassword=hunter2"},
    )
    expect_deny("D1", "secret export-check", st, d, ok_statuses=(400,))

    st, d = req(
        "POST",
        "/task/export-check",
        {"text": "sk-proj-abcdefghijklmnopqrstuvwxyz0123456789"},
    )
    expect_deny("D2", "openai-like key export-check", st, d, ok_statuses=(400,))

    # ── E. Sandbox abuse ──────────────────────────────────────
    st, start3 = req("POST", "/task/start", {"task_type": "coding", "user_id": "redteam-sb"})
    gids = (start3 or {}).get("grant_id")
    st, d = req(
        "POST",
        "/sandbox/python",
        {
            "grant_id": gids,
            "source": (
                "import urllib.request\n"
                "try:\n"
                "  r=urllib.request.urlopen('https://example.com', timeout=3)\n"
                "  print('NET_OK', r.status)\n"
                "except Exception as e:\n"
                "  print('NET_DENY', type(e).__name__)\n"
            ),
        },
        timeout=30,
    )
    stdout = str((d or {}).get("stdout") or "") if isinstance(d, dict) else ""
    net_ok = "NET_OK" in stdout
    expect_safe(
        "E1",
        "sandbox network to example.com denied",
        not net_ok and ("NET_DENY" in stdout or "sandbox_network" in str(d).lower()),
        f"stdout={stdout[:120]} network={(d or {}).get('network') if isinstance(d, dict) else ''}",
        sev_if_bad="MED",
    )

    st, d = req(
        "POST",
        "/sandbox/python",
        {
            "grant_id": gids,
            "source": "open(r'C:\\Windows\\win.ini').read()[:50]",
        },
        timeout=30,
    )
    leaked_win = isinstance(d, dict) and "fonts" in str(d.get("stdout", "")).lower()
    expect_safe(
        "E2",
        "sandbox read win.ini blocked or empty",
        not leaked_win,
        str(d)[:120],
        sev_if_bad="MED",
    )

    st, d = req(
        "POST",
        "/sandbox/python",
        {"grant_id": gids, "source": "raise SystemExit(1)"},
    )
    # then try export with sandbox red
    st, d = req(
        "POST",
        "/task/export",
        {
            "grant_id": gids,
            "draft_filename": "nope.docx",
            "h2_acked": True,
            "artefact_version": "x",
        },
    )
    expect_deny("E3", "export after sandbox-red", st, d)

    # ── F. Orch / attach abuse ────────────────────────────────
    st, d = req(
        "POST",
        "/orch/turn",
        {
            "task_type": "inspection",
            "user_id": "redteam-att",
            "intent": "attach",
            "attach_b64": "!!!not-base64!!!",
            "attach_filename": "x.png",
        },
    )
    expect_deny("F1", "invalid attach_b64", st, d, ok_statuses=(400,))

    st, d = req(
        "POST",
        "/orch/turn",
        {
            "task_type": "inspection",
            "user_id": "redteam-empty",
            "intent": "attach",
            "attach_text": "   ",
            "attach_filename": "empty.txt",
        },
    )
    expect_deny("F2", "empty attach", st, d, ok_statuses=(400,))

    # ── G. HITL bypass ────────────────────────────────────────
    st, s4 = req("POST", "/task/start", {"task_type": "inspection", "user_id": "redteam-hitl"})
    gid4 = (s4 or {}).get("grant_id")
    # draft without h1/h7 may still work on /task/inspect-draft — check export without h2
    st, d = req(
        "POST",
        "/task/inspect-draft",
        {
            "grant_id": gid4,
            "findings": "V-101 thickness 7.6 mm Confidential synthetic",
            "query": "thickness",
        },
        timeout=180,
    )
    draft_name = (d or {}).get("filename") if isinstance(d, dict) else None
    if draft_name:
        st, d = req(
            "POST",
            "/task/export",
            {
                "grant_id": gid4,
                "draft_filename": draft_name,
                "h2_acked": False,
                "artefact_version": (d or {}).get("artefact_version") or "0",
            },
        )
        expect_deny("G1", "export without H2", st, d)
    else:
        expect_safe("G1", "inspect-draft for H2 test", False, f"st={st} no draft", "MED")

    # ── H. MCP / surface ──────────────────────────────────────
    st, d = req("POST", "/mcp/call", {"name": "not_a_real_tool", "arguments": {}})
    # 403 grant_required (no grant) OR 200 ok:false allowlist miss both OK
    expect_deny("H1", "unknown MCP tool", st, d, ok_statuses=(400, 403, 404, 200))
    if st == 200 and isinstance(d, dict) and d.get("ok") is False:
        findings[-1]["blocked"] = True
        findings[-1]["severity"] = "info"

    st, d = req(
        "POST",
        "/mcp/call",
        {"name": "echo_tool", "arguments": {"text": "ping"}},
    )
    expect_deny("H2", "MCP call without grant_id", st, d, ok_statuses=(403, 400, 422))

    # ── I. Monitor / audit integrity ──────────────────────────
    st, d = req("GET", "/audit/verify")
    expect_safe("I1", "audit chain verifies", st == 200 and (d or {}).get("ok") is not False, str(d)[:80])

    open_count = sum(1 for f in findings if not f["blocked"] and f.get("severity") in ("HIGH", "MED"))
    high = [f for f in findings if not f["blocked"] and f.get("severity") == "HIGH"]
    med = [f for f in findings if not f["blocked"] and f.get("severity") == "MED"]

    meta["open_high"] = len(high)
    meta["open_med"] = len(med)
    meta["findings_n"] = len(findings)

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps({"meta": meta, "findings": findings}, indent=2), encoding="utf-8"
    )

    lines = [
        "# KWB adversarial red-team report",
        "",
        f"**When:** {meta['ts']}",
        f"**Target:** `{BASE}` (localhost workbench API)",
        f"**Open HIGH:** {len(high)} · **Open MED:** {len(med)}",
        "",
        "| ID | Attack | Result | Sev | Detail |",
        "|----|--------|--------|-----|--------|",
    ]
    for f in findings:
        res = "BLOCKED" if f["blocked"] else "OPEN"
        lines.append(
            f"| {f['id']} | {f['name']} | {res} | {f.get('severity')} | {str(f.get('detail','')).replace('|','/')[:80]} |"
        )
    lines.extend(
        [
            "",
            "## Open issues to fix",
            "",
        ]
    )
    for f in high + med:
        lines.append(f"- **{f['id']}** ({f['severity']}): {f['name']} — {f.get('detail')}")
    if not high and not med:
        lines.append("- None at HIGH/MED from this pass.")
    lines.extend(
        [
            "",
            "## Scope note",
            "API binds 127.0.0.1 — attacks assume local process access (same as desk).",
            "True network isolation / WAN=0 not proven here.",
            "",
            f"JSON: `{OUT_JSON.as_posix()}`",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nOPEN high={len(high)} med={len(med)} -> {OUT_MD}")
    return 1 if high else 0


if __name__ == "__main__":
    sys.exit(main())
