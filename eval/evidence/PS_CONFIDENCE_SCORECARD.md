# SIH26117 — Problem Statement ↔ Build Confidence Scorecard

**Date:** 2026-09-20  
**Sources:** `sih_research/.../01-problem-statement.md`, `02-combined-problem-statement.md`, `eval/CHECKLIST.md`, `eval/STAGE_RUNBOOK.md`, `PLATFORM_CONCEPTS_STATUS.md`, `CUSTOM_BUILD_PROGRESS.md`, `DESIGN_BUILD_SOT.md`, Mem0 (Workflow B `dfa68ff2…`, OCR/skills/MCP themes)  
**Honesty rule:** Scores are **not marketing**. Air-gap ≠ phone-hotspot LAN peer. G1 floor ≠ multi-model. Monitor A ≠ CERT.

**Overall (weighted): 72%** (was 68%; liveliness + vision path + egress honesty copy — see confidence rebuild 2026-09-20)

Weights favour Expected Solution demo bullets + sovereignty proof (air-gap / egress) over nice-to-have platform polish.

---

## Score legend

| Band | Meaning |
|---|---|
| 85–100 | Demoed with evidence; matches ask with minor caveats |
| 65–84 | Built and smoke-pass; material honesty caveats |
| 40–64 | Partial / floor / framework-only; judges may push |
| 0–39 | Missing, deferred, or claim would be false |

---

## 1. Core product

| # | Requirement (quote or paraphrase) | Explicit / Between-lines | What we built | Evidence | Confidence 0–100 | Honesty note |
|---|---|---|---|---|---|---|
| C1 | Self-hosted workbench on org GPU / mid-range workstation; smaller open-weight OK | Explicit | FastAPI + Electron `kwb-app` + Ollama (local or LAN peer); single-laptop stage path locked | `STAGE_RUNBOOK.md`, `SUMMARY.json` health, `start_demo.ps1` | **88** | Real local deploy. Not packaged installer / not plant GPU ops. |
| C2 | “Not a chatbot” — industrial evidence & document workbench; HITL keeps judgement outside | Explicit + between | Assist → extract → retrieve → DRAFT → self-HITL → **export leave**; no in-app Approver / CERT | `CHECKLIST.md`, leave-pack, DRAFT badge | **82** | Product framing matches. Still chat-shaped UI (Claude Code layout) — OK if walk is workflow. |
| C3 | Agentic: plan multi-step, call tools, iterate (not one-shot) | Explicit | `/orch/turn` + mid-turn `orch_phase` / SSE `/orch/events` + phase chips (not token stream) | orchestrator, App ToolBlock | **80** | Feels alive mid-turn; still turn-based vs Cursor stream |
| C4 | Real deliverables: approval notes, PPT/Word/Excel, working code, calc steps | Explicit | **Word** DRAFT primary; PPTX also exists; sandbox calc; Excel **not** a first-class path | G2 `draft-*.docx`, `word_draft.py`, `pptx_draft.py` | **70** | Word aligns Expected Solution. PPTX extra. Spreadsheet work largely absent. |
| C5 | Local KB connector; ground in manuals/SOPs; cite sources; nothing external | Explicit + between | Grant-scoped `/task/retrieve`, cite-or-abstain skill, fixture knowledge | G6, `data/skills/cite-or-abstain`, `workspace/knowledge/*` | **74** | Demo retrieve under grant. Not full industrial entity-resolution / revision control. |
| C6 | HITL before anything becomes a plant “record”; soft copy leave | Between (combined + WP) | H1/H2/H7/H9; stale `artefact_version`; export leave ends solution | G2/G4/G10, stage A→J | **90** | Strong. Paper Approver intentionally **outside** app — say that aloud. |

**Group roll-up (unweighted mean):** ~79

---

## 2. Security / sovereignty

| # | Requirement (quote or paraphrase) | Explicit / Between-lines | What we built | Evidence | Confidence 0–100 | Honesty note |
|---|---|---|---|---|---|---|
| S1 | Air-gapped — “Nothing leaves the premises” | Explicit | Phone-hotspot **LAN peer** (A↔B) or single-host loopback; **not** true air-gap | Mem0 Workflow B; `HOTSPOT_DETAILED_WORKFLOW.md` | **28** | **Must not claim air-gap.** Strongest honest claim: controlled private LAN / on-prem path. |
| S2 | Proof via logs or **visible network monitor** that no external calls occur | Explicit | Monitor A pack + audit + Status honesty (“private LAN · not air-gap”); mid-turn Live log denser | G5, MonitorPanel posture copy | **55** | Better theatre + honesty. Still ≠ CERT / WAN=0. |
| S3 | Backend not locked to one model; deny unregistered / public cloud models | Explicit + between | Card registry + gateway deny `gpt-4o`; no cloud fallback in gateway path | G8, `gateway.py`, models.yaml | **90** | Fail-closed on public model id is strong. Adoption still often one local tag. |
| S4 | No desk side-door to LLM — Desk → Orch → Pack → Gateway → local `/v1` only | Between | Primary desk uses `/orch/turn`; `kwb-desk` hard-refused; specialists are non-LLM helpers | Mem0 DM decisions; `LEGACY.md`; `specialists.py` | **88** | Architecture holds for demo desk. Do not demo legacy HTML as primary. |
| S5 | Sandbox: code execution isolated; deny-all network posture preferred | Explicit + between | Process sandbox + H9/G10; UI Status says **host-process** (no fake deny-all) | G3, G10, MonitorPanel | **58** | Honesty improved; isolation still floor |
| S6 | Audit trail with `model_id` / routing provenance | Between | Audit jsonl + draft footer `model_id`; `router_select` in G1 | audit files, G1, word draft meta | **85** | Present. Rehearse “Verify chain” on stage. |
| S7 | Grants + revoke block tools (permission-aware) | Between | Grant before tools; revoke → 403 | G6/G7 | **92** | Solid fail-closed story. |

