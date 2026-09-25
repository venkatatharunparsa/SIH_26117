# Demo / PS components verify — built vs designed

**Date:** 2026-09-20  
**Problem:** SIH26117 Knowledge Work Bench (PS demo)  
**Mode:** Single laptop · one model `llama3.2:3b` (G1 floor)  
**Sources of design:** DESK_IA · GATE_90 · WP-05 · CUSTOM Must M1–M10 · UI_CLAUDE_CODE  

**Rule:** **BUILT** = code exists + E2E/API proven · **UI-WIRED** = desk can call it · **NOT REQUIRED** = out of day-1 / refused  

---

## 1. Verdict (one line)

**Yes — all Must components required for the PS demo are built and API-proven.**  
Gaps are **Later / out-of-scope** (installer, PPT, Poppler scanned-PDF rasterization, human Electron click recording) — not missing demo spine. Image OCR + PDF text-layer ingest are wired.

---

## 2. DESK_IA screens (designed → built)

| # | Designed | Built where | E2E proven |
|---|---|---|---|
| 1 Intent | Task type + start | Composer task select + Start | **YES** |
| 2 Files | Attach / fixture | Composer ⌁ attach (text/file/fixture) | **YES** (API uses extract; UI present) |
| 3 Extract + H1 | H1 confirm | `/task/h1-confirm` + next step | **YES** |
| 4 Knowledge | Retrieve + H7 | `/task/retrieve` · `/task/h7-ack` | **YES** |
| 5 DRAFT | Word + version | `/task/inspect-draft` | **YES** |
| 6 Gates | H2 · H9 · stale | h2 · draft-edit · h9 | **YES** |
| 7 Export leave | Soft copy + pack | `/task/export` · leave-pack · artifacts | **YES** |
| 8 Monitor B | Grant/card/model/denies | MonitorPanel on demand | **UI YES** · poll when open |

Fail-closed designed: revoke · secret · bad model · sandbox-red · h2_stale → **ALL API-proven** in E2E/HITL.

---

## 3. Backend components (required for demo)

| Component | File | Demo need | Status |
|---|---|---|---|
| Grants / ACL | `grants.py` | Yes | **BUILT** |
| Model cards + router | `cards.py` + `models.yaml` | Yes (G1 floor) | **BUILT** |
| Artefacts / H2 H7 H9 | `artefacts.py` | Yes | **BUILT** |
| Word DRAFT | `word_draft.py` | Yes | **BUILT** |
| Retrieve cite-or-abstain | `retrieve.py` | Yes | **BUILT** |
| Secrets G9 | `secrets.py` | Yes | **BUILT** |
| Sandbox + G10 | `sandbox.py` | Yes | **BUILT** |
| Gateway G8 | `gateway.py` | Yes | **BUILT** |
| Monitor A ≠ CERT | `monitor_a.py` | Yes | **BUILT** |
| Audit | `audit.py` | Yes | **BUILT** |
| FastAPI routes | `main.py` | Yes | **BUILT** + 18/18 endpoints |
| MCP host / skills runner | mock / files only | **No (day-1)** | Stub / held |
| Live OCR engine | `ocr_extract.py` | Demo-useful | **BUILT (framework)** — Tesseract images + pypdf text PDFs; fixture stub if binary missing. **Org SoT = OCR model** (not day-1) |

---

## 4. Desktop UI components (required for demo)

| Component | Path | Status |
|---|---|---|
| Electron shell | `electron/main.cjs` + preload | **BUILT** |
| App / sessions / stream | `App` · `SessionList` · `Transcript` · `ToolBlock` | **BUILT** |
| Claude Code composer | `Composer.tsx` | **BUILT** |
| Monitor B on demand | `MonitorPanel.tsx` | **BUILT** |
| API client | `api.ts` | **BUILT** |
| Fixtures constants | `constants.ts` | **BUILT** |
| Installer `.exe` | — | **NOT built** (Later — not Must) |
| Next marketing desk | `kwb-desk` | **REJECTED** (correct) |

---

## 5. Demo Must milestones (M1–M10)

| M | Required | Status |
|---|---|---|
| M1–M3 leave downloads | Yes | **PASS** |
| M4–M7 MonB / injects / H7 / walk | Yes | **PASS** |
| M8 evidence | Yes | **PASS** (`eval/evidence/`) |
| M9 checklist signed | Yes | **PASS** (agent; DM optional) |
| M10 stage runbook | Yes | **PASS** |

---

## 6. Integrity components (PS locks)

| Lock | Built? |
|---|---|
| Assist → export leave | **YES** |
| Self-HITL (no in-app Approver) | **YES** |
| DRAFT ≠ CERT · MonA ≠ CERT | **YES** |
| Ollama inference-only / one model floor | **YES** |
| Single-laptop demo mode | **YES** (locked) |

---

## 7. Explicitly NOT required for this demo (do not treat as missing)

- Two-laptop Model Workstation  
- Multi-model G1 full  
- SSO / Admin / Postgres  
- Live plant OCR  
- DeerFlow / OpenHands Canvas  
- Final jury PPTX (process next — not a runtime component)  
- electron-builder installer  

---

## 8. Only residuals before you show PS demo

1. **You:** click Electron once per `eval/STAGE_RUNBOOK.md` (API E2E already green)  
2. **Optional:** PPT slides  
3. **Optional:** DM co-sign checklist  

---

## 9. Evidence pointers

- `eval/evidence/E2E_ONE_MODEL.json` — full one-model walk **ok: true**  
- `eval/evidence/ENDPOINT_VALIDATE.json` — 18/18  
- `eval/evidence/SUMMARY.json` — G1–G10  
- `eval/STAGE_RUNBOOK.md` — operator script  

**Final call for PS demo components:** **COMPLETE for Must.** Residual = human UI rehearsal + pitch deck, not missing software components.
