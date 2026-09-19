# Repo map — what to adopt, add, and refuse

**Date:** 2026-09-17  
**Status:** Design input **before** WP-00. Not a stack lock. Not a fork list.  
**Follow with:** `DESIGN_FOLLOW_LIST_v1.md`  
**Repo catalogue:** `agentic_research/05-definitive-opensource-agentic-ai-repository-atlas.md`  
**Nabhi paper (patterns only):** `agentic_research/01-architecture-implementation-report.md`

We compose a **thin workbench**. We steal **workflows and contracts**. We do **not** become OpenHands, DeerFlow, Open WebUI, or NabhiPersona.

---

## How to read this

| Column | Means |
|---|---|
| **Adopt** | Pattern, interface, or file format to copy in *design*. Code copy only later, after a named OSI license is checked. |
| **Why that only** | The smallest slice that matches this WP. Not “use the whole repo.” |
| **Add (ours)** | SIH26117 / MRPL / air-gap / HITL / Word / grants — nothing in that repo is the product. |
| **Do not take** | Features that fight the PS (WAN, browser OS, cloud brain, marketplace, DCS, uncited chat). |

**Grade.** Atlas and vendor docs are **Observed**. PS need is **Official**. Your 2026-09-17 meanings are **User**. We have **not** re-cloned every repo today.

---

## Global refuse (every WP)

Do **not** take these even if a starred repo has them:

| Refuse | Why | Typical source |
|---|---|---|
| Fork a complete agent OS as the SIH product | Wrong job: coding laptop / research browser / founder Jarvis, not inspection workbench | DeerFlow, Hermes, OpenHands, OpenClaw, OpenAkita |
| Cloud LLM default (OpenRouter, Anthropic API, OpenAI cloud) | **Official** nothing leaves; open-weight | LiteLLM/Portkey *defaults*, Hermes multi-LLM to Claude |
| Public MCP / skill **marketplace** at runtime | **Official** no external calls at any point | MCP Registry, Kilo Marketplace, `npx` servers |
| Anthropic Messages **public HTTPS** MCP connector | Local stdio required; that API cannot attach stdio | Claude Platform MCP connector |
| Always-on OS / browser / computer-use | Shadow IT + WAN + not Expected Solution | Open Interpreter, Browser Use, OpenClaw, Agent S |
| Company Brain that **syncs off-prem** | NabhiPersona cloud brain is the opposite of this PS | Nabhi report §1–2 |
| Agent self-modifies production skills/weights | Untrusted; **User** `.md` needs HITL promotion | Hermes “self-improving” |
| Graph DB as the uniqueness story | **User**: version–task lineage, engine later | Neo4j, Graphiti, Cognee as *the* product |
| Visual “AI app builder” as the workbench | Hides HITL, grants, air-gap | Dify, Langflow, n8n |
| Chat+RAG UI as the product | Local chat already exists; PS wants Word, sandbox, auto-select, WAN=0 | Open WebUI, AnythingLLM, PrivateGPT, Khoj |
| A2A / multi-agent company mesh | Extra protocol; PS is one workbench + specialist agents | A2A, ACP |
| Temporal/Camunda as prototype spine | Durable HITL is an **org idea**; 36h/venue demo does not need a workflow cluster | Temporal, Camunda |
| Voice/telephony stacks | Not in PS | Pipecat, LiveKit, Bolna |
| Writing to DCS/SIS/PLC/EAM | Product never | Any “actions” connector in Onyx/Dify |

---

## Map by follow-list WP

### WP-00 Product contract

| | |
|---|---|
| **Adopt** | Nothing from a repo. Contract is PS. Atlas “company OS” diagram is a **warning label**, not a template. |
| **Why** | Repos sell autonomy. We sell evidence + drafts + HITL. |
| **Add** | Must / ambition / never page. Plugin host + pluggable models + never DCS. |
| **Do not take** | Nabhi “AI-native company OS”; DeerFlow “one repo to study first” as product identity. |

---

### WP-01 Users, jobs, artefacts

| | |
|---|---|
| **Adopt** | **python-docx**, **openpyxl** as *libraries* for Word/Excel (not a harness). Office-as-output, not chat. |
| **Why that only** | Expected Solution is a **Word file**. Description also Excel/PPT/calc-with-steps. No agent repo *is* an inspection-note factory. |
| **Add** | Plant vs generated vs personal `.md` classes. PPT = ambition. Inspection Word template + HITL fields. Calc-with-steps as sandbox output, not LLM arithmetic. |
| **Do not take** | Chat-transcript-to-docx hacks; PPT generators that ignore HITL. |

