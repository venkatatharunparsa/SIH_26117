Here is the complete list of frameworks, repositories, tools, and models discussed across our conversation, organized by category.

---

## 1. Agentic Orchestration & Harnesses

| Name | Notes |
|---|---|
| **Cursor** | Conceptual reference; cloud-based, closed-source. Not usable for air-gapped deployment. |
| **OpenHands** | Open-source agent framework with sandboxed execution and layered architecture. |
| **DeepSeek Harness (dsh)** | Plugin-based agent runtime with web UI; MIT licensed. |
| **OpenHarness** | `Cicizz/OpenHarness` or `HKUDS/OpenHarness`; v0.1.0 released 2026-04-01. Streaming tool calls, subagents, permissions, memory. |
| **aegis-cli** | `rtmx-ai/aegis-cli`; air-gap-native coding harness. Loopback-only by construction. |
| **GanyuanRan/Aegis** | Discipline package for coding agents; not a full orchestrator. |
| **aegiscloud.org / aegisruntime.dev** | Aegis projects focused on MCP capability enforcement. |
| **LangGraph** | Production-grade graph-based multi-agent orchestration. Used by Lyft, AWS reference architecture. Recommended as base orchestrator. |
| **Agno** (formerly Phidata) | Multi-agent framework with built-in agent, team, workflow abstractions. Production-proven. |
| **CrewAI** | Multi-agent framework mentioned as an alternative. |
| **LangChain** | Used for RAG pipelines and tool integration. |
| **Custom asyncio loop** | Minimal purpose-built orchestrator alternative for SIH. |

---

## 2. Sandboxed Code Execution

| Name | Notes |
|---|---|
| **sandbox-mcp** | `pottekkat/sandbox-mcp`; runs code in isolated Docker containers. |
| **code-executor-mcp** | MCP server for Python, JavaScript, shell execution with safety guards. |
| **LangShell** | Stateful, capability-scoped sandbox with AST validation and CBOR snapshots. |
| **E2B** | Mature sandbox backend; cloud-oriented, needs self-hosting. |
| **agent-sandbox** | Kubernetes SIG Apps project for K8s-native isolated workloads. |
| **node-code-sandbox-mcp** | Affected by CVE-2025-53372 (sandbox escape via command injection). |
| **Custom Docker sandbox** | Recommended for SIH: `docker run --rm --network none`, resource limits, import allow-lists, audit logging. |

---

## 3. Document Generation & Office Tools

| Name | Notes |
|---|---|
| **office-worker-mcp** | PyPI package v0.9.8, MIT licensed. Generates DOCX, PPTX, XLSX, PDF fully locally with template support. |
| **paperjsx/mcp-server** | Local MCP server for PPTX, DOCX, PDF, XLSX generation from JSON specs. |
| **python-docx** | Python library for Word document generation. |
| **python-pptx** | Python library for PowerPoint generation. |
| **openpyxl** | Python library for Excel generation. |
| **sympy** | Python library for symbolic calculations. |
| **pandas / numpy** | Data processing libraries used in sandbox allow-lists. |

---

## 4. OCR, Vision & Document Ingestion

| Name | Notes |
|---|---|
| **Docling** | IBM-origin, LF AI & Data hosted. Converts PDFs, DOCX, images into structured Markdown/JSON with layout, tables, reading order. 40M+ downloads. Recommended as core ingestion engine. |
| **Docling MCP** | `docling-mcp` on PyPI; exposes Docling as MCP tools. |
| **Marker v2** | PDF-to-Markdown pipeline supporting 90+ languages. |
| **olmOCR / olmOCR-2-7B (GGUF)** | Optimized for local OCR and handwritten text extraction. |
| **Qwen2.5-VL / Qwen2.5-VL-7B-Instruct** | Strong open-source vision-language model for image and scanned document understanding. |
| **pid-scanner-ocr** | Purpose-built for oil & gas P&ID digitization. |
| **OpenVLM** | Open-source framework for parsing engineering drawings, P&IDs, circuit diagrams. |
| **markitdown** | Converts any source file type to Markdown for RAG ingestion. |

