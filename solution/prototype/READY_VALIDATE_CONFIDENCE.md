# READY VALIDATE — adversarial + endpoint + confidence

**Date:** 2026-09-20 (updated after discussion issue closure)  
**Method:** Live URL/endpoint matrix · G1–G10 walk · HITL smoke · desk↔API map · manual UI · research (SIH offline demo practice)  
**Honesty rule:** Scores below are **not marketing**.

---

## 1. Expected URLs (what is correct)

| What | URL / command | Status |
|---|---|---|
| **API base** | `http://127.0.0.1:8080` | **LIVE** |
| **Health** | `GET /health` | **200** · `desk: apps/kwb-app` |
| **Root discovery** | `GET /` | **200** JSON · Electron primary |
| **Legacy HTML** | `http://127.0.0.1:8080/desk/` | Exists · **do not demo as primary** |
| **Rejected web** | `apps/kwb-desk` | **Hard-fail** on `npm run dev` |
| **Electron desk** | `cd apps/kwb-app && npm run electron:dev` | Primary |
| **One-command start** | `pwsh -File scripts/start_demo.ps1` | **Added** |
| **Vite renderer (debug)** | `http://127.0.0.1:5173/` | Dev only |
| **Ollama** | `http://127.0.0.1:11434` | Required pre-staged tag |
| **OpenAPI** | `http://127.0.0.1:8080/docs` | Available |

---

## 2. Endpoint matrix

**Evidence:** `eval/evidence/ENDPOINT_VALIDATE.json` · `execute_walk` G1–G10 · `MANUAL_TEST_REPORT.md`

Desk actions for Must are **wired** (Start…Export, More injects, Monitor downloads, audit poll + **Verify chain**).

---

## 3. Adversarial Q&A (this pass)

| Q | Answer |
|---|---|
| Is working software ready? | **YES** for API + UI demo. Not “shipped product.” |
| Did we complete everything? | Day-1 Must **yes**. Held: installer, filled PPTX, OCR, G1 full, DM co-sign. |
| Can jury run offline? | **Mostly** — pre-stage Ollama tag; use `start_demo.ps1`. |
| Were denies real HTTP? | **Yes** G8/G9 → 403/400. |
| Does health lie about desk? | **No** — `apps/kwb-app`. |
| Is Electron UI proven? | **Yes** — `MANUAL_TEST_REPORT.md` (Vite renderer = same React as Electron). |

---

## 4. Red-team findings → fixed vs held

| Finding | Severity | Action |
|---|---|---|
| Health/`SUMMARY` legacy `/desk/` | High honesty | **FIXED** |
| G8/G9 soft HTTP 200 | Medium | **FIXED** → 403/400 |
| Orphan `AttachInput.tsx` | Low | **DELETED** |
| DESIGN_BUILD_SOT B5 TEMPLATE | Doc | **FIXED** → SIGNED |
| No recorded UI operator walk | High | **FIXED** — `MANUAL_TEST_REPORT.md` |
| G9 inject false OK | High demo | **FIXED** inject + AKIA regex |
| Deferred G8/revoke/sandbox UI | Medium | **FIXED** — retested PASS |
| Two-terminal launch | Medium | **FIXED** — `scripts/start_demo.ps1` |
| kwb-desk footgun | High | **FIXED** — npm refuse + banner |
| Revoke hang after export | Medium | **FIXED** — revoke-on-export |
| Audit hash UI | Low polish | **FIXED** — Monitor Verify chain |
| Coding next-step weak | Medium | **FIXED** — guided path |
| No `.exe` | Medium | **Held** Later |
| PPT not built | Pitch | **Held** — gate allows start |
| G1 floor only | Honesty | **Held** — do not claim multi-model |

---

## 5. Confidence scores (0–1)

| Axis | Score | Why |
|---|---|---|
| API correctness | **0.93** | Endpoints + G1–G10 + HITL |
| Integrity / fail-closed | **0.93** | HTTP denies + UI injects + AKIA harden |
| Desktop app readiness | **0.86** | Dev Electron + start script; no installer |
| UI Claude Code soak | **0.88** | Manual A→J + G7–G10 injects |
| Offline SIH venue | **0.82** | start_demo.ps1 + preflight Ollama |
| PPT / pitch | **0.30** | Held |
| **Working software ready** | **0.91** | |
| **Jury stage ready** | **0.88** | Needs filled PPT when pitching |
| **Complete product** | **0.68** | Packaging + PPT + Held scope |

---

## 6. Research — what is good for us

| Practice | For KWB |
|---|---|
| Pre-stage Ollama · never pull | **Policy** |
| One command start | **`scripts/start_demo.ps1`** |
| Rehearse full walk | **Done** — MANUAL_TEST_REPORT |
| Freeze features before pitch | **Do** — PPT next when asked |
| No CERT / Approver / dual-model claims | **Integrity** |

---

## 7. Lagging checklist

### Done this pass
- [x] UI STAGE walk + fail-closed injects  
- [x] `start_demo.ps1`  
- [x] G9/AKIA harden · revoke-on-export · audit verify UI · kwb-desk refuse  

### Operator before venue
- [ ] Confirm Ollama `llama3.2:3b` on demo laptop (**no pull**)  
- [ ] Optional: `npm run electron:prod` once  

### Held / pitch
- [ ] Build PPT from `solution/ppt-paused/` when team starts slides  
- [ ] electron-builder installer only if jury demands `.exe`  

---

## 8. Verdict

**Working software (API + fail-closed + UI walk + one-command start): READY** at confidence **0.91**.  

**Filled jury PPTX / installer:** still **Held** — not day-1 defects.
