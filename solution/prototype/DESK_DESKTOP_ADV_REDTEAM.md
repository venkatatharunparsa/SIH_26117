# Desktop desk — adversarial research + red-team verify

**Date:** 2026-09-20  
**Target:** Custom KWB **desktop** application (`apps/kwb-app/` Electron + Vite React)  
**Against:** DESK_IA · GATE_90 · WP-05 export leave · UI_CLAUDE_CODE_ADV · CUSTOM_DEMO Must · Electron security checklist  
**Method:** Requirements map → attack table → code/evidence verify → built / need-to-build / verdict  
**PPT:** Out of scope for this pass (execute gate already 0.90)

---

## 0. Adversarial research (what “good” looks like)

### Product / UX (Claude Code–class agent desks)

| Pattern | Requirement for KWB | Source |
|---|---|---|
| Session stream primary | Center = tool transcript, not marketing hero / wizard splash | UI_CLAUDE_CODE_ADV · user reject of `kwb-desk` |
| Observable tools | Each API call = named tool block + result/deny | Claude Code agent view pattern |
| Composer + status panel | Bottom actions; right Monitor B (grant/card/model/denies/audit) | DESK_IA screens 7–8 + Claude Code |
| Desktop packaging signal | Native window, not “open Chrome :3000” | User: application not web |
| Integrity chrome | DRAFT · not CERT · no Approver · export leave | GATE_90 A4/A5 · WP-05 |

### Electron security (2025 checklist — research)

Sources: Electron security tutorial; Doyensec Electronegativity checklist.

| Control | Expect |
|---|---|
| `nodeIntegration: false` | Mandatory |
| `contextIsolation: true` | Mandatory with preload |
| `sandbox: true` | Strongly recommended |
| Minimal `contextBridge` | No raw `ipcRenderer` / Node leak |
| Navigation / `window.open` hardened | Deny external nav into shell; open via `shell` |
| No remote untrusted URL as primary content | Prefer packaged `loadFile` in prod |

---

## 1. Requirements checklist — built vs need

### A. Packaging / “application not web”

| Req | Status | Evidence |
|---|---|---|
| Primary UI = Electron desktop | **BUILT** | `apps/kwb-app/` · `electron/main.cjs` title **Knowledge Work Bench** |
| Claude Code layout (sessions / stream / Monitor B) | **BUILT** | `SessionList` · `Transcript`+`ToolBlock` · `Composer` · `MonitorPanel` |
| FastAPI stays on `:8080` | **BUILT** | `api.ts` + preload `apiBase` |
| Reject web marketing desk as primary | **BUILT (policy)** | `kwb-desk` = REJECTED/legacy in DEMO_TECH_STACK / progress |
| Installer / `.exe` (double-click ship) | **NEED (Later)** | No electron-builder; `electron:dev` only |
| Operator timing walk on Electron recorded | **NEED (residual)** | CHECKLIST residual #2 · STAGE_RUNBOOK exists |

### B. DESK_IA wires (A→J + HITL)

| Req | Status | Evidence |
|---|---|---|
| Start / task type | **BUILT** | `task/start` · inspection\|coding |
| Files / fixture | **PARTIAL** | Hardcoded FX-EXT-01 load only — no fixture **picker** / upload |
| H1 confirm | **BUILT** | `/task/h1-confirm` |
| Retrieve + cites | **BUILT** | `/task/retrieve` |
| H7 cite review | **BUILT (API SoT)** | `/task/h7-ack`; server ignores client theatre (`main.py`) |
| Inspect DRAFT + version | **BUILT** | `/task/inspect-draft` · Monitor B version |
| H2 self-HITL | **BUILT** | `/task/h2-ack` |
| Export leave + downloads | **BUILT** | `/task/export` · DRAFT + leave-pack buttons |
| Sandbox + H9 | **BUILT** | calc / red / `h9-ack` |
| Fail-closed injects G7/G8/G9 | **BUILT** | revoke · bad model · secret export-check |
| Monitor A start/stop (≠ CERT) | **BUILT** | buttons + honesty badges |
| Monitor B live audit | **BUILT** | poll `/audit/recent` |
| Stale path (draft-edit → h2_stale) | **NEED (desk)** | API has edit; **no `draft-edit` action in Composer** |
| Guided lock / step machine | **DEFER OK** | Claude stream replaces wizard; Must satisfied by action chips + API denials |