---

### WP-02 Plant systems

| | |
|---|---|
| **Adopt** | **Onyx** *connector pattern*: many systems, RBAC, search as a **layer**, not the app. Schema-stable JSON mocks for EAM/DMS. |
| **Why that only** | PS wants a KB **connector**. Onyx is the atlas “enterprise data-access layer.” |
| **Add** | Read-only. Declared destinations. Correspondence as a store type. MOCK in prototype. |
| **Do not take** | Onyx “actions” that write plant systems; 50 SaaS connectors (Slack/Google) that need WAN. |

---

### WP-04 Identity, session, grants

| | |
|---|---|
| **Adopt** | **Microsoft Agent Governance Toolkit** *ideas*: identity, policy, audit (study). Onyx **RBAC/SSO** as org-ambition pattern. Nabhi **trust tiers** (observe → propose → low-risk) — *tier names only*. |
| **Why that only** | No OSS workbench does **task-scoped grants + revoke** the way you asked. Closest is PAM/JIT (**Spec** NIST AC-6), not GitHub stars. |
| **Add** | Person session ≠ task grant. TTL. Classification ceiling (P&ID vs financials). Revoke copies in chat/`.md`. Prototype: local user + grant JSON. |
| **Do not take** | Onyx/Dify cloud SSO as must-work. Nabhi Company Brain tenancy. Standing API keys in MCP configs. |

---

### WP-05 HITL

| | |
|---|---|
| **Adopt** | **LangGraph interrupts** / human-approval *pattern* (checkpoint, resume). **Hermes**: approval before sensitive file ops (*behaviour*, not the agent). **TeamBrain / GBrain**: agent proposes, human promotes to shared memory. Atlas line: “AI proposes drafts, humans promote to canonical truth.” |
| **Why that only** | That is the only HITL that matches approval notes. |
| **Add** | Gates for: fact-sheet, Word download, file **write**, plugin install, skill promotion, policy-vs-user contradiction. Inspection spine steps. |
| **Do not take** | “Skill restrictions as security” (DeerFlow caution in atlas). Auto-merge to plant SOP. |

---

### WP-03 Ingest / multimodal

| | |
|---|---|
| **Adopt** | **Tesseract** and/or **PaddleOCR** as *candidate engines* (not locked). VLM via **same** `/v1` + card as WP-24. Image as **base64 `data:`** only (Ollama-class LCD). |
| **Why that only** | PS: on-device OCR + vision. RAG apps (RAGFlow, AnythingLLM) have OCR *plugins* that often fetch or assume cloud. |
| **Add** | Fail closed if scan unusable. Handwritten/drawings as first-class. Untrusted OCR text → WP-23. Sequential VLM load on mid-GPU. |
| **Do not take** | Remote `https://` image URLs. Cloud Document AI. RAGFlow as the workbench. |

---

### WP-23 Untrusted content

| | |
|---|---|
| **Adopt** | **LlamaFirewall** / **NeMo Guardrails** *ideas* (injection, tool rails). **Presidio** for PII/secret scan on output. **SkillSpector** idea: scan skills/plugins before load. Atlas: “`SKILL.md` is not a security boundary — put the boundary **below** the model.” |
| **Why that only** | Matches MCP security draft + your plugin/`.md` host. |
| **Add** | Treat OCR, RAG chunks, MCP tool text, personal `.md` as untrusted. Bind to grants. |
| **Do not take** | Guardrails that call a cloud moderator API. |

---

### WP-11 Retrieve / RAG

| | |
|---|---|
| **Adopt** | **Haystack** or **LlamaIndex** *pipeline shape* (ingest → retrieve → generate), not the product. **Onyx** hybrid retrieval + ACL *intent*. **GBrain/AKB**: Git + Markdown as **canonical** store, index beside it. |
| **Why that only** | PS is a **connector** to manuals/SOPs/correspondence with citations. Atlas: company brain ≠ vector DB. |
| **Add** | Revision IDs. Grant-aware retrieve. Correspondence corpus. Policy corpus (WP-22). Slow OK. Prototype: local files + citations, not Chroma-as-DMS. |
| **Do not take** | AnythingLLM/Open WebUI as the app. LightRAG/Graphiti as required graph. Mem0/Zep **conversation** memory as plant truth. |

