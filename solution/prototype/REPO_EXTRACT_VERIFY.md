# Repo → extract map (VERIFY THIS)

**Date:** 2026-09-19  
**Status:** **BINDING for desk build** — what we take from where  
**Rule:** Clone/study/slice → compose in `backend/` + desk UI. **Never** fork an agent OS as KWB.

Detail history: `OPENHANDS_EXTRACT.md` · slices on disk: `KWB/required/` · `KWB/README.md`

---

## One-line clarity

| Need | Source | Extract? | Already in our code? |
|---|---|---|---|
| Desk UI (inspection workbench) | **We write** Next.js App Router (`apps/kwb-desk/`) | OpenHands **Canvas = study look only** | **Application UI:** `apps/kwb-desk` → `:3000`. Static `desk/` = **legacy fallback** |
| API / grants / HITL / Word / G1–G10 | **We write** `backend/` | Patterns from map below | **Mostly YES** (v0.4) |
| Sandbox idea | `vendor/software-agent-sdk` | Pattern only → `sandbox.py` | **YES** |
| Gateway `/v1` client | Study OH LLM base_url + **httpx** | Thin client | **YES** `gateway.py` |
| Runtime weights | **Ollama** binary (demo) | Install/adopt tags — **no pull** | Configured |
| Word | **PyPI** python-docx | pip | **YES** |
| OCR day-1 | **Fixture** FX-EXT-01 | No engine required yet | H1 API **YES** |
| MCP later | `vendor/python-sdk` + `vendor/fastmcp` | One MOCK server later | **Not yet** |
| DeerFlow | `vendor/DeerFlow` | **REFUSE product** — ignore | Do not use |

---

## Vendor folders — what each is for

| Path | Role | Take | Refuse |
|---|---|---|---|
| `vendor/software-agent-sdk/` | **Primary study** for jail/execute | Ideas → thin reimplement | Import whole Agent Server |
| `vendor/OpenHands/` | Agent Canvas UI | **Visual/UX study only** | Fork as KWB shell |
| `KWB/required/01…06` | Copied OH slices for reading | Read while coding sandbox/gateway | `pip install` OH into prod |
| `vendor/python-sdk/` | MCP protocol | MOCK MCP host **after** desk spine | Runtime skill install |
| `vendor/fastmcp/` | Easy MCP server | One local MOCK tool | Public registry |
| `vendor/DeerFlow/` | Accident/noise | **Nothing** for product | Any fork |

---

## Desk build — extract plan (what you verify)

| Desk screen (DESK_IA) | Code we write | May study from | Do not copy |
|---|---|---|---|
| Intent / task start | Our Next.js app → `POST /task/start` | Canvas “start task” layout vibe | Canvas routing/chat shell |
| Files / fixtures | Our upload + fixture picker | — | Plant DMS UIs |
| H1 confirm | Our form → `/task/h1-confirm` | OH human-confirm *idea* | Their HITL product |
| Knowledge / cites | Our panel → `/task/retrieve` | — | Onyx/Open WebUI |
| DRAFT Word | Preview path from API | — | Copilot doc UIs |
| H2 / stale / H9 | Our gates → h2-ack, h9-ack, draft-edit | Interrupt *pattern* only | LangGraph-as-app |
| Export leave | Our button → `/task/export` | — | Approver queue UIs |
| Monitor B thin | Our panel → `/audit/recent` + cards | Canvas status strip vibe | CERT dashboards |

**Stack for desk:** **Next.js 15 App Router** (`apps/kwb-desk/`) against FastAPI `127.0.0.1:8080`. Static `desk/index.html` = legacy fallback. No vendor Canvas fork. See `UI_STACK_ADV.md`.

---

## Already extracted / composed (do not re-pull)

| Module | File | Inspired by |
|---|---|---|
| Sandbox | `backend/app/sandbox.py` | OH workspace execute + network=none |
| Gateway | `backend/app/gateway.py` | OH base_url + our deny WAN |
| Grants / cards / Word / HITL / Monitor A / secrets | `backend/app/*` | Ours + freezes |

---

## Never extract (product kill)

DeerFlow · Open WebUI · AnythingLLM · Browser Use · LiteLLM cloud · Graphiti-as-core · OpenHands Cloud · full Agent Server as orchestrator · `npx` skill install.

---

## Confidence

| Question | Answer |
|---|---|
| Full clarity repo → extract? | **YES** for desk build (this file) |
| Need more clones before desk? | **NO** |
| Need DeerFlow? | **NO** |
| PPT extract from repos? | **N/A** — PPT from our freezes/prompts only, after execute ≥0.90 |

**Verify OK?** Reply yes and we start desk UI only against this map.

**Extract status (2026-09-19):** All mapped pulls stored under `KWB/` — see `KWB/PULL_INDEX.md`. Custom components = **next phase after you verify pulls**.

---

## Wave 2 — web extracts (study only)

Pulled via web into `KWB/` (not vendor clones). Each folder has `SOURCE.md`.

| Folder | Status |
|---|---|
| `KWB/from_continue_web/` | OK |
| `KWB/from_onyx_web/` | OK — MIT-path only; **`ee/` blocked** (Enterprise) |
| `KWB/from_haystack_web/` | OK |
| `KWB/from_llamaindex_web/` | OK |
| `KWB/from_presidio_web/` | OK |
| `KWB/from_langgraph_web/` | OK — interrupt/resume notes only |

**Gaps / refuse this pass:**

| Item | Note |
|---|---|
| **GBrain** | **Missing** — no clear public MIT slice for WP-11 provenance fields |
| **Onyx `ee/`** | **Blocked** — Enterprise path; do not extract |
| **DeerFlow** | **Still refuse** — see `KWB/REFUSE/DeerFlow.md`; no product extract |
