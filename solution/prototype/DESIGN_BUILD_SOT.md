# Design-info build locks (GATE_90 B1–B7)

**Date:** 2026-09-19  
**Status:** **LOCKED** post RT fixes — design info **~0.90**  
**Parent:** `GATE_90_DISCUSS.md` · `GATE_90_REDTEAM.md`

| ID | Lock | SoT | Status |
|---|---|---|---|
| **B1** | Desk IA + deny/state wires | `DESK_IA.md` | **DONE** |
| **B2** | Fixture extract + H1 API | FX-EXT-01 · `POST /task/h1-confirm` | **DONE** |
| **B3** | H9 → export deny if sandbox-red | `artefacts.py` · export G10 | **REAL** |
| **B4** | `artefact_version` · H2 stale | `/task/h2-ack` · `/task/draft-edit` | **REAL** |
| **B5** | Eval template + signer | `eval/CHECKLIST.md` | **TEMPLATE** (unsigned OK for design) |
| **B6** | G1 honesty | A3 / WP-18 | **DONE** |
| **B7** | Fixture catalogue on disk | `FIXTURE_CATALOGUE.md` + FX-CODE-01 | **DONE** |

**Build may continue** (desk UI next). PPT still after execute ≥0.90 + signed eval.
