# WP-03 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-01 / WP-02 / WP-04 / WP-05 freezes  
**Status:** **SUPERSEDED by `WP-03_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-03_REDTEAM.md`.  
**Job of WP-03:** Define the **ingest / multimodal path**: how scanned PDFs, handwritten notes, engineering drawings, and photographs become **on-device** OCR/vision extracts that humans verify (**H1**) before KB-as-truth or clean DRAFT acceptance — fail closed, no remote image fetch, engines **not** locked.

**Sources:** Official Description + Expected Solution; WP-00 OCR→human→KB, multimodal `data:`; WP-01 jobs/artefacts; WP-02 user-attach + connector binary boundary; WP-05 H1 hard-block + stale on re-OCR; `DESIGN_REPO_MAP_v1.md` WP-03.

---

## One sentence (proposed)

KWB turns **local** scans/images into **versioned extract artefacts** via **on-device** OCR and/or vision (pluggable cards), then **stops** for human H1 — it does **not** treat raw model output as plant truth, fetch remote images, or auto-index unverified OCR into the org KB.

---

## 1. What WP-03 owns vs does not

| Owns (this WP) | Does not own |
|---|---|
| Input types + ingest path (attach → process → extract artefact) | H1 gate UI policy (**WP-05** — already frozen) |
| Fail-closed rules when scan unusable / model missing | Full injection hardening of OCR text (**WP-23**) |
| Local-only image bytes (`data:` / workspace file) | Model registry / load policy (**WP-24 / WP-10**) |
| Extract artefact schema (fields, confidence flags, version) | Retrieve/rank/cite (**WP-11**) |
| Demo multimodal + inspection-scan spine | Live DMS binary crawl detail (WP-02 modes; ambition) |

**WP-02 reminder:** connector = connect/store contract; **binary OCR of those blobs** = this WP once bytes are in the task/workspace.

---

## 2. Official input types (must be representable)

| # | Type (Official) | Must-work demo? | Notes |
|---|---|---|---|
| 1 | **Scanned PDF** / scanned inspection report | **Yes** — Expected Solution spine | Multi-page OK; page images or embedded raster |
| 2 | **Photographs** / image scan | **Yes** — multimodal task | Local file / paste; no `https://` fetch |
| 3 | **Handwritten notes** | **Yes** as capability (path must exist) | Quality vary; fail-closed or low-confidence flags — not fake SLA |
| 4 | **Engineering drawings** | Path **yes**; dedicated `drawing-review` job = **ambition** (WP-01) | Multimodal understand may still ingest a drawing image |

Do **not** claim certified P&ID vision SLA (WP-00 Never overclaim).

---

## 3. Ingest path (proposed)

```
Local bytes in (user-attach / workspace / allowlisted offline pack)
    → optional PDF rasterize / page split (local)
    → route: OCR engine and/or VLM card (WP-24 id via gateway)
    → EXTRACT artefact (versioned) + confidence/flags
    → H1 hard gate (WP-05) — human correct vs assumed
    → only then: KB treat-as-input / clean DRAFT acceptance path
```

**Re-run** OCR/VLM ⇒ **new extract version** ⇒ H1 + downstream stale (WP-05).

### 3.1 Image / file rules (must)

- Bytes from **local** workspace, user attach, or Admin offline media already staged — **never** model/`http(s)` URL fetch of the document.  
- Multimodal API content = **`data:` / base64 / local path** the runtime already has (WP-00).  
- Classification: inherit attachment/grant ceiling labels where known; unknown org object → fail-closed for org-index (WP-02/04); user-attached demo OK under task grant.

### 3.2 Outputs of ingest (artefacts)

| Artefact | Content |
|---|---|
| **OCR/vision extract sheet** | Text + structured fields + per-field/page confidence + engine/card id + source file hash + `extract_version` |
| **Findings fields** (may be filled post-H1 by agent) | Structured keys for approval note (WP-01) |
| **Page/preview images** (optional) | Local only; for human H1 UI |

Raw model chat ≠ the extract SoT. Extract sheet is the versioned artefact H1 binds to.

---

## 4. Fail-closed (proposed must)

| Condition | Behaviour |
|---|---|
| Required OCR/VLM **card missing** / runtime down | Fail closed — no silent cloud / no skip-to-DRAFT-as-verified |
| Unreadable scan / empty extract | Flag unusable; block H1-as-success; no KB-as-truth |
| Remote URL image requested | **Deny** |
| Grant revoked mid-ingest | Cancel; no further privileged use of partial extract as verified |
| Engine returns success but garbage | H1 still required; worker may reject → re-run or abort |

