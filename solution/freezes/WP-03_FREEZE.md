# WP-03 Ingest and multimodal — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.1** after freeze adversarial). Binding with WP-00 / WP-01 / WP-02 / WP-04 / WP-05. Reopen only if the decision maker explicitly says so.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-03_ARCHITECT_PERSPECTIVE.md`, `WP-03_REDTEAM.md`, **DM 2026-09-18**, freeze red-team `WP-03_FREEZE_REDTEAM.md` (F1–F12).  
**Findings SoT:** `WP-03_REDTEAM.md` · `WP-03_FREEZE_REDTEAM.md`  
**Product:** **KWB**

**Stack / OCR / VLM brands:** not locked (candidates only).

---

## 1. One-sentence contract

KWB **ingests** local scans/images/PDFs through a **pre-LLM plane** (parse → split → OCR/optional VLM → **normalize** to an internal LLM-readable extract) so the **draft/agent LLM never receives raw binaries**; humans **verify extracts with low friction** (focus wrong/low-confidence) under **H1** before KB-as-truth or clean DRAFT acceptance — fail closed, offline only, demo ≤ **5 pages**.

---

## 2. Limits (anti overclaim)

| True | False / refuse |
|---|---|
| Pre-LLM plane prepares **normalized extracts** | Parsers perfectly handle every CAD/proprietary format |
| Optional **VLM** may run **in ingest** | VLM ingest card = the Word-drafting model |
| Low-friction H1 focuses errors | Low friction = skip H1 |
| Page/topic units cover **all** in-scope pages | Topic split is certified document understanding |
| **5 pages** = must-work **demo** ceiling | Eternal product max forever |
| Honest confidence flags | Certified handwritten/P&ID SLA |
| Human H1 on extract | Verified extract = **safe system instructions** (still WP-23) |
| Rasterize→OCR preference | Zero OCR error / hidden-text impossible forever |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **R0** | Full **pre-LLM ingest plane** before draft/agent LLM (parsers, converters, normalizer → internal readable format). |
| **Q1** | Same pipeline + honest confidence; **low-friction verify** — confirm/fix **wrong or low-confidence** extractions. |
| **Q2** | **Page-by-page and/or topic-by-topic**; still process **all** pages in scope; hard regions get explicit attention. |
| **Q3** | **OCR + optional VLM**. |
| **Q4** | Unusable → **clear issue**; worker gives **text and/or new scan** → extract again → **verify again**. |
| **Q5** | Must-work demo limit **5 pages**. |
| **Q6** | Drawing **photo/scan** allowed as multimodal proof; full `drawing-review` job remains ambition (WP-01). |

---

## 4. Pre-LLM ingest plane (core)

Draft/agent LLM sees **normalized extract artefacts**, not raw PDF/image bytes.

| Stage | Job | Output |
|---|---|---|
| **S0 Intake** | Accept **allowlisted** local bytes under task grant; **content sniff** (MIME ≠ trust extension alone); page ≤ demo max + **byte ceiling**; store **immutable original** + hash | `source_file` + hash + class labels if any + sniff result |
| **S1 Parse** | Detect type; PDF parse/rasterize; image decode; plain text pass-through; **encrypted PDF → fail-closed**; **embedded attachments → deny/quarantine** (not auto-merge into extract) | Page images / text streams / structure hints / issues |
| **S2 Split** | **Page** units and optional **topic/segment** units (heuristic OK) | Unit list covering **all** pages in job scope |
| **S3 Extract** | Classical **OCR** and/or optional **VLM** via local `/v1`. **Digital/untrusted PDF:** prefer **rasterize → OCR** (human-visible) over silently trusting a hidden text layer | Per-unit raw extract + confidence |
| **S4 Normalize / convert** | Internal LLM-readable format; **strip metadata** used on model path; **Unicode normalize**; strip zero-width/invisible chars (**log strips**); attach `parser_version` / engine versions | **Extract artefact** `extract_version` |
| **S5 Human H1** | Low-friction verify (WP-05 hard gate) | `human_verified` extract or reject |
| **S6 Hand-off** | **Only after H1 confirm** — normalized **text/fields** enter draft/agent context under grant. Page rasters = H1 UI / ingest VLM — **not** raw PDF to drafter | Context pack input (WP-21 later) |

