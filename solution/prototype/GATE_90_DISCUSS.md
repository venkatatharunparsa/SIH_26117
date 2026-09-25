# Gate to ≥0.90 — post red-team fixes

**DM rule (2026-09-19):** Architecture freeze · Design info · kickoff ≥0.90 before full desk/PPT thrash.

**Pre-verify RT:** `GATE_90_REDTEAM.md` → Criticals **fixed** 2026-09-19.  
**Smoke:** `backend/scripts/hitl_gates_smoke.py` **PASS** (stale deny · sandbox-red H9 · G10) — re-run **PASS** 2026-09-20.

---

## Current → target

| Axis | After RT (honest) | **2026-09-20** | Target |
|---|---|---|---|
| Architecture freeze | ~0.84 | **≥0.90** | ≥0.90 |
| Design info (build) | ~0.76 | **≥0.90** | ≥0.90 |
| Execute-ready | 0.38 → ~0.64 (desk) | **0.90** | ≥0.90 — M1–M10 done |
| Kickoff | GO-WITH-FIXES | **GO** | thicken done; eval signed |

---

## A / B status

| ID | Status |
|---|---|
| A1–A5 freezes | **DONE** + dual-story docs scrubbed |
| B1 DESK_IA wires | **DONE** (Electron `apps/kwb-app`) |
| B2 H1 fixture API | **DONE** `/task/h1-confirm` |
| B3 H9/G10 | **REAL** |
| B4 artefact_version/stale | **REAL** |
| B5 eval | **SIGNED** — `eval/CHECKLIST.md` · `eval/evidence/` populated |
| B6 G1 | **DONE** (floor single-tag adopt) |
| B7 fixtures | **DONE** incl. FX-CODE-01 |

---

## Execute ≥0.90 — closed 2026-09-20

1. Desk UI — Electron primary `apps/kwb-app` (M4–M7 wired)  
2. Signed `eval/CHECKLIST.md` + `eval/evidence/` via `execute_walk.py` — **DONE**  
3. Inspection A→J + fail-closed — `stage_dry_run_aj.py` **PASS**  
4. Runbook — `eval/STAGE_RUNBOOK.md` **DONE**

**PPT:** gate cleared to **start** (execute 0.90). Do not ship slides that claim CERT / in-app Approver / G1 full without offline second tag.

---

## Status

| Mode | Value |
|---|---|
| RT Criticals | **FIXED** |
| Verify-accept arch+design ≥0.90 | **READY for DM** |
| Execute-ready | **0.90** (honest; residual = live Electron timing rehearsal) |
| Next | Operator rehearsal · optional PPT from scrubbed prompts |
