"""Single-model simulation suite — existing local resources only (no pull).

Runs health + station link + platform + file-read + chat-history + OCR + Word orch.
Exit 0 only if all required steps pass. G1 labeled floor_single_tag when one chat tag.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[2]
BASE = "http://127.0.0.1:8080"
SCRIPTS = [
    ("station_link", [sys.executable, str(ROOT / "backend/scripts/validate_station_link.py")]),
    ("platform", [sys.executable, str(ROOT / "backend/scripts/smoke_platform.py")]),
    ("file_read", [sys.executable, str(ROOT / "backend/scripts/smoke_orch_file_read.py")]),
    ("chat_history", [sys.executable, str(ROOT / "backend/scripts/smoke_chat_history.py")]),
    ("ocr", [sys.executable, str(ROOT / "backend/scripts/smoke_ocr_extract.py")]),
    ("word", [sys.executable, str(ROOT / "backend/scripts/smoke_orch_word.py")]),
]


def main() -> int:
    report: dict = {"mode": "single_model_simulation", "g1": "floor_single_tag_adopt", "steps": []}
    c = httpx.Client(timeout=180.0)
    try:
        h = c.get(f"{BASE}/health").json()
    except Exception as e:
        print("FAIL API down:", e)
        return 2
    report["health"] = {
        "ok": h.get("ok"),
        "llm_base_url": h.get("llm_base_url"),
        "ocr": h.get("ocr"),
        "adopted": (h.get("ollama_policy") or {}).get("adopted_chat_tags"),
    }
    print("HEALTH", json.dumps(report["health"], indent=2))

    # Dual task→card routes with same model (floor honesty)
    for task in ("inspection", "coding"):
        r = c.post(
            f"{BASE}/orch/turn",
            json={
                "task_type": task,
                "user_id": "sim-single",
                "intent": "message",
                "message": f"ping {task}",
            },
        )
        j = r.json()
        route = j.get("route") or {}
        step = {
            "name": f"route_{task}",
            "status": r.status_code,
            "card_id": route.get("card_id"),
            "model_id": route.get("model_id"),
            "g1_mode": route.get("g1_mode"),
            "ok": bool(j.get("grant_id")),
        }
        report["steps"].append(step)
        print("ROUTE", task, step)
        if not step["ok"]:
            print("FAIL route", task)
            return 1

    failed = []
    for name, cmd in SCRIPTS:
        print(f"\n==== {name} ====")
        p = subprocess.run(cmd, cwd=str(ROOT))
        ok = p.returncode == 0
        report["steps"].append({"name": name, "ok": ok, "code": p.returncode})
        if not ok:
            # chat_history is in-process and may not need API — still required
            failed.append(name)

    out = ROOT / "eval" / "evidence" / "SINGLE_MODEL_SIM.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    report["failed"] = failed
    report["pass"] = len(failed) == 0
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("\nWROTE", out)
    print("RESULT", "PASS" if report["pass"] else f"FAIL {failed}")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
