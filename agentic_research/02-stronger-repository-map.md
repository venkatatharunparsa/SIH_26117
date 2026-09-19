# A stronger repository map

The previous answer missed the most important category you have now identified: **company brain / institutional memory**.

The strongest current open-source ecosystem is not one list of agent frameworks. It is a stack of distinct systems:

```text
Autonomous application
  + agent harness
  + skills
  + context database
  + organizational memory
  + tools/protocols
  + durable workflows
  + sandbox
  + governance
  + evaluation
```

I went back to primary repository material rather than relying on generic comparison articles. The most consequential correction is that **DeerFlow, Hermes, OpenClaw, OpenViking, GBrain, Hindsight, and company-brain projects such as TeamBrain are different classes of systems** and should not be ranked as if they were interchangeable.

## Executive ranking

### Best complete autonomous systems

| Rank | Repository | Category | Why it matters |
|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | Long-horizon agent harness | Sub-agents, memory, skills, sandbox, artifacts, context engineering, messaging, scheduling |
| 2 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Self-improving autonomous assistant | Skills learned from experience, memory, sub-agents, cron, messaging, multiple execution backends |
| 3 | [OpenClaw](https://github.com/openclaw/openclaw) | Personal-agent operating layer | Gateway, multi-channel communication, nodes, voice, tools, routing, sessions |
| 4 | [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Autonomous coding agent | Repository work, browser, shell, environments, event streams, coding evaluation |
| 5 | [Goose](https://github.com/block/goose) | Extensible developer-agent harness | Local execution, recipes, MCP extensions, provider flexibility |
| 6 | [AgentScope Runtime](https://github.com/agentscope-ai/agentscope-runtime) | Agent serving/runtime | Sandbox execution, Agent-as-a-Service, deployment, observability |
| 7 | [LobeHub](https://github.com/lobehub/lobehub) | Agent operations workspace | Agent hiring, scheduling, reporting, knowledge, skills, and continuous operations |
| 8 | [Khoj](https://github.com/khoj-ai/khoj) | AI second brain | Documents, web, custom agents, scheduling, deep research, self-hosting |
| 9 | [Onyx](https://github.com/onyx-dot-app/onyx) | Enterprise knowledge-agent platform | Connectors, access-aware search, RAG, custom agents, actions, MCP, deep research |
| 10 | [GBrain](https://github.com/garrytan/gbrain) | Personal/company brain | Git-backed knowledge, synthesis, typed graph, gap analysis, multi-user access, agent skills |

DeerFlow’s repository confirms that version 2.0 is a ground-up super-agent harness with sub-agents, memory, sandboxes, skills, context engineering, scheduled tasks, MCP, browser control, and multiple execution modes. [github](https://github.com/bytedance/deer-flow)

Hermes is more than a terminal wrapper: its current repository describes a self-improving loop, autonomous skill creation, persistent memory, session search, user modeling, scheduled automations, parallel sub-agents, multi-platform gateways, and multiple terminal backends. [github](https://github.com/NousResearch/hermes-agent)

OpenClaw’s repository describes a local-first gateway for sessions, channels, tools, events, multi-agent routing, voice, nodes, canvas, cron, and sandboxed non-main sessions. [github](https://github.com/openclaw/openclaw)

## The important distinction

### Framework

A library you assemble:

- LangGraph.
- Letta.
- AgentScope.
- Mastra.
- Agno.
- AutoGen.
- CrewAI.

### Harness

A runtime that gives an agent:

- Tools.
- Context.
- Skills.
- Memory.
- Sub-agents.
- Execution.
- Sessions.
- Recovery.
- Permissions.

Examples:

- DeerFlow.
- Hermes.
- OpenClaw.
- OpenHands.
- Goose.

### Company brain

A shared organizational knowledge and memory substrate:

- GBrain.
- Onyx.
- Cognee.
- OpenViking.
- Khoj.
- Graphiti.
- TeamBrain.
- Hindsight.
- MemOS.

### Governance runtime

Controls what an agent can actually do:

- OpenShell.
- Microsoft Agent Governance Toolkit.
- Pipelock.
- NeMo Guardrails.
- LlamaFirewall.

This distinction is the main reason ordinary “top 10 agent framework” articles are inadequate.

# 1. Complete autonomous applications

## 1. DeerFlow — best long-horizon super-agent harness

Repository: [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

DeerFlow is the strongest complete open-source harness for long-running, multi-stage work.

Its current repository contains actual implementation for:

- `.agent/skills`.
- Backend and frontend.
- Run-event contracts.
- Database-backed state.
- Helm deployment.
- Docker and Kubernetes sandbox modes.
- Browser control.
- Incremental memory.
- Skill quality gates.
- LangGraph checkpoint storage.
- MCP.
- Messaging channels.
- Sub-agents.
- Context compaction.
- Scheduled tasks.
- Observability.
- Custom agent definitions.
- Skill scanning.

The repository lists recent implementation work for incremental agent-scoped Markdown memory, skill review quality gates, browser control, run-event streams, database-backed custom agents, and Kubernetes sandbox provisioning. [github](https://github.com/bytedance/deer-flow)

### Strongest features

- **Sub-agent orchestration:** a lead agent can delegate complex work.
- **Skills:** structured `SKILL.md` capability packages.
- **Progressive context:** skills are loaded only when needed.
- **Sandbox modes:** local, Docker, and Kubernetes-backed execution.
- **Memory:** pluggable memory management and incremental Markdown facts.
- **MCP:** HTTP/SSE and stdio integration.
- **Messaging:** Telegram, Slack, Feishu/Lark, WeChat, WeCom, DingTalk, and others.
- **Scheduled tasks:** agents can operate on a schedule.
- **Artifacts:** reports, slides, pages, images, and files.
- **Observability:** LangSmith, Langfuse, and Monocle support.
- **Security hooks:** deterministic skill scanning and allowed-tool policies.

### Why it beats a normal framework

A framework gives you an agent graph. DeerFlow gives you the start of an **agent operating environment**.

### Critical limitation

The repository itself warns that skill-based restrictions are best-effort behavioral scoping rather than a hard security boundary. Production isolation must be provided by the sandbox and external policy layer. [github](https://github.com/bytedance/deer-flow)

## 2. Hermes Agent — best self-improving general assistant

Repository: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

Hermes is the strongest general-purpose autonomous assistant if your priority is a persistent agent that learns from use.

The current repository describes:

- A built-in learning loop.
- Agent-curated memory.
- Autonomous skill creation.
- Skill improvement.
- FTS5 session search.
- Honcho user modeling.
- Cron scheduling.
- Telegram, Discord, Slack, WhatsApp, Signal, and CLI.
- Parallel sub-agents.
- RPC-based tool pipelines.
- Local, Docker, SSH, Singularity, Modal, and Daytona backends.
- Voice memo transcription.
- MCP.
- Command approval.
- Container isolation.
- Provider flexibility.

 [github](https://github.com/NousResearch/hermes-agent)

### Best use

- Personal operator.
- Persistent researcher.
- Autonomous terminal assistant.
- Agent that improves reusable procedures.
- Multi-channel assistant deployed on a VPS.

### Important architectural idea

Hermes treats completed work as training material for future behavior:

```text
Task
  ↓
Tool execution
  ↓
Outcome
  ↓
Memory
  ↓
Skill creation or improvement
  ↓
Better future execution
```

That is materially different from a stateless chatbot with a vector database.

## 3. OpenClaw — best assistant gateway and device layer

Repository: [openclaw/openclaw](https://github.com/openclaw/openclaw)

OpenClaw is the most complete open-source personal-assistant operating layer.

Its current repository lists:

- WhatsApp.
- Telegram.
- Slack.
- Discord.
- Google Chat.
- Signal.
- iMessage.
- IRC.
- Microsoft Teams.
- Matrix.
- Feishu.
- LINE.
- Mattermost.
- Nextcloud Talk.
- Nostr.
- Twitch.
- Zalo.
- WeChat.
- QQ.
- WebChat.
- macOS/iOS/Android nodes.
- Voice wake.
- Talk mode.
- Live Canvas.
- Browser, canvas, node, cron, and session tools.
- Multi-agent routing.
- Per-agent workspaces.
- Skills.

 [github](https://github.com/openclaw/openclaw)

### Best use

- Always-on assistant.
- Messaging-first automation.
- Multi-device agents.
- Voice-enabled personal assistant.
- Gateway for several bounded agents.

### Security finding

OpenClaw’s defaults distinguish between the main session and non-main sessions. Non-main sessions can run in Docker or OpenShell sandboxes, while host execution is possible for the main session. [github](https://github.com/openclaw/openclaw)

That is the correct pattern for a personal agent:

```text
Private owner session: broader privileges
Group/channel session: sandboxed privileges
Untrusted sender: pairing and allowlist
```

## 4. OpenHands and Goose

### OpenHands

[OpenHands](https://github.com/All-Hands-AI/OpenHands) is the best complete open-source software-engineering agent. It should be evaluated for:

- Coding actions.
- Repository state.
- Shell/browser tools.
- Environment isolation.
- Event-based execution.
- Human oversight.
- SWE-bench-style evaluation.

### Goose

[Goose](https://github.com/block/goose) is the best extensible local developer harness. It is especially interesting for:

- MCP extensions.
- Local-first execution.
- Provider-neutral configuration.
- Reusable recipes.
- Tool-driven terminal operation.

# 2. Company brain and institutional memory

This is the category where the previous material was weakest.

A company brain is not merely “RAG over company documents.” A usable company brain needs:

```text
Knowledge ingestion
+ identity
+ permissions
+ provenance
+ temporal history
+ relationships
+ synthesis
+ gap detection
+ human review
+ agent read/write access
+ organizational memory
```

## Rank 1 — GBrain

Repository: [garrytan/gbrain](https://github.com/garrytan/gbrain)

GBrain is the most directly relevant open-source company-brain repository I found.

Its repository describes a brain layer for OpenClaw and Hermes that provides:

- Git-backed Markdown as the system of record.
- PostgreSQL/PGLite retrieval.
- Hybrid search.
- Synthesis.
- Citations.
- Gap analysis.
- A self-wiring typed knowledge graph.
- Multi-user and team-scoped access.
- 30+ MCP tools.
- 43 curated skills.
- Durable sub-agent jobs.
- Scheduled “dream cycle.”
- Schema packs.
- Agent-authored schema evolution.
- Contradiction detection.
- LongMemEval evaluation.
- Source and brain separation.
- Email, calendar, voice, meeting, and Slack-oriented ingestion patterns.

 [github](https://github.com/garrytan/gbrain)

### Why GBrain is different

Most knowledge systems return:

```text
Here are the top 10 retrieved chunks.
```

GBrain aims to return:

```text
An answer
+ source pages
+ connected entities
+ temporal context
+ missing information
+ possible contradictions
```

Its knowledge graph is constructed from Markdown links and typed references without needing an LLM call for every edge. The repository reports typed edges such as:

- `attended`.
- `works_at`.
- `invested_in`.
- `founded`.
- `advises`.
- `mentions`.

 [github](https://github.com/garrytan/gbrain)

### Company-brain architecture

```text
Git brain repository
        ↓
Markdown pages + frontmatter
        ↓
Postgres/PGLite index
        ↓
Hybrid vector + BM25 retrieval
        ↓
Typed graph traversal
        ↓
Synthesis with citations
        ↓
Gap and contradiction analysis
        ↓
MCP access for agents
```

### Why this is highly relevant for healthcare

The model maps naturally to:

- Hospitals.
- Departments.
- Doctors.
- Vendors.
- Contracts.
- Patients.
- Policies.
- Claims.
- Integrations.
- Incidents.
- Projects.
- Compliance obligations.

For example:

```text
vendor: ABC HMS
  ├── integrates_with → ABDM
  ├── deployed_at → Hospital X
  ├── supports → billing module
  ├── issue → claim export failure
  └── contract_renewal → 2027-03-31
```

That is much more useful than a flat vector search result.

### Limitations

- It is opinionated.
- It is heavily oriented toward OpenClaw/Hermes and Markdown/Git workflows.
- You must validate multi-user authorization carefully.
- The README contains strong self-reported benchmark and scale claims; reproduce them independently before relying on them for procurement.
- Git-backed knowledge does not replace a transactional system of record.

## Rank 2 — Onyx

Repository: [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx)

Onyx is the strongest open-source enterprise search and organizational-knowledge platform in this set.

The repository describes:

- 50+ indexing connectors.
- MCP-based connectors.
- Agentic RAG.
- Web search.
- Code execution.
- File creation.
- Deep research.
- Custom agents.
- Actions.
- Enterprise data connections.
- Access-aware search.
- An interactive CLI for humans and agents.

 [github](https://github.com/onyx-dot-app/onyx)

Onyx is described in its repository documentation as an open-source GenAI and enterprise-search platform connecting company documents, apps, and people. [github](https://github.com/onyx-dot-app/onyx/blob/main/AGENTS.md)

### Best use

- Company-wide internal search.
- Permission-aware enterprise knowledge.
- Deep research over internal systems.
- HR, sales, engineering, support, and operations knowledge.
- Agent access to enterprise connectors.

### Why Onyx belongs in a company-brain shortlist

Unlike a personal memory layer, Onyx starts from the organizational data plane:

```text
Google Drive
Slack
GitHub
Notion
Jira
Confluence
Email
Databases
MCP servers
       ↓
Access-aware indexing
       ↓
Enterprise retrieval
       ↓
Agentic RAG
       ↓
Custom agents and actions
```

The major strength is **connector and permission orientation**.

### Limitation

Onyx is primarily an enterprise knowledge and agent application layer. It is not the same as a continuously self-improving personal-agent memory runtime such as Hermes or Letta.

## Rank 3 — OpenViking

Repository: [volcengine/OpenViking](https://github.com/volcengine/OpenViking)

OpenViking is the strongest context database in the company-brain category.

It unifies:

- Memories.
- Resources.
- Skills.
- Knowledge.

under the `viking://` virtual filesystem. It provides:

- Hierarchical browsing.
- L0 abstracts.
- L1 overviews.
- L2 full details.
- On-demand loading.
- Directory-recursive retrieval.
- Retrieval trajectory observability.
- Session-to-memory conversion.
- Agent integrations.

 [github](https://github.com/volcengine/OpenViking)

### Why it matters

A company brain cannot inject the entire company into every agent context. OpenViking offers:

```text
Company
  ├── departments
  ├── teams
  ├── projects
  ├── policies
  ├── people
  ├── systems
  ├── skills
  └── memories
```

The agent navigates from abstract to detailed context as needed.

### Important license finding

OpenViking’s main project is AGPLv3, while some components have different licenses.  This matters if you are embedding it in a proprietary healthcare SaaS product. [github](https://github.com/volcengine/OpenViking)

## Rank 4 — Cognee

Repository: [topoteretes/cognee](https://github.com/topoteretes/cognee)

Cognee is highly relevant for shared organizational memory because it transforms data into connected knowledge structures.

Best for:

- Knowledge graph construction.
- Shared memory.
- Cross-agent context.
- Graph + vector retrieval.
- Knowledge ingestion pipelines.
- Organization-wide knowledge.

It is a better fit than Mem0 when the core problem is not “remember user preferences” but “understand how people, documents, systems, decisions, and events relate.”

## Rank 5 — Khoj

Repository: [khoj-ai/khoj](https://github.com/khoj-ai/khoj)

Khoj is one of the best ready-to-use open-source “second brain” applications.

The repository describes:

- Self-hosting.
- Web and document answers.
- Local and hosted LLMs.
- Custom agents.
- Custom knowledge.
- Personas.
- Tools.
- Scheduled automation.
- Deep research.
- Semantic search.
- Personal-to-enterprise scaling.

 [github](https://github.com/khoj-ai/khoj)

### Best use

- Personal knowledge assistant.
- Research team knowledge base.
- Document and web research.
- Scheduled reports.
- Private knowledge assistant.

## Rank 6 — Hindsight

Repository: [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

Hindsight is a memory architecture rather than a general company portal. It focuses on:

- Retain.
- Recall.
- Reflect.
- Facts.
- Experiences.
- Mental models.
- Preference-conditioned reasoning.
- Long-term memory evaluation.

The repository and associated paper describe the full memory architecture and benchmark tooling. [arxiv](https://arxiv.org/html/2512.12818v1)

### Why it matters for company brains

A company brain should not only store documents; it should learn:

- What decisions were made.
- Why a decision was made.
- What happened afterward.
- Which policies worked.
- Which vendor claims failed.
- Which procedures repeatedly caused errors.

Hindsight’s “experience + reflection” model is particularly relevant for an operations agent.

## Rank 7 — MemOS

Repository: [MemTensor/MemOS](https://github.com/MemTensor/MemOS)

MemOS positions itself as a memory operating system for agents, with:

- Layered memory.
- Persistent memory.
- Dynamic retrieval.
- Memory updates.
- Skill memory.
- Cross-task reuse.
- Adaptive learning.

 [linkedin](https://www.linkedin.com/posts/sumanth077_memory-operating-system-for-ai-agents-memos-activity-7419359497284087808-heFj)

It is worth studying alongside Memmy because Memmy is an agent runtime while MemOS is more explicitly a memory operating-system direction.

## Rank 8 — Honcho

Repository: [plastic-labs/honcho](https://github.com/plastic-labs/honcho)

Honcho is best for:

- User modeling.
- Agent modeling.
- Group/project identity.
- Cross-session context.
- Evolving relationships.

It is not a full company search system, but it can be the identity/person-model layer inside one.

## Rank 9 — Letta

Repository: [letta-ai/letta](https://github.com/letta-ai/letta)

Letta is best when each organizational agent must maintain and operate its own persistent state.

Use cases:

- A persistent revenue-cycle analyst.
- A vendor-intelligence agent.
- A hospital-operations agent.
- A compliance agent.
- A customer-success agent.

## Rank 10 — TeamBrain and Git-native knowledge systems

TeamBrain is reported as a Git-native organizational brain in which:

- Memories are Markdown with YAML frontmatter.
- Git history is the audit trail.
- Pull requests are the write-approval gate.
- Nothing enters the shared brain without review.

 [linkedin](https://www.linkedin.com/posts/donatien-migue_github-donatienmigueteambrain-the-brain-activity-7487458565029298176-06Yg)

The exact repository should be independently inspected before treating it as a mature production dependency, but the architecture is important:

```text
Agent proposes memory
       ↓
Pull request
       ↓
Human review
       ↓
Merge
       ↓
Shared organizational memory
```

This is a compelling model for:

- Compliance policies.
- Engineering standards.
- Vendor evaluations.
- Hospital SOPs.
- Claims rules.
- Product decisions.
- Integration knowledge.

## Other company-brain candidates

| Repository | Best contribution |
|---|---|
| [GBrain](https://github.com/garrytan/gbrain) | Git-backed shared brain, graph, synthesis, gaps, citations |
| [Onyx](https://github.com/onyx-dot-app/onyx) | Permission-aware enterprise search and agents |
| [OpenViking](https://github.com/volcengine/OpenViking) | Hierarchical context/memory/skills database |
| [Cognee](https://github.com/topoteretes/cognee) | Organizational knowledge graph |
| [Khoj](https://github.com/khoj-ai/khoj) | Self-hosted AI second brain and research |
| [Hindsight](https://github.com/vectorize-io/hindsight) | Reflective long-term memory |
| [MemOS](https://github.com/MemTensor/MemOS) | Memory operating system |
| [Honcho](https://github.com/plastic-labs/honcho) | User/entity modeling |
| [Graphiti](https://github.com/getzep/graphiti) | Temporal knowledge graph |
| [Zep](https://github.com/getzep/zep) | Conversational memory |
| [Mem0](https://github.com/mem0ai/mem0) | Drop-in persistent memory |
| [RAGFlow](https://github.com/infiniflow/ragflow) | Deep-document RAG and grounded citations |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Graph-enhanced RAG |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | Self-hosted document/workspace assistant |
| [LobeHub](https://github.com/lobehub/lobehub) | Agent workspace and operations |
| [MindsDB](https://github.com/mindsdb/mindsdb) | Agents across live enterprise data |
| [NocoBase](https://github.com/nocobase/nocobase) | Internal business workflows, data, permissions |
| [ToolJet](https://github.com/ToolJet/ToolJet) | Internal tools and AI-enabled operations |
| [AFFiNE](https://github.com/toeverything/AFFiNE) | Collaborative knowledge workspace |
| [Outline](https://github.com/outline/outline) | Team knowledge base substrate |
| [BookStack](https://github.com/BookStackApp/BookStack) | Structured self-hosted documentation |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Collaborative knowledge workspace |
| [Obsidian plugins](https://github.com/obsidianmd/obsidian-releases) | Local Markdown knowledge ecosystem |

# 3. Best agent frameworks

| Rank | Repository | Best for |
|---|---|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | Explicit stateful agent workflows |
| 2 | [Letta](https://github.com/letta-ai/letta) | Memory-native stateful agents |
| 3 | [AgentScope](https://github.com/agentscope-ai/agentscope) | Multi-agent applications and runtime integration |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | TypeScript production apps |
| 5 | [Agno](https://github.com/agno-agi/agno) | Integrated Python agent platform |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | Typed and testable Python services |
| 7 | [AutoGen](https://github.com/microsoft/autogen) | Event-driven multi-agent collaboration |
| 8 | [CrewAI](https://github.com/crewAIInc/crewAI) | Role-based teams and workflows |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | Knowledge/data agents |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | Explicit RAG pipelines |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | Programmatic optimization |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | Enterprise Microsoft stack |
| 13 | [Google ADK](https://github.com/google/adk-python) | Google ecosystem |
| 14 | [Smolagents](https://github.com/huggingface/smolagents) | Minimal code agents |
| 15 | [CAMEL](https://github.com/camel-ai/camel) | Agent societies and research |

# 4. Skills and context engineering

## Best repositories

| Rank | Repository | Distinctive role |
|---|---|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | Unified memory/resource/skill filesystem |
| 2 | [DeerFlow skills](https://github.com/bytedance/deer-flow/tree/main/skills) | Runtime skills with allowed-tool policies and quality gates |
| 3 | [Hermes skills](https://github.com/NousResearch/hermes-agent/tree/main/skills) | Skills that can be created and improved from experience |
| 4 | [AGENTS.md](https://github.com/agentsmd/agents.md) | Repository-level agent operating context |
| 5 | [context-mode](https://github.com/mksglu/context-mode) | Externalizes bulky tool output from the context window |
| 6 | [LangMem](https://github.com/langchain-ai/langmem) | Memory management for LangGraph |
| 7 | [claude-mem](https://github.com/thedotmack/claude-mem) | Coding-session capture and recall |
| 8 | [Open Knowledge Format](https://github.com/topics/open-knowledge-format) | Portable Markdown/YAML knowledge bundles |
| 9 | [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | Curated harness patterns and projects |
| 10 | [awesome-agent-skills-security](https://github.com/LLMSecurity/awesome-agent-skills-security) | Skill/tool security references |

Google’s Open Knowledge Format is important because it defines a vendor-neutral, agent- and human-friendly way to represent knowledge as Markdown files with YAML frontmatter. [cloud.google](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)

That is a major direction for company brains:

```text
Knowledge bundle
  ├── policy.md
  ├── decision.md
  ├── person.md
  ├── project.md
  └── procedure.md
```

The advantage is portability. A company should not need to rewrite its institutional knowledge when changing from one agent platform to another.

# 5. Tool protocols and agent networks

## MCP

Core projects:

- [MCP servers](https://github.com/modelcontextprotocol/servers).
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk).
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk).
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector).
- [FastMCP](https://github.com/jlowin/fastmcp).
- [MCP Context Forge](https://github.com/IBM/mcp-context-forge).
- [MCP-UI](https://github.com/idosal/mcp-ui).
- [Supergateway](https://github.com/supercorp-ai/supergateway).
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent).

## Agent-to-agent

- [A2A](https://github.com/a2aproject/A2A).
- [ACP](https://github.com/i-am-bee/acp).
- [AgentField](https://github.com/Agent-Field/agentfield).
- [AgentScope](https://github.com/agentscope-ai/agentscope).
- [AutoGen](https://github.com/microsoft/autogen).
- [CrewAI](https://github.com/crewAIInc/crewAI).
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT).

## Tool/integration platforms

- [Composio](https://github.com/ComposioHQ/composio).
- [n8n](https://github.com/n8n-io/n8n).
- [Pipedream](https://github.com/PipedreamHQ/pipedream).
- [Activepieces](https://github.com/activepieces/activepieces).
- [Windmill](https://github.com/windmill-labs/windmill).
- [NocoBase](https://github.com/nocobase/nocobase).
- [ToolJet](https://github.com/ToolJet/ToolJet).
- [Appsmith](https://github.com/appsmithorg/appsmith).

For healthcare operations, a practical pattern is:

```text
MCP tool
  ↓
typed internal API
  ↓
authorization check
  ↓
hospital tenant scope
  ↓
audit log
  ↓
external HMS/EMR/billing system
```

Do not expose raw database write access to an LLM.

# 6. Voice and realtime systems

## Ranking

| Rank | Repository | Best use |
|---|---|---|
| 1 | [Pipecat](https://github.com/pipecat-ai/pipecat) | Flexible multimodal voice pipelines |
| 2 | [LiveKit Agents](https://github.com/livekit/agents) | WebRTC, realtime, SIP, telephony |
| 3 | [TEN Framework](https://github.com/TEN-framework/ten-framework) | Broad multimodal realtime ecosystem |
| 4 | [Bolna](https://github.com/bolna-ai/bolna) | End-to-end phone/voice agent workflows |
| 5 | [Vocode](https://github.com/vocodedev/vocode-core) | Voice-agent abstractions |
| 6 | [Rasa](https://github.com/RasaHQ/rasa) | Deterministic conversational workflows |
| 7 | [NVIDIA Nemotron Voice Agent](https://github.com/NVIDIA-AI-Blueprints/nemotron-voice-agent) | NVIDIA production blueprint |
| 8 | [Asterisk](https://github.com/asterisk/asterisk) | Telephony |
| 9 | [FreeSWITCH](https://github.com/signalwire/freeswitch) | Carrier-grade media |
| 10 | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Speech recognition |

Pipecat supports single-agent and multi-agent voice systems with specialist handoffs and parallel coordination. [github](https://github.com/pipecat-ai/pipecat)

For a healthcare voice assistant:

```text
LiveKit/Pipecat
   ↓
VAD
   ↓
STT
   ↓
bounded agent
   ↓
policy check
   ↓
HMS/billing/appointment tool
   ↓
TTS
```

The voice agent should not directly decide clinical treatment or execute irreversible billing actions.

# 7. Sandboxes and execution policy

## Ranking

| Rank | Repository | Role |
|---|---|---|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | Policy-enforced autonomous-agent runtime |
| 2 | [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | Identity, policy, audit, governance |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | General sandbox platform |
| 4 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | Stateful Kubernetes agent environments |
| 5 | [gVisor](https://github.com/google/gvisor) | Container isolation |
| 6 | [Firecracker](https://github.com/firecracker-microvm/firecracker) | MicroVM isolation |
| 7 | [Pipelock](https://github.com/lasso-security/pipelock) | MCP-aware egress/firewall |
| 8 | [nsjail](https://github.com/google/nsjail) | Process sandbox |
| 9 | [bubblewrap](https://github.com/containers/bubblewrap) | Linux sandbox |
| 10 | [Microsandbox](https://github.com/zerocore-ai/microsandbox) | Fast isolated execution |

OpenShell’s repository describes declarative YAML policies covering filesystem, network, process, and inference behavior. [github](https://github.com/NVIDIA/OpenShell)

The correct boundary is:

```text
Agent plan
  ↓
Policy decision
  ↓
Tool authorization
  ↓
Argument validation
  ↓
Sandbox
  ↓
Human approval
  ↓
Execution
  ↓
Signed audit event
```

# 8. Governance and guardrails

| Rank | Repository | Main layer |
|---|---|---|
| 1 | [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | Runtime governance, identity, policies, audit |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | Execution and egress policy |
| 3 | [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) | Prompt injection, alignment, code security |
| 4 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Programmable conversational and tool rails |
| 5 | [Pipelock](https://github.com/lasso-security/pipelock) | MCP firewall, DLP, egress mediation |
| 6 | [Guardrails AI](https://github.com/guardrails-ai/guardrails) | Structured output validation |
| 7 | [Presidio](https://github.com/microsoft/presidio) | PII discovery and anonymization |
| 8 | [Invariant](https://github.com/invariantlabs-ai/invariant) | Agent behavior testing |
| 9 | [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanning |
| 10 | [PyRIT](https://github.com/Azure/PyRIT) | Red-team testing |

NeMo Guardrails is designed as an open-source Python package for programmable protection of LLM applications. [docs.nvidia](https://docs.nvidia.com/nemo/guardrails/home)

LlamaFirewall is specifically positioned as a defense layer for security risks associated with agents. [arxiv](https://arxiv.org/html/2505.03574v1)

# 9. Durable autonomous workflows

| Rank | Repository | Use |
|---|---|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | Long-running workflows, retries, approvals, compensation |
| 2 | [Restate](https://github.com/restatedev/restate) | Durable distributed execution |
| 3 | [Hatchet](https://github.com/hatchet-dev/hatchet) | Agent/background tasks |
| 4 | [Inngest](https://github.com/inngest/inngest) | Event-driven durable functions |
| 5 | [Prefect](https://github.com/PrefectHQ/prefect) | Data/Python workflows |
| 6 | [Kestra](https://github.com/kestra-io/kestra) | Declarative orchestration |
| 7 | [n8n](https://github.com/n8n-io/n8n) | Visual business automation |
| 8 | [Dagster](https://github.com/dagster-io/dagster) | Data/asset workflows |
| 9 | [Airflow](https://github.com/apache/airflow) | Scheduled workflows |
| 10 | [Celery](https://github.com/celery/celery) | Distributed task queues |

## Why Temporal belongs in a company brain

A company brain often has jobs that run for hours or days:

- Ingest meetings.
- Transcribe calls.
- Extract entities.
- Update company/person pages.
- Detect contradictions.
- Request review.
- Merge approved knowledge.
- Re-index.
- Notify affected teams.

That is a durable workflow, not a single LLM call.

# 10. Browser and computer-use agents

| Rank | Repository | Best use |
|---|---|---|
| 1 | [Browser Use](https://github.com/browser-use/browser-use) | General browser agent |
| 2 | [Stagehand](https://github.com/browserbase/stagehand) | Structured browser automation |
| 3 | [Agent S](https://github.com/simular-ai/agent-s) | Computer-use agent |
| 4 | [OpenManus](https://github.com/FoundationAgents/OpenManus) | General autonomous browser/task agent |
| 5 | [Skyvern](https://github.com/Skyvern-AI/skyvern) | Browser workflows |
| 6 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | Browser evaluation |
| 7 | [WebArena](https://github.com/web-arena-x/webarena) | Realistic browser benchmark |
| 8 | [Agent Browser](https://github.com/vercel-labs/agent-browser) | Agent browser control |
| 9 | [Playwright](https://github.com/microsoft/playwright) | Browser substrate |
| 10 | [Selenium](https://github.com/SeleniumHQ/selenium) | Browser substrate |

For hospital systems, browser automation should be the last resort after APIs, FHIR/HL7, structured integration, and direct service interfaces.

# 11. Evaluation and observability

## Evaluation

| Rank | Repository | Purpose |
|---|---|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | Agent regression and red-team tests |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | LLM/agent evaluation |
| 3 | [Phoenix](https://github.com/Arize-ai/phoenix) | Tracing and evaluation |
| 4 | [Langfuse](https://github.com/langfuse/langfuse) | Traces, prompts, datasets |
| 5 | [Ragas](https://github.com/explodinggradients/ragas) | RAG evaluation |
| 6 | [τ-bench](https://github.com/sierra-research/tau-bench) | Policy-following tool use |
| 7 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | Coding agents |
| 8 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | Browser agents |
| 9 | [OSWorld](https://github.com/xlang-ai/OSWorld) | Computer-use agents |
| 10 | [ToolSandbox](https://github.com/apple/ToolSandbox) | Tool-use evaluation |

## Company-brain evaluation

A company brain needs tests that ordinary RAG evaluation misses:

- Permission leakage.
- Stale information.
- Contradictory decisions.
- Missing evidence.
- Wrong person/entity resolution.
- Incorrect organizational relationships.
- Time-sensitive knowledge.
- Unauthorized memory writes.
- Citation completeness.
- Cross-team isolation.
- User deletion and retention.
- Tenant-boundary failure.
- Graph hallucinations.

Use a benchmark record like:

```json
{
  "question": "Which vendor owns the unresolved ABDM integration issue?",
  "expected_entities": ["vendor_id", "issue_id", "hospital_id"],
  "required_sources": ["ticket", "contract", "meeting"],
  "allowed_tenants": ["hospital_a"],
  "forbidden_sources": ["hospital_b"],
  "freshness_limit_days": 30,
  "must_report_uncertainty": true
}
```

# 12. License and maturity matrix

| Project | Main license/status to verify | Deployment concern |
|---|---|---|
| DeerFlow | Repository license must be checked for the exact version | Broad capabilities; sandbox required |
| Hermes | MIT according to repository | Host tools and credentials need restriction |
| OpenClaw | Check current root and bundled component licenses | Main session may run on host |
| OpenViking | AGPLv3 main project, other components differ | Important for proprietary SaaS embedding |
| GBrain | MIT according to repository | Strongly opinionated architecture |
| Onyx | Community and enterprise components differ | Verify feature/license boundary |
| Khoj | Self-hosting/license terms must be checked for deployment mode | Good second-brain application |
| Mem0 | Check current repository and commercial features | Cloud/self-hosted boundaries |
| Hindsight | Repository license should be verified at release | Benchmark claims need reproduction |
| Dify | Source-visible/fair-code details require careful review | Plugin/enterprise separation |
| n8n | Source-available/fair-code rather than conventional permissive OSS | Commercial embedding restrictions |
| RAGFlow | Verify current component and enterprise licensing | Infrastructure complexity |
| OpenShell | Check current license and runtime dependencies | Requires privileged infrastructure planning |
| Agent Governance Toolkit | MIT according to Microsoft announcement | Public preview/maturity evaluation |

A repository should be marked:

- **Open-source** only after checking the actual license.
- **Source-available** where use restrictions apply.
- **Production-ready** only after testing recovery, upgrades, authorization, and failure behavior.

# 13. Best stacks by objective

## A. Best autonomous company brain

```text
GBrain
+ OpenViking
+ Onyx
+ Graphiti/Cognee
+ MCP
+ Temporal
+ OpenShell
+ Microsoft Agent Governance Toolkit
+ Langfuse/Phoenix
```

Use this when the company needs:

- Shared memory.
- Personal/team/private scopes.
- Citations.
- Graph relationships.
- Search across company systems.
- Agent read/write access.
- Review gates.
- Long-running enrichment.

## B. Best personal autonomous operator

```text
Hermes
+ Honcho
+ GBrain or OpenViking
+ OpenShell
+ MCP
+ Temporal
+ Langfuse
```

## C. Best multi-channel assistant

```text
OpenClaw
+ OpenViking
+ Mem0/Honcho
+ OpenShell
+ MCP
+ LiveKit/Pipecat
```

## D. Best long-horizon research/coding agent

```text
DeerFlow
+ OpenViking
+ OpenSandbox/OpenShell
+ Temporal
+ Browser Use
+ Promptfoo
+ Phoenix
```

## E. Best healthcare company brain

```text
Onyx          → permission-aware enterprise search
GBrain        → Git-backed typed institutional memory
OpenViking    → hierarchical context and skills
Graphiti      → temporal relationships
Cognee        → knowledge graph construction
Temporal      → durable enrichment workflows
MCP           → typed HMS/EMR/billing tools
OpenShell     → sandbox and network policy
Presidio      → PHI/PII detection
Langfuse      → traces and audit correlation
```

# 14. Healthcare company-brain design

For your specific healthcare IT focus, I would create separate knowledge domains:

```text
company-brain/
├── hospitals/
│   ├── hospital-a/
│   └── hospital-b/
├── people/
│   ├── doctors/
│   ├── administrators/
│   └── vendors/
├── systems/
│   ├── hms/
│   ├── emr/
│   ├── billing/
│   ├── pharmacy/
│   └── abdm/
├── contracts/
├── implementations/
├── incidents/
├── workflows/
├── regulations/
├── product-decisions/
├── competitor-intelligence/
├── revenue-leakage/
└── skills/
```

Every memory should carry:

```yaml
id:
type:
tenant:
source:
source_uri:
created_at:
updated_at:
valid_from:
valid_until:
confidence:
sensitivity:
consent_scope:
author:
review_status:
supersedes:
contradicts:
related_entities:
```

## Example

```yaml
id: incident-abdm-2026-0042
type: integration_incident
tenant: hospital_a
system: abdm
vendor: vendor_x
source: jira_ticket_8841
confidence: verified
review_status: approved
valid_from: 2026-07-12
sensitivity: internal
```

The agent should be able to answer:

- What happened?
- Which hospital was affected?
- Which vendor owns it?
- What evidence supports the conclusion?
- Is the information current?
- Which policies or contracts apply?
- What action is authorized?
- Who must approve it?

That is a company brain. A vector database by itself is not.

# 15. Final winner by category

| Category | Best repository | Reason |
|---|---|---|
| Complete long-horizon harness | DeerFlow | Most complete combination of sub-agents, skills, memory, sandbox, context, artifacts |
| Self-improving assistant | Hermes Agent | Learning loop, skills, memory, scheduling, delegation, gateway |
| Personal-agent gateway | OpenClaw | Channels, devices, sessions, voice, routing, nodes |
| Autonomous coding | OpenHands | Full coding environment and execution |
| Developer harness | Goose | Extensible local tools and protocol design |
| Stateful agent runtime | Letta | Memory is native to the agent |
| Context database | OpenViking | Hierarchical memory/resource/skill filesystem |
| User/entity modeling | Honcho | Evolving people, agents, groups, projects |
| Company brain | GBrain | Shared Git-backed brain, graph, synthesis, gaps, citations |
| Enterprise knowledge platform | Onyx | Permission-aware connectors and agentic search |
| Document brain | RAGFlow | Deep document understanding and grounded answers |
| Second brain | Khoj | Self-hosted docs/web/custom agents/research |
| Reflective memory | Hindsight | Retain, recall, reflect, mental models |
| Memory OS | MemOS | Layered, persistent, evolving memory |
| Graph memory | Graphiti | Temporal relationships |
| Knowledge graph | Cognee | Connected organizational memory |
| Tool protocol | MCP | Standard agent-to-tool interface |
| Agent-to-agent protocol | A2A | Agent interoperability |
| Durable workflows | Temporal | Recovery, retries, approvals, compensation |
| Voice pipeline | Pipecat | Flexible realtime orchestration |
| Realtime/telephony | LiveKit Agents | WebRTC/SIP/scaling |
| Sandbox runtime | OpenShell | Declarative filesystem/network/process policy |
| Governance | Microsoft Agent Governance Toolkit | Identity, policy, isolation, audit |
| Agent security | LlamaFirewall | Injection/alignment/code security |
| Interaction rails | NeMo Guardrails | Programmable conversational/tool policies |
| Agent firewall | Pipelock | MCP-aware egress/DLP mediation |
| Agent evaluation | Promptfoo | Regression and red-team testing |
| Observability | Langfuse/Phoenix | Tracing, evaluation, cost, retrieval inspection |

# Final recommendation

If your goal is to study the best open-source systems rather than merely install an SDK, clone these in this order:

1. [DeerFlow](https://github.com/bytedance/deer-flow)
2. [Hermes Agent](https://github.com/NousResearch/hermes-agent)
3. [OpenClaw](https://github.com/openclaw/openclaw)
4. [GBrain](https://github.com/garrytan/gbrain)
5. [OpenViking](https://github.com/volcengine/OpenViking)
6. [Onyx](https://github.com/onyx-dot-app/onyx)
7. [OpenHands](https://github.com/All-Hands-AI/OpenHands)
8. [Goose](https://github.com/block/goose)
9. [Hindsight](https://github.com/vectorize-io/hindsight)
10. [Letta](https://github.com/letta-ai/letta)
11. [Cognee](https://github.com/topoteretes/cognee)
12. [Graphiti](https://github.com/getzep/graphiti)
13. [MemOS](https://github.com/MemTensor/MemOS)
14. [AgentScope Runtime](https://github.com/agentscope-ai/agentscope-runtime)
15. [OpenShell](https://github.com/NVIDIA/OpenShell)
16. [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)
17. [MCP](https://github.com/modelcontextprotocol/servers)
18. [Temporal](https://github.com/temporalio/temporal)
19. [Pipecat](https://github.com/pipecat-ai/pipecat)
20. [Onyx CLI and connectors](https://github.com/onyx-dot-app/onyx)

The strongest “company brain” architecture is:

```text
GBrain
  + Onyx
  + OpenViking
  + Graphiti/Cognee
  + Hindsight
  + MCP
  + Temporal
  + OpenShell
  + Microsoft Agent Governance Toolkit
  + Langfuse/Phoenix
```

The strongest “autonomous assistant” architecture is:

```text
DeerFlow or Hermes
  + OpenClaw gateway
  + OpenViking/Honcho/GBrain
  + MCP
  + Temporal
  + OpenShell
  + Pipecat/LiveKit
  + Promptfoo/Langfuse
```

The single most important correction to the competing answer is this:

> **GBrain and Onyx should not be treated as ordinary memory projects; they represent two different company-brain strategies. GBrain is a Git-backed, graph-aware, synthesis-oriented institutional brain. Onyx is a connector-heavy, permission-aware enterprise knowledge and agent platform. OpenViking is the context substrate that can organize resources, skills, and memory beneath either strategy.**

For healthcare SaaS, I would use **Onyx for enterprise connector/search**, **GBrain for governed institutional memory**, **OpenViking for hierarchical context and skills**, **Graphiti/Cognee for temporal organizational knowledge**, and **Temporal + OpenShell + Agent Governance Toolkit** for durable, controlled autonomous operations.