---

### WP-22 Three-source verification

| | |
|---|---|
| **Adopt** | GBrain *citation + gap* idea. Ragas *evaluation* later (WP-18), not runtime. Atlas company-brain questions: what source, is it current, what contradicts, who approves. |
| **Why that only** | Almost no repo implements **file vs user vs policy** as three corpora. |
| **Add** | Contradiction policy. `NOT FOUND`. User utterance is a claim. |
| **Do not take** | “The LLM reconciles conflicts” as the gate. |

---

### WP-07 Tools, prompts, specialist agents

| | |
|---|---|
| **Adopt** | **mcp-agent** / **Goose**: MCP-first tools. **OpenHands** *tool host + event stream + human intervention* for **coding specialist only**. **Continue**: thin client, `base_url` + `api_key` + `model`. **PydanticAI** *typed tools* as a candidate style. Atlas: agent reasons **inside** a loop; do not let the framework own the company. |
| **Why that only** | PS tool list is small and local. Goose/Continue are **hosts**, closer than CrewAI societies. |
| **Add** | Specialists: inspect, code, spreadsheet — **no shared super-context**. File write gated. Iterate until HITL/stop. System policy ≠ skill. |
| **Do not take** | CrewAI/AutoGen swarms. Smolagents “code everything.” OpenHands **browser**. Continue **cloud models**. LangGraph lock. |

---

### WP-16 Execution sandbox

| | |
|---|---|
| **Adopt** | **OpenHands** / Cursor-class: **jail ≠ inference process**. **gVisor / nsjail / bubblewrap / Firecracker** as *org isolation menu*. Prototype candidate: container **`--network=none`** for generated code/tests/calc only. **Semgrep** on generated code (optional). |
| **Why that only** | Expected Solution: run **and verify**. Atlas minimum: policy → gateway → sandbox (fs/net/process/time). |
| **Add** | Never wrap GPU/Ollama in that jail. Calc `CR=(t_prev−t_curr)/Δt` in sandbox, not in the LLM. |
| **Do not take** | Kubernetes Agent Sandbox as prototype. OpenSandbox as the product. DeerFlow K8s provisioner. |

---

### WP-08 Plugin host (MCP)

| | |
|---|---|
| **Adopt** | **MCP spec + Python/TS SDK** (stdio, localhost). **FastMCP** for *writing* our demo servers. **Goose / Cursor / Claude Desktop** *host UX*: user adds a server in config. **Agent Skills** + optional **Agent Plugins** layout (`plugin.json` + `skills/` + `mcp.json`) as *pack format*. **Pipelock** *idea*: MCP-aware egress. **Docker MCP** guidance: allowlist, sign/pin, container, intercept. |
| **Why that only** | **User** + **Official** Claude/Codex metaphor. SDKs are the protocol; hosts are the UX. |
| **Add** | Offline install (WP-19). Allowlist. Default-deny egress **below** the model. HITL on install. No registry at runtime. One local demo server is enough to *be* a host. |
| **Do not take** | `modelcontextprotocol/servers` Google Drive/Slack/GitHub. MCP Registry. IBM/Microsoft **federation** gateways. Remote Streamable HTTP to the internet. |

---

### WP-24 Model registry (pluggable models)

| | |
|---|---|
| **Adopt** | **Continue / OpenHands / LM Studio**: models as **catalog entries**, client unchanged. **Dify “model management”** *UI idea only*. **Ollama/vLLM `GET /v1/models`**: liveness **ids**, not cards. **Our Model Cards** (prior paper) — re-confirm at freeze. |
| **Why that only** | PS: add without redesign. No serving repo stores **roles / vision / tools / classification**. |
| **Add** | Card schema. Add **and remove**. Open-weight on-prem only. OCR/VLM as cards. Fail closed if id not registered. |
| **Do not take** | Ollama as the workbench. LiteLLM **provider** list (OpenAI/Anthropic). Hugging Face download in the UI. |

---

### WP-06 Orchestration + routing