**Never:** skip S4–S5 and paste raw binary into the drafter.  
**Never:** remote URL fetch at S0.  
**Never:** S6 without H1 confirm (no “implicit accept” path).  
**Re-run S3–S4** ⇒ new `extract_version` ⇒ H1 stale + downstream stale (WP-05).

**Partial units:** any required unit `unusable` / failed → pack cannot be fully `human_verified` unless worker **explicitly** marks skip-with-issue or remediates (Q4). No silent success on garbage pages.

---

## 5. Internal LLM-readable format (contract, not brand)

Minimum extract artefact fields:

| Field | Purpose |
|---|---|
| `extract_id` / `extract_version` | Version for H1 binding |
| `source_hash` | Provenance (original immutable) |
| `parser_version` / `engine_versions` | Replay / audit |
| `units[]` | `page_no` and/or `topic_id` + text |
| `fields[]` | Structured findings keys (as available) |
| `confidence` / flags per unit or field | Drive low-friction H1 |
| `engine_card_ids` | OCR and/or VLM ids used |
| `issues[]` | Unreadable regions, parse errors, strips log refs |
| `trust_label` | `machine_extract` → after H1 `human_verified` (still **untrusted-as-instructions** → WP-23) |
| `status` | `draft_extract` \| `human_verified` \| `rejected` \| `unusable` |

**Must-work allowlisted intake types (S0):** PDF, PNG, JPEG, WebP, TIFF, and **plain text** supplement. Others = fail-closed or ambition later.

**Demo bounds:** ≤ **5 pages** and an Admin-set **byte ceiling** (demo must define a default; exact MB not brand-locked).

This artefact (text/fields) is what later stages may feed the **draft/agent LLM** — after H1. Rasters stay for H1/VLM ingest UI.

---

## 6. Low-friction H1 (with WP-05)

- H1 remains **hard** — no clean DRAFT accept / KB-as-truth without human confirm on the extract pack.  
- UX intent: show extract beside source; **highlight low-confidence and flagged-wrong** units/fields; worker corrects those; explicit **confirm** on the pack (high-confidence bulk confirm OK only as part of that explicit confirm — not silent auto-accept).  
- Worker corrections = material change ⇒ new version rules as WP-05.  
- Machine confidence ≠ H1.

---

## 7. Official input types

| Type | Must-work | Notes |
|---|---|---|
| Scanned PDF / inspection scan | **Yes** | ≤5 pages demo; all pages processed |
| Photographs / image scans | **Yes** | Multimodal path |
| Handwritten notes | **Yes** path | Same pipeline; honest confidence |
| Engineering drawings | Ingest path **yes**; job ambition | Photo/scan OK for multimodal proof (Q6) |
| Worker-typed supplement | **Yes** (Q4) | After unusable or to fix gaps; still H1 |

---

## 8. Page / topic units (Q2)

- Default unit: **page**.  
- Optional: **topic/segment** within or across pages (heuristic; not certified).  
- Job incomplete until **all pages** in submitted scope are extracted or explicitly marked skipped-with-issue.  
- Hard-to-verify units must surface in H1 UI (flags).

---

## 9. OCR + optional VLM (Q3)

| Path | Role |
|---|---|
| Classical OCR (candidates: Tesseract / PaddleOCR — **not locked**) | Primary text from scans |
| Optional VLM (open-weight card, local `/v1`) | Assist layout/handwriting/drawing photo understanding |
| Draft/agent LLM | **After** normalize + H1 — separate card/route (WP-06/24) |

Mid-GPU: sequential load OK (WP-10). Log which card ids ran (Expected Solution routing proof may use other tasks too).

---

## 10. Fail-closed & unusable (Q4)

| Condition | Behaviour |
|---|---|
| Missing OCR/VLM card / runtime | Fail closed — no cloud fallback |
| Remote `http(s)` image/doc URL | **Deny** |
| Unusable / empty extract | Status `unusable`; **show issues clearly**; block verified path |
| Remediation | New scan attach and/or typed input → S0–S4 again → **H1 again** |
| Grant revoked mid-ingest | Cancel; partial ≠ verified |
| Encrypted / password PDF | Fail closed + clear issue |
| Embedded PDF attachments | Deny or quarantine — do not auto-ingest into extract |
| MIME / type mismatch vs sniff | Fail closed or quarantine |
| Scope > **5 pages** or over byte ceiling (must-work demo) | Fail-closed or labelled unsupported for demo (Admin may raise later — ambition) |

