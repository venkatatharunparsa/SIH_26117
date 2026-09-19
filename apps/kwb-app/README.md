# Knowledge Work Bench — desktop application

**Electron + Vite + React** agent workbench for SIH26117.  
Window title: **Knowledge Work Bench**. Talks to FastAPI at `127.0.0.1:8080`.

Research: [`../../solution/prototype/UI_CLAUDE_CODE_ADV.md`](../../solution/prototype/UI_CLAUDE_CODE_ADV.md)

`apps/kwb-desk/` (Syne hero Next.js) is **rejected / legacy** — do not demo as primary UI.

## Layout (Claude Code-like)

| Region | Role |
|---|---|
| Left | Sessions / tasks list |
| Center | Action stream (tool blocks) + composer |
| Right | Monitor B — grant, card, model, denies, audit, leave downloads |

## Prerequisites

- Node 20+ / npm
- FastAPI running:

```bash
cd ../../backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8080
```

## Launch desktop app

```bash
cd apps/kwb-app
npm install
npm run electron:dev
```

This starts Vite on `127.0.0.1:5173` and opens an Electron window titled **Knowledge Work Bench**.

### Renderer-only (no Electron chrome)

```bash
npm run dev
# → http://127.0.0.1:5173
```

## Inspection path (against API)

In the composer action row:

1. `task/start` → grant + card/model in Monitor B  
2. `load FX-EXT-01` → fixture extract  
3. `h1-confirm` → same-user extract ack  
4. `retrieve` → cite-or-abstain  
5. `h7-ack` → cite review  
6. `inspect-draft` → Word **DRAFT** (badge in title bar)  
7. `h2-ack` → self-check  
8. `export leave` → soft copy; download DRAFT / leave pack from Monitor B  

Integrity: **DRAFT** badge · **not CERT** · no Approver · export leave only.

## Packaging

Double-click installers / `electron-builder` = **Later**. Dev path is `npm run electron:dev`.

## Env

```text
VITE_KWB_API=http://127.0.0.1:8080   # optional; default already correct
```
