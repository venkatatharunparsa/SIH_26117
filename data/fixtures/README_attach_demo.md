# README — Vessel thickness desk note (attach demo)

Confidential synthetic — SIH26 Knowledge Work Bench demo file.
Attach this README from the desk composer to exercise extract → company match → Confirm extract → PPTX draft.

## Asset
- Tag: **V-101** shell course A
- Location: North quadrant, ~1.2 m above grade

## Measurement
- Measured thickness: **7.6 mm**
- Compare to SOP-THK-001 minimum: **8.0 mm**

## Notes
Pit indication near weld toe. Recommend reduced inspection interval and notify integrity engineer.
This note should match internal SOP / KWB policy / brand rules in the knowledge shelf.

## Desired deliverable
After human Confirm extract and cite review, generate a **PowerPoint DRAFT** (PPTX)
suitable for a short integrity briefing — not a plant record, not CERT.

---

## OCR / PDF fixtures (demo ingest)

**Decision (2026-09-20):** day-1 demo uses the **OCR framework** path (`pypdf` + Tesseract/`pytesseract`, fixture stub if missing). Organisation target / SoT is an **OCR model** (vision/neural) — not required for this attach demo; framework may remain an optional fallback later.

| File | Role |
|---|---|
| `README_attach_demo.md` | Plain text attach (original path) |
| `scan_vessel_V101.png` | Image OCR fixture (Tesseract framework) |
| `vessel_note_text.pdf` | PDF **text layer** via pypdf (not OCR) |
| `extract_vessel_h1.md` | Fixture stub text when OCR framework binary missing |

Regenerate binaries: `python backend/scripts/gen_ocr_fixtures.py`

### Windows — Tesseract (for live image OCR)

1. Install [UB Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) (includes English).
2. Ensure `tesseract.exe` is on `PATH` (installer option), or set `TESSDATA_PREFIX`.
3. `pip install -r requirements.txt` (includes `pytesseract`, `pillow`, `pypdf`).
4. Restart API. Check `GET /health` → `ocr.tesseract: true`.

Without the binary, attaching a PNG still reaches **Confirm extract** via the fixture stub and is labeled **NOT live OCR**.

**Not day-1:** Poppler / `pdf2image` for scanned PDF pages — use the PNG fixture or a text-layer PDF instead.

### Desk demo steps

1. Start API + desk (`scripts/start_demo.ps1` or uvicorn + `npm run electron:dev`).
2. Composer ⌁ → **Document…** → pick `data/fixtures/vessel_note_text.pdf` or `scan_vessel_V101.png`.
3. Confirm ask shows source line (`pypdf` / `tesseract` / `fixture stub`).
4. Enter → Confirm extract → cite review → PPTX as before.

Smoke: `python backend/scripts/smoke_ocr_extract.py`
