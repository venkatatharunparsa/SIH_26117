# SIH_26117

**Knowledge Work Bench (KWB)** — Smart India Hackathon 2026 problem statement SIH26117 (MRPL · Software · Smart Automation).

Offline-first knowledge workbench for plant/office knowledge work: an Electron desk UI plus a local FastAPI backend, with fail-closed gates, HITL checkpoints, and authz-first retrieval patterns.

## What's in this repo

| Path | Role |
|------|------|
| `apps/kwb-app/` | Electron + Vite desk shell |
| `apps/kwb-desk/` | Next.js desk UI |
| `backend/` | FastAPI gateway, sandbox, and app services |
| `solution/` | Freezes, architecture, demo/build plans |
| `KWB/` | Curated vendor *extracts* and integration notes (not full upstream clones) |
| `sih_research/` | Problem research, design inventories, PPT kits |
| `config/`, `desk/`, `eval/` | Config, desk assets, eval checklist |

## Not in this repo

Full third-party clones under `vendor/` (OpenHands, DeerFlow, MCP SDKs, etc.) are **local study only** and are gitignored. See `KWB/PULL_INDEX.md` and `KWB/INTEGRATION_LOG.md`.

## Quick start (local)

```bash
# Backend
cd backend
pip install -r requirements.txt   # or root requirements.txt
# run your FastAPI entrypoint (see backend/app)

# Desk UI
cd apps/kwb-desk
cp .env.example .env.local        # set NEXT_PUBLIC_KWB_API
npm install
npm run dev

# Electron shell (optional)
cd apps/kwb-app
npm install
npm run dev
```

## Docs to read first

1. `solution/README.md` — solution map and freeze index  
2. `solution/prototype/DEMO_TECH_STACK.md` — demo-narrowed stack  
3. `solution/prototype/CUSTOM_BUILD_PROGRESS.md` — build status  
4. `KWB/README.md` — extract vs refuse policy  

## License / attribution

Upstream extracts under `KWB/` retain their original licenses (see `KWB/LICENSE-OpenHands-SDK` and per-folder `SOURCE.md`). Product code in `backend/` and `apps/` is team work for SIH26117.