Machine confidence flags help the human; they are **not** H1.

---

## 5. Engines & models (candidates — not locked)

| Layer | Candidate pattern | Freeze rule |
|---|---|---|
| Classical OCR | Tesseract and/or PaddleOCR *candidates* | Brand **not** locked |
| Vision / document VLM | Open-weight via same local `/v1` + **card** (WP-24) | Id from registry; sequential load OK on mid-GPU |
| PDF rasterize | Local library (not locked) | No cloud Document AI |

**Routing (ambition/must touch):** inspection scan may use OCR+light VLM; photo understand may prefer VLM — exact router = WP-06; WP-03 only requires **path exists** and **two-task auto-select** still visible at org level (Expected Solution).

---

## 6. Mapping to jobs

| Job | Ingest role |
|---|---|
| `inspect-to-note` | Scanned report → extract → H1 → findings → DRAFT |
| `multimodal-understand` | Image/scan → extract/understanding fields (may feed inspect) |
| `drawing-review` | Drawing bytes → extract/understand (**ambition** job) |
| Connector-sourced PDF | Same path once bytes local under grant |

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Local ingest for **scan/PDF + photograph** on Expected Solution path.  
2. Handwritten path **exists** (may be same OCR/VLM pipeline with honesty on quality).  
3. Extract artefact versioned; H1 before verified use (WP-05).  
4. Fail closed on missing model / unusable scan / remote URL.  
5. No cloud Document AI; fully offline.  
6. Multimodal demo: image or scanned document understanding showable.  
7. Engines = pluggable candidates; not hardcoded forever in workbench redesign sense.

### Org-ambition

- High-quality handwritten / dense P&ID symbol understanding.  
- Batch ingest from WP-02 drop-zone / DMS export packs.  
- Drawing-specific skills / templates.  
- Rich H1 UI (side-by-side page + field editor).

### Deferred

- Perfect multi-column table reconstruction SLA.  
- Certified metrology / thickness reading from photos.  
- Streaming camera / mobile capture app product.

### Never

- Remote `https://` (or any WAN) fetch of images/docs for ingest.  
- Cloud OCR/Document AI.  
- Auto-index unverified OCR as plant SOP truth.  
- Skip H1 then claim verified extract.  
- Claim industrial vision certification / MRPL KPI hours.  
- Treat OCR text as trusted instructions (boundary → **WP-23**).

---

## 8. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Tesseract/PaddleOCR *as candidates*; VLM via local `/v1` + card; `data:` image pattern |
| **Add** | Versioned extract sheet; fail-closed matrix; four Official types; handwritten first-class path; tie to H1/stale |
| **Refuse** | Cloud Document AI; RAGFlow-as-workbench; remote image URLs; locking one OCR brand in freeze |

---

## 9. Boundary vs later WPs

| Topic | WP-03 | Later |
|---|---|---|
| H1 / stale / re-OCR | Consumes WP-05 | — |
| Injection via OCR text | Mark untrusted | **WP-23** |
| Index verified extracts into KB | After H1 only | **WP-11** / policy |
| Which card to pick | Path + card id on artefact | **WP-06 / WP-24** |
| GPU load/unload | Sequential OK | **WP-10** |

---

## 10. Open questions for decision maker

1. **Handwritten must-work bar:** same pipeline + honest low-confidence OK for demo, or separate labelled handwritten sample required in jury script?  
2. **Multi-page PDF:** must process **all** pages before H1, or H1 per page / per pack with “pages N–M” version?  
3. **OCR vs VLM for inspection scan:** prefer classical OCR first then VLM assist, or single VLM path for must-work? (Recommend: **OCR+optional VLM**, either card logged.)  
4. **Unusable scan:** abort task only, or allow worker to **type/correct empty extract** then H1 on typed content?  
5. **Max input size (demo):** e.g. N pages / M MB soft limit with fail-closed above — freeze a soft demo limit or leave unset?  
6. **Drawing in multimodal must-work:** one photo/scan of a drawing OK as multimodal proof, without claiming full `drawing-review` job?

---

## 11. Next after your decisions

**Done.** Frozen as `WP-03_FREEZE.md` rev 1.0. Next: **WP-23**.
