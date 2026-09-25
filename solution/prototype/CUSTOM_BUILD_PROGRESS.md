# Custom build progress — SIH26117

**Updated:** 2026-09-20  
**Plan:** `CUSTOM_DEMO_BUILD_PLAN.md` · UI research: `UI_CLAUDE_CODE_ADV.md`  
**Scope:** **KWB = desktop application (Electron)** + FastAPI — not a web/marketing desk

---

## D0 / D1 / D2 status (API + desk + eval)

| Item | Status | Notes |
|---|---|---|
| **M1–M3** leave-with | **PASS** | artifacts + leave-pack; re-verified 2026-09-20 |
| **M4–M7** desk maturity + H7 | **PASS** | MonB / injects / H7 SoT / step locks; re-verified 2026-09-20 |
| **M8** execute evidence | **PASS** | `backend/scripts/execute_walk.py` → `eval/evidence/*` (G1–G10 all true) |
| **M9** checklist | **PASS** | `eval/CHECKLIST.md` **SIGNED** — G1 **floor**; `demo_ready: true` |
| **M10** stage runbook | **PASS** | `eval/STAGE_RUNBOOK.md` (inspection + fail-closed + MonA≠CERT) |

### Stage dry-run (same day)

| Walk | Result | Evidence |
|---|---|---|
| Inspection A→J + fail-closed G9/G7 | **PASS** | `eval/evidence/STAGE_DRY_RUN_AJ.json` |
| HITL stale + G10 | **PASS** | `backend/scripts/hitl_gates_smoke.py` |

---

## Application UI — Claude Code desk

| Item | Status | Notes |
|---|---|---|
| Electron scaffold | **PASS** | `apps/kwb-app/` — Electron + Vite + React |
| Claude Code layout | **PASS** | Sessions · stream+attach+composer · Monitor B **on demand** |
| Attach (text/doc/fixture) | **PASS** | Inside Claude Code `Composer` popover (orphan AttachInput removed) |
| Endpoint validate 18/18 | **PASS** | `eval/evidence/ENDPOINT_VALIDATE.json` · G8/G9 HTTP harden |
| Red-team P0–P2 | **PASS** | draft-edit · H7 · will-navigate · fixtures · `kwb-desk/LEGACY.md` |
| API client | **PASS** | `http://127.0.0.1:8080` |
| Integrity chrome | **PASS** | DRAFT badge · not CERT · no Approver · export leave |
| `apps/kwb-desk/` | **REJECTED / legacy** | Do not demo |
| Static `desk/` | **Legacy** | HTML fallback only |

**Refuse (honoured):** Syne hero · Open WebUI clone · DeerFlow/OH Canvas fork · rewrite FastAPI · final jury PPTX this pass.

---

## Execute score (honest re-score 2026-09-20)

| Axis | Score | Notes |
|---|---|---|
| Architecture freeze | **≥0.90** | unchanged |
| Design info | **≥0.90** | unchanged |
| **Execute-ready** | **0.90** | Must M1–M10 done; signed G pack; A→J API dry-run + fail-closed |
| **PPT-ready** | **0.35** | **NO-GO** until team builds slides (gate cleared for start) |
| G1 mode | **floor** | single local tag `llama3.2:3b` · two cards — do not claim full multi-tag |

**Residual (does not drop below 0.90):** human-timed Electron jury rehearsal not recorded this session — follow `eval/STAGE_RUNBOOK.md` once before stage. Optional DM human co-sign on checklist.

**Exact gap if raising toward 0.92+:** live Electron A→J timing + optional second offline chat tag for G1 full (never pull).

---

## How to run (desktop application)

```text
# Terminal A — API
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8080

# Terminal B — Electron desk
cd apps/kwb-app
npm install
npm run electron:dev
# → window title: Knowledge Work Bench
```

Renderer-only (debug): `cd apps/kwb-app && npm run dev` → `http://127.0.0.1:5173`

---

## Next

- Operator rehearsal with `eval/STAGE_RUNBOOK.md` (Electron)  
- PPT **may start** now that execute ≥0.90 — still scrub prompts; no CERT / Approver-in-app claims  
- Electron packaging / installer = **Later**
