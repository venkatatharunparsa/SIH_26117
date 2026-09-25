# SIH_26117

**Knowledge Work Bench (KWB)** — Smart India Hackathon 2026 problem statement SIH26117 (MRPL · Software · Smart Automation).

Offline-first knowledge workbench: **Electron desk** (`apps/kwb-app`) + local FastAPI backend, with fail-closed gates, self-HITL checkpoints, and authz-first retrieval.

## What's in this repo

| Path | Role |
|------|------|
| `apps/kwb-app/` | **Primary desk** — Electron + Vite + React |
| `apps/kwb-desk/` | **Rejected / legacy** — Next.js marketing UI — do not demo |
| `backend/` | FastAPI gateway, sandbox, grants, audit, Monitor A |
| `solution/` | Freezes, architecture, demo/build plans |
| `KWB/` | Curated vendor *extracts* and integration notes (not full upstream clones) |
| `sih_research/` | Problem research, design inventories, PPT kits |
| `config/`, `desk/`, `eval/` | Config, legacy HTML desk assets, eval checklist + evidence |

## Not in this repo

Full third-party clones under `vendor/` (OpenHands, DeerFlow, MCP SDKs, etc.) are **local study only** and are gitignored. See `KWB/PULL_INDEX.md` and `KWB/INTEGRATION_LOG.md`.

## Quick start (local)

**One command (recommended for stage):**

```powershell
pwsh -File scripts/start_demo.ps1
```

Starts API `:8080` then Electron desk. Requires Ollama with `llama3.2:3b` already adopted (**no pull**).

**Two terminals (manual):**

```bash
# Terminal A — API (bind loopback only)
cd backend
pip install -r requirements.txt   # or root requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8080
# → http://127.0.0.1:8080/health

# Terminal B — Electron desk (primary)
cd apps/kwb-app
npm install
npm run electron:dev
# → window: Knowledge Work Bench
```

Prod-packaged renderer smoke (no Vite): `cd apps/kwb-app && npm run electron:prod`

Renderer-only debug: `cd apps/kwb-app && npm run dev` → `http://127.0.0.1:5173`

**Do not** use `apps/kwb-desk` for the jury demo (`npm run dev` there hard-fails).

### Eval / evidence (optional)

```bash
# API must be up
python backend/scripts/execute_walk.py          # G1–G10 → eval/evidence/
python backend/scripts/stage_dry_run_aj.py      # A→J + fail-closed
```

Stage cheat-sheet: `eval/STAGE_RUNBOOK.md` · Checklist: `eval/CHECKLIST.md`

## Docs to read first

1. `solution/README.md` — solution map and freeze index  
2. `solution/prototype/DEMO_TECH_STACK.md` — demo-narrowed stack  
3. `solution/prototype/CUSTOM_BUILD_PROGRESS.md` — build status  
4. `eval/STAGE_RUNBOOK.md` — one-page stage walk  
5. `KWB/README.md` — extract vs refuse policy  

## License / attribution

Upstream extracts under `KWB/` retain their original licenses (see `KWB/LICENSE-OpenHands-SDK` and per-folder `SOURCE.md`). Product code in `backend/` and `apps/` is team work for SIH26117.
