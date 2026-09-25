# Word DRAFT — complete requirement design (DM lock before further build)

**Status:** DESIGN for DM accept — **do not implement further stack** (second LLM, multimodal, PPTX-primary) until this is accepted.  
**Date:** 2026-09-20  
**Binding contract:** Official SIH26117 **Expected Solution** — *scanned inspection → key findings → approval note as a **Word** file*.  
**DM already locked:** Word = primary inspection deliverable; PPTX = secondary / org-ext only.

**Mem0 keys:** `SIH26 WORD REQUIREMENT` · `SIH26 DM DECISIONS` · `SIH26 BUILD AUDIT BOARD`

---

## 1. One-sentence requirement

KWB must produce a **labelled Word `.docx` DRAFT approval / inspection recommendation note** on the orch spine after human Confirm extract + cite review, then Self-check DRAFT + Export leave — **Gateway never builds the file**; Orch/Workbench does.

---

## 2. Problem-statement alignment

| Source | Requirement | Word implication |
|---|---|---|
| Expected Solution | Agentic E2E → **Word** approval note | `.docx` is the **must-demo** artefact |
| Description | Approval notes, PPT/Word/Excel | PPT/Excel = ambition / Later — **not** substitute for Word on stage |
| Batch4 (Mem0) | Inspection Recommendation Note — decision first, evidence, cites, DRAFT | Structure the `.docx` sections (below) |
| Org O2/O3 | Word must · Excel/PPT ORG EXT · Pack→Gateway only · export ends path | Gateway ≠ Word builder; no in-app forward-accept |

---

## 3. In scope (this requirement)

1. **Primary artefact:** `.docx` with visible **DRAFT** banner (not plant record, not CERT).  
2. **Spine:** Desk → `/orch/turn` → grant/card → ingest/extract → **Confirm extract** → retrieve/cites → **Review citations** → **Word DRAFT** → secrets check → **Self-check DRAFT** → **Export leave** → store (+ revoke grant).  
3. **Content sources:** confirmed extract + company-doc cites + (optional) sandbox calc lines when present.  
4. **Download / leave-with:** desk can download `.docx`; leave-pack prefers `.docx`.  
5. **Audit:** `word_draft` event + `artefact_version` + grant_id in meta.  
6. **Secrets scan** on docx text before export leave (existing pattern).  
7. **Stale deny:** re-OCR / re-extract bumps version; old Word version cannot pass Self-check / export as current.

---

## 4. Out of scope (explicit)

| Item | Status |
|---|---|
| PPTX as Expected Solution proof | **Out** — secondary only after Word locked |
| In-app Approver / forward-accept | **Out** — paper approval outside KWB |
| Live plant template governance / SSO | **Out** / Later |
| Excel corrosion workbook | Later / sandbox proof separate |
| Gateway writing `.docx` | **Forbidden** |
| Claiming CERT / plant SoR | **Forbidden** |
| Second LLM / multimodal vision | **Paused** until this Word req is accepted + Word path is primary on orch |

---

## 5. Document structure (required sections)

Minimum sections in the `.docx` (order fixed for demo honesty):

1. **Banner:** `DRAFT — NOT A PLANT RECORD — FOR EXPORT / REVIEW ONLY`  
2. **Title:** e.g. Inspection recommendation / thickness note  
3. **Meta line:** UTC generated · `model_id` · `task_id` · `artefact_version` · `grant_id` (short) · `card_id`  
4. **Decision / recommendation first** (one short paragraph — Batch4)  
5. **Equipment / asset** (id, location if known)  
6. **Findings / defect / evidence** (from Confirm extract — human-acked text)  
7. **Citations** (bullets; if none → literal `NOT FOUND — no grounded citations`)  
8. **Actions / restrictions / monitoring** (from extract or “NOT STATED”)  
9. **Footer:** Status DRAFT · export leave ends path · no in-app accept-for-forward  

**Optional (if sandbox ran):** short “Verified calc/code” block with sandbox job id — never invent numbers.

**Must not:** invent missing thickness/CR; hide adverse findings; strip DRAFT badge.

---

## 6. Functional requirements (FR)

| ID | Requirement | Accept test |
|---|---|---|
| FR-W1 | Orch inspection happy path writes **`.docx`**, not `.pptx`, as primary draft | After cite confirm → `draft.format=docx` · file under `workspace/artifacts/` |
| FR-W2 | Existing `/task/inspect-draft` remains Word and is consistent with orch fields | G2 smoke still PASS |
| FR-W3 | Desk shows Download DRAFT for `.docx` | UI link `/artifacts/{file}?grant_id=` |
| FR-W4 | Self-check DRAFT + export leave work on `.docx` | Secrets + H2 + leave-ready + grant revoke |
| FR-W5 | Leave-pack zip includes Word DRAFT | `/task/leave-pack` with `.docx` |
| FR-W6 | PPTX path disabled or demoted | Orch default `draft_format=docx`; PPTX only via explicit Later/secondary intent |
| FR-W7 | Template fields align FX-TPL-01 | title, asset, finding, recommendation, citations, DRAFT status |
| FR-W8 | Cite-or-abstain reflected in Word | Empty cites → NOT FOUND line |

