# The Definitive Open-Source Agentic AI Repository Atlas

You asked for something dramatically better than what you were given. The real upgrade is not just more GitHub links—it is a **structured, production-grade taxonomy** that separates **agent applications, durable workflows, company memory, protocols, security, sandboxes, skills, evaluation, and deployment** so you can assemble an actual autonomous operating system rather than a fragile chatbot.

The strongest current architecture is:

```text
Company data
  → governed knowledge layer
  → contextual memory
  → agent runtime
  → durable workflow engine
  → MCP/A2A gateway
  → isolated execution
  → human approval
  → audit and evaluation
```

The repositories below are selected for **architectural importance, implementation depth, deployability, activity, and relevance to autonomous workflows**. Repository claims—especially benchmarks and security claims—should still be independently tested.

***

## 1. Best Complete Agent Systems

| Repository | Best Use | Why It Matters | Caution |
|---|---|---|---|
| [DeerFlow](https://github.com/bytedance/deer-flow) | Long-horizon research and business agents | Combines sub-agents, memory, skills, context engineering, browser control, scheduled tasks, MCP, artifacts, tracing, and sandboxes | Skill restrictions are not a hard security boundary |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Persistent personal or terminal operator | Strong focus on persistent sessions, skill creation, scheduled tasks, sub-agents, memory, and multiple execution backends | Treat autonomous self-modification as untrusted until sandboxed |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Autonomous software engineering | Deep coding-agent environment with tools, browser interaction, execution environments, event streams, and human intervention | Primarily optimized for software tasks |
| [Goose](https://github.com/block/goose) | Local extensible developer agent | Strong MCP orientation, provider flexibility, terminal workflows, and extension architecture | Less of a complete company operating system |
| [OpenClaw](https://github.com/openclaw/openclaw) | Messaging-first, always-on personal agent | Useful gateway model for channels, devices, sessions, browser, voice, cron, skills, and per-agent workspaces | Needs strict identity, allowlists, and execution isolation |
| [OpenAkita](https://github.com/openakita/openakita) | AI-company-style assistant | Integrates multiple agents, computer use, files, schedules, channels, memory, skills, dashboards, and MCP | Verify recovery, authorization, tenancy, and long-running reliability |
| [LobeHub](https://github.com/lobehub/lobehub) | Human-facing agent operations | Strong workspace and "agent team" administration direction | More product/workspace-oriented than infrastructure-oriented |
| [Khoj](https://github.com/khoj-ai/khoj) | Self-hosted second brain | Practical personal/team knowledge, search, agents, scheduled automation, and research | Less suitable as the complete enterprise control plane |
| [Dify](https://github.com/langgenius/dify) | Self-hosted AI application platform | Combines workflows, agents, RAG, tools, model management, and application operations | Visual abstractions can hide operational complexity |
| [Onyx](https://github.com/onyx-dot-app/onyx) | Enterprise search and agents | Over 50 connector patterns, agentic RAG, custom agents, deep research, actions, MCP, RBAC, SSO, and audit features | Best used as the enterprise data-access layer, not the entire memory architecture |

**DeerFlow** is the best single repository to study first. Its current repository shows active work around run-event contracts, checkpoint storage, incremental agent-scoped memory, browser control, Kubernetes sandbox provisioning, skill review gates, and database-backed custom agents.

**Onyx** is particularly valuable when the first problem is connecting agents safely to company systems. Its repository documents hybrid retrieval, custom agents, actions, code execution, deep research, more than 50 connectors, deployment through Docker/Kubernetes/Helm, and MIT-licensed Community Edition features.

***

## 2. Company Brain and Organizational Memory

A company brain is not simply "RAG." It needs:

- Source provenance.
- Access control.
- Temporal validity.
- Entity and relationship resolution.
- Human-reviewed writes.
- Contradiction handling.
- Citation and evidence.
- Tenant isolation.
- Deletion and retention policies.
- Search plus synthesis.
- Memory of outcomes, not just documents.

### Highest-Value Repositories

| Repository | Category | Best Role |
|---|---|---|
| [GBrain](https://github.com/garrytan/gbrain) | Git-backed institutional brain | Reviewed Markdown knowledge, graph relationships, synthesis, citations, gap analysis, MCP, and multi-user scopes |
| [AKB](https://github.com/dnotitia/akb) | Git-native agent knowledgebase | Simpler organizational memory model with Git, hybrid retrieval, and MCP read/write |
| [TeamBrain](https://github.com/donatienmigue/teambrain) | Governed team memory pattern | Agent proposes a knowledge change, humans review it through pull requests, then it enters shared memory |
| [OpenViking](https://github.com/volcengine/OpenViking) | Context database | Unifies memories, resources, and skills in a navigable virtual filesystem |
| [Cognee](https://github.com/topoteretes/cognee) | Knowledge graph construction | Converts documents and events into connected graph plus vector context |
| [Graphiti](https://github.com/getzep/graphiti) | Temporal knowledge graph | Tracks changing facts, people, vendors, incidents, ownership, and policies over time |
| [Hindsight](https://github.com/vectorize-io/hindsight) | Reflective memory | Retain, recall, reflect, experiences, facts, and mental models |
| [MemOS](https://github.com/MemTensor/MemOS) | Memory operating system | Layered memory, persistence, skills, and adaptive retrieval |
| [Honcho](https://github.com/plastic-labs/honcho) | User and agent modeling | Identity, preferences, relationships, groups, and evolving user models |
| [Mem0](https://github.com/mem0ai/mem0) | Drop-in memory layer | General-purpose persistent memory across agent frameworks |
| [Zep](https://github.com/getzep/zep) | Temporal conversational memory | Conversation and user context with structured temporal retrieval |
| [Supermemory](https://github.com/supermemoryai/supermemory) | Cross-agent memory | Persistent user and agent memory across applications |
| [mxLore](https://github.com/MicrotronX/mxLore) | Coding institutional memory | Architectural decisions, specifications, plans, findings, and lessons through MCP |
| [xbrain](https://github.com/mrboups/xbrain) | Shared human-agent memory | Shared memory plane for people and agents |
| [MemClaw](https://github.com/caura-ai/memclaw) | Multi-agent memory governance | Shared memory and coordination patterns |
| [Recall](https://github.com/joseairosa/recall) | Organizational memory | Persistent knowledge for teams and agents |

### My Ranking

**Best company brain:** GBrain.

GBrain's repository is unusually aligned with the phrase "company brain": it uses a Git-backed Markdown system of record, searchable database indexing, typed graph edges, MCP, citations, synthesis, gap analysis, and scope-aware access. The repository claims a company-brain mode in which users see only authorized slices of shared knowledge. Those are strong architectural ideas, but the access-control and benchmark claims should be independently audited before production use.

**Best enterprise knowledge layer:** Onyx.

**Best context substrate:** OpenViking.

OpenViking treats memories, resources, and skills as one virtual filesystem using `viking://`, with hierarchical browsing, L0 abstracts, L1 overviews, L2 details, on-demand loading, and retrieval trajectories. The project is active and technically ambitious, but its main project is AGPLv3, so licensing must be reviewed before embedding it in a proprietary SaaS product.

**Best temporal memory layer:** Graphiti.

**Best reflective memory layer:** Hindsight.

### Recommended Company-Brain Data Model

```yaml
id: incident-abdm-2026-0042
tenant: hospital_a
entity_type: integration_incident
system: abdm
vendor: vendor_x
source_uri: jira://hospital-a/8841
source_hash: sha256:...
created_at: 2026-07-12T10:20:00+05:30
updated_at: 2026-08-10T15:10:00+05:30
valid_from: 2026-07-12
valid_until:
confidence: verified
sensitivity: internal
review_status: approved
supersedes:
contradicts:
related_entities:
  - vendor_x
  - abdm_gateway
  - hospital_a
```

The agent should never answer only "what does memory say?" It should answer:

1. What happened?
2. Which source proves it?
3. Which tenant or hospital is affected?
4. Is the information current?
5. What contradicts it?
6. What action is authorized?
7. Who must approve that action?

***

## 3. Agent Frameworks and Orchestration

### Stateful and Production-Oriented Frameworks

| Repository | Best Strength |
|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Explicit state machines, checkpoints, interrupts, human approval, and resumable agents |
| [Letta](https://github.com/letta-ai/letta) | Memory-native stateful agents |
| [AgentScope](https://github.com/agentscope-ai/agentscope) | Multi-agent applications and broader runtime ecosystem |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript production agents and workflows |
| [PydanticAI](https://github.com/pydantic/pydantic-ai) | Typed, testable Python agent services |
| [Agno](https://github.com/agno-agi/agno) | Integrated Python agent platform |
| [Microsoft AutoGen](https://github.com/microsoft/autogen) | Event-driven multi-agent collaboration |
| [AG2](https://github.com/ag2ai/ag2) | AutoGen-derived conversational multi-agent systems |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Role-based agents and flows |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Data-connected retrieval agents |
| [Haystack](https://github.com/deepset-ai/haystack) | Explicit retrieval and generation pipelines |
| [DSPy](https://github.com/stanfordnlp/dspy) | Optimizable programmatic LLM systems |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | Microsoft-oriented enterprise integrations |
| [Google ADK](https://github.com/google/adk-python) | Google agent ecosystem |
| [Smolagents](https://github.com/huggingface/smolagents) | Minimal code agents |
| [CAMEL](https://github.com/camel-ai/camel) | Agent societies and research |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | MCP-first composable agents |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Lightweight tools, handoffs, tracing, and guardrails |

### Which Framework Should You Choose?

- Choose **LangGraph** when reliability, checkpoints, interrupts, and explicit state matter.
- Choose **Letta** when persistent memory is the central primitive.
- Choose **PydanticAI** for typed Python business services.
- Choose **Mastra** for a TypeScript-heavy product team.
- Choose **AgentScope** for multi-agent experimentation that may later become a service.
- Choose **CrewAI** when role-based orchestration is more important than deep runtime control.
- Choose **LlamaIndex** or **Haystack** when enterprise data ingestion and retrieval dominate.
- Use **DeerFlow** if you want a complete implementation rather than assembling every primitive yourself.

A common mistake is using a framework's agent loop as the workflow engine. Let the agent reason inside a workflow, but let a durable workflow runtime own retries, timers, compensation, approvals, and recovery.

***

## 4. Autonomous Workflows and Company Operations

### AI-Company and Agent-Operations Repositories

| Repository | What It Provides |
|---|---|
| [OpenOPC](https://github.com/HKUDS/OpenOPC) | AI-company model, task decomposition, organizational memory, self-improvement, and office-like operations |
| [qm](https://github.com/yc-software/qm) | Multiplayer agent workspace with Slack/web interaction, scoped memory, files, permissions, cron, and durable sandboxes |
| [Paperclip](https://github.com/paperclipai/paperclip) | Company-style agent operations and work management |
| [LobeHub](https://github.com/lobehub/lobehub) | Agent hiring, scheduling, reporting, and workspace management |
| [OpenAkita](https://github.com/openakita/openakita) | Integrated AI-company assistant with channels, skills, schedules, memory, and delegation |
| [Agentic OS](https://github.com/modimihir07/agentic-os) | Unified agent dashboard, shared brain folder, scheduler, skills, routing, and cost analytics |
| [AgentField](https://github.com/Agent-Field/agentfield) | Callable agent services, coordination, memory, async execution, and audit trails |
| [AgentScope Runtime](https://github.com/agentscope-ai/agentscope-runtime) | Serving, sandboxing, deployment, APIs, and observability |

These projects are excellent for studying product and control-plane ideas, but do not confuse a compelling "AI company" metaphor with production-grade autonomy. Test isolation, recovery, permissions, auditability, and failure handling.

### Autonomous Coding and Multi-Agent Work

| Repository | Best Use |
|---|---|
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Full autonomous coding environment |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | Research and benchmark-driven software agents |
| [Aider](https://github.com/Aider-AI/aider) | Terminal-based pair programming and repository editing |
| [OpenCode](https://github.com/anomalyco/opencode) | Open-source terminal coding agent |
| [Cline](https://github.com/cline/cline) | IDE-based coding agent |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) | Fork-oriented IDE agent workflows |
| [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) | Computer and code execution |
| [Browser Use](https://github.com/browser-use/browser-use) | Browser task automation |
| [Stagehand](https://github.com/browserbase/stagehand) | Programmable browser agents |
| [Agent S](https://github.com/simular-ai/agent-s) | Computer-use research |
| [Composio Agent Orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | Decompose work, spawn parallel agents, coordinate CI and reviews |
| [Vibe Kanban](https://github.com/BloopAI/vibe-kanban) | Kanban-style multi-agent coordination |
| [Conductor](https://github.com/conductor-oss/conductor) | Parallel agents with isolated Git worktrees |
| [Gastown](https://github.com/steveyegge/gastown) | Multi-agent worker/town model |
| [Claude Squad](https://github.com/smtg-ai/claude-squad) | Multiple terminal agents |
| [Automaker](https://github.com/Auto-Context/automaker) | Autonomous coding workflow application |
| [CLI Agent Orchestrator](https://github.com/awslabs/cli-agent-orchestrator) | Hierarchical terminal-based agent orchestration |
| [GitHub Agentic Workflows](https://github.com/github/gh-aw) | Markdown-authored agent tasks inside GitHub Actions |

The most important distinction:

```text
Coding agent = can modify a repository
Coding orchestrator = can plan, parallelize, review, merge, retry, and report
```

GitHub Agentic Workflows are especially useful for repository-native automation: triage, documentation, pull-request review, CI analysis, and maintenance. They are not a replacement for a general durable agent runtime, but they demonstrate a practical path from natural-language intent to GitHub-native execution.

***

## 5. Protocols, Security, and Runtime Infrastructure

### MCP

| Repository | Role |
|---|---|
| [MCP servers](https://github.com/modelcontextprotocol/servers) | Reference servers for common systems |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Python server/client implementation |
| [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | TypeScript implementation |
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | Debugging and inspection |
| [FastMCP](https://github.com/jlowin/fastmcp) | Fast MCP server development |
| [MCP Registry](https://github.com/modelcontextprotocol/registry) | Server discovery and metadata |
| [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | MCP gateway and federation |
| [Microsoft MCP Gateway](https://github.com/microsoft/mcp-gateway) | Kubernetes-oriented MCP lifecycle and routing |
| [MCP-UI](https://github.com/idosal/mcp-ui) | Interactive MCP-generated interfaces |
| [Supergateway](https://github.com/supercorp-ai/supergateway) | Transport bridging |

### A2A, Gateways, and Registries

| Repository | Role |
|---|---|
| [A2A](https://github.com/a2aproject/A2A) | Agent-to-agent interoperability |
| [ACP](https://github.com/i-am-bee/acp) | Agent communication protocol |
| [Agentgateway](https://github.com/agentgateway/agentgateway) | Agent-to-agent and agent-to-tool security/data plane |
| [Agent Registry](https://github.com/agentoperations/agent-registry) | Registry for agents, MCP servers, and skills |
| [Agent Registry Dev](https://github.com/agentregistry-dev/agentregistry) | Agent artifact registry |

**Agentgateway** is one of the most important infrastructure additions because it centralizes controls that should not be reinvented in every agent. Its repository describes MCP/A2A support, RBAC, multi-tenancy, dynamic configuration, OpenAPI transformation, and Rust-based performance characteristics. It is Apache-2.0 licensed.

### Durable Workflows

| Repository | Best Use |
|---|---|
| [Temporal](https://github.com/temporalio/temporal) | Durable execution, retries, timers, approvals, compensation |
| [Restate](https://github.com/restatedev/restate) | Durable distributed services |
| [Hatchet](https://github.com/hatchet-dev/hatchet) | Agent/background task orchestration |
| [Inngest](https://github.com/inngest/inngest) | Event-driven functions |
| [Prefect](https://github.com/PrefectHQ/prefect) | Python workflows |
| [Kestra](https://github.com/kestra-io/kestra) | Declarative workflows |
| [n8n](https://github.com/n8n-io/n8n) | Visual integrations and AI workflows |
| [Dagster](https://github.com/dagster-io/dagster) | Data and asset workflows |
| [Apache Airflow](https://github.com/apache/airflow) | Scheduled data pipelines |
| [Camunda](https://github.com/camunda/camunda) | BPMN and human-approved business processes |
| [Celery](https://github.com/celery/celery) | Distributed task queues |
| [Dagu](https://github.com/dagu-org/dagu) | YAML-defined workflow scheduling |
| [Windmill](https://github.com/windmill-labs/windmill) | Developer-oriented workflows and scripts |

### Sandboxing and Governance

| Repository | Role |
|---|---|
| [OpenShell](https://github.com/NVIDIA/OpenShell) | Declarative filesystem, network, process, and inference policy |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | General agent sandbox platform |
| [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | Stateful Kubernetes execution |
| [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | Identity, policy, audit, governance, and sandboxing |
| [gVisor](https://github.com/google/gvisor) | Container isolation |
| [Firecracker](https://github.com/firecracker-microvm/firecracker) | MicroVM isolation |
| [Microsandbox](https://github.com/zerocore-ai/microsandbox) | Isolated code execution |
| [nsjail](https://github.com/google/nsjail) | Process sandboxing |
| [bubblewrap](https://github.com/containers/bubblewrap) | Linux sandboxing |
| [Pipelock](https://github.com/lasso-security/pipelock) | MCP-aware egress and data-loss controls |
| [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) | Prompt-injection and code safety |
| [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Conversation and tool rails |
| [Presidio](https://github.com/microsoft/presidio) | PII and PHI detection |
| [SkillSpector](https://github.com/nvidia/skillspector) | Skill supply-chain scanning |
| [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability testing |
| [PyRIT](https://github.com/Azure/PyRIT) | AI red-team testing |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Regression, red-team, and agent evaluation |
| [Invariant](https://github.com/invariantlabs-ai/invariant) | Agent behavior testing |
| [Semgrep](https://github.com/semgrep/semgrep) | Generated-code security analysis |

The minimum safe architecture for an agent that can execute commands is:

```text
Agent
  ↓
Policy engine
  ↓
Gateway
  ├── identity
  ├── authorization
  ├── rate limits
  ├── allowed domains
  └── audit
  ↓
Sandbox
  ├── filesystem scope
  ├── network scope
  ├── process scope
  └── time/resource limits
  ↓
External action
```

A `SKILL.md` instruction is not a security boundary. Prompt instructions can be ignored, tools can be misused, and skills can contain malicious instructions. Put the boundary below the model.

***

## 6. Skills and Agent Supply Chain

| Repository | Role |
|---|---|
| [Agent Skills specification](https://github.com/agentskills/agentskills) | Portable skill format |
| [Anthropic skills](https://github.com/anthropics/skills) | Reference skills |
| [Google skills](https://github.com/google/skills) | Cloud, security, reliability, and cost skills |
| [NVIDIA skills](https://github.com/nvidia/skills) | NVIDIA-related skills |
| [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) | Copilot customizations and skills |
| [Kilo Marketplace](https://github.com/Kilo-Org/kilo-marketplace) | Skills and MCP assets |
| [Agent Operations Registry](https://github.com/agentoperations/agent-registry) | Agent, skill, and MCP metadata |
| [MCP Registry](https://github.com/modelcontextprotocol/registry) | MCP server discovery |
| [Vercel skills](https://github.com/vercel-labs/skills) | Skill discovery and installation |
| [fast-agent](https://github.com/evalstate/fast-agent) | MCP and skill-oriented agent tooling |

A production skill should declare more than a name and description:

```yaml
name:
version:
inputs:
outputs:
allowed_tools:
required_permissions:
allowed_domains:
filesystem_scope:
network_scope:
data_classification:
side_effects:
approval_required:
timeout:
retry_policy:
rollback:
audit_events:
dependencies:
provenance:
signature:
```

Never install arbitrary agent skills directly into a privileged runtime. Scan them, pin versions, require provenance, and run them first in a disposable environment.

***

## 7. Voice, Browser, and Real-World Interfaces

### Voice and Realtime

| Repository | Best Use |
|---|---|
| [Pipecat](https://github.com/pipecat-ai/pipecat) | Flexible voice and multimodal pipelines |
| [LiveKit Agents](https://github.com/livekit/agents) | WebRTC, SIP, telephony, and scale |
| [TEN Framework](https://github.com/TEN-framework/ten-framework) | Voice, vision, avatars, and multimodal agents |
| [Bolna](https://github.com/bolna-ai/bolna) | End-to-end voice orchestration |
| [Vocode](https://github.com/vocodedev/vocode-core) | Voice-agent abstractions |
| [Rasa](https://github.com/RasaHQ/rasa) | Controlled dialogue systems |
| [Asterisk](https://github.com/asterisk/asterisk) | Telephony |
| [FreeSWITCH](https://github.com/signalwire/freeswitch) | Communications/media |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Speech-to-text |

### Browser and Computer Use

- [Browser Use](https://github.com/browser-use/browser-use)
- [Stagehand](https://github.com/browserbase/stagehand)
- [Playwright](https://github.com/microsoft/playwright)
- [Agent S](https://github.com/simular-ai/agent-s)
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)
- [OSWorld](https://github.com/xlang-ai/OSWorld)

***

## 8. Knowledge, Data, and Inference Substrate

### Enterprise RAG and Knowledge Applications

- [Onyx](https://github.com/onyx-dot-app/onyx)
- [RAGFlow](https://github.com/infiniflow/ragflow)
- [Khoj](https://github.com/khoj-ai/khoj)
- [Dify](https://github.com/langgenius/dify)
- [LlamaIndex](https://github.com/run-llama/llama_index)
- [Haystack](https://github.com/deepset-ai/haystack)
- [LightRAG](https://github.com/HKUDS/LightRAG)
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)
- [MindsDB](https://github.com/mindsdb/mindsdb)
- [Langflow](https://github.com/langflow-ai/langflow)

### Storage and Retrieval

- [Postgres](https://github.com/postgres/postgres)
- [pgvector](https://github.com/pgvector/pgvector)
- [Neo4j](https://github.com/neo4j/neo4j)
- [Apache AGE](https://github.com/apache/age)
- [FalkorDB](https://github.com/FalkorDB/FalkorDB)
- [Kùzu](https://github.com/kuzudb/kuzu)
- [Qdrant](https://github.com/qdrant/qdrant)
- [Weaviate](https://github.com/weaviate/weaviate)
- [Milvus](https://github.com/milvus-io/milvus)
- [Vespa](https://github.com/vespa-engine/vespa)
- [LanceDB](https://github.com/lancedb/lancedb)
- [OpenSearch](https://github.com/opensearch-project/OpenSearch)
- [Elasticsearch](https://github.com/elastic/elasticsearch)

### Model Gateways and Serving

- [LiteLLM](https://github.com/BerriAI/litellm)
- [vLLM](https://github.com/vllm-project/vllm)
- [SGLang](https://github.com/sgl-project/sglang)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Ollama](https://github.com/ollama/ollama)
- [Bifrost](https://github.com/maximhq/bifrost)
- [Portkey Gateway](https://github.com/Portkey-AI/gateway)
- [Helicone](https://github.com/Helicone/helicone)
- [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway)
- [OpenLLMetry](https://github.com/traceloop/openllmetry)

***

## 9. Evaluation and Observability

| Repository | What to Measure |
|---|---|
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Agent regression and security |
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM and agent quality |
| [Phoenix](https://github.com/Arize-ai/phoenix) | Traces and evaluation |
| [Langfuse](https://github.com/langfuse/langfuse) | Traces, prompts, datasets, scores |
| [Ragas](https://github.com/explodinggradients/ragas) | RAG quality |
| [τ-bench](https://github.com/sierra-research/tau-bench) | Tool-use policy compliance |
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | Coding agents |
| [BrowserGym](https://github.com/ServiceNow/BrowserGym) | Browser agents |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | Computer-use agents |
| [ToolSandbox](https://github.com/apple/ToolSandbox) | Tool-use behavior |
| [MemoryData](https://github.com/OpenDataBox/MemoryData) | Memory benchmarks |
| [Workspace-Bench](https://github.com/OpenDataBox/Workspace-Bench) | Long-horizon workspace tasks |
| [LongMemEval](https://github.com/xiaowu0162/LongMemEval) | Long-term memory |
| [Agent Memory Paper List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) | Memory research taxonomy |

A company brain should be tested against:

- Cross-tenant data leakage.
- Unauthorized memory writes.
- Stale facts.
- Contradictory sources.
- Incorrect entity resolution.
- Missing citations.
- Incorrect temporal reasoning.
- Permission changes failing to propagate.
- Memory poisoning.
- Skill poisoning.
- Incomplete deletion.
- Wrong source ranking.
- Hallucinated graph relationships.
- Actions taken without approval.

***

## 10. Three Reference Architectures

### A. Governed Enterprise Company Brain

```text
Google Drive / Slack / GitHub / Jira / Notion / Email / EMR
                         ↓
             Onyx connectors and ingestion
                         ↓
       Raw storage + source metadata + permissions
                         ↓
              Cognee and Graphiti enrichment
                         ↓
                OpenViking context hierarchy
                         ↓
              GBrain or AKB reviewed memory
                         ↓
                    Agentgateway
                         ↓
                  MCP and A2A agents
                         ↓
               LangGraph or DeerFlow
                         ↓
                      Temporal
                         ↓
                    OpenShell
                         ↓
              Human approval and audit
```

### B. Autonomous Company Operator

```text
OpenClaw / Hermes / DeerFlow
          ↓
      Agent router
          ↓
Research · Sales · Finance · Legal · Operations · Engineering
          ↓
Permissioned shared company brain
          ↓
MCP/A2A gateway
          ↓
Durable workflows
          ↓
Sandboxed execution
          ↓
Approval, audit, rollback
```

### C. Healthcare SaaS

```text
Onyx
  → permission-aware source retrieval

GBrain/AKB
  → reviewed institutional knowledge

Graphiti
  → temporal vendors, hospitals, incidents, contracts

Cognee
  → entity and relationship construction

OpenViking
  → hierarchical context and skills

LangGraph
  → specialist-agent state

Temporal
  → durable authorization and operations workflows

MCP
  → typed HMS, billing, pharmacy, and business tools

Agentgateway
  → identity, RBAC, routing, telemetry

OpenShell
  → execution isolation

Presidio
  → PHI/PII detection

Langfuse/Phoenix
  → traces, evaluation, and audit
```

***

## My Final Shortlist

### If you want one repository

**DeerFlow** — best broad implementation of a modern long-horizon agent harness.

### If you want a company brain

**GBrain** — strongest Git-backed, graph-aware, cited institutional-memory direction.

### If you want enterprise connectors

**Onyx** — strongest starting point for access-aware company search and agent actions.

### If you want context engineering

**OpenViking** — strongest dedicated context database direction, with hierarchical retrieval and memory/resource/skill unification.

### If you want durable business workflows

**Temporal** — keep agents inside durable, replayable workflows instead of allowing an agent loop to own reliability.

### If you want agents to communicate safely

**MCP + A2A + Agentgateway** — tool access, agent interoperability, authentication, policy, routing, and observability.

### If you want production safety

**OpenShell or OpenSandbox + Agent Governance Toolkit + Presidio + Promptfoo + Langfuse/Phoenix**.

### My Recommended Stack

```text
DeerFlow or LangGraph
  + GBrain or AKB
  + Onyx
  + OpenViking
  + Graphiti
  + Cognee
  + MCP
  + A2A
  + Agentgateway
  + Temporal
  + OpenShell
  + Presidio
  + Promptfoo
  + Langfuse or Phoenix
  + LiteLLM
```

The genuinely important insight is this:

```text
An autonomous agent is not a company operating system.

A company operating system requires:
memory
+ permissions
+ workflow durability
+ protocols
+ sandboxing
+ identity
+ human approval
+ audit
+ evaluation
+ rollback
```

That is the difference between a repository that produces impressive demos and a stack capable of running reliable autonomous business operations.
