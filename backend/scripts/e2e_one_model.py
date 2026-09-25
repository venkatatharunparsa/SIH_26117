"""End-to-end single-laptop / one-model demo walk.

Runs inspection A→J + fail-closed + coding smoke against live API.
Writes eval/evidence/E2E_ONE_MODEL.json
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
OUT = ROOT / "eval" / "evidence" / "E2E_ONE_MODEL.json"


def req(method: str, path: str, body: dict | None = None):
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    r = urllib.request.Request(f"{BASE}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=120) as res:
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
            return e.code, {"raw": raw[:300].decode(errors="replace")}


def main() -> int:
    steps = []
    ok_all = True

    def step(name: str, method: str, path: str, body=None, expect=range(200, 300)):
        nonlocal ok_all
        st, data = req(method, path, body)
        passed = st in expect if not isinstance(expect, range) else st in expect
        if isinstance(expect, set):
            passed = st in expect
        steps.append({"name": name, "method": method, "path": path, "status": st, "ok": passed, "body_keys": list(data)[:8] if isinstance(data, dict) else type(data).__name__})
        print(f"{'PASS' if passed else 'FAIL'} {name} -> {st}")
        if not passed:
            ok_all = False
            print(f"  detail: {str(data)[:240]}")
        return st, data

    # 0 health + one-model honesty
    st, health = step("health", "GET", "/health")
    model_tags = ((health or {}).get("ollama_policy") or {}).get("adopted_chat_tags") or []

    # 1 start inspection
    st, start = step("start_inspection", "POST", "/task/start", {"task_type": "inspection", "user_id": "e2e-one"})
    gid = (start or {}).get("grant_id")
    route = (start or {}).get("route") or {}
    mid = route.get("model_id")
    card = route.get("card_id")

    # 2 h1
    step("h1", "POST", "/task/h1-confirm", {"grant_id": gid, "extract_text": "V-101 thickness 7.6 mm Confidential synthetic", "h1_acked": True})

    # 3 retrieve
    step("retrieve", "POST", "/task/retrieve", {"grant_id": gid, "query": "thickness vessel minimum", "k": 5})

    # 4 h7
    step("h7", "POST", "/task/h7-ack", {"grant_id": gid, "h7_acked": True})

    # 5 draft
    st, draft = step(
        "inspect_draft",
        "POST",
        "/task/inspect-draft",
        {
            "grant_id": gid,
            "title": "E2E one-model DRAFT",
            "findings": "Measured 7.6 mm below SOP 8.0 mm. Confidential synthetic.",
            "query_for_cites": "thickness vessel minimum",
            "h7_acked": True,
        },
    )
    fn = (draft or {}).get("filename")
    ver = (draft or {}).get("artefact_version")

    # 6 h2
    step("h2", "POST", "/task/h2-ack", {"grant_id": gid, "draft_filename": fn, "artefact_version": ver})

    # 7 stale deny BEFORE export revoke (edit bumps version; old ver must 400)
    st, edited = step(
        "draft_edit",
        "POST",
        "/task/draft-edit",
        {"grant_id": gid, "draft_filename": fn, "findings": "Edited findings after H2. Confidential synthetic.", "title": "E2E one-model DRAFT"},
    )
    ver2 = (edited or {}).get("artefact_version") or ver
    step("export_stale_deny", "POST", "/task/export", {"grant_id": gid, "draft_filename": fn, "h2_acked": True, "artefact_version": ver}, expect={400})

    # 8 export leave (new version) + downloads
    step("h2_after_edit", "POST", "/task/h2-ack", {"grant_id": gid, "draft_filename": fn, "artefact_version": ver2})
    step("export", "POST", "/task/export", {"grant_id": gid, "draft_filename": fn, "h2_acked": True, "artefact_version": ver2})
    step("artifact_download", "GET", f"/artifacts/{fn}?grant_id={gid}")
    step("leave_pack", "GET", f"/task/leave-pack?grant_id={gid}&draft_filename={fn}")

    # 9 fail-closed G8 G9 (grant may be revoked after export — still expect deny)
    step("g8_bad_model", "POST", "/gateway/chat", {"grant_id": gid, "model": "gpt-4o", "messages": [{"role": "user", "content": "x"}]}, expect={403, 400})
    step("g9_secret", "POST", "/task/export-check", {"text": "api_key=sk-abcdefghijklmnopqrstuvwxyz"}, expect={400})

    # 10 coding card (G1: floor=same model OR full=distinct models on two cards)
    st, start2 = step("start_coding", "POST", "/task/start", {"task_type": "coding", "user_id": "e2e-code"})
    route2 = (start2 or {}).get("route") or {}
    mid2 = route2.get("model_id")
    card2 = route2.get("card_id")
    g1_ok = bool(card and card2 and card != card2 and mid and mid2)
    steps.append({
        "name": "g1_two_cards",
        "ok": g1_ok,
        "card_a": card,
        "card_b": card2,
        "model_a": mid,
        "model_b": mid2,
        "mode": "full_two_tag" if mid != mid2 else "floor_single_tag_adopt",
    })
    print(f"{'PASS' if g1_ok else 'FAIL'} g1 two cards ({card}/{card2} -> {mid}/{mid2})")
    if not g1_ok:
        ok_all = False

    gid2 = (start2 or {}).get("grant_id")
    step("sandbox_calc", "POST", "/sandbox/calc", {"grant_id": gid2, "expression": "8.0-7.6"})
    step("h9", "POST", "/task/h9-ack", {"grant_id": gid2, "accept": True})

    # monitor A
    st, mon = step("mon_a_start", "POST", "/monitor-a/start", {})
    sid = (mon or {}).get("session_id") or ""
    step("mon_a_stop", "POST", f"/monitor-a/stop?session_id={sid}", {})

    # G7 revoke on fresh grant
    st, start3 = step("start_for_revoke", "POST", "/task/start", {"task_type": "inspection", "user_id": "e2e-revoke"})
    gid3 = (start3 or {}).get("grant_id")
    step("g7_revoke", "POST", "/task/revoke", {"grant_id": gid3})
    step("g7_tool_deny", "POST", "/task/retrieve", {"grant_id": gid3, "query": "thickness", "k": 2}, expect={403, 400})
    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "mode": "single_laptop_one_model",
        "ok": ok_all,
        "adopted_chat_tags": model_tags,
        "inspection_model_id": mid,
        "inspection_card_id": card,
        "coding_model_id": mid2,
        "coding_card_id": card2,
        "g1_mode": "floor_single_tag_adopt",
        "steps": steps,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\n{'PASS' if ok_all else 'FAIL'} E2E one-model -> {OUT}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