| | |
|---|---|
| **Adopt** | Plan → act → observe → iterate (generic). **LangGraph** *state + interrupt* as a **candidate**, not default. **DeerFlow** *sub-agents + skill review* as **study**, not fork. Task-type router is **ours** (coding ≠ summary). |
| **Why that only** | Expected Solution: auto-select ≥2 types. Ollama model dropdown is **not** that (prior red-team). |
| **Add** | Route to **WP-24 cards**. Iterate. No safety autonomy. Specialist dispatch. |
| **Do not take** | DeerFlow browser/scheduler. LangGraph as identity. LiteLLM “load balancer” as task intelligence. |

---

### WP-21 Context assembly

| | |
|---|---|
| **Adopt** | **OpenViking** *progressive disclosure* (L0/L1/L2, on-demand) as **idea**. **Agent Skills** progressive load. **DeerFlow** “context engineering” as a phrase to steal, not the code. |
| **Why that only** | **User**: what data to pass. Atlas OpenViking is the dedicated “context substrate.” License AGPLv3 — **do not embed** without legal freeze; pattern only. |
| **Add** | Pack to **grant**. Citations in, P&ID binders out. Tool-result size caps before gateway. |
| **Do not take** | OpenViking as a required database. Dump-full-repo context (Aider/Cline default habit). |

---

### WP-09 LLM gateway

| | |
|---|---|
| **Adopt** | **Continue/OpenHands client triad.** Serving LCD from **llama.cpp / Ollama / vLLM / SGLang** docs. **LiteLLM / Envoy AI Gateway / Portkey** *only* as: one `/v1` socket, auth, timeout — **if** they can run **offline with empty provider list**. |
| **Why that only** | Gateway is software to the runtime, not CUDA. |
| **Add** | Schema-valid requests. Card check. `data:` images only. No cloud rewrite. Model id must be registered. |
| **Do not take** | LiteLLM proxying OpenAI. Helicone cloud observability. Any gateway that “fails over” to WAN. |

---

### WP-10 Runtime

| | |
|---|---|
| **Adopt** | **vLLM / llama.cpp / Ollama / LM Studio / SGLang** as **interchangeable `/v1` servers**. Hardware probe on **this** plane (`nvidia-smi`), not OpenAI. |
| **Why that only** | PS: own GPU; workstation or server; smaller model if 120B absent. |
| **Add** | Load policy (catalog vs VRAM). Sequential on mid-GPU. Pre-stage weights (WP-19). |
| **Do not take** | Lock one binary in WP-00. Ollama telemetry. “Ollama routes models” as task router. |

---

### WP-12 Output gates

| | |
|---|---|
| **Adopt** | **Presidio** (PII). **NeMo Guardrails** *output rails* idea. Semgrep on code artefacts. |
| **Why that only** | Scan before download. |
| **Add** | Classification on generated Word. Citation present. Sandbox pass required for calc/code. DRAFT badge. |
| **Do not take** | Cloud DLP APIs. |

---

### WP-17 Audit log

| | |
|---|---|
| **Adopt** | **Langfuse / Phoenix / OpenLLMetry** *self-host trace* pattern (prompt, model id, tools). Onyx *audit feature* intent. |
| **Why that only** | Expected Solution allows **logs**. Need model id + plugin id. |
| **Add** | Grant, HITL, retrieval revision, export. Offline. CERT-In-shaped fields at freeze. |
| **Do not take** | Langfuse Cloud. Traces that upload prompts off-prem. |

---

### WP-14 Task–version lineage

| | |
|---|---|
| **Adopt** | **GBrain / AKB / TeamBrain**: Git + Markdown + **reviewed writes**. **Graphiti** *bitemporal* idea (valid_from / valid_until) as **fields**, not Neo4j. Atlas YAML: `source_uri`, `source_hash`, `supersedes`, `contradicts`, `review_status`. |
| **Why that only** | **User** asked relations of versions and tasks, not a graph product. Git is the honest document-control analogue. |
| **Add** | `task_id` ↔ input version ↔ model card ↔ draft version ↔ HITL. Engine undecided. |
| **Do not take** | Cognee/Neo4j/FalkorDB as default. Mem0 as plant SOP store. |

---

### WP-13 Monitors