---

## 11. Must / ambition / deferred / never

### Must-work

1. Pre-LLM plane S0–S6.  
2. Versioned extract artefact (§5).  
3. OCR + optional VLM path.  
4. Low-friction H1 with honest confidence (still hard gate).  
5. Page (and optional topic) units; all pages ≤5 in demo.  
6. Unusable issue + remediate + re-verify.  
7. Multimodal: photo or scan understanding showable (drawing photo OK).  
8. Offline only; no cloud Document AI.  
9. Handwritten path = same pipeline + honest confidence.

### Org-ambition

- >5 pages / higher byte caps; batch DMS/drop-zone ingest; rich drawing-review job; better topic segmentation; richer H1 editor.  
- **Two-source diff** (native PDF text layer vs OCR) as injection/junk detector.  
- Optional language hint packs for OCR.

### Deferred

- Certified metrology from photos; mobile capture product; perfect table SLA.  
- Full malware AV / signed enterprise quarantine product (Admin offline-media path remains WP-00).

### Never

- Raw binary to draft LLM as normal path.  
- Remote URL ingest.  
- Cloud OCR/Document AI.  
- Auto-index unverified OCR as plant truth.  
- Skip H1 / S6 without H1 confirm.  
- Treat `human_verified` extract as trusted **system instructions** (WP-23).  
- Claim P&ID/handwritten certification or MRPL KPI hours.  
- Lock a single OCR brand as permanent product identity.  
- Auto-extract embedded PDF attachments into the main extract.

---

## 12. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Tesseract/PaddleOCR *candidates*; local VLM `data:` pattern | Official on-device |
| **Adopt** | MIME sniff + allowlist; rasterize→OCR preference; metadata/Unicode strip; immutable original + parser_version | Ingest hygiene (Observed) |
| **Add** | S0–S6 plane; extract schema; low-friction H1; 5-page + byte ceiling demo; unusable remediation; trust_label | KWB |
| **Refuse** | Cloud Document AI; RAGFlow-as-KWB; remote URLs; “handle all CAD”; AV-as-must-work; verified=safe-prompt |

---

## 13. Boundary vs later WPs

| Topic | WP-03 | Later |
|---|---|---|
| H1 / stale | Consumes WP-05 | — |
| OCR text injection | Untrusted label | **WP-23** |
| KB index of extracts | After verified only | **WP-11** |
| Which draft model | Hand-off only | **WP-06 / WP-24** |
| GPU load | Sequential OK | **WP-10** |
| Context packing | Feeds extract | **WP-21** |

---

## 14. Demo acceptance

1. Attach ≤5-page scan → stages run → extract shown (not raw PDF in drafter).  
2. Low-confidence fields highlighted → worker fixes → H1 confirm.  
3. Unusable page → issue shown → new scan or typed text → re-extract → H1.  
4. Optional VLM card id logged when used; OCR card id logged.  
5. Drawing or photo multimodal understanding showable.  
6. Attempt remote URL image → denied.  
7. Draft path uses **verified/normalized** extract.

---

## 15. Explicitly not locked

OCR/VLM product names, PDF library, JSON vs markdown store, topic-segment algorithm, exact confidence thresholds, UI wireframes.

---

## 16. Findings traceability

| ID | Where |
|---|---|
| R0, Q1–Q6 | §3–§10 |
| M1–M8 (pre-freeze) | §4–§10 |
| F1–F12 (freeze red-team) | §2, §4, §5, §10, §11 |
| A1–A6 / freeze A1–A5 | §2, §11 Never |
| Adopt | §12 |

**Confidence:** **0.90** after rev 1.1 (`WP-03_FREEZE_REDTEAM.md`).

---

## 17. Next

**WP-23** — Untrusted content / injection (OCR, RAG, MCP, `.md`) — consumes `trust_label` + delimiters.

---

## 18. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze: pre-LLM plane + DM Q1–Q6 |
| **1.1** | Freeze red-team F1–F12: sniff/allowlist, immutable original, raster+OCR preference, S4 hygiene, partial units, encrypted/embed deny, trust_label, S6 tighten, byte ceiling |
