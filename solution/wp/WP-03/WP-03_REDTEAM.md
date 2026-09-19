# WP-03 ingest — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-03_ARCHITECT_PERSPECTIVE.md`  
**DM answers + new requirement:** see §0  
**Against:** Official Description/Expected Solution; WP-00 multimodal + OCR→human→KB; WP-01 artefacts; WP-02 boundary; WP-05 H1/stale; `DESIGN_REPO_MAP_v1.md` WP-03.

---

## 0. Decision-maker input (binding)

| ID | Decision |
|---|---|
| **R0 Pre-LLM plane** | Ingest must **handle inputs before the generation/agent LLM**: parsers, converters, normalizers → **internal LLM-readable format**. Do not dump raw PDF/binary at the drafter. |
| **Q1 Handwritten / H1 UX** | Same pipeline + **honest confidence**. After extraction, **low-friction verify**: ask confirmation especially for **wrong / low-confidence** fields — not re-approve every character blindly. |
| **Q2 Multi-page** | Process **page-by-page and/or topic-by-topic**, but cover **all pages**. Hard-to-verify regions get explicit human attention. |
| **Q3** | **OCR + optional VLM** (recommended). |
| **Q4 Unusable** | **Raise issue clearly**; worker supplies **corrected text** and/or **new scan**; then run extract + **verify again** (H1). |
| **Q5** | Demo soft limit **5 pages** (fail-closed / warn above for must-work demo). |
| **Q6** | Drawing **photo/scan** OK as multimodal proof without full `drawing-review` job. |

---

## Verdict

| Question | Answer |
|---|---|
| Architect path sound? | **Yes** — needs R0 plane + Q1–Q6 |
| Missing? | Pre-LLM pipeline stages; low-friction H1 UX contract; page/topic units; 5-page limit; remediable unusable path |
| Overhyped risk? | “Handle **everything**” / perfect parsers; VLM confused with drafter LLM; topic split as magic |
| Within bounds? | **Yes** if stages are honest and engines not locked |
| Confidence after fills | **~0.87** |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Pre-LLM ingest plane | Stages: Intake → Parse/Split → OCR/VLM → **Normalize** → Extract artefact → H1 → only then Agent/Draft LLM |
| **M2** | “LLM-readable internal format” | Versioned structured extract (text + fields + page/topic ids + confidence) — e.g. markdown/JSON **shape**, brand not locked |
| **M3** | Low-friction H1 vs hard-block | H1 still **hard** (WP-05); UX = review extract, **focus wrong/low-confidence**, confirm corrects; blanket “accept all high-confidence” may be allowed **only** if worker explicitly confirms the pack |
| **M4** | Page + topic units | Unit of work = page and/or topic segment; **all pages** in scope ≤5 for demo; incomplete pack ≠ verified |
| **M5** | Unusable remediation | Issue codes + UI; accept replacement scan or typed supplement; new extract version → re-H1 |
| **M6** | 5-page demo limit | Must-work demo ≤5 pages; above = fail-closed or labelled unsupported for demo |
| **M7** | OCR vs generation LLM | Optional VLM is **ingest/understanding** card; **≠** approval-note writer model (routing WP-06) |
| **M8** | Parser honesty | PDF/image/text parsers = best-effort; fail-closed on unsupported; no cloud parse |

---

## 2. Overhyped → fix

| Attack | Fix language |
|---|---|
| **A1** “Handle everything” | Handle **declared** input classes (Official four + text supplement); not every proprietary CAD |
| **A2** Pre-LLM means no models | Classical parse/OCR allowed; **VLM may run in ingest plane**; **draft/agent LLM** waits for normalized+H1 extract |
| **A3** Topic-by-topic perfect | Topic split = heuristic/optional assist; human still verifies; no claim of perfect sectioner |
| **A4** Low friction = skip H1 | Forbidden — WP-05 hard-block remains |
| **A5** 5 pages = product forever | **Demo must-work** soft ceiling; org ambition may raise via Admin later |
| **A6** One OCR brand | Candidates only |

---

## 3. Adopt / refuse

| Adopt | Why | Refuse |
|---|---|---|
| Tesseract/PaddleOCR *candidates* | On-device OCR | Cloud Document AI |
| Local VLM via `/v1` + card | Optional vision | Remote image URL |
| Parse→normalize→generate pipeline shape | R0 | RAGFlow-as-workbench |
| Extract version + H1 | WP-05 | Auto-KB unverified OCR |

---

## 4. Disposition

**Applied.** → **`WP-03_FREEZE.md` rev 1.0**. Next: **WP-23**.
