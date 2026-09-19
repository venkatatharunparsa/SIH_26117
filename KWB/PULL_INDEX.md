# KWB PULL_INDEX — vendor → folder map

**Project:** SIH26117 Knowledge Work Bench  
**Rule:** Reference extracts only (MIT / Apache). Prefer copy + `SOURCE.md`. Do **not** treat these trees as runnable product packages. Do **not** extract DeerFlow / Open WebUI / Browser Use / cloud LiteLLM.

| Upstream repo | KWB folder | Purpose | Integrate later? |
|---|---|---|---|
| `vendor/software-agent-sdk/` | `required/01_execute_command` … `06_architecture` | Sandbox / terminal / LLM `base_url` / architecture notes | **Yes** — patterns into `backend/` (thin reimpl; already partly done) |
| `vendor/software-agent-sdk/` | `from_software_agent_sdk/07_events_observation` | Observation / action event shapes | **Yes** — field shapes for audit + H9 |
| `vendor/software-agent-sdk/` | `from_software_agent_sdk/08_skills_example` | One `SKILL.md` layout example | **Yes** — offline skills pack format |
| `vendor/OpenHands/` (Agent Canvas) | `from_openhands_canvas/` | Architecture + UI study notes | **Study only** — no UI fork |
| `vendor/python-sdk/` | `from_mcp_python_sdk/` | MCP client/server entry modules | **Later** — protocol for MCP MOCK |
| `vendor/fastmcp/` | `from_fastmcp/` | FastMCP decorator API + echo demo | **Later** — one MOCK server |
| `vendor/DeerFlow/` | `REFUSE/DeerFlow.md` | Explicit non-extract | **No** |
| Continue.dev (web) | `from_continue_web/` | OpenAI-shape `apiBase`/`model` client | **Study** — thin httpx gateway |
| Onyx (web) | `from_onyx_web/` | ACL-before-retrieve intent + MOCK schema | **Study** — G6 grant filter |
| Haystack (web) | `from_haystack_web/` | retrieve→cite pipeline shape | **Study** — WP-11 outline |
| LlamaIndex (web) | `from_llamaindex_web/` | CitationQueryEngine shape | **Study** — WP-11 alternate |
| Presidio (web) | `from_presidio_web/` | PII analyzer / PatternRecognizer | **Optional pip** — G9 deepen |
| LangGraph (web) | `from_langgraph_web/` | interrupt/resume HITL *pattern* | **Notes only** — not runtime owner |

## Existing required slices (verified present)

| Folder | Files (approx) | Status |
|---|---|---|
| `required/01_execute_command` | 2 | OK |
| `required/02_workspace_local` | 3 | OK |
| `required/03_docker_network` | 1 | OK |
| `required/04_terminal` | 14 | OK |
| `required/05_llm_base_url` | 3 | OK |
| `required/06_architecture` | 1 | OK |

## Wave 2 web study slices (2026-09-19)

| Folder | Files | Status |
|---|---|---|
| `from_continue_web/` | 4 | OK — docs YAML excerpts |
| `from_onyx_web/` | 5 | OK — MIT-path ACL filter + MOCK JSON |
| `from_haystack_web/` | 4 | OK — pipeline outline |
| `from_llamaindex_web/` | 4 | OK — citation templates trimmed |
| `from_presidio_web/` | 4 | OK — analyzer hello + PatternRecognizer |
| `from_langgraph_web/` | 2 | OK — notes only (allowlisted pattern) |

## MISSING notes (see per-folder SOURCE.md)

- `from_openhands_canvas`: dedicated short HITL/confirm **docs** under `docs/` — **MISSING** (confirm UX is TS-only; pointers in `ui_notes.md`).
- GBrain provenance fields (WP-11) — **not extracted** (no clear public MIT slice this pass).

## Licenses

| Slice | License |
|---|---|
| OpenHands SDK / Canvas extracts | MIT |
| MCP Python SDK | MIT |
| FastMCP | Apache-2.0 |
| Continue (web) | Apache-2.0 |
| Onyx (web, non-`ee/`) | MIT Expat (`ee/` = Enterprise — refused) |
| Haystack (web) | Apache-2.0 |
| LlamaIndex (web) | MIT |
| Presidio (web) | MIT |
| LangGraph (web) | notes only — confirm at pin |

## Product code

Do **not** modify `backend/` or `desk/` from this extract pass. Wire patterns later under work-package control.
