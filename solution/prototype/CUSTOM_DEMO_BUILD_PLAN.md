# Custom demo build plan — SIH26117 Knowledge Work Bench

**Date:** 2026-09-19  
**Method:** Adversarial research + red-team against DESK_IA · APPLICATION_FLOW A→J · backend v0.5 · `desk/index.html` · eval · KWB integrate (patterns only)  
**Rule:** Custom = **our** `desk/` + thin `backend/` gaps + signed goldens. **Not** more vendor pulls.  
**PPT:** Still blocked until execute ≥0.90.

---

## Verdict (ruthless)

| Question | Answer |
|---|---|
| Is current `desk/index.html` enough for SIH jury demo **as-is**? | **NO.** It is a wired **API console**, not a leave-with workbench. Jury cannot download Word/audit; Monitor B does not show live denies; fail-closed injects (G8/G9) missing; eval unsigned; no evidence pack. |
| Do we need richer custom **React** UI? | **Not for Must MVP.** Thicken **this HTML desk** + 2–3 API endpoints + run/sign goldens. React canvas = **Should/Later** polish if time after execute ≥0.90. |
| What kills demo if we skip custom? | See attack table §1. Highest: no leave-with artefacts · unsigned eval · H7 theatre · CERT overclaim · PPT early. |
| API gaps remaining? | **Thin:** artefact download · leave pack (docx+audit) · fixture list (optional) · server H7 ack · optional auto-revoke on export. Spine (start→H1→retrieve→draft→H2→export→sandbox/H9→Monitor A) **already exists**. |

**Bottom line:** Stop pulling vendors. Build **custom desk maturity + leave-with + goldens** only.

---

## 1. Adversarial attack table

What kills the jury demo if we skip custom work (or fake maturity):

| ID | Attack | How it lands | Severity | Mitigate with **our** custom |
|---|---|---|---|---|
| A1 | **Leave-with empty hands** | Export returns JSON path; desk has **no download** of `.docx` / audit. Jury asks “what do I take?” — shrug. | **Critical** | `GET /artifacts/{name}` + desk “Download DRAFT / audit pack” |
| A2 | **Eval unsigned / no evidence** | `eval/CHECKLIST.md` TEMPLATE; `eval/evidence/` **absent**. Cannot claim G1–G10. | **Critical** | Run `execute_walk.py` → fill evidence → DM co-sign |
| A3 | **H7 cite theatre** | Desk sets `h7_acked` in JS only; API trusts body flag. Skip-click or curl without review. | **High** | Persist H7 on grant/artefact server-side; desk cannot draft without prior `/task/h7-ack` |
| A4 | **Button-soup ≠ A→J story** | Single panel; “files” step is fake; no fail-closed overlays. Looks like Postman. | **High** | Guided step lock + stale/sandbox-red/secret banners per DESK_IA |
| A5 | **Monitor B ≠ denies** | Local state only; never calls `/audit/recent`. Jury cannot see revoke/deny trail. | **High** | Poll `/audit/recent`; show last deny codes |
| A6 | **Fail-closed invisible** | Revoke exists; **no G8/G9 buttons**; secret/bad-model not demoable from desk. | **High** | Inject buttons → `export-check` / gateway deny; surface `error` codes |
| A7 | **Monitor A = CERT slip** | Verbal WAN=0 / CERT-In without honesty. | **Critical (language)** | Keep desk honesty line; never claim CERT (already labelled — guard PPT too) |
| A8 | **G1 dual-model lie** | Claim ≥2 models when floor single-tag. | **High** | Desk + checklist label **G1 floor** when `model_id` shared |
| A9 | **React rewrite thrash** | Rebuild Vite/React before goldens → miss execute ≥0.90 / PPT gate. | **High (process)** | **Refuse** React until Must HTML MVP + signed eval |
| A10 | **More vendor / MCP / skills** | Integrate FastMCP host or skill runner mid-demo. | **Medium** | Explicitly deferred (INTEGRATION_LOG) — do not touch |
| A11 | **PPT before execute ≥0.90** | Slides outrun runnable desk. | **Critical (process)** | GATE_90 still binds |
| A12 | **Grant hangs after export** | Flow I4 revoke-at-end not wired on export. | **Medium** | Optional `revoke_on_export` or desk revoke after leave |
| A13 | **No Word open path** | Generate DRAFT but cannot show banner/DRAFT badge live. | **Medium** | Download + open locally; optional HTML excerpt of findings |

