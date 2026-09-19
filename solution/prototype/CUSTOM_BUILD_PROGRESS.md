# Custom build progress — SIH26117

**Updated:** 2026-09-19  
**Plan:** `CUSTOM_DEMO_BUILD_PLAN.md` · UI research: `UI_CLAUDE_CODE_ADV.md`  
**Scope this pass:** **KWB = desktop application (Electron)** + FastAPI — not a web/marketing desk

---

## D0 / D1 status (API + desk maturity) — preserved

| Item | Status | Notes |
|---|---|---|
| **M1–M3** leave-with | **PASS** | unchanged |
| **M4–M7** desk maturity + H7 | **PASS** | API unchanged; wired into Electron stream UI |
| **M8–M10** execute evidence / checklist / runbook | **Not this pass** | Eval scripts left alone; do not block on UI |

---

## Application UI (this pass) — Claude Code desk

| Item | Status | Notes |
|---|---|---|
| Adversarial research | **PASS** | `solution/prototype/UI_CLAUDE_CODE_ADV.md` |
| Electron scaffold | **PASS** | `apps/kwb-app/` — Electron + Vite + React |
| Claude Code layout | **PASS** | Left sessions · center stream+composer · right Monitor B |
| API client | **PASS** | `http://127.0.0.1:8080` — start, h1, retrieve, draft, h2, export, leave-pack, sandbox, monitor-a, audit |
| Integrity chrome | **PASS** | DRAFT badge · not CERT · no Approver · export leave |
| `apps/kwb-desk/` | **REJECTED / legacy** | Syne hero Next marketing UI — do not demo |
| Static `desk/` | **Legacy** | HTML fallback only |

**Refuse (honoured):** Syne hero landings · Open WebUI clone · DeerFlow/OH Canvas fork · rewrite FastAPI.

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

- M8–M10 eval evidence if not done  
- Electron packaging / double-click installer = **Later**  
- PPT still after execute ≥0.90
