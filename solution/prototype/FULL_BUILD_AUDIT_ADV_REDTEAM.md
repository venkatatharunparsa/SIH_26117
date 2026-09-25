# FULL BUILD AUDIT — adversarial + red-team + PRD exam

**Date:** 2026-09-20 (re-audited after gap closure)  
**Problem:** SIH26117 Knowledge Work Bench  
**Rule for this document:** **Honesty over comfort.** Claims require path/evidence. Gaps named explicitly.  
**Author mode:** Inventory → adversarial Q → red-team per layer → PRD exam → missed/undone/held → verdict  

---

## 0. Honesty preamble (read first)

| Claim often heard | Honest status |
|---|---|
| “Execute = 0.90, demo ready” | **True for API** (G1–G10 + A→J dry-run) **and** recorded **UI walk** (`eval/evidence/MANUAL_TEST_REPORT.md`). |
| “Checklist signed” | Signed by **prototype agent smoke**; DM human co-sign remains **optional / Held**. |
| “G1 multi-model” | **FALSE if claimed.** G1 is **floor** — one chat tag `llama3.2:3b`, two cards. |
| “Desktop app shipped” | **Dev Electron** primary (`apps/kwb-app`). Installer / `.exe` = **Held / Later**. |
| “PPT ready” | Execute gate **cleared**. Final jury PPTX = **Held** (prompts in `solution/ppt-paused/`). Format template ≠ filled deck. |
| “Custom components complete” | **Yes** — Claude Code composer. Orphan `AttachInput.tsx` **removed**. UI walk re-evidenced. |
| “OCR live” | **Held / day-1 fixture** — paste/fixture extract only (GATE B2). Not a demo blocker. |
| “MCP / skills production” | **Held** — MCP mock OFF; skills files without runner. |

If any prior chat sounded stronger than this table — **this table wins**.

---

## 1. Complete writeup — what has been done (do not miss)

### 1.1 Process / governance (docs + freezes)

| Done | Where |
|---|---|
| Org design → diagrams → demo-narrow → REAL → red-team process | `solution/prototype/*` |
| GATE_90 A1–A5 + B1–B7 design locks | `GATE_90_DISCUSS.md`, `DESIGN_BUILD_SOT.md`, `GATE_90_REDTEAM.md` |
| WP freezes / verifies (00, 01, 05, 13, 18, 20, …) | `solution/wp/WP-*/` |
| Integrity locks: assist→export leave; self-HITL; no in-app Approver; Admin=IT; Monitor A ≠ CERT; Ollama inference-only **no pull** | Freezes + health payload |
| DESK_IA screens + deny codes + state machine | `DESK_IA.md` |
| Custom demo plan + progress | `CUSTOM_DEMO_BUILD_PLAN.md`, `CUSTOM_BUILD_PROGRESS.md` |
| UI stack research (Next then rejected) | `UI_STACK_ADV.md` |
| Claude Code desk research | `UI_CLAUDE_CODE_ADV.md` |
| Desktop red-team | `DESK_DESKTOP_ADV_REDTEAM.md` |
| Workbench component verify | `WORKBENCH_COMPONENTS_VERIFY.md` |
| Repo extract / pull maps | `REPO_EXTRACT_VERIFY.md`, `REPO_PULL_MAP.md`, `KWB/PULL_INDEX.md` |
| Tech stack / architecture diagrams | `DEMO_TECH_STACK.md`, org/demo diagram docs |
| GitHub clean push (vendor excluded) | `https://github.com/venkatatharunparsa/SIH_26117` |
| Manual UI software test | `eval/evidence/MANUAL_TEST_REPORT.md` |

### 1.2 Backend (FastAPI REAL)

**Path:** `backend/app/` · version in health **0.5.0** · bind `127.0.0.1:8080`

