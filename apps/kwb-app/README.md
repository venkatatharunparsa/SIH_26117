# Knowledge Work Bench — desktop application

**Electron + Vite + React** agent workbench for SIH26117.  
Window title: **Knowledge Work Bench**. Talks to FastAPI at `127.0.0.1:8080`.

Research: [`../../solution/prototype/UI_CLAUDE_CODE_ADV.md`](../../solution/prototype/UI_CLAUDE_CODE_ADV.md)

`apps/kwb-desk/` (Syne hero Next.js) is **rejected / legacy** — do not demo as primary UI.

## Layout (Claude Code-like)

| Region | Role |
|---|---|
| Left | Sessions / tasks list |
| Center | Attach (text/doc/fixture) · action stream · composer |
| Right | **Monitor B on demand** — click titlebar **Monitor B** (closed by default) |

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

1. Attach: paste text · choose document (`.txt`/`.md`/`.png`/`.jpg`/`.pdf`) · or load fixture (FX-*)  
2. Orchestrator extract → **Confirm extract** (H1) — Enter to accept  
3. Cite review → PPTX DRAFT → self-check → export leave  

Binary attaches go through `/orch/turn` with `attach_b64` (pypdf text PDF · Tesseract image OCR · honest fixture stub if Tesseract missing). See `data/fixtures/README_attach_demo.md` for Windows Tesseract install.

Integrity: **DRAFT** badge · **not CERT** · no Approver · export leave only · Monitor on demand.

## Packaging

Double-click installers / `electron-builder` = **Later**. Dev path is `npm run electron:dev`.

## Env

```text
VITE_KWB_API=http://127.0.0.1:8080   # optional; default already correct
```