**Group roll-up:** ~69 (pulled down hard by S1/S2)

---

## 3. Workflows (inspect Word, coding sandbox, multimodal)

| # | Requirement (quote or paraphrase) | Explicit / Between-lines | What we built | Evidence | Confidence 0–100 | Honesty note |
|---|---|---|---|---|---|---|
| W1 | Agentic E2E: scanned inspection → key findings → **Word** approval note | Explicit | Inspection walk + Word DRAFT; Workflow B LAN peer E2E PASS grant `dfa68ff2d9114e8c` | G2, `STAGE_DRY_RUN_AJ`, Mem0 Workflow B, MANUAL_TEST_REPORT | **90** | Matches Expected Solution deliverable (**Word not PPTX-only**). Fixture/OCR quality varies. |
| W2 | Coding task run and verified in a sandbox | Explicit | `/sandbox/calc` + H9; coding card route; UI guided path | G3, G10 | **78** | Verified for demo calc. Isolation honesty: process mode, not full jail. |
| W3 | Multimodal: image / scanned document understanding (OCR **and** vision models on-device) | Explicit | OCR framework + **optional moondream** vision path on image attach via Gateway (falls back to Tesseract/stub) | `orchestrator._try_vision_scan`, G4, ROBUST OCR | **62** | Vision wired when tag present on A; still not every attach; stub if vision fails |
| W4 | Spreadsheet work as a first-class tool | Explicit (tools list) | No mature Excel agent path | — | **25** | Gap vs description; not in Expected Solution demo bullets — still a judge probe risk. |
| W5 | Calculations with steps shown | Explicit | Sandbox stdout + H9 report | G3 | **70** | Calc demo OK; not a full engineering calc notebook product. |

**Group roll-up:** ~61

---

## 4. Platform (routing, MCP/plugins, skills)

| # | Requirement (quote or paraphrase) | Explicit / Between-lines | What we built | Evidence | Confidence 0–100 | Honesty note |
|---|---|---|---|---|---|---|
| P1 | Support multiple open-weight models; add later without redesign | Explicit | YAML cards + routing rules; adopt local tags only (no pull) | `config/models.yaml`, ollama_policy in SUMMARY | **72** | Architecture OK. Runtime often single adopted chat tag. |
| P2 | **Automatically** pick right model for ≥2 task types (coding ≠ summary/inspect) | Explicit | ≥2 task→**card** routes; **full two-tag** after `cards.py` fix: `inspect-draft→llama3.2:3b`, `code-assist→qwen2.5-coder:7b` (no longer adopts `moondream` for coding) | `ROBUST_E2E_REPORT.md`, `E2E_ONE_MODEL.json`, `SINGLE_MODEL_SIM.json` | **86** | Full Expected Solution auto-select now smoke-proven on LAN peer. Rehearse live; VRAM may unload between tags on 8GB. |
| P3 | Skills library for task families | Between | `data/skills/*` progressive load into orch pack | PLATFORM_CONCEPTS, skills README | **70** | Demo-wired; not marketplace / OpenHands runner. |
| P4 | Role-based prompts | Between | `roles.py` inspection/coding/freestyle/summary | PLATFORM_CONCEPTS | **75** | Present for demo. |
| P5 | MCP / plugins for tools & connectors | Between (platform ambition) | In-process allowlist `mcp_host.py`; `/mcp/status|tools|call` | PLATFORM_CONCEPTS | **50** | Partial. Not full stdio/SSE lifecycle / registry / plant MCP. |
| P6 | Multi-step orch + specialists (extract/cite) without LLM side-doors | Between | `specialists.py` + orch attach path | PLATFORM_CONCEPTS, smokes | **78** | Good for demo story. |

**Group roll-up:** ~66

---

## 5. Demo ops (two-laptop / stage)