---

## 2. Already done vs custom still required (honest)

### Already done (do **not** rebuild)

| Layer | Status | Evidence |
|---|---|---|
| Arch / design freezes | ≥0.90 | GATE_90 A1–A5 · B1–B7 |
| DESK_IA screens + deny codes | LOCKED | `DESK_IA.md` |
| Backend HITL spine | REAL | `/task/*`, sandbox, Monitor A, gateway, secrets |
| KWB vendor patterns | Integrated | `KWB/INTEGRATION_LOG.md` — patterns only |
| Desk HTML shell + most walk buttons | **EXISTS** | `desk/index.html` mounted at `/desk/` |
| HITL smoke | Script ready | `backend/scripts/hitl_gates_smoke.py` |
| Full G1–G10 API walk script | Script ready | `backend/scripts/execute_walk.py` |
| Fixtures / SOP packs | Present | `data/fixtures/`, retrieve |
| MCP MOCK stub | OFF by default | `/mcp/status` — **leave deferred** |
| Skills pack placeholder | Files only | `data/skills/` — **no runner** |

### Custom still required (ours only)

| Gap | Why jury cares |
|---|---|
| Artefact / leave-pack **download** API + desk buttons | F7 leave-with |
| Monitor B live audit/denies | Proof of fail-closed |
| Guided A→J + fail-closed inject UI (G8/G9/stale) | Stage walk survivable |
| Server-side **H7** ack | Cite review not theatre |
| Fixture picker (list + load FX-*) | Files screen honesty |
| Run `execute_walk` → `eval/evidence/*` + **sign** checklist | execute ≥0.90 |
| Demo runbook (operator cheat-sheet) | One-person stage |

**Not required for demo:** React rewrite · full MCP · skill runner · **OCR model** (org SoT — day-1 uses framework Tesseract/pypdf already) · SSO · Admin console · continuous Monitor A UI · Excel/PPT artefacts · more KWB pulls.

---

## 3. Confidence scores (0–1)

| Axis | Now | After proposed custom MVP | Notes |
|---|---|---|---|
| Architecture freeze | **0.90** | 0.90 | Unchanged |
| Design info | **0.90** | 0.90 | Unchanged |
| **Execute-ready** | **0.64** | **0.90–0.92** | Desk exists (↑ from 0.52) but leave-with + evidence + H7 + MonB still open |
| **PPT-ready** | **0.35** | **0.85** | Only after execute ≥0.90 + scrubbed prompts |
| **Jury-demo** | **0.38** | **0.82** | Stage walk + leave-with + signed G pack; residual: G1 floor honesty, MonA≠CERT |
| Start React rewrite now | **0.25** | — | **NO-GO** until Must MVP done |
| Start PPT now | **0.35** | — | **NO-GO** until execute ≥0.90 |

**Score delta vs READY_NOW_VERIFY:** execute 0.52→**0.64** (desk HTML landed); jury 0.28→**0.38** (still cannot claim signed A→J leave-with). PPT unchanged **NO-GO**.

---

## 4. Custom build backlog (Must / Should / Later)

Only **OUR** code. No vendor pulls.

### Must (blocks execute ≥0.90 / jury)

| # | Item | Where |
|---|---|---|
| M1 | `GET /artifacts/{filename}` (docx FileResponse, grant-scoped or demo-local) | `backend/app/main.py` |
| M2 | `GET /task/leave-pack?grant_id=&draft=` → zip/json manifest: docx path + recent audit slice + Monitor A sha if present | backend |
| M3 | Desk: **Download DRAFT** + **Download leave pack** after export OK | `desk/index.html` |
| M4 | Desk: poll `/audit/recent` into Monitor B; show last deny `error` codes | desk |
| M5 | Desk: fail-closed injects — secret text → export-check; bad model → gateway; keep revoke + stale edit | desk |
| M6 | `POST /task/h7-ack` + store on grant; `inspect-draft` reads server flag (ignore client-only) | backend + desk |
| M7 | Guided step enable/disable matching DESK_IA state machine (incl. coding branch) | desk |
| M8 | Run `execute_walk.py` with API up → write `eval/evidence/*` | ops |
| M9 | Fill + **sign** `eval/CHECKLIST.md` (G1 mode floor/full) | eval |
| M10 | One-page stage runbook (inspection + one fail-closed + MonA honesty) | `solution/prototype/` or `eval/` |

