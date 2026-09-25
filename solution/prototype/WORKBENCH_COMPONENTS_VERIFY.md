# Workbench custom components — verify

**Date:** 2026-09-20  
**App:** `apps/kwb-app/` (Electron desktop)  
**Against:** DESK_IA · UI_CLAUDE_CODE_ADV · DESK_DESKTOP_ADV_REDTEAM

## Component inventory

| Component | Path | Role | Status |
|---|---|---|---|
| **App shell** | `src/App.tsx` | Sessions state · tool runner · titlebar · Monitor toggle | **DONE** |
| **SessionList** | `src/components/SessionList.tsx` | Left rail · new session | **DONE** |
| **Transcript** | `src/components/Transcript.tsx` | Center stream | **DONE** |
| **ToolBlock** | `src/components/ToolBlock.tsx` | Tool call cards | **DONE** |
| **AttachInput** | *(removed)* | Folded into Composer attach popover 2026-09-20 | **DONE** |
| **Composer** | `src/components/Composer.tsx` | Claude Code prompt + next step + attach/more | **DONE** |
| **MonitorPanel** | `src/components/MonitorPanel.tsx` | Monitor B on demand (not always on) | **DONE** (toggle) |
| **api client** | `src/lib/api.ts` | FastAPI 8080 | **DONE** |
| **constants / fixtures** | `src/lib/constants.ts` | FX catalogue | **DONE** |
| **Electron main** | `electron/main.cjs` | Window · isolation · will-navigate | **DONE** |
| **Preload** | `electron/preload.cjs` | Minimal bridge | **DONE** |
| **Styles** | `src/styles/app.css` | Desktop dense chrome | **DONE** |

## DESK_IA screen coverage

| Screen | Component coverage | Status |
|---|---|---|
| 1 Intent | Session + task type + start | **DONE** |
| 2 Files | AttachInput (text / file / fixture) | **DONE** |
| 3 Extract + H1 | Attach + h1-confirm | **DONE** |
| 4 Knowledge | retrieve + h7 | **DONE** |
| 5 DRAFT | inspect-draft | **DONE** |
| 6 Gates | h2 · h9 · draft-edit stale | **DONE** |
| 7 Export leave | export + downloads (via Monitor) | **DONE** |
| 8 Monitor B thin | Click **Monitor B** in titlebar | **DONE** (on demand) |

## Not custom workbench UI (out of day-1)

| Item | Status |
|---|---|
| Approver queue | **REFUSED** (by design) |
| CERT badge | **REFUSED** |
| Next.js `kwb-desk` | **LEGACY** — see `apps/kwb-desk/LEGACY.md` |
| Electron installer (.exe) | **Later** |
| Live OCR / SSO / Admin | **Later** |

## Verdict

**All Must custom workbench components for the desktop desk are complete** after 2026-09-20 attach + Monitor-on-demand + red-team P0/P1 fixes.

Residual non-component: human operator timing walk (`eval/STAGE_RUNBOOK.md`); packaging Later.
