"""Multi-task outsider E2E: inspection (field PDF+image) + coding sandbox in parallel grants.

Honest: not true OS-thread multitasking of the UI — two independent grants proving
the workbench can run the industrial spine and the coding spine without cross-talk.
"""
from __future__ import annotations

import base64
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / "data" / "fixtures"
BASE = "http://127.0.0.1:8080"
OUT = ROOT / "eval" / "evidence" / "OUTSIDER_MULTITASK_E2E.json"


def call(method: str, path: str, body: dict | None = None, timeout: float = 240.0) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={"Content-Type": "application/json"} if body is not None else {},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        try:
            return {"ok": False, "http": e.code, "detail": json.loads(detail)}
        except Exception:
            return {"ok": False, "http": e.code, "detail": detail}


def orch(body: dict) -> dict:
    return call("POST", "/orch/turn", body)


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def ensure_field_fixtures() -> None:
    pdf = FIX / "field_inspection_form_V101.pdf"
    png = FIX / "scan_vessel_V101_field.png"
    if pdf.is_file() and png.is_file():
        return
    subprocess.check_call(
        [sys.executable, str(ROOT / "backend" / "scripts" / "gen_field_form_fixtures.py")]
    )


def run_inspection() -> dict:
    ensure_field_fixtures()
    pdf = FIX / "field_inspection_form_V101.pdf"
    png = FIX / "scan_vessel_V101_field.png"
    step: dict = {"task": "inspection", "files": [pdf.name, png.name]}

    # 1) attach multi-page field PDF
    a = orch(
        {
            "task_type": "inspection",
            "intent": "attach",
            "attach_b64": b64(pdf),
            "attach_filename": pdf.name,
            "attach_content_type": "application/pdf",
            "user_id": "multitask-insp",
        }
    )
    step["pdf_attach_ok"] = bool(a.get("ok"))
    step["pdf_engine"] = a.get("ingest_engine")
    step["grant_id"] = a.get("grant_id")
    extract = a.get("extract_text") or ""
    step["pdf_keys"] = [k for k in ("V-101", "7.6", "SOP-THK") if k in extract]
    if not a.get("grant_id"):
        step["grade"] = "FAIL"
        step["error"] = a.get("detail") or a.get("error")
        return step
    gid = a["grant_id"]

    # 2) also attach field image on same grant (iterate)
    img = orch(
        {
            "grant_id": gid,
            "task_type": "inspection",
            "intent": "attach",
            "attach_b64": b64(png),
            "attach_filename": png.name,
            "attach_content_type": "image/png",
            "user_id": "multitask-insp",
        }
    )
    step["img_attach_ok"] = bool(img.get("ok"))
    step["img_engine"] = img.get("ingest_engine")
    step["img_live_ocr"] = img.get("live_ocr")

    # 3) walk confirms toward Word
    cur = orch(
        {
            "grant_id": gid,
            "task_type": "inspection",
            "intent": "confirm",
            "message": "",
            "user_id": "multitask-insp",
        }
    )
    draft = None
    if isinstance(cur.get("draft"), dict):
        draft = cur["draft"].get("filename")
    for _ in range(8):
        if draft:
            break
        intent = "confirm" if cur.get("ask") else "continue"
        cur = orch(
            {
                "grant_id": gid,
                "task_type": "inspection",
                "intent": intent,
                "message": "",
                "user_id": "multitask-insp",
            }
        )
        if isinstance(cur.get("draft"), dict):
            draft = cur["draft"].get("filename")
    step["draft"] = draft
    step["route"] = cur.get("route") or a.get("route")
    step["draft_ok"] = bool(draft and str(draft).lower().endswith(".docx"))
    step["grade"] = (
        "PASS"
        if step["draft_ok"] and step["pdf_attach_ok"] and len(step["pdf_keys"]) >= 2
        else "PARTIAL"
        if step.get("draft_ok")
        else "FAIL"
    )
    return step


def run_coding() -> dict:
    step: dict = {"task": "coding"}
    # Fresh coding turn
    chat = orch(
        {
            "task_type": "coding",
            "intent": "message",
            "message": "Compute 3*7+1 and show steps briefly.",
            "user_id": "multitask-code",
        }
    )
    step["chat_ok"] = bool(chat.get("ok"))
    step["route"] = chat.get("route")
    step["model"] = (chat.get("route") or {}).get("model_id")
    step["grant_id"] = chat.get("grant_id")
    # Sandbox calc if endpoint available
    if chat.get("grant_id"):
        calc = call(
            "POST",
            "/sandbox/calc",
            {
                "grant_id": chat["grant_id"],
                "expression": "3*7+1",
            },
            timeout=60,
        )
        step["sandbox"] = {
            "ok": calc.get("ok"),
            "http": calc.get("http"),
            "result": calc.get("result") or calc.get("stdout") or calc.get("detail"),
        }
    else:
        step["sandbox"] = {"ok": False, "error": "no_grant"}

    distinct = "coder" in str(step.get("model") or "").lower() or "qwen" in str(
        step.get("model") or ""
    ).lower()
    step["model_distinct_from_inspect_hint"] = distinct
    sb_ok = bool(step.get("sandbox", {}).get("ok"))
    if step["chat_ok"] and distinct and sb_ok:
        step["grade"] = "PASS"
    elif step["chat_ok"] and (distinct or sb_ok):
        step["grade"] = "PARTIAL"
    elif step["chat_ok"]:
        step["grade"] = "PARTIAL"
    else:
        step["grade"] = "FAIL"
    return step


def main() -> int:
    health = call("GET", "/health")
    report: dict = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "health_ok": bool(health.get("ok")),
        "inference": health.get("inference_label"),
        "tasks": [],
    }
    if not health.get("ok"):
        report["fatal"] = "API down"
        OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("FAIL health")
        return 1

    # True parallel grants (two threads)
    with ThreadPoolExecutor(max_workers=2) as pool:
        futs = {
            pool.submit(run_inspection): "inspection",
            pool.submit(run_coding): "coding",
        }
        for fut in as_completed(futs):
            result = fut.result()
            report["tasks"].append(result)
            print(result.get("task"), result.get("grade"), result.get("draft") or result.get("model"))

    grades = [t.get("grade") for t in report["tasks"]]
    report["summary"] = {
        "pass": grades.count("PASS"),
        "partial": grades.count("PARTIAL"),
        "fail": grades.count("FAIL"),
    }
    # Cross-check: inspection grant != coding grant
    gids = [t.get("grant_id") for t in report["tasks"] if t.get("grant_id")]
    report["grants_isolated"] = len(set(gids)) == len(gids) and len(gids) >= 2

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("WROTE", OUT)
    print("SUMMARY", report["summary"], "isolated", report["grants_isolated"])
    if report["summary"]["fail"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
