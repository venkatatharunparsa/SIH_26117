# KWB → workbench INTEGRATION_LOG

**Date:** 2026-09-19  
**Project:** SIH26117  
**Rule:** Patterns into `backend/app/*` — no `openhands.*` imports, no OH/MCP pip into prod, no desk custom UI this pass.

## Integrated

| Area | From KWB | Into | What changed |
|---|---|---|---|
| Sandbox env strip | `required/01` command + redact | `backend/app/sandbox.py` | Expanded strip list, `OH_SESSION_API_KEYS_` prefix, secret-name patterns; docstring cites KWB paths; `network=none` docker path kept |
| CommandResult / H9 | `required/02` + `07_events_observation` | `sandbox.py`, `artefacts.py`, export audit | `observation_fields()`; audit events carry `ok`, `exit_code`, `duration_ms`, truncated `stderr` |
| Gateway | `required/05` + `from_continue_web` | `backend/app/gateway.py` | Docstring triad (apiBase+model); local-only + card allowlist confirmed; **no LiteLLM** |
| Secrets G9 | `from_presidio_web` | `backend/app/secrets.py` | Regex expansion (provider key prefixes, bearer, slack/gh/hf); **no Presidio dep** |
| Retrieve ACL | `from_onyx_web` | `backend/app/retrieve.py` | Comment: ACL-before-retrieve / grant shelves; logic unchanged |
| Cite pipeline notes | `from_haystack_web` + `from_llamaindex_web` | `retrieve.py` docstring | Cite-or-abstain shape notes only |
| HITL interrupt | `from_langgraph_web` | `artefacts.py`, `main.py` | Docstring/comment pattern only; **no LangGraph dep** |
| Skills pack | `08_skills_example` | `data/skills/` | One adapted `SKILL.md` + README placeholder (no runner) |
| MCP MOCK | `from_mcp_python_sdk` + `from_fastmcp` | `backend/app/mcp_mock.py` + `/mcp/status`, `/mcp/echo` | Thin stub; `SOVEREIGN_MCP_MOCK` **OFF** by default → “not enabled” |

## Deferred

- Desk **custom React components** (next phase after this integrate)
- Full MCP host / stdio-SSE / FastMCP server process
- Skill runner / progressive load into LLM context
- Presidio as optional pip deepen
- Haystack / LlamaIndex / Onyx / LangGraph as runtime
- DeerFlow / Open WebUI / Browser Use / Onyx `ee/` / LiteLLM cloud (**refuse**)

## Verify

```text
cd backend
python -c "from app import main, sandbox, gateway, secrets"
python scripts/hitl_gates_smoke.py   # API on 127.0.0.1:8080
```