| # | Requirement (quote or paraphrase) | Explicit / Between-lines | What we built | Evidence | Confidence 0–100 | Honesty note |
|---|---|---|---|---|---|---|
| D1 | Demonstrable on single workstation or server | Explicit | Locked stage path: one machine API+Electron+Ollama | STAGE_RUNBOOK, execute_walk | **92** | Primary jury path. |
| D2 | Two-laptop: local models on A, workbench on B; **no public LLM** on gateway path | Between (demo ops) | Hotspot link scripts; Workflow B PASS → `http://10.45.226.121:11434` + Word leave | Mem0 Workflow B; HOTSPOT docs | **86** | High for **local models / no public LLM in gateway path**. Low if sold as air-gap. |
| D3 | Operator runbook + signed eval pack | Between | CHECKLIST SIGNED; stage dry-run; manual UI report | CHECKLIST, STAGE_DRY_RUN, MANUAL_TEST | **88** | Execute ~0.90. PPT pitch still weak separately. |
| D4 | Visible sovereignty theatre without lying (Monitor A ≠ CERT) | Between | Scripts + integrity chrome + say-aloud lines | STAGE_RUNBOOK §3 | **80** | Process exists; depends on operator discipline. |

**Group roll-up:** ~87 (for ops readiness; does not raise S1)

---

## Weighted overall

| Bucket | Weight | Roll-up | Contribution |
|---|---|---|---|
| Expected Solution critical demos (W1+W2+W3+P2+C1) | 40% | ~77 | 30.8 |
| Sovereignty proof (S1+S2+S3+S4) | 25% | ~64 | 16.0 |
| Core workbench + HITL + KB (C2–C6) | 15% | ~80 | 12.0 |
| Platform extensibility (P1,P3–P6,S5–S7) | 10% | ~72 | 7.2 |
| Demo ops (D1–D4) | 10% | ~87 | 8.7 |
| **Total** | **100%** | | **~75** raw → **adjusted −7** for air-gap / multimodal / sandbox shortfalls judges will probe |

### Final overall: **72%**

**Interpretation:** Strong **working prototype** for an honest SIH demo (Word inspection walk, **dual-model auto-select**, mid-turn phase liveliness, gateway deny, HITL, local Ollama path, two-laptop LAN peer, optional moondream vision). Remaining hard gaps: **true air-gap proof**, **sandbox deny-all**, and pitch/PPT scrub.

---

## Top 5 gaps to close before finals

1. **Air-gap / egress proof (S1–S2)** — Either run a real offline venue rehearsal with NIC evidence, or drop the air-gap claim and script the honest line: “private LAN / on-prem gateway; Monitor A = evidence pack, not CERT.” Score stays low until proof matches claim.
2. **Multimodal vision (W3)** — Move beyond Tesseract/fixture framework to a staged local vision/OCR model path (`moondream` is on A but unused on inspect Word walk).
3. **Sandbox deny-all (S5)** — Tighten isolation story (no-net container or documented host-process limits) so “verified in a sandbox” survives red-team.
4. **Rehearsal + pitch integrity (D3/D4 + PPT)** — Live Electron A→J + dual-model switch timing on 8GB; scrub slides of CERT / Approver-in-app / air-gap overclaims. PPT-ready still ~0.30–0.35.
5. **G1 live rehearsal** — Dual tags are smoke-proven; still rehearse inspect→coder unload/load on Laptop A so venue latency doesn’t surprise.

---

## Claim cheat-sheet (say / don’t say)

| Say | Don’t say |
|---|---|
| Local open-weight via Gateway; public model ids denied | “Fully air-gapped” on hotspot demo |
| Auto-select: `inspect-draft→llama3.2:3b`, `code-assist→qwen2.5-coder:7b` (smoke-proven) | “Many models” without naming tags |
| Word DRAFT soft copy; paper approval outside | “Certified plant record” / in-app Approver |
| Monitor A evidence pack · desk **NOT CERT** | “CERT-In certified” / “WAN=0 proven forever” |
| OCR framework (+ fixture); vision model staged | “Full multimodal vision LLM” today |
| Two-laptop = private LAN peer local Ollama | “Nothing can leave because hotspot” |
| Turn-based orch + mid-turn phase events (not Cursor token stream) | “Same live agent UX as Cursor” |

See also: `DECISION_AND_GAP_AUDIT.md` pitch lines.

---

## Evidence index (primary)

| Artefact | Role |
|---|---|
| `eval/CHECKLIST.md` | G1–G10 SIGNED (floor note may lag; see ROBUST for full two-tag) |
| `eval/evidence/DECISION_AND_GAP_AUDIT.md` | Decisions keep/revise + pitch lines |
| `eval/evidence/ROBUST_E2E_REPORT.md` | LAN peer + G1 full two-tag |
| `eval/evidence/SUMMARY.json` | Execute walk aggregate |
| `eval/STAGE_RUNBOOK.md` | Jury walk + honesty lines |
| `eval/evidence/MANUAL_TEST_REPORT.md` | UI operator walk |
| Mem0 Workflow B `dfa68ff2d9114e8c` | Two-laptop Gateway + Word PASS; **not** air-gap |
| `solution/prototype/PLATFORM_CONCEPTS_STATUS.md` | Skills/roles/MCP/vision honesty |
| `solution/prototype/CUSTOM_BUILD_PROGRESS.md` | Execute 0.90 / PPT 0.35 |
