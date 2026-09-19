# SOURCE — from_software_agent_sdk

**Upstream:** `vendor/software-agent-sdk/`  
**License:** MIT (`vendor/software-agent-sdk/LICENSE`)  
**Role:** Extra slices beyond `KWB/required/` (events/observations + one skills layout).

## What was copied

| KWB path | Upstream path |
|---|---|
| `07_events_observation/observation.py` | `openhands-sdk/openhands/sdk/event/llm_convertible/observation.py` |
| `07_events_observation/action.py` | `.../event/llm_convertible/action.py` |
| `07_events_observation/base.py` | `.../event/base.py` |
| `07_events_observation/types.py` | `.../event/types.py` |
| `07_events_observation/error_classification.py` | `.../event/error_classification.py` |
| `07_events_observation/event__init__.py` | `.../event/__init__.py` |
| `07_events_observation/llm_convertible__init__.py` | `.../event/llm_convertible/__init__.py` |
| `07_events_observation/tool_schema.py` | `openhands-sdk/openhands/sdk/tool/schema.py` |
| `08_skills_example/code-style-guide/SKILL.md` | `examples/05_skills_and_plugins/01_loading_agentskills/example_skills/code-style-guide/SKILL.md` |

## What KWB will use later

- Observation / action event field shapes for audit + H9 evidence (stdout/stderr/tool result mapping).
- `SKILL.md` frontmatter + progressive-load layout for our offline skills packs (WP-07/15).

## What NOT to import as product

- Full OpenHands event bus, condenser, ACP tool-call events, streaming deltas.
- Marketplace / plugin loader / `npx` skill install at runtime.
- Do not `import openhands.*` from these copies — study and reimplement thin shapes in `backend/`.

## MISSING

None for the planned slices above.