---

## 7. Non-functional / trust (NFR)

| ID | Requirement |
|---|---|
| NFR-W1 | Word built only on Workbench plane — **never** in Gateway |
| NFR-W2 | Model text used in findings must have passed Pack→Gateway if LLM-assisted; template fill may be deterministic from extract |
| NFR-W3 | Fail-closed audit if draft write fails |
| NFR-W4 | Classification: treat as confidential synthetic in demo fixtures |
| NFR-W5 | Honest labels on UI/PPT: “Word DRAFT”, never “approved plant note” |

---

## 8. API / orch contract (target)

```
POST /orch/turn
  attach / confirm_extract / confirm_cites
  → tools include word_draft (not pptx_draft as primary)
  → response.draft = { filename, path, format: "docx", artefact_version, download }

POST /task/inspect-draft   (unchanged contract — Word)
GET  /artifacts/{name}?grant_id=
POST /task/self-check      (docx)
POST /task/export-leave    (docx)
GET  /task/leave-pack      (docx required)
```

**Grant / card:** inspection → `inspect-draft` card (or successor) — card does **not** build Word; it only selects model for any LLM assist before draft.

---

## 9. Desk UX requirements

1. After cite confirm: stream note **“Word DRAFT written”** + download affordance.  
2. Self-check ask uses plain language **Self-check DRAFT** (not bare H2).  
3. Monitor / More menu: Download DRAFT · Leave pack.  
4. Do not present PPTX as the inspection success artefact in the default flow.

---

## 10. Current code vs this requirement (honest gap)

| Piece | Today | Gap |
|---|---|---|
| `word_draft.py` | Exists — banner, findings, cites, DRAFT | Missing decision-first, asset, actions sections; thin vs Batch4 |
| `/task/inspect-draft` | Writes Word | OK for G2 |
| `/orch/turn` cite→draft | Writes **PPTX** (`draft_format=pptx`) | **Must flip to Word** after DM accept |
| FX-TPL-01 | Markdown field list | Not fully applied in `write_inspection_draft` |
| Leave-pack | Prefers docx | OK if orch emits docx |

---

## 11. Demo script (Word-primary — after implement)

1. Start API + Electron desk.  
2. Attach fixture README or PDF extract (vessel V-101).  
3. **Confirm extract** → **Review citations**.  
4. System writes **`draft-*.docx`**.  
5. **Self-check DRAFT** → **Export leave**.  
6. Open `.docx`: DRAFT banner + decision + findings + cites visible.  
7. Jury leave-with: Word + optional leave-pack zip.

---

## 12. Acceptance checklist (DM sign)

- [ ] Sections in §5 accepted (add/remove?)  
- [ ] Orch primary = Word; PPTX secondary confirmed  
- [ ] No further multi-model / multimodal build until Word path implements this  
- [ ] PPT slides will say Word DRAFT (not PPTX) for Expected Solution  
- [ ] Optional: enrich `word_draft.py` to Batch4 sections in same change set  

---

## 13. Implementation order (only after DM accept of this doc)

1. Flip orch draft writer Word-primary + smoke `smoke_orch_word.py`  
2. Enrich `write_inspection_draft` to §5 sections  
3. Desk copy / download defaults to docx  
4. Update BUILD AUDIT BOARD in Mem0: Word gap closed  
5. **Then** discuss second LLM + multimodal  

---

## 14. DM answers (locked 2026-09-20)

1. **LLM polish before Word** — After cite confirm, Orch runs **one Pack→Gateway polish pass** on extract+cites, then fills `.docx`. Do **not** invent cites/numbers; abstain with NOT STATED / NOT FOUND.  
2. **Proper Word** — Full §5 Batch4-style sections (not thin findings-only).  
3. **Plain DRAFT** — no company logo for SIH demo (unless DM adds later).

### Polish contract
```
inputs: confirmed extract, cite lines, task/card meta
via: Pack → Gateway → model_id on grant card
output (structured): decision, asset, location, findings, recommendation, actions, restrictions, monitoring
then: word_draft.write_inspection_draft(...) → .docx
fail: if Gateway deny/error → do not write fake polish; return error (honest)
```

---

**Status:** §14 locked — **implement Word-primary + polish now**.  
Second LLM / multimodal still paused until Word path is primary and smokes PASS.