### C. Integrity language (non-negotiable)

| Req | Status | Evidence |
|---|---|---|
| DRAFT badge | **BUILT** | titlebar |
| not CERT | **BUILT** | titlebar + Monitor B + rail |
| No Approver picker / queue | **BUILT** | absent from UI |
| Export leave (not forward-accept) | **BUILT** | copy + API |
| G1 floor honesty | **BUILT (eval)** | CHECKLIST signed floor — desk does not claim dual models |
| Monitor A ≠ CERT | **BUILT** | labels |

### D. Custom Must (M1–M10) — backend + desk maturity

| M | Status | Note |
|---|---|---|
| M1–M3 leave/download | **BUILT** | API + Monitor B downloads |
| M4–M7 audit/injects/H7/A→J | **BUILT** | API + Electron wire |
| M8–M10 evidence/checklist/runbook | **BUILT** | `eval/evidence/` · SIGNED · `STAGE_RUNBOOK.md` |

### E. Electron hardening

| Control | Status | Evidence |
|---|---|---|
| `nodeIntegration: false` | **PASS** | `main.cjs` |
| `contextIsolation: true` | **PASS** | `main.cjs` |
| `sandbox: true` | **PASS** | `main.cjs` |
| Minimal preload bridge | **PASS** | `platform` · `isElectron` · `apiBase` only |
| `setWindowOpenHandler` → external | **PASS** | deny + `shell.openExternal` |
| `will-navigate` / deny remote hijack | **GAP** | not registered — Medium |
| Prod `loadFile(dist)` path | **BUILT (code)** | present; packaging Later |
| Download via `window.open` | **WEAK** | may feel webby; prefer `shell.openExternal` / session download — Low |

---

## 2. Red-team attack table (what we built)

| ID | Attack | Against our build | Severity | Verdict |
|---|---|---|---|---|
| **RT-D1** | “Still a website” | Electron window + title + `kwbDesktop.isElectron`; no Syne hero | **Critical (product)** | **MITIGATED** for demo framing. Residual: no installer → jury may still ask “where is the .exe?” |
| **RT-D2** | Demo wrong app (`kwb-desk` :3000) | `scripts/refuse-legacy.cjs` hard-fail + REJECTED page + LEGACY.md | **High** | **FIXED** |
| **RT-D3** | Leave-with empty hands | Monitor B download DRAFT + leave pack | **Critical** | **MITIGATED** |
| **RT-D4** | CERT / Approver slip in UI | Badges + copy audited — no Approver control | **Critical** | **MITIGATED** in desk code |
| **RT-D5** | H7 client theatre | `h7Acked` only on success; **server SoT** blocks draft | **Medium** | **FIXED** |
| **RT-D6** | Stale H2 invisible on stage | Composer `Edit draft (stale H2)` → `/task/draft-edit` | **High (demo)** | **FIXED** |
| **RT-D7** | Fail-closed invisible | G8/G9/revoke/sandbox-red retested in UI | **High** | **FIXED** |
| **RT-D8** | Monitor B dead | `/audit/recent` polled + **Verify chain** | **High** | **FIXED** |
| **RT-D9** | Eval unsigned / no evidence | M8–M10 SIGNED 2026-09-20 | **Critical** | **MITIGATED** |
| **RT-D10** | G1 dual-model lie | Checklist floor only | **High** | **MITIGATED** (process) — keep PPT honest |
| **RT-D11** | Electron XSS → RCE | Isolation + sandbox + `will-navigate` | **High (security)** | **FIXED** |
| **RT-D12** | Dev loads `http://127.0.0.1:5173` | `electron:dev` + `electron:prod` (dist) | **Medium** | **OK** |
| **RT-D13** | Fixture screen fake | Attach popover fixture picker | **Medium** | **FIXED** |
| **RT-D14** | Button soup ≠ story | Claude Code composer + next-step | **Medium** | **FIXED** |
| **RT-D15** | Operator never rehearsed A→J | `MANUAL_TEST_REPORT.md` | **Medium** | **FIXED** |

