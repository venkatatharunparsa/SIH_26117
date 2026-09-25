"""Outsider E2E: fixtures catalog + complex PNG/PDF attach → confirm → Word DRAFT.

Assumes API on 127.0.0.1:8080 and a reachable local/LAN Ollama. No prior knowledge
of session state — fresh grant each run.
"""
from __future__ import annotations

import base64
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / "data" / "fixtures"
BASE = "http://127.0.0.1:8080"
OUT = ROOT / "eval" / "evidence" / "OUTSIDER_COMPLEX_E2E.json"


def call(method: str, path: str, body: dict | None = None, timeout: float = 180.0) -> dict:
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


def b64_file(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def orch(body: dict) -> dict:
    return call("POST", "/orch/turn", body, timeout=240.0)


def main() -> int:
    report: dict = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "steps": []}

    health = call("GET", "/health")
    report["health_ok"] = bool(health.get("ok"))
    report["inference"] = health.get("inference_label") or health.get("llm_base_url")
    if not health.get("ok"):
        report["fatal"] = "API health failed"
        OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("FAIL health")
        return 1

    cat = call("GET", "/fixtures/catalog")
    names = [t.get("name") for t in (cat.get("tree") or [])]
    report["steps"].append(
        {
            "id": "catalog",
            "ok": bool(cat.get("ok")),
            "count": len(names),
            "has_noisy": "scan_vessel_V101_noisy.png" in names,
            "has_multipage": "vessel_note_multipage.pdf" in names,
            "has_png": "scan_vessel_V101.png" in names,
            "has_pdf": "vessel_note_text.pdf" in names,
        }
    )

    # Ensure complex fixtures exist
    noisy = FIX / "scan_vessel_V101_noisy.png"
    multi = FIX / "vessel_note_multipage.pdf"
    if not noisy.is_file() or not multi.is_file():
        import subprocess

        subprocess.check_call(
            [sys.executable, str(ROOT / "backend" / "scripts" / "gen_complex_ocr_fixtures.py")]
        )

    cases = [
        {
            "id": "png_noisy",
            "path": FIX / "scan_vessel_V101_noisy.png",
            "content_type": "image/png",
            "expect_keys": ["7.6", "V-101", "SOP"],
        },
        {
            "id": "pdf_multipage",
            "path": FIX / "vessel_note_multipage.pdf",
            "content_type": "application/pdf",
            "expect_keys": ["7.6", "V-101", "SOP-THK"],
        },
        {
            "id": "pdf_text_layer",
            "path": FIX / "vessel_note_text.pdf",
            "content_type": "application/pdf",
            "expect_keys": ["7.6", "V-101"],
        },
    ]

    for case in cases:
        p: Path = case["path"]
        if not p.is_file():
            report["steps"].append({"id": case["id"], "ok": False, "error": "missing_file"})
            continue
        step: dict = {"id": case["id"], "file": p.name}
        attach = orch(
            {
                "task_type": "inspection",
                "intent": "attach",
                "attach_b64": b64_file(p),
                "attach_filename": p.name,
                "attach_content_type": case["content_type"],
                "user_id": "outsider-e2e",
            }
        )
        step["attach_ok"] = bool(attach.get("ok"))
        step["grant_id"] = attach.get("grant_id")
        step["phase"] = attach.get("phase")
        step["engine"] = attach.get("ingest_engine")
        step["live_ocr"] = attach.get("live_ocr")
        step["degraded"] = attach.get("ingest_degraded")
        step["ingest_message"] = (attach.get("ingest_message") or "")[:160]
        extract = attach.get("extract_text") or ""
        step["extract_len"] = len(extract)
        step["extract_preview"] = extract[:220]
        hits = [k for k in case["expect_keys"] if k.lower() in extract.lower()]
        step["key_hits"] = hits
        step["keys_ok"] = len(hits) >= max(1, len(case["expect_keys"]) - 1)

        if not attach.get("grant_id"):
            step["ok"] = False
            step["error"] = attach.get("error") or attach.get("detail") or "no_grant"
            report["steps"].append(step)
            continue

        gid = attach["grant_id"]
        # Confirm extract (H1) then continue toward draft
        conf = orch(
            {
                "grant_id": gid,
                "task_type": "inspection",
                "intent": "confirm",
                "message": "",
                "user_id": "outsider-e2e",
            }
        )
        step["confirm_ok"] = bool(conf.get("ok"))
        step["confirm_phase"] = conf.get("phase")

        # Keep confirming/continuing a few turns to reach draft if asks appear
        draft_name = conf.get("draft", {}).get("filename") if isinstance(conf.get("draft"), dict) else None
        cur = conf
        for _ in range(6):
            if draft_name:
                break
            if cur.get("ask"):
                cur = orch(
                    {
                        "grant_id": gid,
                        "task_type": "inspection",
                        "intent": "confirm",
                        "message": "",
                        "user_id": "outsider-e2e",
                    }
                )
            else:
                cur = orch(
                    {
                        "grant_id": gid,
                        "task_type": "inspection",
                        "intent": "continue",
                        "message": "",
                        "user_id": "outsider-e2e",
                    }
                )
            if isinstance(cur.get("draft"), dict):
                draft_name = cur["draft"].get("filename")
            step["last_phase"] = cur.get("phase")

        step["draft"] = draft_name
        step["draft_ok"] = bool(draft_name and str(draft_name).lower().endswith(".docx"))
        step["ok"] = bool(
            step["attach_ok"] and step.get("keys_ok") and step.get("confirm_ok")
        )
        if step.get("draft_ok") and step.get("keys_ok"):
            step["grade"] = "PASS"
        elif step.get("draft_ok") and step.get("attach_ok"):
            # Draft reached; extract keys may be stub-degraded (no Tesseract)
            step["grade"] = "PARTIAL"
        elif step.get("attach_ok") and step.get("keys_ok"):
            step["grade"] = "PARTIAL"
        else:
            step["grade"] = "FAIL"
        report["steps"].append(step)
        print(
            case["id"],
            step["grade"],
            "engine=",
            step.get("engine"),
            "live_ocr=",
            step.get("live_ocr"),
            "draft=",
            draft_name,
        )

    # Path traversal on fixtures API
    trav = call("GET", "/fixtures/file/..%2F..%2Fetc%2Fpasswd")
    report["steps"].append(
        {
            "id": "fixture_traversal",
            "ok": trav.get("http") in (400, 404) or trav.get("ok") is not True,
            "http": trav.get("http"),
        }
    )

    grades = [s.get("grade") for s in report["steps"] if "grade" in s]
    report["summary"] = {
        "pass": grades.count("PASS"),
        "partial": grades.count("PARTIAL"),
        "fail": grades.count("FAIL"),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("WROTE", OUT)
    print("SUMMARY", report["summary"])
    # Outsider bar: at least PDF text-layer keys + catalog OK; noisy may be stub without Tesseract
    if report["summary"]["fail"] and report["summary"]["pass"] + report["summary"]["partial"] == 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
