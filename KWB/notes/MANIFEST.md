# Per-slice manifests

Master index: [`../PULL_INDEX.md`](../PULL_INDEX.md)

---

## 01_execute_command
| File | From |
|---|---|
| `command.py` | `software-agent-sdk/.../sdk/utils/command.py` |
| `redact.py` | `software-agent-sdk/.../sdk/utils/redact.py` |

**Use:** subprocess timeout; strip API keys from child env.

## 02_workspace_local
| File | From |
|---|---|
| `models.py` | `.../workspace/models.py` (`CommandResult`) |
| `local.py` | `.../workspace/local.py` |
| `base.py` | `.../workspace/base.py` (deps of local) |

**Use:** result shape for H9 / audit.

## 03_docker_network
| File | From |
|---|---|
| `docker_workspace.py` | `.../workspace/docker/workspace.py` |

**Use:** `network` field → `--network none` (WP-16). Jail ≠ GPU.

## 04_terminal
| File | From |
|---|---|
| `timeout_policy.py`, `impl.py`, `definition.py`, … | `openhands-tools/.../tools/terminal/` |
| `terminal/windows_terminal.py`, `subprocess_terminal.py` | same |

**Use:** Windows-friendly shell ideas if we outgrow process jail.

## 05_llm_base_url
| File | From |
|---|---|
| `chat_options.py`, `common.py` | `.../llm/options/` |
| `llm_base_url_fields.py.snippet` | fields from `llm.py` (not full LiteLLM client) |

**Use:** confirm OpenAI-shape `base_url` + `model` for gateway.

## 06_architecture
| File | From |
|---|---|
| `architecture.md` | `vendor/OpenHands/docs/architecture.md` |

**Use:** product boundary notes only.

---

## from_software_agent_sdk / 07_events_observation
| File | From |
|---|---|
| `observation.py`, `action.py`, `base.py`, `types.py`, … | `openhands-sdk/.../sdk/event/` |
| `tool_schema.py` | `openhands-sdk/.../sdk/tool/schema.py` |

**Use:** observation/action field shapes for audit + H9.  
**Manifest:** `from_software_agent_sdk/SOURCE.md`

## from_software_agent_sdk / 08_skills_example
| File | From |
|---|---|
| `code-style-guide/SKILL.md` | `examples/.../code-style-guide/SKILL.md` |

**Use:** offline `SKILL.md` progressive-load layout.  
**Manifest:** `from_software_agent_sdk/SOURCE.md`

---

## from_openhands_canvas (STUDY ONLY)
| File | From |
|---|---|
| `docs/architecture.md` | `vendor/OpenHands/docs/architecture.md` |
| `ui_notes.md` | written (study / refuse) |
| HITL confirm docs | **MISSING** in upstream `docs/` — TS pointers in `ui_notes.md` |

**Use:** desk vibe + confirm metaphor only. **Do not** fork UI.  
**Manifest:** `from_openhands_canvas/SOURCE.md`

---

## from_mcp_python_sdk
| Slice | From |
|---|---|
| `mcp/client/*`, `mcp/server/*`, `mcp/types/*`, `mcp/shared/{exceptions,message}.py` | `vendor/python-sdk/src/mcp/...` |
| `LICENSE` | MIT |

**Use:** MCP protocol study for later MOCK. Tree kept &lt;30 files.  
**Manifest:** `from_mcp_python_sdk/SOURCE.md`

---

## from_fastmcp
| Slice | From |
|---|---|
| `core/{__init__,settings,types}.py`, `core/server/server.py`, `core/tools/*` | `vendor/fastmcp/fastmcp_slim/fastmcp/...` |
| `examples/echo.py` | `vendor/fastmcp/examples/echo.py` |
| `LICENSE` | Apache-2.0 |

**Use:** decorator API study for one MOCK. Full slim tree not copied (path pointers in SOURCE).  
**Manifest:** `from_fastmcp/SOURCE.md`

---

## from_continue_web (Wave 2 — web)
| File | From |
|---|---|
| `NOTES.md`, `excerpt_openai_compatible_config.yaml.md` | https://docs.continue.dev/customize/model-providers/top-level/openai |
| `LICENSE.Apache-2.0.txt` | Apache-2.0 notice |

**Use:** `apiBase` + `model` triad for gateway. **Do not** fork Continue UI.  
**Manifest:** `from_continue_web/SOURCE.md`

## from_onyx_web (Wave 2 — web)
| File | From |
|---|---|
| `excerpt_document_access_filter.py.md` | `backend/onyx/db/document_access.py` (MIT path) |
| `mock_acl_schema.example.json` | KWB-authored MOCK (intent only) |
| `NOTES.md` | docs.onyx.app connectors overview |

**Use:** ACL-before-retrieve → G6 grant filter / NOT FOUND. **Refuse** `ee/` and Onyx product.  
**Manifest:** `from_onyx_web/SOURCE.md`

## from_haystack_web (Wave 2 — web)
| File | From |
|---|---|
| `excerpt_rag_cite_pipeline.py` | docs creating-pipelines + AnswerBuilder (outline) |
| `NOTES.md` | retrieve→cite DAG |

**Use:** WP-11 pipeline shape. Not a Haystack runtime.  
**Manifest:** `from_haystack_web/SOURCE.md`

## from_llamaindex_web (Wave 2 — web)
| File | From |
|---|---|
| `excerpt_citation_query_engine.py.md` | trimmed `citation_query_engine.py` templates |
| `NOTES.md` | CitationQueryEngine tutorial |

**Use:** numbered Source N + `[n]` cites. Alternate to Haystack.  
**Manifest:** `from_llamaindex_web/SOURCE.md`

## from_presidio_web (Wave 2 — web)
| File | From |
|---|---|
| `excerpt_analyzer_hello.py` | analyzer docs + adding_recognizers |
| `NOTES.md` | AnalyzerEngine / PatternRecognizer |

**Use:** optional G9 deepen (`pip`); regex remains day-1.  
**Manifest:** `from_presidio_web/SOURCE.md`

## from_langgraph_web (allowlisted pattern — web)
| File | From |
|---|---|
| `NOTES.md` | https://docs.langchain.com/oss/python/langgraph/interrupts |

**Use:** interrupt/resume metaphor for H* gates only. **Refuse** LangGraph-as-product.  
**Manifest:** `from_langgraph_web/SOURCE.md`

---

## REFUSE
| Entry | Why |
|---|---|
| `REFUSE/DeerFlow.md` | Explicit non-extract — wrong product, cloud skills, out of plan |
| Open WebUI / Browser Use / cloud LiteLLM | Wave 3 / user refuse — not extracted |
| Onyx `ee/` | Enterprise License — not copied |
| GBrain provenance | Named in WP-11; no clear public MIT slice this pass — **MISSING** |