---

## 3. Verify: did we build according to requirements?

### Verdict (honest)

| Axis | Score | Call |
|---|---|---|
| Desktop application (not web product) | **0.88** | **YES** for SIH demo architecture. Not **1.0** until packaging or clear “desktop window” jury script. |
| DESK_IA + HITL integrity | **0.90** | **YES** on API + primary wires. Gap: **stale edit UI**. |
| Claude Code desk IA | **0.85** | **YES** layout/stream. Polish (S1–S5) optional. |
| Custom Must M1–M10 | **0.90** | **YES** — evidence signed. |
| Electron security baseline | **0.82** | **PASS-WITH-FIXES** (`will-navigate`). |
| Overall “built to requirements” | **0.88** | **GO for desk demo** · **fix High gaps before jury if time** |

### Built (keep)

1. Electron + Vite React workbench `apps/kwb-app/`  
2. Session / stream / composer / Monitor B custom components  
3. Full inspection + coding tool path wired to FastAPI  
4. Integrity chrome (DRAFT / not CERT / export leave / no Approver)  
5. Leave downloads · audit poll · fail-closed injects  
6. Eval evidence + signed checklist + stage runbook  
7. Sensible Electron defaults (isolation, sandbox, minimal preload)

### Need to build / fix (priority)

| Pri | Item | Why |
|---|---|---|
| **P0** | Add **draft-edit** (or clear findings → re-draft) in Composer + clear `h2Ok` | DESK_IA stale walk — jury “edit then export” |
| **P0** | Fix H7 client branch (only set `h7Acked` on success) | UI honesty / RT-D5 |
| **P1** | `will-navigate` deny off-allowlist in `main.cjs` | Electron red-team residual |
| **P1** | One timed human Electron A→J per `STAGE_RUNBOOK.md` | Close CHECKLIST residual |
| **P2** | Fixture picker (list FX-*) | DESK_IA Files honesty |
| **P2** | Banner or quarantine `apps/kwb-desk` | Kill wrong-demo footgun |
| **P3** | electron-builder installer | True shippable desktop |
| **Later** | S1–S5 polish · auto-revoke toast · DRAFT excerpt preview | Should-only |

### Explicitly not required (do not thrash)

- Rewrite FastAPI into Electron  
- Bring back Next hero desk as primary  
- DeerFlow / OpenHands Canvas fork  
- Full OCR engine / SSO / Admin console  
- Claiming CERT or in-app Approver  
- G1 “full” without offline second model tag  

---

## 4. Bottom line (updated 2026-09-20)

**Custom desktop desk meets Must requirements.** UX: attach text/doc + Monitor B **on demand**.

### Fix log (this session)

| Item | Result |
|---|---|
| P0 draft-edit | **FIXED** — Composer `draft-edit (stale)` → `/task/draft-edit` |
| P0 H7 honesty | **FIXED** — `h7Acked` only on success |
| P1 will-navigate | **FIXED** — allowlist renderer + API + file; else external |
| P2 fixture picker | **FIXED** — AttachInput fixture mode (FX-EXT-01 / SCAN / SOP) |
| P2 kwb-desk footgun | **FIXED** — npm refuse + REJECTED banner + LEGACY.md |
| UX attach | **FIXED** — paste text / choose document / fixture |
| UX Monitor always-on | **FIXED** — closed by default; titlebar **Monitor B** toggles |
| P1 human timing walk | **FIXED** — `eval/evidence/MANUAL_TEST_REPORT.md` |
| G8/G9/revoke UI retest | **FIXED** — MANUAL_TEST_REPORT fail-closed section |
| One-command start | **FIXED** — `scripts/start_demo.ps1` |
| Audit verify UI | **FIXED** — Monitor **Verify chain** |
| P3 installer | **Later** |

Component verify: `WORKBENCH_COMPONENTS_VERIFY.md` — **all Must custom workbench components DONE**.