| | |
|---|---|
| **Adopt** | Host firewall / packet log (OS), not a React badge alone. **Langfuse** UI *only* as operator “why this model” inspiration. **Pipelock** egress idea for MCP. |
| **Why that only** | **Official**: visible network monitor or logs; zero external at any point. |
| **Add** | Audience A WAN=0. Audience B: card, grant, HITL, plugins. WAN unplug in demo. |
| **Do not take** | App-only “offline mode” while Ollama/HF still phones home. Helicone SaaS. |

---

### WP-15 Personal `.md` harness

| | |
|---|---|
| **Adopt** | **Agent Skills spec** + **Hermes skill files** (auto `.md` from repeated work). **OpenViking** skills-as-files idea. Progressive disclosure. |
| **Why that only** | **User** definition of self-learning. Spec is Official-format. |
| **Add** | Personal vs org promotion HITL. No weight train. Internet `compatibility` unloadable. |
| **Do not take** | Hermes autonomous self-modification. Skills Hub / Vercel install. Anthropic/Google skill packs that need cloud. |

---

### WP-18 Fail-closed + eval

| | |
|---|---|
| **Adopt** | **Promptfoo** (agent regression + red-team). **Ragas** (RAG). **τ-bench** *tool policy* idea. **Garak / PyRIT** later for injection. Golden tasks = Expected Solution list. |
| **Why that only** | Atlas eval section is for quality bars, not UX. |
| **Add** | Tests: two model ids in log, WAN=0, unregistered model, expired grant, missing citation. |
| **Do not take** | SWE-bench as our score (wrong product). Cloud eval runners. |

---

### WP-19 Offline update

| | |
|---|---|
| **Adopt** | Nothing that `pip`/`npx`/`ollama pull` at runtime. **Air-gap MCP** operator guides (deny-all egress). Pin-by-digest idea from Docker MCP. |
| **Why that only** | PS add-model-later + zero external calls. |
| **Add** | USB/approved media → stage weights → register card; same for plugins. |
| **Do not take** | Hugging Face hub in the workbench. MCP Registry. Ollama library pull. |

---

### WP-20 Connection diagram

| | |
|---|---|
| **Adopt** | Atlas *safe agent* pipeline (policy → gateway → sandbox) **plus** our two planes (workbench / runtime / code jail). |
| **Why that only** | Need one picture of **frozen** WPs, not DeerFlow’s architecture poster. |
| **Add** | Grant, cards, plugin host, WP-22, monitors A/B. |
| **Do not take** | Atlas “recommended stack” dump (DeerFlow+GBrain+Onyx+OpenViking+Graphiti+Temporal+LiteLLM) as our diagram. |

---

## What no repo gives us (must add)

These are why we are not “Open WebUI + plugins”:

1. Task **auto-select** logged with **two Model Card ids** (Expected Solution).  
2. Inspection **scan → HITL fact sheet → Word** (not chat).  
3. Sandbox **verify** + calc-with-steps, jail ≠ GPU.  
4. **Visible WAN=0** including model/plugin install.  
5. **Task grants + revoke** (NIST-shaped, not SSO).  
6. **Three-source** file / user / policy.  
7. Offline **plugin + model** catalogs (plugs without marketplace).  
8. Never-write plant control systems.

---

## Study shortlist when a WP starts (still not a lock)

| When walking | Open these, ignore the rest of the atlas |
|---|---|
| WP-07 / 08 / 15 | MCP spec + SDK, Goose, Continue, Agent Skills, Hermes *skills only* |
| WP-16 | OpenHands sandbox split; gVisor/nsjail *docs* |
| WP-09 / 10 / 24 | llama.cpp, vLLM, Ollama, LM Studio `/v1` docs; Continue client |
| WP-11 / 14 / 22 | Onyx *connectors/ACL*, GBrain/AKB *Git+cite*, Haystack *pipeline* |
| WP-05 / 06 | LangGraph interrupts *docs*; TeamBrain promote-via-review |
| WP-23 / 12 / 18 | LlamaFirewall/Presidio *ideas*; Promptfoo |
| WP-13 / 19 | OS packet log; Docker MCP allowlist; not Helicone Cloud |
| Never as product | DeerFlow, OpenClaw, Dify, Open WebUI, AnythingLLM, NabhiPersona cloud brain |

---

## Rule for every later WP discussion

Name **one** adopt slice, **one** add, **one** refuse. If the slice needs a brand (LangGraph vs loop), freeze is still “candidate list, not locked” until you say lock.
