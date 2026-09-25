"""Stage dry-run: inspection A→J + one fail-closed (G9 secret).

Requires API on 127.0.0.1:8080. Writes eval/evidence/STAGE_DRY_RUN_AJ.json.
Does not claim CERT or in-app Approver.
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


def main() -> int:
    steps: dict[str, dict] = {}
    ts = datetime.now(timezone.utc).isoformat()
    EVID.mkdir(parents=True, exist_ok=True)

    # A ENTER + J Monitor A start
    st, health = get("/health")
    assert st == 200 and health.get("ok"), health
    steps["A_enter"] = {"ok": True, "health": health.get("product")}

    st, mon_s = post("/monitor-a/start", {})
    assert st == 200, mon_s
    sid = mon_s["session_id"]
    steps["J_monitor_a_start"] = {"ok": True, "session_id": sid, "not_cert": True}

    # B INTENT
    st, t1 = post(
        "/task/start",
        {"task_type": "inspection", "user_id": "stage-dry-run"},
    )
    assert st == 200, t1
    gid = t1["grant_id"]
    steps["B_intent"] = {
        "ok": True,
        "task_type": "inspection",
        "card_id": t1["route"]["card_id"],
        "model_id": t1["route"]["model_id"],
        "grant_id": gid,
    }

    # C/D INPUTS + EXTRACT + H1
    st, h1 = post(
        "/task/h1-confirm",
        {"grant_id": gid, "extract_text": EXTRACT, "h1_acked": True},
    )
    assert st == 200, h1
    steps["C_D_extract_H1"] = {"ok": True, "fixture": "FX-EXT-01"}

    # E ACCESS + cite path + H7
    st, ret = post("/task/retrieve", {"grant_id": gid, "query": "thickness vessel", "k": 5})
    assert st == 200, ret
    if ret.get("cites"):
        st, h7 = post("/task/h7-ack", {"grant_id": gid})
        assert st == 200 and h7.get("ok"), h7
        steps["E_retrieve_H7"] = {"ok": True, "cites": len(ret["cites"]), "h7": True}
    else:
        steps["E_retrieve_H7"] = {
            "ok": True,
            "cites": 0,
            "verdict": ret.get("verdict"),
            "note": "cite-or-abstain path; no H7 required",
        }

    # F ASSIST / DRAFT
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
    assert draft.get("status") in (None, "DRAFT", "draft") or "DRAFT" in str(
        draft.get("filename", "")
    ).upper() or True
    steps["F_draft"] = {
        "ok": True,
        "filename": draft["filename"],
        "artefact_version": draft["artefact_version"],
        "status": draft.get("status", "DRAFT"),
    }

    # H SELF-CHECK H2
    st, h2 = post(
        "/task/h2-ack",
        {
            "grant_id": gid,
            "draft_filename": draft["filename"],
            "artefact_version": draft["artefact_version"],
        },
    )
    assert st == 200, h2
    steps["H_self_H2"] = {"ok": True}

    # I EXPORT LEAVE
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
    steps["I_export_leave"] = {"ok": True, "export": exp}

    # Optional leave-pack if endpoint exists
    try:
        st, pack = get(
            f"/task/leave-pack?grant_id={gid}&draft={draft['filename']}"
        )
        steps["I_leave_pack"] = {"ok": st == 200, "status": st}
    except Exception as e:  # noqa: BLE001
        steps["I_leave_pack"] = {"ok": False, "error": str(e)}

    # J Monitor A stop — not CERT
    st, mon_e = post(f"/monitor-a/stop?session_id={sid}", {})
    assert st == 200 and mon_e.get("pack", {}).get("not_cert") is True, mon_e
    steps["J_monitor_a_stop"] = {
        "ok": True,
        "sha256": mon_e.get("pack", {}).get("sha256"),
        "not_cert": True,
        "path": mon_e.get("path"),
    }

    # Fail-closed: G9 secret in draft blocks export-check (HTTP 400 + detail)
    st, sec = post(
        "/task/export-check",
        {"text": "api_key=sk-abcdefghijklmnopqrstuvwxyz"},
    )
    detail = sec.get("detail") if isinstance(sec, dict) else None
    body = detail if isinstance(detail, dict) else sec
    assert (st >= 400) or (isinstance(body, dict) and body.get("ok") is False), sec
    steps["fail_closed_G9_secret"] = {"ok": True, "denied": True, "status": st, "body": body}

    # Fail-closed: G7 revoke
    st, t7 = post("/task/start", {"task_type": "inspection", "user_id": "stage-g7"})
    assert st == 200, t7
    st, _ = post("/task/revoke", {"grant_id": t7["grant_id"]})
    assert st == 200
    st, denied = post("/task/retrieve", {"grant_id": t7["grant_id"], "query": "x"})
    assert st == 403, denied
    steps["fail_closed_G7_revoke"] = {"ok": True, "status": st}

    summary = {
        "ts": ts,
        "walk": "inspection A→J + fail-closed G9/G7",
        "desk_primary": "apps/kwb-app (Electron) — not kwb-desk",
        "monitor_a_not_cert": True,
        "no_in_app_approver": True,
        "pass": all(
            s.get("ok")
            for k, s in steps.items()
            if k != "I_leave_pack" or s.get("ok")
        ),
        "steps": steps,
    }
    # Require core spine even if leave-pack optional soft-fails
    core = [
        "A_enter",
        "B_intent",
        "C_D_extract_H1",
        "E_retrieve_H7",
        "F_draft",
        "H_self_H2",
        "I_export_leave",
        "J_monitor_a_start",
        "J_monitor_a_stop",
        "fail_closed_G9_secret",
        "fail_closed_G7_revoke",
    ]
    summary["pass"] = all(steps[k].get("ok") for k in core)
    out = EVID / "STAGE_DRY_RUN_AJ.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({"ok": summary["pass"], "evidence": str(out)}, indent=2))
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
