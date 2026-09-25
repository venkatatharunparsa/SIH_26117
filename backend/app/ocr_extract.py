"""Ingest: PDF text layer + image OCR → plain text for H1 Confirm extract.

Architecture split (locked 2026-09-20):
- **Demo / day-1:** OCR *framework* path — Tesseract (`pytesseract`) + pypdf (+ honest fixture stub).
- **Organisation SoT:** OCR *model* (vision/neural) — not implemented here; optional later combine with framework as fallback.

Demo-viable path (honest labels):
- Text PDFs → pypdf (no Tesseract needed)
- Images (png/jpg/…) → pytesseract + Pillow when Tesseract binary is installed
- Scanned PDFs without Poppler → no page rasterization; degrade to fixture stub
- Missing Tesseract on images → clear message + optional fixture stub for demo reliability

Never claim live OCR when using the fixture stub. Never claim org OCR-model quality from this module.
"""

from __future__ import annotations

import io
from pathlib import Path
from typing import Any

from .config import DATA_DIR, ROOT

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}
PDF_SUFFIXES = {".pdf"}
TEXT_SUFFIXES = {".txt", ".md", ".csv", ".json", ".log"}

# Synthetic vessel note — same substance as FX-EXT-01 / README attach demo
_FIXTURE_STUB_TEXT = """# Confidential synthetic — SIH demo OCR fixture stub

## Asset
- Tag: **V-101** shell course A
- Location: North quadrant, ~1.2 m above grade

## Measurement
- Measured thickness: **7.6 mm**
- Compare to SOP-THK-001 minimum: **8.0 mm**

## Notes
Pit indication near weld toe. Recommend reduced inspection interval and notify integrity engineer.
"""

_FIXTURE_IMAGE = DATA_DIR / "fixtures" / "scan_vessel_V101.png"
_FIXTURE_PDF = DATA_DIR / "fixtures" / "vessel_note_text.pdf"
_FIXTURE_EXTRACT_MD = DATA_DIR / "fixtures" / "extract_vessel_h1.md"


def tesseract_available() -> bool:
    try:
        import pytesseract
        from pytesseract import TesseractNotFoundError
    except ImportError:
        return False
    try:
        pytesseract.get_tesseract_version()
        return True
    except (TesseractNotFoundError, OSError, Exception):
        return False


def _suffix(filename: str | None, content_type: str | None = None) -> str:
    name = (filename or "").lower()
    suf = Path(name).suffix.lower()
    if suf:
        return suf
    ct = (content_type or "").lower()
    if "pdf" in ct:
        return ".pdf"
    if "png" in ct:
        return ".png"
    if "jpeg" in ct or "jpg" in ct:
        return ".jpg"
    if "text" in ct or "markdown" in ct:
        return ".txt"
    return ""


def _fixture_stub_text() -> str:
    if _FIXTURE_EXTRACT_MD.is_file():
        try:
            return _FIXTURE_EXTRACT_MD.read_text(encoding="utf-8").strip()
        except OSError:
            pass
    return _FIXTURE_STUB_TEXT.strip()


def _decode_plain(data: bytes) -> str:
    for enc in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(enc).strip()
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace").strip()


def extract_pdf_text_layer(data: bytes) -> tuple[str, dict[str, Any]]:
    """Selectable text via pypdf. Empty ⇒ likely scan (no Poppler rasterization here)."""
    try:
        from pypdf import PdfReader
    except ImportError as e:
        return "", {
            "engine": "none",
            "ok": False,
            "error": "pypdf_missing",
            "message": f"pypdf not installed: {e}",
        }
    try:
        reader = PdfReader(io.BytesIO(data))
        parts: list[str] = []
        for page in reader.pages:
            t = page.extract_text() or ""
            if t.strip():
                parts.append(t.strip())
        text = "\n\n".join(parts).strip()
        meta: dict[str, Any] = {
            "engine": "pypdf",
            "ok": True,
            "pages": len(reader.pages),
            "chars": len(text),
        }
        if not text:
            meta["message"] = (
                "PDF has no selectable text layer (likely a scan). "
                "Poppler/pdf2image not required for day-1 — use an image fixture "
                "or install Tesseract and attach a PNG/JPG raster of the page."
            )
            meta["scanned_like"] = True
        else:
            meta["message"] = f"PDF text layer via pypdf ({len(reader.pages)} page(s))"
        return text, meta
    except Exception as e:
        return "", {
            "engine": "pypdf",
            "ok": False,
            "error": "pdf_parse_failed",
            "message": f"PDF parse failed: {e}",
        }


