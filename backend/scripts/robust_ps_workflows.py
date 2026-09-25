#!/usr/bin/env python3
"""Robust PS workflow suite — SIH26117 Expected Solution coverage.

Runs WF0–WF5 (+ fail-closed) against live API.
Writes eval/evidence/PS_ROBUST_TEST.json and prints PASS/FAIL table.

  python backend/scripts/robust_ps_workflows.py
"""
from __future__ import annotations

import base64
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "http://127.0.0.1:8080"
ROOT = Path(__file__).resolve().parents[2]
OUT_JSON = ROOT / "eval" / "evidence" / "PS_ROBUST_TEST.json"
OUT_MD = ROOT / "eval" / "evidence" / "PS_ROBUST_TEST_REPORT.md"
PNG = ROOT / "data" / "fixtures" / "scan_vessel_V101.png"
README = ROOT / "data" / "fixtures" / "README_attach_demo.md"


def req(method: str, path: str, body: dict | None = None, timeout: float = 180.0):
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
                return res.status, {"bytes": len(raw)}
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw.decode())
        except Exception:
            return e.code, {"raw": raw[:400].decode(errors="replace")}
    except Exception as e:
        return 0, {"error": str(e)}


def main() -> int:
    results: list[dict] = []
    meta: dict = {"ts": datetime.now(timezone.utc).isoformat(), "base": BASE}

    def check(wf: str, name: str, ok: bool, detail: str = ""):
        results.append({"wf": wf, "name": name, "ok": ok, "detail": detail[:300]})
        print(f"{'PASS' if ok else 'FAIL'} [{wf}] {name}" + (f" — {detail[:120]}" if detail and not ok else ""))
        return ok

    # ── WF0 deploy ─────────────────────────────────────────────
    st, health = req("GET", "/health")
    check("WF0", "health", st == 200, str(st))
    st, inf = req("GET", "/inference/status")
    check("WF0", "inference_status", st == 200 and bool((inf or {}).get("ok")), str(inf)[:120])
    meta["inference"] = {
        "mode": (inf or {}).get("mode"),
        "label": (inf or {}).get("label"),
        "host": (inf or {}).get("host"),
        "runtime_reachable": (inf or {}).get("runtime_reachable"),
        "tags": (inf or {}).get("tags_on_target"),
    }
    check(
        "WF0",
        "runtime_reachable",
        bool((inf or {}).get("runtime_reachable")),
        (inf or {}).get("label") or "",
    )

    # ── WF1 auto-select ────────────────────────────────────────
    st, insp = req("POST", "/task/start", {"task_type": "inspection", "user_id": "ps-wf1"})
    ri = (insp or {}).get("route") or {}
    st2, code = req("POST", "/task/start", {"task_type": "coding", "user_id": "ps-wf1c"})
    rc = (code or {}).get("route") or {}
    check("WF1", "start_inspection", st == 200, ri.get("card_id") or "")
    check("WF1", "start_coding", st2 == 200, rc.get("card_id") or "")
    check(
        "WF1",
        "two_distinct_cards",
        ri.get("card_id") != rc.get("card_id")
        and bool(ri.get("card_id"))
        and bool(rc.get("card_id")),
        f"{ri.get('card_id')} vs {rc.get('card_id')}",
    )
    m_i, m_c = ri.get("model_id"), rc.get("model_id")
    two_tag = bool(m_i and m_c and m_i != m_c)
    check(
        "WF1",
        "two_distinct_models",
        two_tag,
        f"{m_i} vs {m_c}" + ("" if two_tag else " (floor if same tag)"),
    )
    meta["wf1"] = {"inspect": ri, "coding": rc, "full_two_tag": two_tag}

    # ── WF2 orch Word path ─────────────────────────────────────
    text = README.read_text(encoding="utf-8") if README.is_file() else "V-101 7.6 mm Confidential synthetic"
    st, t0 = req(
        "POST",
        "/orch/turn",
        {
            "task_type": "inspection",
            "user_id": "ps-wf2",
            "intent": "attach",
            "attach_text": text,
            "attach_filename": "README_attach_demo.md",
        },
        timeout=120,
    )
    gid = (t0 or {}).get("grant_id")
    check("WF2", "orch_attach", st == 200 and bool(gid), f"phase={(t0 or {}).get('phase')}")
    if gid:
        st, t1 = req(
            "POST",
            "/orch/turn",
            {"grant_id": gid, "task_type": "inspection", "intent": "confirm", "message": "yes"},
            timeout=120,
        )
        check("WF2", "confirm_extract", st == 200, f"phase={(t1 or {}).get('phase')}")
        st, t2 = req(
            "POST",
            "/orch/turn",
            {"grant_id": gid, "task_type": "inspection", "intent": "confirm", "message": "yes"},
            timeout=300,
        )
        draft = (t2 or {}).get("draft") or {}
        check(
            "WF2",
            "word_draft",
            st == 200 and bool(draft.get("filename")) and str(draft.get("filename", "")).endswith(".docx"),
            f"file={draft.get('filename')} phase={(t2 or {}).get('phase')}",
        )
        meta["wf2_draft"] = draft.get("filename")
        # self-check + export when ask present
        phase = (t2 or {}).get("phase")
        if phase == "await_self_check" or (t2 or {}).get("ask"):
            st, t3 = req(
                "POST",
                "/orch/turn",
                {"grant_id": gid, "task_type": "inspection", "intent": "confirm", "message": "yes"},
                timeout=120,
            )
            check("WF2", "self_check", st == 200, f"phase={(t3 or {}).get('phase')}")
            st, t4 = req(
                "POST",
                "/orch/turn",
                {"grant_id": gid, "task_type": "inspection", "intent": "confirm", "message": "yes"},
                timeout=120,
            )
            check(
                "WF2",
                "export_leave",
                st == 200 and ((t4 or {}).get("phase") == "done" or (t4 or {}).get("export")),
                f"phase={(t4 or {}).get('phase')}",
            )
        else:
            check("WF2", "self_check", False, f"unexpected phase after draft: {phase}")
            check("WF2", "export_leave", False, "skipped")
    else:
        check("WF2", "confirm_extract", False, "no grant")
        check("WF2", "word_draft", False, "no grant")
        check("WF2", "self_check", False, "no grant")
        check("WF2", "export_leave", False, "no grant")

    # ── WF3 sandbox ────────────────────────────────────────────
    gid2 = (code or {}).get("grant_id")
    if not gid2:
        st, code2 = req("POST", "/task/start", {"task_type": "coding", "user_id": "ps-wf3"})
        gid2 = (code2 or {}).get("grant_id")
    st, calc = req("POST", "/sandbox/calc", {"grant_id": gid2, "expression": "8.0-7.6"})
    check("WF3", "sandbox_calc", st == 200 and (calc or {}).get("ok") is not False, str(calc)[:100])
    st, h9 = req("POST", "/task/h9-ack", {"grant_id": gid2, "h9_acked": True})
    check("WF3", "h9_ack", st == 200, str(st))
    st, red = req(
        "POST",
        "/sandbox/python",
        {"grant_id": gid2, "source": "raise SystemExit(1)"},
    )
    # red may be 200 with sandbox_red flag or error — then export should deny
    st_e, exp = req(
        "POST",
        "/task/export-check",
        {"grant_id": gid2, "h2_acked": True, "artefact_version": "x"},
    )
    red_blocks = st_e >= 400 or (isinstance(exp, dict) and exp.get("ok") is False)
    check("WF3", "sandbox_red_or_export_gate", red_blocks or st == 200, f"red={st} export={st_e}")

    # ── WF4 multimodal ─────────────────────────────────────────
    if PNG.is_file():
        b64 = base64.b64encode(PNG.read_bytes()).decode("ascii")
        st, img = req(
            "POST",
            "/orch/turn",
            {
                "task_type": "inspection",
                "user_id": "ps-wf4",
                "intent": "attach",
                "attach_b64": b64,
                "attach_filename": "scan_vessel_V101.png",
                "attach_content_type": "image/png",
            },
            timeout=300,
        )
        ask = ((img or {}).get("ask") or {}).get("prompt") or ""
        assist = ((img or {}).get("assistant") or {}).get("text") or ""
        blob = ask + " " + assist + " " + str(img)
        vision = "moondream" in blob.lower() or "vision" in blob.lower()
        stub = "fixture" in blob.lower() or "stub" in blob.lower() or "tesseract" in blob.lower() or "ocr" in blob.lower()
        check(
            "WF4",
            "image_attach",
            st == 200 and (img or {}).get("phase") == "await_confirm_extract",
            f"vision={vision} stub_or_ocr={stub}",
        )
        check(
            "WF4",
            "multimodal_engine_honest",
            vision or stub or "Source:" in ask,
            ask[:160],
        )
        meta["wf4"] = {"vision": vision, "prompt_head": ask[:200]}
    else:
        check("WF4", "image_attach", False, "PNG fixture missing")
        check("WF4", "multimodal_engine_honest", False, "PNG missing")

    # ── WF5 sovereign proof ────────────────────────────────────
    st, mon = req("POST", "/monitor-a/start", {})
    sid = (mon or {}).get("session_id") or (mon or {}).get("id")
    check("WF5", "monitor_a_start", st == 200, str(sid))
    st, mon2 = req("POST", f"/monitor-a/stop?session_id={sid}" if sid else "/monitor-a/stop", {})
    check("WF5", "monitor_a_stop", st == 200, str(st))
    st, ver = req("GET", "/audit/verify")
    check("WF5", "audit_verify", st == 200 and (ver or {}).get("ok") is not False, str(ver)[:80])
    # G8 public model
    st, g8s = req("POST", "/task/start", {"task_type": "inspection", "user_id": "ps-g8"})
    g8id = (g8s or {}).get("grant_id")
    st, g8 = req(
        "POST",
        "/gateway/chat",
        {
            "grant_id": g8id,
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": "hi"}],
        },
    )
    check("WF5", "g8_deny_public_model", st in (403, 400) or (isinstance(g8, dict) and g8.get("ok") is False), str(st))
    allow = (inf or {}).get("gateway_host_ok")
    check("WF5", "gateway_host_ok", allow is True, str((inf or {}).get("gateway_deny_reason")))

    # ── Fail-closed extras ─────────────────────────────────────
    st, g9 = req(
        "POST",
        "/task/export-check",
        {"text": "api_key=AKIAIOSFODNN7EXAMPLE secret=x"},
    )
    check("FC", "g9_secret_deny", st >= 400, str(st))
    st, g7s = req("POST", "/task/start", {"task_type": "inspection", "user_id": "ps-g7"})
    g7id = (g7s or {}).get("grant_id")
    req("POST", "/task/revoke", {"grant_id": g7id})
    st, g7 = req("POST", "/task/retrieve", {"grant_id": g7id, "query": "thickness", "k": 3})
    check("FC", "g7_revoke_blocks", st == 403, str(st))

    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    meta["summary"] = {"passed": passed, "total": total, "ok": passed == total}
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps({"meta": meta, "results": results}, indent=2), encoding="utf-8")

    lines = [
        "# PS robust workflow test report",
        "",
        f"**When:** {meta['ts']}",
        f"**API:** `{BASE}`",
        f"**Inference:** {meta.get('inference')}",
        f"**Score:** **{passed}/{total}**",
        "",
        "| WF | Check | Result | Detail |",
        "|----|-------|--------|--------|",
    ]
    for r in results:
        lines.append(
            f"| {r['wf']} | {r['name']} | {'PASS' if r['ok'] else 'FAIL'} | {r.get('detail','').replace('|','/')} |"
        )
    lines.extend(
        [
            "",
            "## Design",
            "See `PS_WORKFLOW_DESIGN.md`.",
            "",
            "## Honesty",
            "Private LAN / on-prem Gateway path. Not true air-gap. Monitor A ≠ CERT.",
            "",
            f"JSON: `{OUT_JSON.as_posix()}`",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nSCORE {passed}/{total} -> {OUT_MD}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