### Should (raises jury confidence; do if Must finishes early)

| # | Item |
|---|---|
| S1 | `GET /fixtures` list + desk picker (FX-EXT-01, scan stub) — no plant DMS |
| S2 | Auto-revoke grant after successful export (I4) + desk toast |
| S3 | Show DRAFT banner text / findings excerpt in desk after generate |
| S4 | `export_walk` also drives desk-visible scenario IDs for replay |
| S5 | Hash-chain verify button → `/audit/verify` on Monitor B |

### Later (explicit defer — do **not** start now)

| # | Item |
|---|---|
| L1 | Custom React+Vite Claude-like canvas (study OpenHands Canvas vibe only) |
| L2 | Full MCP host / FastMCP process / stdio-SSE |
| L3 | Skill runner / progressive load into LLM |
| L4 | **OCR model** (org SoT) — demo already on Tesseract/pypdf framework + fixture stub |
| L5 | Admin full console · SSO · Excel/PPT · hybrid vector · continuous WAN UI |

---

## 5. Recommended build sequence

| Day / step | Work | Exit |
|---|---|---|
| **D0 (½ day)** | M1–M3 leave-with downloads | Export → browser file in hand |
| **D1 (½–1 day)** | M4–M7 desk maturity + H7 server | Guided A→J + visible denies + no cite theatre |
| **D1 evening** | M8–M9 execute_walk + sign checklist | Evidence dir populated; `demo_ready` path clear |
| **D2 am** | M10 runbook · dry-run stage (inspection + revoke or secret) | Operator can solo |
| **Gate** | Re-score execute; if ≥0.90 → unpause PPT from scrubbed prompts only | PPT work starts |
| **If spare** | S1–S5 only | Polish |
| **Refuse until after PPT draft** | L1–L5 | No thrash |

Estimated custom effort to execute ≥0.90: **~1.5–2 focused days** (not a React project).

---

## 6. Explicitly NOT custom (use existing / refuse)

| Do this instead | Refuse |
|---|---|
| Call existing `/task/*`, `/sandbox/*`, `/monitor-a/*`, `/gateway/chat`, `/audit/*` | New orchestration framework |
| Read KWB notes for patterns already integrated | Re-clone OH / DeerFlow / Onyx `ee/` / LiteLLM cloud |
| Fixture H1 (`FX-EXT-01`) | Live plant browse / DMS |
| G1 floor honesty label | Fake second model pull |
| Monitor A honesty: evidence pack ≠ CERT | CERT-In / WAN=0 theatre without artefact |
| Self-HITL only | In-app Approver queue |
| Export leave = soft copy off box | Forward-accept / plant SoR write |
| MCP stub OFF | Full MCP lifecycle for demo |
| `data/skills/` as files | Skill runner into context |
| HTML thicken | Fork OpenHands Canvas as product |

---

## API gap summary (precise)

| Endpoint / capability | Status |
|---|---|
| Task start → H1 → retrieve → draft → H2 → edit/stale → export | **DONE** |
| Sandbox calc/python → H9 → G10 deny | **DONE** |
| Monitor A start/stop | **DONE** |
| Gateway deny + revoke | **DONE** |
| Secrets scan / export-check | **DONE** |
| Static `/desk/` | **DONE** |
| Artefact **download** | **MISSING** (Must M1) |
| Leave **pack** (docx + audit) | **MISSING** (Must M2) |
| Server **H7** ack | **MISSING** (Must M6) |
| Fixture catalog API | Optional (Should S1) |
| Upload multipart | **Not needed** day-1 (fixture pick OK) |
| Full MCP / skills | **Deferred** |

---

## Pointers

- Prior execute gap note: `EXECUTE_90_ADV.md` (partially superseded — desk HTML now exists; leave-with/evidence still open)  
- Scores SoT after this pass: this file + one-liners in `GATE_90_DISCUSS.md` / `READY_NOW_VERIFY.md`  
- Desk SoT: `DESK_IA.md` · Flow: `APPLICATION_FLOW_COMMON.md` A→J  
- Integrate history: `KWB/INTEGRATION_LOG.md` (desk React deferred — HTML MVP first)
