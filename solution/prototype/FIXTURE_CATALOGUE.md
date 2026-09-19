# Fixture catalogue — Confidential synthetic (GATE_90 B7)

**Date:** 2026-09-19  
**Status:** **LOCKED** — design-info B7 (paths on disk; coding fixture optional)  
**Label on every file:** **Confidential synthetic** — not real plant SoR.

---

## Must-have for inspection walk

| ID | Path | On disk | Use | Gate |
|---|---|---|---|---|
| **FX-SOP-01** | `data/fixtures/sop_thickness.txt` | **Yes** | Retrieve / cite MOCK | E · G6 |
| **FX-EXT-01** | `data/fixtures/extract_vessel_h1.md` | **Yes** | Pre-baked extract for **H1** (no OCR day-1) | D · G4 · B2 |
| **FX-SCAN-01** | `data/fixtures/scan_vessel_stub.txt` | **Yes** | Attached scan stub metadata | C |
| **FX-TPL-01** | `data/fixtures/tpl_inspection_note.md` | **Yes** | Minimal template fields for Word DRAFT | C · F · G2 |

## Optional / coding walk

| ID | Path | On disk | Use |
|---|---|---|---|
| **FX-CODE-01** | `data/fixtures/calc_thickness.py` | **Yes** | Sandbox + H9 demo input |
| **FX-SECRET-01** | inline in eval only | N/A | G9 inject (do not commit real secrets) |

---

## Rules

- No real MRPL / plant documents.  
- PPT and jury captions must say **Confidential synthetic**.  
- Day-1 G4 = **FX-EXT-01 + H1** (OCR engine = thicken later — B2).