---

## 5. RAG, Vector Search & Embeddings

| Name | Notes |
|---|---|
| **Qdrant** | Local vector database with HNSW, dense + sparse hybrid search. |
| **qdrant-client** | Python client for Qdrant. |
| **FastEmbed** | Lightweight ONNX-based embedding library maintained by Qdrant. |
| **nomic-embed-text** | Local embedding model via Ollama. |
| **bge-reranker-v2-m3** | Local cross-encoder reranker. |
| **bge-reranker-base** | Smaller reranker alternative via FastEmbed. |
| **agentic-rag reference** | LangChain + Agno + Qdrant + FastEmbed reference implementation. |
| **local-rag** | Semantic memory and code intelligence MCP server. |
| **LangChain MCP Adapters** | `langchain-mcp-adapters`; wraps MCP servers as LangChain tools. |

---

## 6. Model Routing

| Name | Notes |
|---|---|
| **vibe-llm-router** | Ollama-based router that directs prompts to appropriate model. |
| **@dev-ahmed/ai-router** | Uses Ollama as task judge for deterministic routing. |
| **Custom rule-based router** | Recommended for SIH: lightweight classifier + model registry inside orchestrator. |

---

## 7. Hardware Analysis & Model Compatibility

| Name | Notes |
|---|---|
| **llmfit** | Inspects CPU, RAM, GPU, VRAM; scores models on quality, speed, fit, context. |
| **bytefit** | Probes VRAM, RAM, NVMe bandwidth; hard anti-paging refusal. |
| **model-fit** | Computes real memory budget: weights + KV cache + overhead. |
| **calibr** | Measurement-based approach: runs actual models, measures tok/s, VRAM, paging. |
| **LocalAI-Advisor** | Windows hardware detection including CPU instruction sets, multi-GPU VRAM, RAM channels. |
| **llm-pulse** | `check` command gives "Can I run this?" verdict with GPU layer-offload guidance. |
| **LLMcalc (llm-infra-planner)** | Concurrent user capacity planning with SLO-aware TTFT/TPOT. |
| **local-llm-setup** | One-command detect, install, configure, smoke test. |
| **infrctl** | Local-first CLI for Ollama. |
| **RamaLama** | Container-native model deployment with OpenAI-compatible API. |
| **harbor** | Runs LLMs locally with minimal config, pre-connected to Open WebUI. |
| **chimeraforge** | Model-agnostic LLM deployment planner with 12 lifecycle commands. |
| **ic-engine** | Auto-picks local inference backend based on VRAM. |
| **AIMA** | AI Inference Managed by AI; single Go binary, K3S deployment, 61 MCP tools. |

---

## 8. Model Deployment & Inference

| Name | Notes |
|---|---|
| **Ollama** | Simplest local model deployment; no API key for localhost. |
| **vLLM** | Production GPU inference with PagedAttention, continuous batching. |
| **llama.cpp / llama-server** | `ggml-org/llama.cpp`; GGUF-native, CPU/GPU hybrid, OpenAI-compatible API. |
| **Docker** | Container runtime for sandbox and services. |
| **Podman** | Alternative container manager used by RamaLama. |
| **Kubernetes / K3S** | Used by AIMA for edge fleet management. |
| **Nginx / Go gateway** | Reverse proxy for API-key auth in front of llama.cpp. |
| **OpenAI SDK / OpenAI-compatible endpoints** | Standard API interface for local models. |
| **PagedAttention** | vLLM feature for KV cache management. |
| **Continuous batching / async batching** | Throughput optimizations in vLLM. |

---

## 9. Open-Weight Models

