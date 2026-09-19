# Gate to ≥0.90 — post red-team fixes

**DM rule (2026-09-19):** Architecture freeze · Design info · kickoff ≥0.90 before full desk/PPT thrash.

**Pre-verify RT:** `GATE_90_REDTEAM.md` → Criticals **fixed** 2026-09-19.  
**Smoke:** `backend/scripts/hitl_gates_smoke.py` **PASS** (stale deny · sandbox-red H9 · G10).

---

## Current → target

| Axis | After RT (honest) | **After fixes** | Target |
|---|---|---|---|
| Architecture freeze | ~0.84 | **≥0.90** | ≥0.90 |
| Design info (build) | ~0.76 | **≥0.90** | ≥0.90 |
| Execute-ready | 0.38 | **~0.64** (desk HTML landed; leave-with + evidence + H7 still open) | ≥0.90 — see `CUSTOM_DEMO_BUILD_PLAN.md` |
| Kickoff | GO-WITH-FIXES | **GO** | thicken desk MVP (not React rewrite) |

---

## A / B status

| ID | Status |
|---|---|
| A1–A5 freezes | **DONE** + dual-story docs scrubbed |
| B1 DESK_IA wires | **DONE** |
| B2 H1 fixture API | **DONE** `/task/h1-confirm` |
| B3 H9/G10 | **REAL** |
| B4 artefact_version/stale | **REAL** |
| B5 eval | **TEMPLATE** (unsigned — blocks demo_ready only) |
| B6 G1 | **DONE** |
| B7 fixtures | **DONE** incl. FX-CODE-01 |

---

## Remaining before execute ≥0.90

1. Desk UI per `DESK_IA.md` — **shell exists** (`desk/index.html`); thicken leave-with + MonB + H7 + fail-closed injects per `CUSTOM_DEMO_BUILD_PLAN.md`  
2. Signed `eval/CHECKLIST.md` + `eval/evidence/` via `execute_walk.py`  
3. Full inspection A→J walk on stage  

**PPT:** still paused until execute ≥0.90.

---

## Status

| Mode | Value |
|---|---|
| RT Criticals | **FIXED** |
| Verify-accept arch+design ≥0.90 | **READY for DM** |
| Next | Custom MVP in `CUSTOM_DEMO_BUILD_PLAN.md` (Must M1–M10) · then goldens · PPT after execute ≥0.90 |
