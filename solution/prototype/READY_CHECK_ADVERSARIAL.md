# KWB readiness check — deep adversarial (2026-09-19)

**Status:** **SUPERSEDED for GATE scores** — 2026-09-19.  
**Do not use this file for architecture/design ≥0.90 claims or PPT fill.**  
**Current SoT:** `GATE_90_DISCUSS.md` + `GATE_90_REDTEAM.md` (honest ~0.84 arch / ~0.76 design / 0.38 execute; **GO-WITH-FIXES**).

**Historical question:** Did we have full information for building or PPT?  
**Historical method:** Adversarial pass on freezes · org/demo diagrams · REAL code · PPT pause pack · G1–G10.  
**Historical verdict:** Neither fully ready — kept below for archaeology only.

---

## Confidence scores (ready check) — HISTORICAL snapshot

| Axis | Score | One-line why |
|---|---|---|
| **Architecture freeze** | **0.68** | O1–O6 + D1–D6 + stack accepted; **WP-05 dual story** + **WP-20 unfrozen** |
| **Workbench build-ready** | **0.38** | API spine REAL; **no desk UI**, no OCR/H1, no H9/G10, G1 one-model honesty, export import risk |
| **PPT-ready** | **0.42** | Content skeleton exists under `ppt-paused/`; **no locked PPTX**; S2 failed; HITL/G1 unsafe on slides |
| **Jury-demo-ready** | **0.22** | Cannot run signed A→J desk walk + G1–G10 pack today |
| **Information completeness (build SoT)** | **0.72** | Enough design to code against; gaps are **implementation + freeze reconcile**, not “blank paper” |
| **Information completeness (PPT SoT)** | **0.55** | Enough themes; **not** enough reconciled freeze language + honest metrics + final assets |

**Bottom line score for “full information?”**  
- Build: **~0.72 design info** / **~0.38 execute-ready**  
- PPT: **~0.55 content info** / **~0.42 slide-ready**  

→ Prefer **continue workbench build** (process already pivoted). Do **not** resume PPT until WP-05 + G1 honesty fixed.

---

## What we DO have (full enough)

### For building
- Flow A→J locked · assist→export · no forward-accept  
- Org O1–O6 + demo D1–D6 accepted  
- Demo stack BOM + REAL/MOCK/LATER  
- Ollama = inference only · no pull · adopted `llama3.2:3b`  
- Backend modules: grants, cards, gateway, Word DRAFT, retrieve, sandbox, Monitor A, secrets, audit chain  
- Fail-closed script stub · eval checklist template  

### For PPT (partial)
- `solution/ppt-paused/PPT_CONTENT_DESIGN.md`  
- Slide prompts + prior red-team  
- Architecture narrative inputs (diagrams, Expected Solution maps)  

---

## Critical blockers

### Build
1. No Claude-like **desk UI**  
2. **G4/H1 OCR** not in code  
3. **H9 / G10** sandbox→export gate missing  
4. **G1** claims ≥2 `model_id`s; reality = one chat tag (honest dual-card)  
5. **eval/** not signed G1–G10 pack  
6. **WP-05** freeze still Approver vs self-HITL  
7. Export path may miss `ARTIFACTS_DIR` import (verify/fix before demo)

### PPT
1. Work **paused**; no official filled PPTX in repo  
2. **S2** image not accepted  
3. HITL dual story unsafe on slides  
4. Dual-model / air-gap wording easy to overclaim vs code  
5. Team ID placeholders  

---

## Dual stories (highest risk)

| Topic | Conflict |
|---|---|
| HITL | WP-05 **Approver** vs F6/diagrams **self-HITL** |
| G1 | WP-18 ≥2 **model_ids** vs adopted **one** chat model |
| Monitor A | “WAN=0 proof” pitch vs loopback snapshot artefact |
| WP-20 | Connection docs open · not frozen |

---

## Recommended path (adversarial)

1. Reopen **WP-05** → self-HITL / export-leave (unblocks PPT + demo honesty)  
2. Minimal **desk UI** + inspection + fail-closed walk  
3. Code: H1 fixture · H9/G10 · fix export · second model **only if staged offline** (no pull) or rewrite G1 pass language  
4. Sign **eval/** pack  
5. Only then resume PPT with honest captions  

---

## Answer to “full information for building or PPT?”

| | Full information? | Ready to ship? |
|---|---|---|
| **Workbench build** | **Mostly yes** (design SoT ~0.72) | **No** (execute ~0.38) |
| **PPT** | **Partially** (~0.55) | **No** (~0.42) |

You are **paper-strong + spine-started**, not **demo-complete** or **PPT-locked**.