| Name | Notes |
|---|---|
| **Qwen2.5-Coder-7B-Instruct (GGUF)** | `liodon-ai/Qwen2.5-Coder-7B-Instruct-imatrix-GGUF`; coding tasks. |
| **DeepSeek-R1-Distill-Qwen-7B (GGUF)** | `unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF`; reasoning, summarization, drafting. |
| **Qwen2.5-VL-7B-Instruct (GGUF)** | `ggml-org/Qwen2.5-VL-7B-Instruct-GGUF`; vision, OCR, diagram understanding. |
| **Qwen3-Coder 30B-A3B** | MoE coding model; ~22GB at Q4_K_M. |
| **DeepSeek-R1-Distill-Qwen 14B** | Larger reasoning model. |
| **Llama 3, Mistral, Command A+** | General open-weight models mentioned as options. |
| **Gemma 3 27B, Mistral Small 3.2 24B, Qwen3 30B-A3B** | Models discussed in hardware sizing examples. |
| **Qwen 3.5-35B-A3B** | MoE model mentioned for 24GB GPU. |
| **Qwen2-VL-OCR-2B-Instruct-GGUF** | Smaller OCR model mentioned in critique. |

---

## 10. MCP Servers & Protocol

| Name | Notes |
|---|---|
| **MCP (Model Context Protocol)** | Standard for agent tool integration. |
| **LangChain MCP Adapters** | `langchain-mcp-adapters`; bridges MCP servers to LangChain/LangGraph. |
| **Docling MCP** | Document ingestion via MCP. |
| **Sandbox MCP** | Code execution via MCP. |
| **RAG MCP** | Vector DB queries via MCP. |
| **Office Worker MCP** | Document generation via MCP. |
| **File I/O MCP** | File read/write via MCP. |
| **Calculator MCP** | Sympy-based calculations via MCP. |

---

## 11. Air-Gap & Security

| Name | Notes |
|---|---|
| **iptables / nftables** | Host-level egress default-deny. |
| **tcpdump** | Network traffic capture for proof. |
| **ss / netstat** | Connection monitoring. |
| **nethogs / iftop** | Per-process bandwidth monitoring. |
| **Docker internal network** | No external gateway. |
| **Audit logging** | JSONL/SQLite logs of all tool calls and connection attempts. |
| **CVE-2025-53372** | Sandbox escape vulnerability in node-code-sandbox-mcp < 1.3.0. |
| **SecuritySecrets table** | Credential storage pattern mentioned in deployment doc. |

---

## 12. Supporting Libraries & Utilities

| Name | Notes |
|---|---|
| **SQLite** | Local checkpoints for LangGraph state. |
| **JSONL** | Audit log format. |
| **ONNX Runtime** | Backend for FastEmbed. |
| **PyPI packages** | `langgraph`, `langchain-mcp-adapters`, `docling`, `docling-mcp`, `qdrant-client`, `fastembed`, `office-worker-mcp`. |
| **Docker images** | `qdrant/qdrant`, `ghcr.io/ggml-org/llama.cpp:server-cuda`. |

---

## 13. Repositories Referenced by URL or Owner

- `Cicizz/OpenHarness`
- `HKUDS/OpenHarness`
- `rtmx-ai/aegis-cli`
- `GanyuanRan/Aegis`
- `pottekkat/sandbox-mcp`
- `docling-project/docling`
- `ggml-org/llama.cpp`
- `liodon-ai/Qwen2.5-Coder-7B-Instruct-imatrix-GGUF`
- `unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF`
- `ggml-org/Qwen2.5-VL-7B-Instruct-GGUF`
- `qdrant/qdrant` (Docker image)
- `ghcr.io/ggml-org/llama.cpp` (Docker image)

---

This list covers every framework, repository, tool, and model we have discussed. Some were recommended, some were verified, and some were mentioned as alternatives or cautionary examples. If you want, I can now consolidate this into a **final locked stack table** with only the components you will actually use for SIH 2026.
