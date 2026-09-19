# A defensible, expanded repository atlas

The competing answer is good, but it still has three weaknesses:

1. It treats “company brain” as mainly GBrain + Onyx + OpenViking, while missing newer Git-native knowledgebases, agent-operation systems, registries, and shared-memory projects.
2. It mixes mature infrastructure with early repositories and self-reported claims without a consistent maturity or licensing framework.
3. It lists components but does not show which repositories can be combined into an actual autonomous operating system.

This version separates **complete applications**, **agent harnesses**, **company brains**, **memory engines**, **workflow runtimes**, **protocol gateways**, **skills**, **sandboxing**, **voice**, **evaluation**, and **enterprise data systems**.

A GitHub topic search currently returns thousands of repositories—for example, more than 4,000 under `ai-agents` and more than 2,600 under `agent-memory`—so “all repositories” is not a meaningful quality standard by itself. The useful standard is original implementation, current activity, deployability, architectural significance, license clarity, and evidence of real execution paths. [github](https://github.com/topics/ai-agents)

## Executive shortlist

### Complete autonomous applications

| Rank | Repository | Best description | Maturity view |
|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | Long-horizon super-agent harness | Strong implementation breadth; requires hardening |
| 2 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Self-improving personal/terminal agent | Feature-rich; security must be externally enforced |
| 3 | [OpenClaw](https://github.com/openclaw/openclaw) | Multi-channel personal-agent gateway | Broadest assistant surface; opinionated |
| 4 | [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Autonomous software-engineering environment | Strongest coding-agent product |
| 5 | [Goose](https://github.com/block/goose) | Extensible local developer harness | Strong protocol/extension orientation |
| 6 | [OpenAkita](https://github.com/openakita/openakita) | All-in-one multi-agent assistant/company concept | Broad feature set; verify maturity carefully |
| 7 | [LobeHub](https://github.com/lobehub/lobehub) | Agent workspace and operations layer | Strong product/UI direction |
| 8 | [Khoj](https://github.com/khoj-ai/khoj) | Self-hosted second brain and research agent | Practical personal/team deployment |
| 9 | [Onyx](https://github.com/onyx-dot-app/onyx) | Enterprise search and agent platform | Strong connector and permission orientation |
| 10 | [OpenOPC](https://github.com/HKUDS/OpenOPC) | AI-native company automation concept | Interesting company-automation direction; validate production depth |
| 11 | [Memmy Agent](https://github.com/MemTensor/memmy-agent) | Local agent runtime plus memory hub | Interesting unified runtime/memory model |
| 12 | [Agentic OS](https://github.com/modimihir07/agentic-os) | Local multi-agent control plane | Useful reference architecture; early-stage |

DeerFlow’s own repository presents version 2.0 as a long-horizon super-agent harness with sub-agents, memory, skills, sandboxes, context engineering, scheduled tasks, MCP, browser control, and multiple execution modes. [github](https://github.com/bytedance/deer-flow)

Hermes describes a built-in learning loop, autonomous skill creation, persistent memory, session search, user modeling, scheduled tasks, parallel sub-agents, multi-platform gateways, and several execution backends. [github](https://github.com/NousResearch/hermes-agent)

OpenClaw’s repository exposes a much broader assistant surface: channels, devices, sessions, voice, canvas, browser, cron, nodes, multi-agent routing, skills, and sandboxed sessions. [github](https://github.com/openclaw/openclaw)

OpenAkita explicitly positions itself as an all-in-one multi-agent assistant that can operate a computer, manage files, run scheduled tasks, communicate over several channels, use MCP and skills, and manage memory through an agent dashboard. [github](https://github.com/openakita/openakita)

## How to judge a repository

I would score each project using these dimensions:

| Dimension | Questions |
|---|---|
| Originality | Does it contain an actual runtime or only wrappers/examples? |
| Execution depth | Can it use tools, run processes, browse, edit files, and resume? |
| State | Does it checkpoint, persist sessions, and recover from failure? |
| Memory | Does it support facts, events, skills, and organizational knowledge? |
| Context | Can it selectively load relevant information rather than dump everything into prompts? |
| Autonomy | Can it schedule, delegate, retry, and continue across sessions? |
| Governance | Are permissions, approvals, isolation, audit, and tenancy explicit? |
| Interoperability | Does it support MCP, A2A, OpenAPI, or typed APIs? |
| Deployment | Can it run locally, Docker, Kubernetes, or air-gapped? |
| Maturity | Releases, tests, issue activity, upgrade path, documentation |
| License | Permissive OSS, copyleft, source-available, or unclear? |
| Evidence | Benchmarks reproduced independently or only claimed in README? |

GitHub stars are not enough. A project with 100,000 stars can still be unsuitable for autonomous production execution if it lacks recovery, authorization, sandboxing, and auditability.

# 1. Complete autonomous systems

## DeerFlow

Repository: [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

DeerFlow is the best overall repository for studying a full long-horizon agent harness.

### Implementation areas

- Lead-agent planning.
- Sub-agent delegation.
- `SKILL.md` capability packages.
- Progressive skill loading.
- Memory.
- Context compaction.
- Browser control.
- MCP.
- Database-backed state.
- LangGraph checkpoint storage.
- Local/Docker/Kubernetes sandbox modes.
- Scheduled tasks.
- Messaging channels.
- Artifacts.
- Run-event streams.
- Observability.
- Skill scanning.
- Custom-agent definitions.

The repository’s recent implementation history includes incremental Markdown memory, skill quality gates, browser control, database-backed agents, run-event contracts, and Kubernetes sandbox provisioning. [github](https://github.com/bytedance/deer-flow)

### Best for

- Research agents.
- Coding agents.
- Content-producing agents.
- Long-running business analysts.
- Multi-agent workflows.

### Weakness

DeerFlow’s skill restrictions are behavioral controls, not a hard security boundary. The actual boundary must be OpenShell, OpenSandbox, gVisor, Firecracker, or an equivalent execution layer.

## Hermes Agent

Repository: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

Hermes is the strongest repository for a self-improving personal agent.

### Distinctive features

- Persistent sessions.
- FTS5 session search.
- Agent-curated memory.
- Autonomous skill creation.
- Skill improvement.
- Cron and scheduled tasks.
- Parallel sub-agents.
- MCP.
- Telegram, Discord, Slack, WhatsApp, Signal, and CLI interfaces.
- Voice memo transcription.
- Local, Docker, SSH, Singularity, Modal, and Daytona execution.
- Command approval.
- Multiple model providers.
- User modeling through Honcho.

 [github](https://github.com/NousResearch/hermes-agent)

### Best for

- An autonomous operator.
- Terminal automation.
- Personal research.
- A persistent agent that improves its own procedures.

### Architectural pattern

```text
Task
  ↓
Reason
  ↓
Use tools
  ↓
Observe outcome
  ↓
Store useful experience
  ↓
Create or improve a skill
  ↓
Reuse the skill later
```

That is substantially more ambitious than adding conversation history to an LLM.

## OpenClaw

Repository: [openclaw/openclaw](https://github.com/openclaw/openclaw)

OpenClaw is best understood as a personal-agent operating layer and gateway.

### It provides

- Multi-channel communication.
- Multi-device nodes.
- Gateway control plane.
- Session routing.
- Voice wake and talk mode.
- Canvas.
- Browser.
- Cron.
- Node tools.
- Per-agent workspaces.
- Skills.
- Model routing.
- Multi-agent operation.
- Sandboxed non-main sessions.

 [github](https://github.com/openclaw/openclaw)

### Best for

- A messaging-first assistant.
- An always-on assistant.
- A multi-device operator.
- A gateway in front of several bounded agents.

### Key design

```text
Owner session       → broader privileges
Team/channel session → restricted workspace
Untrusted sender    → pairing/allowlist
Tool execution      → sandbox and policy layer
```

## OpenHands

Repository: [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)

Best open-source autonomous coding environment.

Study it for:

- Repository interaction.
- Shell and browser tools.
- Event streams.
- Agent actions.
- Execution environments.
- Human intervention.
- Coding benchmarks.
- Task state.

## Goose

Repository: [block/goose](https://github.com/block/goose)

Best developer-agent harness for studying:

- Local execution.
- MCP extension points.
- Reusable recipes.
- Provider neutrality.
- Terminal workflows.
- Tool-driven development.

## OpenAkita

Repository: [openakita/openakita](https://github.com/openakita/openakita)

OpenAkita deserves inclusion because it explicitly combines:

- Multiple cooperating agents.
- AI-company metaphor.
- Web search.
- Computer operation.
- File management.
- Scheduled tasks.
- Telegram, Feishu, WeCom, DingTalk, and QQ.
- Agent dashboard.
- Skill marketplace.
- MCP management.
- Memory review.
- Scheduler.
- Delegation.

 [github](https://github.com/openakita/openakita)

It may be especially useful as a reference for an integrated assistant product, but I would not rank it above DeerFlow/Hermes/OpenClaw without independently testing:

- Recovery.
- Security.
- Multi-tenant isolation.
- Tool authorization.
- Upgrade stability.
- Long-running task reliability.

## LobeHub

Repository: [lobehub/lobehub](https://github.com/lobehub/lobehub)

LobeHub is moving toward an agent-operations product. Its repository describes a “Chief Agent Operator” that organizes agents into continuous operations by hiring, scheduling, and reporting. [github](https://github.com/lobehub/lobehub/blob/canary/README.md)

Best for:

- Agent workspace.
- Human-facing operations.
- Agent teams.
- Skills and knowledge.
- Scheduling and reporting.
- Visual administration.

## Khoj

Repository: [khoj-ai/khoj](https://github.com/khoj-ai/khoj)

Khoj is one of the strongest ready-to-use second-brain applications:

- Self-hosted.
- Web and document search.
- Local/online models.
- Custom agents.
- Custom knowledge.
- Scheduled automation.
- Deep research.
- Personas and tools.

 [github](https://github.com/khoj-ai/khoj)

## Onyx

Repository: [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx)

Onyx is better classified as an open-source enterprise knowledge and agent platform than as a memory library.

It provides:

- More than 50 connector patterns.
- MCP-based connectors.
- Access-aware enterprise search.
- Agentic RAG.
- Deep research.
- Custom agents.
- Actions.
- Code/file tools.
- Human and agent CLI access.

 [github](https://github.com/onyx-dot-app/onyx)

# 2. Company brain and organizational memory

## The company-brain taxonomy

| Type | Core question | Best projects |
|---|---|---|
| Enterprise search | Can the agent find the right company data? | Onyx, RAGFlow |
| Git-native brain | Can knowledge be reviewed, versioned, and audited? | GBrain, AKB, TeamBrain |
| Context database | Can the agent navigate memory, resources, and skills? | OpenViking |
| Knowledge graph | Can the system understand relationships? | Cognee, Graphiti, Neo4j |
| Reflective memory | Can the agent learn from outcomes? | Hindsight, MemOS |
| Identity memory | Can it model people, groups, and agents? | Honcho |
| Shared agent memory | Can multiple agents share memory safely? | MemClaw, xbrain, Memmy |
| Company automation | Can agents run company functions? | OpenOPC, qm, OpenAkita |
| Knowledge workspace | Can humans curate and use the brain? | Khoj, LobeHub, AFFiNE, Outline |
| Knowledge format | Can knowledge move between vendors? | Open Knowledge Format, Agent Skills |

## Rank 1 — GBrain

Repository: [garrytan/gbrain](https://github.com/garrytan/gbrain)

GBrain is the most directly aligned with “company brain.”

### Core model

- Brain = database.
- Source = repository mounted into that brain.
- Workspace = agent configuration, skills, memory, and schedules.
- Human/team access = OAuth-scoped.
- Agent access = MCP.
- System of record = Git-backed Markdown.
- Search = hybrid retrieval.
- Relationships = typed graph.
- Output = synthesis with sources, relationships, and gaps.

Its company-brain tutorial describes separate shared, customer, and internal repositories mounted into a brain and served through an HTTP MCP endpoint with per-user access. [github](https://github.com/garrytan/gbrain/blob/master/docs/tutorials/company-brain.md)

The repository claims multi-user/federated company-brain deployment, OAuth scoping, more than 30 MCP tools, typed graph traversal, synthesis, gap analysis, and separate personal/team/company scopes. [github](https://github.com/garrytan/gbrain)

### GBrain’s strongest idea

```text
Workspace repo
  → agent configuration, skills, memory, schedules

Brain repo
  → knowledge pages, people, meetings, projects, decisions

Shared sources
  → internal docs, customer repos, wiki, contracts

MCP server
  → permission-aware agent access
```

This separation is valuable. It prevents agent configuration and institutional knowledge from becoming one uncontrolled folder.

### Best for

- Vendor intelligence.
- Company and people knowledge.
- Meeting and decision memory.
- Product strategy.
- Competitive intelligence.
- Healthcare implementation knowledge.
- Cross-agent institutional memory.

### Limitations

- Opinionated around Git/Markdown and its own agent ecosystem.
- README claims need independent benchmarking.
- Git is not a transactional database.
- Clinical truth must remain in the HMS/EMR source of truth.
- Multi-user authorization needs adversarial testing.

## Rank 2 — Onyx

Repository: [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx)

Onyx is the best option when the company brain starts with enterprise connectors and permissions.

### Best for

- Company-wide search.
- Internal support.
- HR/engineering/sales knowledge.
- Enterprise documents.
- Permission-aware retrieval.
- Deep research.
- Custom agents with actions.

### Difference from GBrain

| GBrain | Onyx |
|---|---|
| Institutional memory and synthesis | Enterprise search and retrieval |
| Git/Markdown system of record | Connector/indexing system |
| Typed graph and gap analysis | Access-aware data plane |
| Agent-authored knowledge | Company data discovery |
| Personal/team/company brain hierarchy | Enterprise data integration |

Use Onyx when the problem is “find and reason over all our systems.” Use GBrain when the problem is “build a governed, evolving, explainable company memory.”

## Rank 3 — OpenViking

Repository: [volcengine/OpenViking](https://github.com/volcengine/OpenViking)

OpenViking is the best context substrate.

It unifies:

- Memories.
- Resources.
- Skills.
- Knowledge.

as a hierarchical virtual filesystem using `viking://`. [github](https://github.com/volcengine/OpenViking)

### Context model

```text
viking://company/
├── departments/
├── projects/
├── people/
├── systems/
├── policies/
├── skills/
└── memories/
```

Instead of sending an entire document corpus to the model:

```text
1. Browse coarse context.
2. Identify relevant branches.
3. Load an overview.
4. Retrieve detailed files only when needed.
5. Record the retrieval trajectory.
```

### Why it is important

This is context engineering as infrastructure, not prompt decoration.

### License

The main project is AGPLv3, so proprietary SaaS embedding requires careful legal review. [github](https://github.com/volcengine/OpenViking)

## Rank 4 — Cognee

Repository: [topoteretes/cognee](https://github.com/topoteretes/cognee)

Cognee is the strongest candidate for transforming a company’s unstructured information into a connected knowledge graph.

Best for:

- Organization-wide knowledge.
- Graph + vector retrieval.
- Shared agent memory.
- Entity and relationship extraction.
- Cross-agent knowledge.
- Continuous ingestion.

## Rank 5 — Graphiti

Repository: [getzep/graphiti](https://github.com/getzep/graphiti)

Graphiti is strongest for temporal organizational knowledge:

```text
Vendor X owned issue Y
from July 4 to July 21,
until Vendor Z took over.
```

That temporal structure is critical for:

- Vendor histories.
- Contract changes.
- Policy versions.
- Staffing changes.
- Implementation timelines.
- Incident ownership.

## Rank 6 — Hindsight

Repository: [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

Hindsight is a reflective memory engine with:

- Retain.
- Recall.
- Reflect.
- Facts.
- Experiences.
- Mental models.
- Preference-conditioned reasoning.

 [arxiv](https://arxiv.org/html/2512.12818v1)

It is useful when the company brain must remember not only “what was written” but also “what happened after the decision.”

## Rank 7 — MemOS

Repository: [MemTensor/MemOS](https://github.com/MemTensor/MemOS)

MemOS presents a memory-operating-system direction with layered memory, dynamic retrieval, persistence, skill memory, and adaptive updates. [linkedin](https://www.linkedin.com/posts/sumanth077_memory-operating-system-for-ai-agents-memos-activity-7419359497284087808-heFj)

## Rank 8 — Honcho

Repository: [plastic-labs/honcho](https://github.com/plastic-labs/honcho)

Best for:

- User modeling.
- Group/project identity.
- Agent identity.
- Evolving relationships.
- Cross-session personalization.

## Rank 9 — AKB

Repository: [dnotitia/akb](https://github.com/dnotitia/akb)

AKB—Agent Knowledgebase—is a newly relevant Git-backed organizational-memory project. Its description is unusually direct:

- Organizational memory for AI agents.
- Git-backed knowledge base.
- MCP interface.
- Agents can read and write.
- Hybrid retrieval.

 [github](https://github.com/dnotitia/akb)

This is a genuine company-brain candidate, not merely a personal notes application.

### Why AKB matters

It may represent a simpler alternative to GBrain:

```text
Git repository
  ↓
Knowledgebase service
  ↓
Hybrid search
  ↓
MCP read/write
```

### Maturity classification

I would classify AKB as **emerging**, because the repository is recent. It deserves testing, but not automatic production adoption.

## Rank 10 — TeamBrain

TeamBrain’s reported architecture is compelling:

- Markdown memories.
- YAML frontmatter.
- Git history.
- Pull-request approval.
- Shared team knowledge.
- Reproducible claims.
- Typed consent gates.

 [linkedin](https://www.linkedin.com/posts/donatien-migue_github-donatienmigueteambrain-the-brain-activity-7487458565029298176-06Yg)

This is an excellent governance pattern for organizational memory:

```text
Agent proposes
  ↓
PR generated
  ↓
Reviewer validates
  ↓
Merge
  ↓
Shared brain updated
```

Treat it as an architectural pattern until the repository’s code, release history, license, and maintenance are independently validated.

## Rank 11 — GBrain alternatives and shared-memory projects

| Repository | Role |
|---|---|
| [xbrain](https://github.com/mrboups/xbrain) | A shared memory plane for humans and agents |
| [MemClaw](https://github.com/caura-ai/memclaw) | Multi-agent memory governance patterns |
| [Recall](https://github.com/joseairosa/recall) | Persistent and organizational shared memory |
| [Memora](https://github.com/agentic-box/memora) | MCP memory with structured, semantic, graph, and source-backed context |
| [Memori MCP](https://github.com/MemoriLabs/memori-mcp) | Persistent memory through MCP |
| [mxLore](https://github.com/MicrotronX/mxLore) | Institutional memory for coding agents with 45 MCP tools |
| [In-Memoria](https://github.com/pi22by7/In-Memoria) | Codebase memory and cross-session pattern learning |
| [agentmemory](https://github.com/rohitg00/agentmemory) | Memory for coding-agent pipelines |
| [Mem0](https://github.com/mem0ai/mem0) | General drop-in memory layer |
| [Zep](https://github.com/getzep/zep) | Conversational/context memory |
| [Supermemory](https://github.com/supermemoryai/supermemory) | Cross-agent persistent memory |

`mxLore` is specifically aimed at architectural decisions, specs, plans, findings, and lessons learned through MCP and provides an institutional-memory model for coding agents. [github](https://github.com/MicrotronX/mxLore)

# 3. AI-company and agent-operations systems

These are distinct from memory databases. They try to coordinate agents as an operating team.

## Rank 1 — OpenOPC

Repository: [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)

OpenOPC describes itself as a self-growing, AI-native company that learns from every task and builds organizational memory. [github](https://github.com/HKUDS/OpenOPC)

### Relevant ideas

- Agents as company workers.
- Task decomposition.
- Organizational memory.
- Self-improvement.
- Office-style applications.
- CLI/UI.
- Feishu and WeChat integrations.

### Best use

Study it for the “AI company” product model, but verify:

- Worker isolation.
- Long-running task recovery.
- Authorization.
- Audit.
- Tool security.
- Actual business-process coverage.

## Rank 2 — qm

Repository: [yc-software/qm](https://github.com/yc-software/qm)

qm describes itself as a multiplayer agent harness for work, operating in Slack and on the web. Its description includes:

- Company-brain retrieval.
- Internal app creation.
- Publishing apps to the right people.
- Scoped memory.
- Files.
- Keychain views.
- Permissions.
- Cron.
- Durable sandboxes.
- Provider/harness interchangeability.

 [github](https://github.com/yc-software/qm)

This is highly relevant to the “company operating system” idea because it treats rooms, people, memory, files, permissions, and durable sandboxes as one work environment.

## Rank 3 — LobeHub

Repository: [lobehub/lobehub](https://github.com/lobehub/lobehub)

LobeHub is the strongest human-facing agent operations workspace. It frames itself as a “Chief Agent Operator” that hires, schedules, and reports on an AI team. [github](https://github.com/lobehub/lobehub/blob/canary/README.md)

## Rank 4 — OpenAkita

[OpenAkita](https://github.com/openakita/openakita) is an all-in-one implementation of the AI-company metaphor: multiple agents, dashboard, skills, scheduling, memory, channels, computer operation, and MCP. [github](https://github.com/openakita/openakita)

## Rank 5 — Agentic OS

Repository: [modimihir07/agentic-os](https://github.com/modimihir07/agentic-os)

Agentic OS combines:

- Multiple agent CLIs.
- Unified dashboard.
- Shared brain folder.
- SQLite FTS5 memory.
- Cron scheduler.
- Skill hub.
- Cost analytics.
- Task routing.

 [modimihir07.github](https://modimihir07.github.io/agentic-os/)

This is useful for studying how to wrap existing agents into one control plane, although it appears more like a reference implementation than a mature infrastructure platform.

## Rank 6 — AgentField

Repository: [Agent-Field/agentfield](https://github.com/Agent-Field/agentfield)

AgentField is aimed at making agents callable as services, with:

- Routing.
- Coordination.
- Memory.
- Asynchronous execution.
- Cryptographic audit trails.

 [github](https://github.com/aloth/awesome-ai-agents)

## Rank 7 — AgentScope Runtime

Repository: [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)

AgentScope Runtime is relevant when AI-company agents need to become deployable services rather than local scripts:

- Secure sandboxing.
- Durable serving.
- Agent APIs.
- Scalable deployment.
- Observability.

 [github](https://github.com/orgs/agentscope-ai/repositories)

# 4. Agent frameworks

## Recommended ranking

| Rank | Repository | Actual strength |
|---|---|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | Explicit stateful workflows and interrupts |
| 2 | [Letta](https://github.com/letta-ai/letta) | Memory-native stateful agents |
| 3 | [AgentScope](https://github.com/agentscope-ai/agentscope) | Multi-agent and runtime ecosystem |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | TypeScript production applications |
| 5 | [Agno](https://github.com/agno-agi/agno) | Integrated Python agent platform |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | Typed, testable Python services |
| 7 | [AutoGen](https://github.com/microsoft/autogen) | Event-driven multi-agent systems |
| 8 | [CrewAI](https://github.com/crewAIInc/crewAI) | Role-based crews and flows |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | Data and retrieval agents |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | Explicit retrieval/generation pipelines |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | Optimizable programmatic LLM systems |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | Enterprise Microsoft ecosystem |
| 13 | [Google ADK](https://github.com/google/adk-python) | Google agent ecosystem |
| 14 | [Smolagents](https://github.com/huggingface/smolagents) | Minimal code agents |
| 15 | [CAMEL](https://github.com/camel-ai/camel) | Agent societies and research |
| 16 | [PraisonAI](https://github.com/MervinPraison/PraisonAI) | Multi-agent app orchestration |
| 17 | [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | MCP-first composable agents |
| 18 | [AG2](https://github.com/ag2ai/ag2) | AutoGen-derived conversational agents |
| 19 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Lightweight tools/handoffs/guardrails |
| 20 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Microsoft-supported multi-language agents |

Microsoft’s Agent Framework documentation describes agent and multi-agent workflow support across .NET, Python, and Go, but the Go implementation is still marked public preview and some capabilities are not yet available. [learn.microsoft](https://learn.microsoft.com/en-us/agent-framework/overview/)

# 5. Autonomous coding and work orchestration

## Complete coding environments

- [OpenHands](https://github.com/All-Hands-AI/OpenHands).
- [Goose](https://github.com/block/goose).
- [SWE-agent](https://github.com/SWE-agent/SWE-agent).
- [Aider](https://github.com/Aider-AI/aider).
- [OpenCode](https://github.com/anomalyco/opencode).
- [Cline](https://github.com/cline/cline).
- [Roo Code](https://github.com/RooCodeInc/Roo-Code).
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter).
- [Agent S](https://github.com/simular-ai/agent-s).
- [Devika](https://github.com/stitionai/devika).

## Multi-agent coding orchestrators

| Repository | Best contribution |
|---|---|
| [Composio Agent Orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | Plans tasks, spawns parallel agents, handles CI, merge conflicts, and reviews |
| [Vibe Kanban](https://github.com/BloopAI/vibe-kanban) | Kanban-style multi-agent task coordination |
| [Conductor](https://github.com/conductor-oss/conductor) | Parallel agents in isolated Git worktrees |
| [Gastown](https://github.com/steveyegge/gastown) | Multi-agent coding-town/worker model |
| [Claude Squad](https://github.com/smtg-ai/claude-squad) | Terminal orchestration for multiple agents |
| [Automaker](https://github.com/Auto-Context/automaker) | Autonomous coding workflow application |
| [CLI Agent Orchestrator](https://github.com/awslabs/cli-agent-orchestrator) | Hierarchical multi-agent orchestration over terminal sessions |
| [Agentic OS](https://github.com/modimihir07/agentic-os) | Unified dashboard over multiple coding/research agents |
| [GitHub Agentic Workflows](https://github.com/github/gh-aw) | Markdown-authored agent workflows inside GitHub Actions |
| [Paperclip](https://github.com/paperclipai/paperclip) | Company-style autonomous agent operations and work management |

Composio’s official announcement describes Agent Orchestrator as an open-source system where an agent decomposes a feature, assigns tasks to coding agents, and manages parallel execution. [composio](https://composio.dev/blog/the-self-improving-ai-system-that-built-itself)

GitHub Agentic Workflows are a major addition to this category: Markdown files describe desired repository behavior, `gh aw` compiles them into GitHub Actions, and an agent executes tasks such as triage, documentation, pull-request review, CI analysis, and repository maintenance. [github](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/)

This is not a general autonomous-agent runtime. It is a very practical **repository-level agent automation system**.

# 6. Skills ecosystem

## Standards and registries

| Repository | Role |
|---|---|
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Open Agent Skills specification |
| [anthropics/skills](https://github.com/anthropics/skills) | Reference skills repository |
| [google/skills](https://github.com/google/skills) | Google Cloud skills |
| [nvidia/skills](https://github.com/nvidia/skills) | NVIDIA product skills |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | GitHub/Copilot skills and customizations |
| [Kilo Marketplace](https://github.com/Kilo-Org/kilo-marketplace) | Skills, MCP servers, and modes |
| [agentoperations/agent-registry](https://github.com/agentoperations/agent-registry) | Vendor-neutral agents, skills, and MCP registry |
| [agentregistry-dev/agentregistry](https://github.com/agentregistry-dev/agentregistry) | Agent artifact registry |
| [MCP Registry](https://github.com/modelcontextprotocol/registry) | MCP server registry |
| [fast-agent](https://github.com/evalstate/fast-agent) | Skill installation/registry support |
| [skills.sh](https://github.com/vercel-labs/skills) | Agent-skill discovery and installation tooling |

The Agent Skills specification describes skills as portable folders containing specialized knowledge and workflows. [github](https://github.com/agentskills/agentskills)

GitHub’s `gh skill` command is designed to discover, install, manage, and publish skills across multiple agent hosts, including Copilot, Claude Code, Cursor, Codex, and Gemini CLI. [github](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/)

Google’s official skills repository includes cloud skills and Well-Architected security, reliability, and cost-optimization skills. [cloud.google](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository)

### Skill security

The skill supply chain is a serious risk. NVIDIA’s SkillSpector scans repositories, URLs, archives, directories, and files for prompt injection, data exfiltration, privilege escalation, malicious code, MCP tool poisoning, and other risks. [github](https://github.com/nvidia/skillspector)

OWASP’s Agentic Skills project identifies SkillSpector as an Apache-2.0 skill-aware scanner. [owasp](https://owasp.org/www-project-agentic-skills-top-10/skill-scanner-integration)

A 2026 Snyk study reported security flaws in a substantial fraction of publicly available agent skills; treat skill marketplaces as untrusted package registries until scanned and reviewed. [snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)

## Production skill contract

```yaml
name:
version:
description:
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

# 7. Protocols, gateways, and registries

## MCP

Core repositories:

- [MCP servers](https://github.com/modelcontextprotocol/servers).
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk).
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector).
- [FastMCP](https://github.com/jlowin/fastmcp).
- [MCP Registry](https://github.com/modelcontextprotocol/registry).
- [MCP Context Forge](https://github.com/IBM/mcp-context-forge).
- [Microsoft MCP Gateway](https://github.com/microsoft/mcp-gateway).
- [MCP-UI](https://github.com/idosal/mcp-ui).
- [Supergateway](https://github.com/supercorp-ai/supergateway).
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent).

## A2A and ACP

- [A2A](https://github.com/a2aproject/A2A).
- [ACP](https://github.com/i-am-bee/acp).
- [AgentField](https://github.com/Agent-Field/agentfield).
- [AgentScope](https://github.com/agentscope-ai/agentscope).

## Agentgateway

Repository: [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway)

Agentgateway is not just an MCP proxy. It is an open-source agent connectivity data plane covering:

- MCP.
- A2A.
- LLM traffic.
- Authentication.
- Authorization.
- RBAC.
- Rate limiting.
- TLS.
- Retries.
- OpenTelemetry.
- Multi-tenancy.
- Tool federation.
- OpenAPI-to-tool exposure.

The project is hosted under the Linux Foundation and is designed as an agent-native proxy for agent-to-agent, agent-to-tool, and agent-to-LLM communication. [agentgateway](https://agentgateway.dev/docs/kubernetes/main/)

This is one of the most important additions to a production architecture because the gateway centralizes controls that should not be duplicated in every agent:

```text
Agents
  ↓
Agentgateway
  ├── auth
  ├── authorization
  ├── tool routing
  ├── A2A routing
  ├── rate limits
  ├── tracing
  └── policy
  ↓
MCP servers / A2A agents / LLM providers
```

## MCP Gateway

Repository: [microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway)

Microsoft MCP Gateway is focused on lifecycle management and scalable, session-aware MCP-server routing in Kubernetes. [github](https://github.com/microsoft/mcp-gateway)

## Agent registry

Repository: [agentoperations/agent-registry](https://github.com/agentoperations/agent-registry)

Agent Registry is vendor-neutral and framework-agnostic, using:

- A2A Agent Cards for agents.
- MCP metadata for servers.
- Agent Skills metadata for skills.
- OCI registry concepts.

 [github](https://github.com/agentoperations/agent-registry)

# 8. Voice and realtime agents

| Rank | Repository | Best use |
|---|---|---|
| 1 | [Pipecat](https://github.com/pipecat-ai/pipecat) | Flexible voice/multimodal pipeline |
| 2 | [LiveKit Agents](https://github.com/livekit/agents) | WebRTC, SIP, telephony, scale |
| 3 | [TEN Framework](https://github.com/TEN-framework/ten-framework) | Voice, vision, avatar, multimodal |
| 4 | [Bolna](https://github.com/bolna-ai/bolna) | End-to-end voice-agent orchestration |
| 5 | [Vocode](https://github.com/vocodedev/vocode-core) | Voice-agent abstractions |
| 6 | [Rasa](https://github.com/RasaHQ/rasa) | Controlled dialogue |
| 7 | [Nemotron Voice Agent](https://github.com/NVIDIA-AI-Blueprints/nemotron-voice-agent) | End-to-end NVIDIA blueprint |
| 8 | [Asterisk](https://github.com/asterisk/asterisk) | Telephony |
| 9 | [FreeSWITCH](https://github.com/signalwire/freeswitch) | Communications/media |
| 10 | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | STT |

Pipecat’s repository supports single-agent and multi-agent voice systems, specialist handoffs, and parallel coordination. [github](https://github.com/pipecat-ai/pipecat)

# 9. Durable workflows and scheduling

| Rank | Repository | Strength |
|---|---|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | Durable execution, retries, timers, approvals, compensation |
| 2 | [Restate](https://github.com/restatedev/restate) | Durable distributed services |
| 3 | [Hatchet](https://github.com/hatchet-dev/hatchet) | Distributed agent/background tasks |
| 4 | [Inngest](https://github.com/inngest/inngest) | Event-driven functions |
| 5 | [Prefect](https://github.com/PrefectHQ/prefect) | Python workflows |
| 6 | [Kestra](https://github.com/kestra-io/kestra) | Declarative workflows |
| 7 | [n8n](https://github.com/n8n-io/n8n) | Visual integrations |
| 8 | [Dagster](https://github.com/dagster-io/dagster) | Data/asset workflows |
| 9 | [Airflow](https://github.com/apache/airflow) | Scheduled pipelines |
| 10 | [Camunda](https://github.com/camunda/camunda) | BPMN, business process, human approvals |
| 11 | [Celery](https://github.com/celery/celery) | Distributed task queues |
| 12 | [Dagu](https://github.com/dagu-org/dagu) | YAML workflow scheduling |
| 13 | [Windmill](https://github.com/windmill-labs/windmill) | Developer-oriented workflows and scripts |

Temporal should own a hospital process such as:

```text
Prior authorization
  ↓
Collect documents
  ↓
Classify missing information
  ↓
Request human approval
  ↓
Submit
  ↓
Poll insurer
  ↓
Escalate on timeout
  ↓
Record outcome
```

The agent can reason inside the workflow. It should not own the workflow’s durability.

# 10. Sandboxing, execution, and runtime governance

## Ranking

| Rank | Repository | Scope |
|---|---|---|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | Agent runtime policy for files, network, processes, inference |
| 2 | [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | Identity, policies, sandboxing, audit, governance |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | General sandbox platform |
| 4 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | Stateful Kubernetes execution |
| 5 | [Agentgateway](https://github.com/agentgateway/agentgateway) | Protocol/data-plane governance |
| 6 | [Pipelock](https://github.com/lasso-security/pipelock) | MCP-aware egress and DLP |
| 7 | [AgentWall](https://github.com/agentwall/Agentwall) | Local-agent safety and observability |
| 8 | [gVisor](https://github.com/google/gvisor) | Container isolation |
| 9 | [Firecracker](https://github.com/firecracker-microvm/firecracker) | MicroVM isolation |
| 10 | [Microsandbox](https://github.com/zerocore-ai/microsandbox) | Isolated code execution |
| 11 | [nsjail](https://github.com/google/nsjail) | Process sandbox |
| 12 | [bubblewrap](https://github.com/containers/bubblewrap) | Linux sandbox |

OpenShell describes declarative policies for filesystem, network, process, and inference control. [github](https://github.com/NVIDIA/OpenShell)

Agentgateway provides centralized protocol traffic controls, including RBAC, authorization, retries, rate limits, and telemetry. [agentgateway](https://agentgateway.dev/docs/kubernetes/main/)

AgentWall is described as an open-source runtime safety and observability layer for local agents. [arxiv](https://arxiv.org/html/2605.16265v1)

# 11. Guardrails and security testing

| Rank | Repository | Best role |
|---|---|---|
| 1 | [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | Runtime governance |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | Execution boundary |
| 3 | [Agentgateway](https://github.com/agentgateway/agentgateway) | Protocol gateway and authorization |
| 4 | [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) | Injection/alignment/code security |
| 5 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Dialogue and tool rails |
| 6 | [Pipelock](https://github.com/lasso-security/pipelock) | Egress/DLP/MCP firewall |
| 7 | [Guardrails AI](https://github.com/guardrails-ai/guardrails) | Output/schema validation |
| 8 | [Presidio](https://github.com/microsoft/presidio) | PII/PHI detection |
| 9 | [SkillSpector](https://github.com/nvidia/skillspector) | Skill supply-chain scanning |
| 10 | [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability testing |
| 11 | [PyRIT](https://github.com/Azure/PyRIT) | Red-team testing |
| 12 | [Promptfoo](https://github.com/promptfoo/promptfoo) | Regression and security evaluation |
| 13 | [Invariant](https://github.com/invariantlabs-ai/invariant) | Agent behavior testing |
| 14 | [Semgrep](https://github.com/semgrep/semgrep) | Generated-code analysis |

# 12. Knowledge and enterprise data systems

## Enterprise search and RAG

| Rank | Repository | Use |
|---|---|---|
| 1 | [Onyx](https://github.com/onyx-dot-app/onyx) | Enterprise connectors, permissions, custom agents |
| 2 | [RAGFlow](https://github.com/infiniflow/ragflow) | Deep-document understanding |
| 3 | [Khoj](https://github.com/khoj-ai/khoj) | Self-hosted second brain |
| 4 | [Dify](https://github.com/langgenius/dify) | Self-hosted agent/RAG applications |
| 5 | [LlamaIndex](https://github.com/run-llama/llama_index) | Data connectors and retrieval agents |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | Explicit retrieval pipelines |
| 7 | [LightRAG](https://github.com/HKUDS/LightRAG) | Graph-enhanced RAG |
| 8 | [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | Workspaces and local/private documents |
| 9 | [MindsDB](https://github.com/mindsdb/mindsdb) | Agents over live data |
| 10 | [LobeChat/LobeHub](https://github.com/lobehub/lobehub) | Agent workspace and knowledge UI |

## Data/graph substrates

- [Neo4j](https://github.com/neo4j/neo4j).
- [Apache AGE](https://github.com/apache/age).
- [FalkorDB](https://github.com/FalkorDB/FalkorDB).
- [Kùzu](https://github.com/kuzudb/kuzu).
- [Qdrant](https://github.com/qdrant/qdrant).
- [Weaviate](https://github.com/weaviate/weaviate).
- [Milvus](https://github.com/milvus-io/milvus).
- [Vespa](https://github.com/vespa-engine/vespa).
- [LanceDB](https://github.com/lancedb/lancedb).
- [Postgres + pgvector](https://github.com/pgvector/pgvector).
- [OpenSearch](https://github.com/opensearch-project/OpenSearch).
- [Elasticsearch](https://github.com/elastic/elasticsearch).

For company memory, the best default is often hybrid:

```text
Postgres = authoritative metadata and permissions
Object storage = source files and artifacts
Search index = lexical retrieval
Vector index = semantic retrieval
Graph database = relationships and temporal links
Git = reviewed institutional knowledge
MCP/gateway = controlled agent access
```

# 13. Model gateways and inference infrastructure

This category matters because autonomous agents generate many calls, retries, fallback requests, and tool-related model interactions.

| Rank | Repository | Role |
|---|---|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | Unified model gateway, routing, fallback, budgets |
| 2 | [vLLM](https://github.com/vllm-project/vllm) | High-throughput model serving |
| 3 | [SGLang](https://github.com/sgl-project/sglang) | Efficient structured generation/serving |
| 4 | [llama.cpp](https://github.com/ggerganov/llama.cpp) | Local CPU/GPU model inference |
| 5 | [Ollama](https://github.com/ollama/ollama) | Local model packaging and serving |
| 6 | [Bifrost](https://github.com/maximhq/bifrost) | High-performance LLM gateway |
| 7 | [Portkey](https://github.com/Portkey-AI/gateway) | Provider gateway and reliability layer |
| 8 | [Helicone](https://github.com/Helicone/helicone) | Gateway, logging, cost, caching |
| 9 | [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) | Kubernetes/Envoy LLM gateway |
| 10 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | OpenTelemetry instrumentation |

LiteLLM’s gateway model includes routing, fallbacks, spend tracking, rate limits, caching, and an OpenAI-compatible interface. [litellm](https://www.litellm.ai/)

# 14. Evaluation and observability

## Evaluation

| Rank | Repository | Best for |
|---|---|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | Agent regression and red teaming |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | LLM/agent evaluation |
| 3 | [Phoenix](https://github.com/Arize-ai/phoenix) | Tracing and evaluation |
| 4 | [Langfuse](https://github.com/langfuse/langfuse) | Traces, prompts, datasets, scores |
| 5 | [Ragas](https://github.com/explodinggradients/ragas) | RAG evaluation |
| 6 | [τ-bench](https://github.com/sierra-research/tau-bench) | Tool-use policy compliance |
| 7 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | Coding agents |
| 8 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | Browser agents |
| 9 | [OSWorld](https://github.com/xlang-ai/OSWorld) | Computer-use agents |
| 10 | [ToolSandbox](https://github.com/apple/ToolSandbox) | Tool-use evaluation |
| 11 | [MemoryData](https://github.com/OpenDataBox/MemoryData) | Unified memory benchmarks |
| 12 | [Workspace-Bench](https://github.com/OpenDataBox/Workspace-Bench) | Large workspace/file dependency tasks |
| 13 | [Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) | Memory research taxonomy |
| 14 | [Awesome Long-Horizon Agents](https://github.com/RUC-NLPIR/Awesome-Long-Horizon-Agents) | Long-horizon systems and benchmarks |

MemoryData unifies several memory benchmark families, including MemoryAgentBench, LoCoMo, LongBench, and MemBench, under one execution interface. [github](https://github.com/OpenDataBox/MemoryData)

LongMemEval-V2 specifically evaluates whether memory systems help agents acquire experience and become knowledgeable colleagues in customized environments. [arxiv](https://arxiv.org/html/2605.12493v1)

## Company-brain evaluation

A company brain needs tests for:

- Cross-tenant leakage.
- Stale information.
- Wrong entity resolution.
- Contradictory facts.
- Unauthorized writes.
- Missing citations.
- Incorrect temporal reasoning.
- Bad access filtering.
- Graph hallucinations.
- Memory poisoning.
- Deletion/retention failure.
- Permission changes not propagating.
- Skill poisoning.
- Incorrect source ranking.

Example:

```json
{
  "question": "Which vendor owns the unresolved ABDM issue?",
  "allowed_tenant": "hospital_a",
  "required_sources": [
    "contract",
    "incident_ticket",
    "last_review_meeting"
  ],
  "freshness_days": 30,
  "must_cite": true,
  "must_report_conflict": true,
  "forbidden_tenants": ["hospital_b"]
}
```

# 15. Better reference architectures

## Architecture A — governed company brain

```text
Sources
  ├── Google Drive
  ├── Slack
  ├── GitHub
  ├── Jira
  ├── Notion
  ├── email
  ├── HMS/EMR
  └── contracts
        ↓
Onyx connectors / ingestion workers
        ↓
Raw object storage + source metadata
        ↓
Entity extraction and normalization
        ↓
Graphiti/Cognee
        ↓
OpenViking context hierarchy
        ↓
GBrain/AKB reviewed knowledge layer
        ↓
Agentgateway
        ↓
MCP/A2A agents
        ↓
LangGraph/Letta/DeerFlow
        ↓
Temporal workflows
        ↓
OpenShell sandbox
        ↓
Human approval and external action
```

## Architecture B — autonomous company operator

```text
OpenClaw or Hermes gateway
        ↓
Agent router
        ↓
Specialized workers:
  ├── research
  ├── sales
  ├── finance
  ├── legal
  ├── operations
  ├── engineering
  └── customer success
        ↓
Shared but permissioned company brain
        ↓
Agentgateway
        ↓
MCP/A2A tools and services
        ↓
Temporal
        ↓
Sandbox
        ↓
Approval/audit
```

## Architecture C — healthcare company brain

```text
Company knowledge
  ├── hospitals
  ├── departments
  ├── doctors
  ├── vendors
  ├── contracts
  ├── HMS/EMR
  ├── billing
  ├── pharmacy
  ├── ABDM
  ├── incidents
  ├── regulations
  └── product decisions

Onyx       → source access and permission-aware search
GBrain/AKB  → reviewed institutional memory
Graphiti   → temporal relationships
Cognee     → graph construction and connected context
OpenViking → context/skills/resource hierarchy
Temporal   → durable enrichment and approval workflows
MCP        → typed HMS and business tools
Agentgateway → authentication, authorization, routing, telemetry
OpenShell  → execution boundary
Presidio   → PHI/PII control
Langfuse   → trace and evidence audit
```

# 16. Healthcare memory schema

Do not treat an agent memory table as a clinical source of truth.

Use a source-backed record:

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
consent_scope: hospital_a_operations
review_status: approved
supersedes:
contradicts:
related_entities:
  - vendor_x
  - abdm_gateway
  - hospital_a
```

The agent should answer:

- What happened?
- Which source proves it?
- Which hospital is affected?
- Who owns the issue?
- Is the information current?
- What contract or policy applies?
- What action is authorized?
- Who must approve it?

# 17. Top three by category

| Category | 1 | 2 | 3 |
|---|---|---|---|
| Complete autonomous harness | DeerFlow | Hermes | OpenClaw |
| Autonomous coding | OpenHands | Goose | SWE-agent |
| Agent operations workspace | LobeHub | qm | OpenAkita |
| AI-company runtime | OpenOPC | OpenAkita | qm |
| Agent framework | LangGraph | Letta | AgentScope |
| TypeScript framework | Mastra | LangGraph JS | OpenAI Agents SDK JS |
| Python typed framework | PydanticAI | Agno | Fast-agent |
| Multi-agent collaboration | AgentScope | AutoGen/AG2 | CrewAI |
| Company brain | GBrain | AKB | TeamBrain |
| Enterprise knowledge | Onyx | RAGFlow | Dify |
| Context database | OpenViking | Cognee | Graphiti |
| Reflective memory | Hindsight | MemOS | Letta |
| Drop-in memory | Mem0 | Zep | Supermemory |
| Shared team memory | GBrain | xbrain | Recall |
| Git-native memory | GBrain | AKB | TeamBrain |
| Institutional coding memory | mxLore | codebase-memory-mcp | Mem0 |
| Skills standard | Agent Skills spec | AGENTS.md | Open Knowledge Format |
| Skill registry | agent-registry | MCP Registry | Kilo Marketplace |
| Skill security | SkillSpector | Pipelock | Promptfoo |
| Tool protocol | MCP | FastMCP | MCP Context Forge |
| Agent network | A2A | ACP | Agentgateway |
| Protocol gateway | Agentgateway | Microsoft MCP Gateway | MCP Context Forge |
| Voice pipeline | Pipecat | LiveKit Agents | TEN |
| Voice platform | Bolna | Vocode | Rasa |
| Durable workflows | Temporal | Restate | Hatchet |
| Business process | Camunda | Temporal | n8n |
| Sandbox | OpenShell | OpenSandbox | Kubernetes Agent Sandbox |
| Governance | Agent Governance Toolkit | OpenShell | Agentgateway |
| Agent security | LlamaFirewall | NeMo Guardrails | Pipelock |
| Browser agents | Browser Use | Stagehand | Agent S |
| Model gateway | LiteLLM | Bifrost | Envoy AI Gateway |
| Evaluation | Promptfoo | DeepEval | Phoenix |
| Memory benchmark | MemoryData | LongMemEval | Mem2ActBench |
| Observability | Langfuse | Phoenix | OpenTelemetry |

# Final verdict

## Best repository to study first

**DeerFlow**.

It is the best single repository for understanding how a modern long-horizon agent harness combines:

```text
planning
+ sub-agents
+ skills
+ memory
+ context management
+ sandbox
+ tools
+ MCP
+ browser
+ scheduled work
+ artifacts
+ observability
```

## Best company brain

**GBrain**, if you want Git-backed, graph-aware, cited, multi-user institutional memory.

## Best enterprise knowledge system

**Onyx**, if your central requirement is permission-aware search and agent access across company systems.

## Best context substrate

**OpenViking**, if you need a navigable hierarchy of memories, skills, resources, and knowledge.

## Best AI-company operating layer

**qm**, **OpenOPC**, and **OpenAkita** are the most relevant newer projects to investigate, but they should be treated as emerging systems until their recovery, security, licensing, and operational maturity are independently validated. [github](https://github.com/openakita/openakita)

## Best production architecture

```text
DeerFlow/Hermes/OpenClaw
  + GBrain or AKB
  + Onyx
  + OpenViking
  + Cognee/Graphiti
  + MCP
  + Agentgateway
  + Temporal
  + OpenShell
  + Agent Governance Toolkit
  + Pipecat/LiveKit
  + Promptfoo
  + Langfuse/Phoenix
```

## My recommendation for your healthcare SaaS work

Build a **bounded company brain**, not an unrestricted super-agent:

- **Onyx** for connector-based enterprise search.
- **GBrain or AKB** for reviewed institutional memory.
- **OpenViking** for hierarchical context and skills.
- **Graphiti** for temporal vendor, hospital, incident, and contract relationships.
- **Cognee** for ingestion and knowledge-graph construction.
- **LangGraph** for specialist-agent state.
- **Temporal** for long-running workflows.
- **MCP plus Agentgateway** for governed tools and agent-to-agent communication.
- **OpenShell** for filesystem/network/process isolation.
- **Presidio** for PHI/PII controls.
- **Pipecat/LiveKit** for voice.
- **Promptfoo, MemoryData, Langfuse, and Phoenix** for evaluation and operations.

The key improvement over the supplied answer is the inclusion of the missing operational layers:

```text
AKB and TeamBrain
OpenOPC and qm
OpenAkita and Agentic OS
Agentgateway
Agent Registry
Agent Skills specification
SkillSpector
GitHub Agentic Workflows
Composio Agent Orchestrator
MCP Gateway
MemoryData
Open Knowledge Format
```

These projects cover the gap between “an agent that can call tools” and “a governed company operating system whose agents can remember, collaborate, learn, schedule work, access enterprise systems, and produce auditable outcomes.”
