"""Full execute walk for G1–G10 evidence — API on 127.0.0.1:8080.

Writes eval/evidence/*.json and updates checklist notes.
Does not invent CERT or plant approval.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8080"
ROOT = Path(__file__).resolve().parents[2]
EVID = ROOT / "eval" / "evidence"
EXTRACT = (
    "Confidential synthetic FX-EXT-01\n"
    "Asset V-101 shell course A\n"
    "Measured thickness 7.6 mm\n"
    "Compare SOP-THK-001 minimum 8.0 mm."
)


def post(path: str, body: dict | None = None) -> tuple[int, dict]:
    data = json.dumps(body or {}).encode("utf-8")
    req = urllib.request.Request(
        BASE + path,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw": raw}


def get(path: str) -> tuple[int, dict]:
    req = urllib.request.Request(BASE + path, method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))


def save(name: str, payload: dict) -> Path:
    EVID.mkdir(parents=True, exist_ok=True)
    path = EVID / name
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def main() -> int:
    results: dict[str, dict] = {}
    ts = datetime.now(timezone.utc).isoformat()

    st, health = get("/health")
    assert st == 200 and health.get("ok"), health
    results["health"] = health

    # Monitor A
    st, mon_s = post("/monitor-a/start", {})
    assert st == 200, mon_s
    sid = mon_s["session_id"]

    # G1 — two task types
    st, t1 = post("/task/start", {"task_type": "inspection", "user_id": "exec-walk"})
    assert st == 200, t1
    st, t2 = post("/task/start", {"task_type": "coding", "user_id": "exec-walk"})
    assert st == 200, t2
    g1 = {
        "routes": [
            {"task_type": "inspection", **t1["route"], "grant_id": t1["grant_id"]},
            {"task_type": "coding", **t2["route"], "grant_id": t2["grant_id"]},
        ],
        "g1_mode": "floor_single_tag_adopt"
        if t1["route"].get("model_id") == t2["route"].get("model_id")
        else "full_distinct_model_ids",
        "distinct_cards": t1["route"]["card_id"] != t2["route"]["card_id"],
    }
    assert g1["distinct_cards"], g1
    results["G1"] = g1
    save("G1_routing.json", g1)

    gid = t1["grant_id"]

    # G4 / H1
    st, h1 = post(
        "/task/h1-confirm",
        {"grant_id": gid, "extract_text": EXTRACT, "h1_acked": True},
    )
    assert st == 200, h1
    results["G4_H1"] = h1
    save("G4_h1.json", h1)

    # G6 retrieve
    st, ret = post("/task/retrieve", {"grant_id": gid, "query": "thickness vessel", "k": 5})
    assert st == 200, ret
    results["G6"] = {"verdict": ret.get("verdict"), "cite_count": len(ret.get("cites") or [])}
    save("G6_retrieve.json", ret)

    if ret.get("cites"):
        st, h7ack = post("/task/h7-ack", {"grant_id": gid})
        assert st == 200 and h7ack.get("ok"), h7ack
    # G2 draft (server H7 SoT — client h7_acked ignored)
    st, draft = post(
        "/task/inspect-draft",
        {
            "grant_id": gid,
            "title": "Inspection thickness note (DRAFT)",
            "findings": "Measured 7.6 mm below 8.0 mm min. Confidential synthetic.",
            "query_for_cites": "thickness vessel",
        },
    )
    assert st == 200, draft
    results["G2"] = {
        "filename": draft["filename"],
        "artefact_version": draft["artefact_version"],
        "status": draft.get("status"),
    }
    save("G2_draft.json", draft)

    # H2 + export leave
    st, _ = post(
        "/task/h2-ack",
        {
            "grant_id": gid,
            "draft_filename": draft["filename"],
            "artefact_version": draft["artefact_version"],
        },
    )
    assert st == 200
    st, exp = post(
        "/task/export",
        {
            "grant_id": gid,
            "draft_filename": draft["filename"],
            "h2_acked": True,
            "artefact_version": draft["artefact_version"],
        },
    )
    assert st == 200, exp
    results["export_leave"] = exp
    save("export_leave.json", exp)

    # G5 Monitor A stop
    st, mon_e = post(f"/monitor-a/stop?session_id={sid}", {})
    assert st == 200 and mon_e.get("pack", {}).get("not_cert") is True, mon_e
    results["G5"] = {
        "path": mon_e.get("path"),
        "sha256": mon_e.get("pack", {}).get("sha256"),
        "not_cert": True,
    }
    save("G5_monitor_a.json", mon_e)

    # G3 sandbox + H9 on coding grant
    gid2 = t2["grant_id"]
    st, calc = post("/sandbox/calc", {"grant_id": gid2, "expression": "8.0-7.6"})
    assert st == 200 and calc.get("ok") is True, calc
    st, h9 = post("/task/h9-ack", {"grant_id": gid2, "accept": True})
    assert st == 200, h9
    results["G3_H9"] = {"sandbox": calc, "h9": h9}
    save("G3_sandbox_h9.json", results["G3_H9"])

    # G10 sandbox-red export deny
    st, t3 = post("/task/start", {"task_type": "coding", "user_id": "g10"})
    assert st == 200
    g10id = t3["grant_id"]
    st, red = post("/sandbox/python", {"grant_id": g10id, "source": "raise SystemExit(1)"})
    assert st == 200 and red.get("ok") is False, red
    st, d10 = post(
        "/task/inspect-draft",
        {"grant_id": g10id, "title": "Code note", "findings": "sandbox red path"},
    )
    assert st == 200
    st, _ = post(
        "/task/h2-ack",
        {
            "grant_id": g10id,
            "draft_filename": d10["filename"],
            "artefact_version": d10["artefact_version"],
        },
    )
    assert st == 200
    st, deny10 = post(
        "/task/export",
        {
            "grant_id": g10id,
            "draft_filename": d10["filename"],
            "h2_acked": True,
            "artefact_version": d10["artefact_version"],
        },
    )
    assert st == 400 and "sandbox_red" in str(deny10), deny10
    results["G10"] = deny10
    save("G10_sandbox_red_deny.json", deny10)

    # G9 secret
    st, sec = post("/task/export-check", {"text": "api_key=sk-abcdefghijklmnopqrstuvwxyz"})
    assert st == 200 and sec.get("ok") is False, sec
    results["G9"] = sec
    save("G9_secret_deny.json", sec)

    # G8 bad model
    st, t8 = post("/task/start", {"task_type": "inspection", "user_id": "g8"})
    assert st == 200
    st, bad = post(
        "/gateway/chat",
        {
            "grant_id": t8["grant_id"],
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": "hi"}],
        },
    )
    g8_ok = (st >= 400) or (
        isinstance(bad, dict)
        and (bad.get("ok") is False or bad.get("error") == "gateway_deny")
    )
    assert g8_ok, bad
    results["G8"] = {"status": st, "body": bad, "pass": True}
    save("G8_deny.json", results["G8"])

    # G7 revoke
    st, t7 = post("/task/start", {"task_type": "inspection", "user_id": "g7"})
    assert st == 200
    st, _ = post("/task/revoke", {"grant_id": t7["grant_id"]})
    assert st == 200
    st, denied = post("/task/retrieve", {"grant_id": t7["grant_id"], "query": "x"})
    assert st == 403, denied
    results["G7"] = denied
    save("G7_revoke.json", denied)

    st, audit = get("/audit/verify")
    results["audit_chain"] = audit
    save("audit_verify.json", audit)

    summary = {
        "ts": ts,
        "desk": "http://127.0.0.1:8080/desk/",
        "g1_mode": g1["g1_mode"],
        "pass": {
            "G1": True,
            "G2": True,
            "G3": True,
            "G4": True,
            "G5": True,
            "G6": True,
            "G7": True,
            "G8": True,
            "G9": True,
            "G10": True,
        },
        "monitor_a_not_cert": True,
        "boundary": "assist→export leave · no forward-accept",
    }
    save("SUMMARY.json", {**summary, "results": results})

    print(json.dumps({"ok": True, "summary": summary["pass"], "g1_mode": g1["g1_mode"], "evidence": str(EVID)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
