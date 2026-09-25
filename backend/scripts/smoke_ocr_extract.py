"""Smoke: OCR/PDF ingest → orch Confirm extract → cites (H1 spine).

Honest labels:
- PDF text layer → engine=pypdf (not OCR)
- PNG with Tesseract installed → engine=tesseract, live_ocr=true
- PNG without Tesseract → engine=fixture_stub, degraded=true (NOT live OCR)

Usage (API must be up):
  python backend/scripts/smoke_ocr_extract.py
"""
from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

import httpx

BASE = "http://127.0.0.1:8080"
ROOT = Path(__file__).resolve().parents[2]
PNG = ROOT / "data" / "fixtures" / "scan_vessel_V101.png"
PDF = ROOT / "data" / "fixtures" / "vessel_note_text.pdf"


def _b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def main() -> int:
    if not PNG.is_file() or not PDF.is_file():
        print("Fixtures missing — run: python backend/scripts/gen_ocr_fixtures.py")
        return 1

    c = httpx.Client(timeout=60.0)

    # Health / OCR capability
    h = c.get(f"{BASE}/health")
    print("HEALTH", h.status_code)
    health = h.json()
    ocr = health.get("ocr") or {}
    print("OCR_STATUS", json.dumps(ocr, indent=2))
    tess = bool(ocr.get("tesseract"))

    # Open grant via orch chat (LLM may deny — grant still OK)
    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "task_type": "inspection",
            "user_id": "smoke-ocr",
            "intent": "message",
            "message": "ocr smoke",
            "messages": [{"role": "user", "content": "ocr smoke"}],
        },
    )
    chat = r.json()
    gid = chat.get("grant_id")
    print("CHAT", r.status_code, "grant", bool(gid))
    if not gid:
        print("FAIL: no grant")
        return 1

    # 1) Text text-layer PDF
    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "grant_id": gid,
            "intent": "attach",
            "attach_b64": _b64(PDF),
            "attach_filename": "vessel_note_text.pdf",
            "attach_content_type": "application/pdf",
        },
    )
    pdf_att = r.json()
    print(
        "PDF_ATTACH",
        r.status_code,
        "engine=",
        pdf_att.get("ingest_engine"),
        "live_ocr=",
        pdf_att.get("live_ocr"),
        "degraded=",
        pdf_att.get("ingest_degraded"),
    )
    assert r.status_code == 200, pdf_att
    assert pdf_att.get("ingest_engine") == "pypdf", pdf_att
    assert pdf_att.get("live_ocr") is False
    assert pdf_att.get("ask", {}).get("confirm_action") == "confirm_extract"
    assert "7.6" in (pdf_att.get("extract_text") or "") or any(
        "7.6" in str(b) for b in (pdf_att.get("extract_bullets") or [])
    ), pdf_att

    # Confirm extract → cites
    r = c.post(
        f"{BASE}/orch/turn",
        json={"grant_id": gid, "intent": "confirm", "message": ""},
    )
    h1 = r.json()
    print("CONFIRM_EXTRACT", r.status_code, h1.get("phase"))
    assert r.status_code == 200, h1
    assert h1.get("ask", {}).get("confirm_action") == "confirm_cites"

    # Fresh grant for image path (avoid phase confusion)
    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "task_type": "inspection",
            "user_id": "smoke-ocr-img",
            "intent": "message",
            "message": "ocr image",
            "messages": [{"role": "user", "content": "ocr image"}],
        },
    )
    gid2 = r.json().get("grant_id")
    assert gid2, r.json()

    r = c.post(
        f"{BASE}/orch/turn",
        json={
            "grant_id": gid2,
            "intent": "attach",
            "attach_b64": _b64(PNG),
            "attach_filename": "scan_vessel_V101.png",
            "attach_content_type": "image/png",
        },
    )
    img_att = r.json()
    print(
        "PNG_ATTACH",
        r.status_code,
        "engine=",
        img_att.get("ingest_engine"),
        "live_ocr=",
        img_att.get("live_ocr"),
        "degraded=",
        img_att.get("ingest_degraded"),
        "msg=",
        (img_att.get("ingest_message") or "")[:120],
    )
    assert r.status_code == 200, img_att
    assert img_att.get("ask", {}).get("confirm_action") == "confirm_extract"

    if tess:
        assert img_att.get("ingest_engine") == "tesseract", img_att
        assert img_att.get("live_ocr") is True
        assert img_att.get("ingest_degraded") is False
        blob = (img_att.get("extract_text") or "") + " ".join(
            str(b) for b in (img_att.get("extract_bullets") or [])
        )
        assert "V-101" in blob or "7.6" in blob, img_att
        print("PNG_LIVE_OCR OK")
    else:
        assert img_att.get("ingest_engine") == "fixture_stub", img_att
        assert img_att.get("live_ocr") is False
        assert img_att.get("ingest_degraded") is True
        assert "NOT live OCR" in (img_att.get("ingest_message") or "") or "fixture" in (
            img_att.get("ingest_message") or ""
        ).lower()
        print("PNG_FIXTURE_STUB OK (Tesseract binary not installed — honest degrade)")

    # Side path: /task/attach-extract with PDF
    r = c.post(
        f"{BASE}/task/attach-extract",
        json={
            "grant_id": gid2,
            "file_b64": _b64(PDF),
            "filename": "vessel_note_text.pdf",
            "content_type": "application/pdf",
        },
    )
    side = r.json()
    print("ATTACH_EXTRACT_PDF", r.status_code, side.get("ingest_engine"))
    assert r.status_code == 200, side
    assert side.get("ingest_engine") == "pypdf"

    print("SMOKE OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except httpx.ConnectError:
        print("API not up — start uvicorn then re-run", file=sys.stderr)
        raise SystemExit(2)
