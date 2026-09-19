# KWB — required OpenHands extracts + vendor study slices

**Purpose:** Only the slices we need from mapped vendors, copied here so we integrate without hunting inside `vendor/`.

**Master index:** [`PULL_INDEX.md`](PULL_INDEX.md) — repo → folder → purpose → integrate later?

**Rule:** These files are **reference extracts** (MIT / Apache-2.0). Prefer wiring through `backend/app/*` (already thin-reimplemented for sandbox/gateway). Do **not** treat this folder as a runnable OpenHands / MCP / FastMCP install — many imports still expect full packages.

**Source clones (full):** `vendor/OpenHands/` · `vendor/software-agent-sdk/` · `vendor/python-sdk/` · `vendor/fastmcp/`  
**Wave 2 study (web-fetched, not vendored):** `from_continue_web/` · `from_onyx_web/` · `from_haystack_web/` · `from_llamaindex_web/` · `from_presidio_web/` · `from_langgraph_web/`  
**Plan:** `solution/prototype/OPENHANDS_EXTRACT.md` · `solution/prototype/REPO_PULL_MAP.md`  
**REFUSE:** DeerFlow / Open WebUI / Browser Use / cloud LiteLLM — see `REFUSE/DeerFlow.md`

---

## Layout

```text
KWB/
  PULL_INDEX.md                  ← master index
  README.md                      ← you are here
  LICENSE-OpenHands-SDK          ← MIT (SDK)
  required/                      ← primary OH SDK extracts
    01_execute_command/
    02_workspace_local/
    03_docker_network/
    04_terminal/
    05_llm_base_url/
    06_architecture/
  from_software_agent_sdk/       ← extra OH SDK slices
    07_events_observation/
    08_skills_example/
    SOURCE.md
  from_openhands_canvas/         ← STUDY ONLY (no UI fork)
    docs/
    ui_notes.md
    SOURCE.md
  from_mcp_python_sdk/           ← MCP protocol study (<30 files)
    SOURCE.md
  from_fastmcp/                  ← FastMCP study for one MOCK later
    SOURCE.md
  from_continue_web/             ← Wave 2 web: apiBase + model triad
  from_onyx_web/                 ← Wave 2 web: ACL-before-retrieve
  from_haystack_web/             ← Wave 2 web: retrieve→cite DAG
  from_llamaindex_web/           ← Wave 2 web: CitationQueryEngine
  from_presidio_web/             ← Wave 2 web: PII analyzer patterns
  from_langgraph_web/            ← allowlisted interrupt pattern (notes)
  REFUSE/
    DeerFlow.md
  notes/
    MANIFEST.md
```

---

## Map → our workbench

| Folder | Take idea | Already in `backend/` | Next use |
|---|---|---|---|
| `01_execute_command` | timeout, strip secrets from env | `app/sandbox.py` | tighten env strip list |
| `02_workspace_local` | `CommandResult` shape | `SandboxResult` | H9 evidence fields |
| `03_docker_network` | `--network` hook | docker path in sandbox | keep `none` default |
| `04_terminal` | Windows terminal / timeout policy | process jail | optional richer shell later |
| `05_llm_base_url` | `model` + `base_url` | `app/gateway.py` | Model Cards |
| `06_architecture` | jail ≠ product UI | — | design only |
| `07_events_observation` | observation/action event fields | audit JSONL | H9 / audit shape |
| `08_skills_example` | `SKILL.md` layout | — | offline skills packs |
| `from_openhands_canvas` | HITL confirm metaphor | — | desk gates (study) |
| `from_mcp_python_sdk` | MCP session/stdio API | — | MCP MOCK later |
| `from_fastmcp` | `@mcp.tool` echo style | — | one MOCK later |
| `from_continue_web` | `apiBase` + `model` triad | `app/gateway.py` | cards + deny WAN |
| `from_onyx_web` | authz before retrieve | — | G6 grant filter / NOT FOUND |
| `from_haystack_web` | retrieve→cite DAG | — | WP-11 outline |
| `from_llamaindex_web` | numbered Source N cites | — | WP-11 alternate |
| `from_presidio_web` | AnalyzerEngine / PatternRecognizer | regex gate | optional G9 deepen |
| `from_langgraph_web` | interrupt / resume | — | H* gates (pattern only) |

---

## REFUSE (not copied as product)

Agent Canvas UI fork, DeerFlow, Open WebUI, Browser Use, cloud LiteLLM / public providers, cloud sandbox, browser tools, Agent Server as orchestrator, marketplace skills, full `llm.py` / LiteLLM stack, OAuth MCP demos, Onyx EE / product UI, Haystack/LlamaIndex as app shell, Presidio cloud remote detectors, LangGraph-as-owner of grants.

---

## Integrate order

1. Read `PULL_INDEX.md`, then `01` + `02` + `03` when changing sandbox.  
2. Read `05` + `from_continue_web` when changing gateway / cards.  
3. Read `07` when shaping audit / H9 evidence.  
4. Read `08` when designing offline `SKILL.md` packs.  
5. Read Canvas `ui_notes.md` + `from_langgraph_web` only for HITL metaphors — never fork UI / never lock LangGraph.  
6. Read MCP / FastMCP slices only when building the MOCK.  
7. Read Onyx / Haystack / LlamaIndex when building retrieve + cites (G6 / WP-11).  
8. Read Presidio when deepening G9 beyond regex.  
9. Keep product code in `backend/` / `desk/` — copy patterns, avoid importing these paths as packages.