def extract_image_ocr(data: bytes) -> tuple[str, dict[str, Any]]:
    """OCR image bytes with Tesseract. Honest failure when binary missing."""
    try:
        from PIL import Image
    except ImportError as e:
        return "", {
            "engine": "none",
            "ok": False,
            "error": "pillow_missing",
            "message": f"Pillow not installed: {e}",
        }
    try:
        import pytesseract
        from pytesseract import TesseractNotFoundError
    except ImportError:
        return "", {
            "engine": "none",
            "ok": False,
            "error": "pytesseract_missing",
            "message": (
                "pytesseract Python package missing. "
                "pip install pytesseract and install Tesseract OCR for Windows."
            ),
        }
    try:
        img = Image.open(io.BytesIO(data))
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        text = (pytesseract.image_to_string(img) or "").strip()
        return text, {
            "engine": "tesseract",
            "ok": True,
            "chars": len(text),
            "message": "Image OCR via Tesseract (live)",
            "tesseract": True,
        }
    except TesseractNotFoundError:
        return "", {
            "engine": "none",
            "ok": False,
            "error": "tesseract_binary_missing",
            "message": (
                "Tesseract OCR binary not found on PATH. "
                "Install from https://github.com/UB-Mannheim/tesseract/wiki "
                "(Windows) then restart the API. Until then demo can use fixture stub."
            ),
        }
    except Exception as e:
        return "", {
            "engine": "tesseract",
            "ok": False,
            "error": "ocr_failed",
            "message": f"OCR failed: {e}",
        }


def ingest_bytes(
    data: bytes,
    *,
    filename: str | None = None,
    content_type: str | None = None,
    allow_fixture_fallback: bool = True,
) -> dict[str, Any]:
    """Turn file bytes into extract text + honest engine metadata."""
    if not data:
        return {
            "ok": False,
            "text": "",
            "engine": "none",
            "degraded": False,
            "error": "empty_file",
            "message": "Attached file is empty",
            "filename": filename,
        }

    suf = _suffix(filename, content_type)
    label = filename or f"attach{suf or ''}"

    if suf in TEXT_SUFFIXES or (not suf and content_type and "text" in content_type):
        text = _decode_plain(data)
        return {
            "ok": bool(text.strip()),
            "text": text,
            "engine": "plain",
            "degraded": False,
            "message": "Plain text attach (no OCR)",
            "filename": label,
            "live_ocr": False,
        }

    if suf in PDF_SUFFIXES:
        text, meta = extract_pdf_text_layer(data)
        if text.strip():
            return {
                "ok": True,
                "text": text,
                "engine": "pypdf",
                "degraded": False,
                "live_ocr": False,
                "message": meta.get("message") or "PDF text layer (pypdf)",
                "filename": label,
                "meta": meta,
            }
        # Scanned / empty — optional fixture stub for demo reliability
        if allow_fixture_fallback:
            stub = _fixture_stub_text()
            return {
                "ok": True,
                "text": stub,
                "engine": "fixture_stub",
                "degraded": True,
                "live_ocr": False,
                "error": meta.get("error") or "pdf_no_text_layer",
                "message": (
                    (meta.get("message") or "No PDF text layer.")
                    + " Using fixture stub — NOT live OCR. "
                    "Attach a PNG/JPG of the page after installing Tesseract for live OCR."
                ),
                "filename": label,
                "meta": meta,
            }
        return {
            "ok": False,
            "text": "",
            "engine": meta.get("engine") or "pypdf",
            "degraded": False,
            "live_ocr": False,
            "error": meta.get("error") or "pdf_no_text_layer",
            "message": meta.get("message") or "No PDF text layer and fixture fallback disabled",
            "filename": label,
            "meta": meta,
        }

    if suf in IMAGE_SUFFIXES:
        text, meta = extract_image_ocr(data)
        if text.strip() and meta.get("ok"):
            return {
                "ok": True,
                "text": text,
                "engine": "tesseract",
                "degraded": False,
                "live_ocr": True,
                "message": meta.get("message") or "Image OCR via Tesseract (live)",
                "filename": label,
                "meta": meta,
            }
        if allow_fixture_fallback:
            stub = _fixture_stub_text()
            why = meta.get("message") or meta.get("error") or "OCR unavailable"
            return {
                "ok": True,
                "text": stub,
                "engine": "fixture_stub",
                "degraded": True,
                "live_ocr": False,
                "error": meta.get("error") or "ocr_unavailable",
                "message": f"{why} Using fixture stub — NOT live OCR.",
                "filename": label,
                "meta": meta,
            }
        return {
            "ok": False,
            "text": "",
            "engine": meta.get("engine") or "none",
            "degraded": False,
            "live_ocr": False,
            "error": meta.get("error") or "ocr_failed",
            "message": meta.get("message") or "OCR failed",
            "filename": label,
            "meta": meta,
        }

    return {
        "ok": False,
        "text": "",
        "engine": "none",
        "degraded": False,
        "live_ocr": False,
        "error": "unsupported_type",
        "message": (
            f"Unsupported attach type {suf or content_type or '(unknown)'}. "
            "Use .txt/.md, .pdf (text layer), or .png/.jpg (OCR)."
        ),
        "filename": label,
    }


def ingest_path(
    path: Path,
    *,
    allow_fixture_fallback: bool = True,
) -> dict[str, Any]:
    data = path.read_bytes()
    return ingest_bytes(
        data,
        filename=path.name,
        allow_fixture_fallback=allow_fixture_fallback,
    )


def status() -> dict[str, Any]:
    """Capability probe for /health or smoke scripts."""
    return {
        "tesseract": tesseract_available(),
        "pypdf": True,
        "pillow": True,
        "pdf2image": False,  # optional / not day-1
        "fixture_image": _FIXTURE_IMAGE.is_file(),
        "fixture_pdf": _FIXTURE_PDF.is_file(),
        "fixture_root": str((DATA_DIR / "fixtures").resolve()),
        "repo_root": str(ROOT),
    }