| Module | Role |
|---|---|
| `main.py` | Routes: health, audit, cards, task/*, artifacts, leave-pack, export-check, monitor-a, sandbox, gateway, mcp stub · **revoke-on-export** after leave |
| `grants.py` | Grant lifecycle / tool ACL |
| `cards.py` | Task→card→model routes |
| `artefacts.py` | Draft meta, H2/H7/H9, stale, fingerprint |
| `word_draft.py` | Word DRAFT generation |
| `retrieve.py` | Cite-or-abstain under grant |
| `secrets.py` | G9 secret scan |
| `sandbox.py` | calc/python + H9 observation fields |
| `gateway.py` | Local model allowlist (deny gpt-4o) |
| `monitor_a.py` | Evidence pack start/stop (**not CERT**) |
| `audit.py` | Event log / verify |
| `mcp_mock.py` | Stub; OFF by default |
| `config.py` | Config / models |

**Scripts (evidence):**  
`execute_walk.py`, `stage_dry_run_aj.py`, `hitl_gates_smoke.py`, `test_m1_m3_leavepack.py`, `test_m4_m7_desk_maturity.py`, `validate_endpoints.py`, `e2e_one_model.py`

**Eval:** `eval/evidence/G1…G10*.json`, `SUMMARY.json` (all G true, floor, desk=`apps/kwb-app`), `STAGE_DRY_RUN_AJ.json`, `MANUAL_TEST_REPORT.md`, `CHECKLIST.md` SIGNED, `STAGE_RUNBOOK.md` (single-laptop locked)

### 1.3 Custom Must milestones (M1–M10)

| M | Claim | Evidence type |
|---|---|---|
| M1–M3 | Artefact download + leave-pack | API + desk download buttons |
| M4–M7 | MonB audit, injects, server H7, guided path | API + Electron wire |
| M8 | Evidence pack | `eval/evidence/*` |
| M9 | Signed checklist | `eval/CHECKLIST.md` |
| M10 | Stage runbook | `eval/STAGE_RUNBOOK.md` |

### 1.4 Desk UI evolution (honest history)

| Generation | Path | Outcome |
|---|---|---|
| 1 | `desk/index.html` static | API console — **legacy** |
| 2 | `apps/kwb-desk` Next Syne hero | User rejected — **LEGACY.md** + **npm hard-fail** |
| 3 | `apps/kwb-app` Electron + chip soup | Worked; user: clumsy / not Claude Code |
| 4 | **Current** Claude Code composer | Stream + one prompt + Start/next + ⌁ attach + ··· more + Monitor on demand |

**Current components:**  
`App.tsx`, `SessionList`, `Transcript`, `ToolBlock`, `Composer` (CC style), `MonitorPanel` (toggle), `api.ts`, `constants.ts` (fixtures), `electron/main.cjs` + `preload.cjs`, CSP fix for Vite, `will-navigate` harden.

**Orphan:** `AttachInput.tsx` — **deleted** (folded into Composer).

### 1.5 KWB extracts (not a web app)

Curated slices under `KWB/` (`required/`, `from_*_web`, etc.) → patterns into backend per `INTEGRATION_LOG.md`.  
Full clones stay in local `vendor/` (**gitignored**, not pushed).

### 1.6 Data / config

- `data/fixtures/` (extract, SOP, calc, templates)  
- `data/skills/` placeholder (runner = Held)  
- `config/models.yaml`  
- `.gitignore` excludes vendor, node_modules, .env, runtime DBs  

### 1.7 What was explicitly **refused** (and kept refused)

DeerFlow / OpenHands Canvas fork · Open WebUI skin · LiteLLM cloud · Ollama pull · in-app Approver · CERT claims · rewriting FastAPI into Electron  

---

## 2. Adversarial questioning (interrogation of our own claims)

### Q1. Is the product a desktop application?

**A:** **Yes for demo.** Electron `BrowserWindow` titled Knowledge Work Bench loads Vite in **dev** (`npm run electron:dev`).  
**Held:** double-click installer / `.exe` packaging.

### Q2. Did we finish custom workbench components?

**A:** **Yes** (sessions, stream, composer, monitor-on-demand, API client, Electron shell). Coding next-step is now Sandbox → H9 → Draft → H2 → Export (parity with inspection guidance).

### Q3. Is execute really ≥0.90?

**A:** **Yes** — API (`SUMMARY.json`) + UI A→J + G9 (`MANUAL_TEST_REPORT.md`).  
**Overclaim risk:** Saying “installer shipped” or “G1 full multi-model” = **lie**.

### Q4. Is HITL real or theatre?

**A:** **Real on server.** H7 SoT; H2 stale; G10 sandbox-red; secrets on export; **revoke-on-export** closes shelf after leave.

### Q5. Can the UI still go blank?

**A:** CSP blank **was hit** and **fixed** (`unsafe-eval` for Electron+Vite). Prod `loadFile(dist)` path exists in `electron/main.cjs`; `vite build` is the smoke for that path.

### Q6. Does evidence prove the desk?

**A:** **Yes.** `SUMMARY.json` / health cite **`apps/kwb-app`**. Manual UI report covers composer walk. Legacy `/desk/` exists but is not primary.

### Q7. Is PPT done?

**A:** **Held.** Gate allows start; prompts exist; filled SIH PPTX not delivered this pass.

### Q8. Did GitHub push include only our work?

**A:** **Intended yes** — vendor ignored. KWB extracts + apps + backend + solution pushed.

### Q9. Is Claude Code UI “done”?

**A:** **Yes for demo.** Button soup removed; manual soak recorded; G9 inject string fixed + retested.

### Q10. What would a hostile jury ask that hurts us?

1. “Where is the `.exe`?” → we run `electron:dev` (Held packaging).  
2. “Show two models” → G1 **floor** only.  
3. “Is Monitor A CERT-In?” → must say **no**.  
4. “Who approved?” → **no in-app Approver**; paper outside.  
5. “Live OCR?” → fixture only (Held).  
6. “Sign the checklist yourself” → agent-signed; DM optional.

---

## 3. Red-team each built layer

### RT-L1 — Backend spine

| Attack | Result |
|---|---|
| Skip H2 / stale export | Mitigated (smoke PASS) |
| Secret in export | Mitigated G9 |
| Public model | Mitigated G8 |
| Revoke then tool | Mitigated G7 |
| Sandbox-red export | Mitigated G10 |
| Fake H7 client-only | Mitigated server SoT |
| Grant hang after export | **Mitigated** — revoke-on-export |
| Ollama pull mid-demo | Policy + config; **operational** risk if someone pulls anyway |
| MCP enabled by accident | Default OFF — verify env on stage box |

**Loose ends:** embed model not adopted (`nomic-embed-text` not_adopted) — intentional floor.

### RT-L2 — Electron desk

| Attack | Result |
|---|---|
| XSS→RCE via nodeIntegration | Mitigated (off + isolation + sandbox) |
| Hostile navigation | `will-navigate` allowlist — **mitigated** |
| CSP blank window | **Hit in real use** → fixed; watch regressions |
| Demo wrong app (`kwb-desk`) | **Mitigated** — `npm run dev` hard-fails + REJECTED page banner |
| Monitor always-on clutter | Fixed (on demand) |
| Button soup / clumsy | Fixed (CC composer) — soak **recorded** |
| Attach binary .docx | **Denied by design** (text only) — tell jury |
| Coding walk autopilot | **Fixed** — guided Sandbox → H9 → Draft → H2 → Export |
| G9 inject false OK | **Fixed** — inject uses `api_key=sk-…` |

### RT-L3 — Eval / evidence

| Attack | Result |
|---|---|
| Unsigned checklist | Mitigated agent sign; DM co-sign **optional Held** |
| Claim G1 full | Would be **false** — floor only |
| Evidence ≠ desk | **Closed** — `SUMMARY` + health + `MANUAL_TEST_REPORT` cite `apps/kwb-app` |
| Stale DESIGN_BUILD_SOT B5 | **Closed** — B5 = **SIGNED** |

### RT-L4 — KWB extracts

| Attack | Result |
|---|---|
| Shipping vendor clones | Mitigated gitignore |
| Runtime import of OH | Refused — patterns only |
| Claiming “we built OpenHands” | Would be **false** — study extracts |

### RT-L5 — Process / PPT

| Attack | Result |
|---|---|
| PPT before execute | Gate held historically; execute **cleared** — slides still **Held** |
| CERT language in slides | Scrub required when deck is built |

---

## 4. PRD / requirement exam (DESK_IA + GATE + product locks)

### 4.1 Day-1 / demo Must (all closed)

| Requirement (PRD-like) | Built? | Completeness |
|---|---|---|
| Offline-first workbench | **Yes** | Local API + Ollama (both required on stage laptop) |
| Assist → export leave | **Yes** | API + UI + revoke-on-export |
| Self-HITL H1/H2/H7/H9 | **Yes** | API + UI next/slash/more |
| No in-app Approver | **Yes** | Absent |
| DRAFT ≠ CERT · MonA ≠ CERT | **Yes** | Labels + evidence |
| Cite-or-abstain | **Yes** | retrieve |
| Fail-closed revoke/secret/model/sandbox | **Yes** | G7–G10 + UI G9 |
| A→J inspection walk | **Yes** | API + UI (`MANUAL_TEST_REPORT.md`) |
| Desktop application | **Yes (dev Electron)** | Installer separately Held |
| Claude Code–like desk | **Yes** | Composer + soak evidence |
| Fixture / files input | **Yes** | Attach popover + fixtures |
| Evidence desk honesty | **Yes** | `SUMMARY` / health → `apps/kwb-app` |
| Orphan AttachInput | **Yes (removed)** | Folded into Composer |
| Rejected Next desk footgun | **Yes (hard-fail)** | `refuse-legacy.cjs` + banner |

### 4.2 Held / out of day-1 (not open defects)

| Item | Status | Note |
|---|---|---|
| Live plant OCR | **Held** | Fixture extract is day-1 SoT (GATE B2) |
| SSO / Admin console | **Held** | Admin=IT outside app |
| Full MCP host | **Held** | Mock OFF |
| Skill runner | **Held** | Placeholder files only |
| Excel/PPT artefacts | **Held** | Word DRAFT is day-1 |
| Jury filled PPTX | **Held** | Prompts ready; deck not this pass |
| G1 full ≥2 model_ids | **Held** | Floor locked for single-laptop; no pull |
| DM human checklist co-sign | **Held** | Optional team process |
| electron-builder installer | **Held** | Later unless jury demands `.exe` |

---

## 5. Missed · undone · held (master list)

### 5.1 Critical / high — **cleared this re-audit**

1. ~~Human Electron/Vite A→J + fail-closed~~ → `MANUAL_TEST_REPORT.md`  
2. ~~Re-evidence after CC composer~~ → same + G9 inject fix  
3. ~~SUMMARY desk URL honesty~~ → `apps/kwb-app`  
4. ~~Orphan AttachInput~~ → deleted  
5. ~~DESIGN_BUILD_SOT B5 TEMPLATE drift~~ → SIGNED  
6. ~~kwb-desk footgun~~ → npm refuse + banner  
7. ~~Coding next-step~~ → guided path  
8. ~~Revoke-on-export~~ → `main.py` export  

**Still operator-owned before stage:** confirm Ollama tag `llama3.2:3b` present (**no pull**).

### 5.2 Medium — residual polish (**closed**)

9. ~~Prod Electron path~~ → `npm run electron:prod`.  
10. ~~Audit hash UI~~ → Monitor **Verify chain**.  
11. ~~One-command start~~ → `scripts/start_demo.ps1`.  
12. ~~G8/sandbox-red/revoke UI~~ → `MANUAL_TEST_REPORT.md`.  

### 5.3 Held / Later (known, not forgotten)

11. electron-builder **installer**  
12. Live OCR engine  
13. SSO / Admin / Postgres / hybrid RAG  
14. Real MCP host + skill runner  
15. G1 **full** second offline model tag  
16. Final **PPTX** from scrubbed prompts  
17. DM co-sign if team requires  

### 5.4 Known breakage points (can break demo)

| Breaker | Why |
|---|---|
| API down / wrong port | Desk shows offline; all tools fail |
| Ollama down / wrong tag | Draft/retrieve degrade or fail |
| CSP regression | Blank Electron window (already happened) |
| Bypass `legacy:force-dev` on purpose | Still shows REJECTED — do not demo |
| Claim CERT / Approver / dual-model | Integrity fail with judges |
| Binary Office attach expectation | UI refuses — must use text extract |

---

## 6. What we **actually** have (one paragraph)

We have a **local FastAPI knowledge workbench** with real grants, HITL gates, Word DRAFT, export leave (with **revoke-on-export**), sandbox/H9, Monitor A evidence packs, and fail-closed denies — proven by **automated API walks**, an agent-signed G1–G10 checklist at G1 **floor**, and a **recorded UI A→J + G9** walk on the Claude Code composer desk. The **primary UI** is **Electron+Vite React** (`apps/kwb-app`); rejected Next desk **hard-fails** on `npm run dev`. Vendor code was studied via **KWB extracts**, not shipped as clones. Still **Held** (not day-1 defects): installer, filled jury PPT, live OCR, MCP/skills runners, G1 full multi-model, DM co-sign. That is the truthful inventory.

---

## 7. Verdict scores (honest, post-audit)

| Axis | Score | Note |
|---|---|---|
| Architecture / design freezes | **0.90** | Held |
| Backend REAL + eval scripts | **0.92** | Strong + revoke-on-export |
| Desktop app claim | **0.86** | Dev Electron proven; no package |
| UI Claude Code claim | **0.88** | Redesigned + manual soak |
| Execute “stage ready” | **0.90** | API + UI walk; Held items out of day-1 |
| PPT | **0.20–0.35** | Held — not built |
| Overall product honesty | **Pass if we speak this document** · **Fail if we overclaim** |

---

## 8. Recommended next actions (ordered)

1. Operator: confirm Ollama `llama3.2:3b` on jury laptop (**no pull**).  
2. Prefer `pwsh -File scripts/start_demo.ps1` on stage.  
3. Start PPT **only** with scrubbed integrity language when team asks.  
4. Packaging only if jury demands `.exe`.  

---

**End of audit.** No false CERT. No claim of installer or G1 full. Day-1 “No” gaps from prior audit **closed or reclassified as Held**.
