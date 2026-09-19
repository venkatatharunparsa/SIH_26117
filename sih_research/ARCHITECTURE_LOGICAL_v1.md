# Logical architecture v1 — SIH26117 Sovereign Workbench

**Date:** 2026-09-16  
**Status:** Locked at the *logical* layer. Runtime product (Ollama / vLLM / LM Studio / llama.cpp) is **not** locked.  
**Binding MVP:** Expected Solution in `sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`.

---

## 1. Planes (locked)

```
┌─────────────────────────────────────────────────────────────┐
│  WORKBENCH PLANE  (software, model-agnostic, no GPU needed) │
│  Laptop B / analyst PC / later plant workstation            │
│                                                             │
│  UI  →  Orchestrator  →  Policy  →  Tools  →  Deliverables  │
│                 │                                           │
│                 │  OpenAI-compatible HTTP only              │
│                 ▼                                           │
│         InferenceClient(base_url, api_key, timeout)         │
│         + ModelCards (OUR registry, not OpenAI spec)        │
└────────────────────────────┬────────────────────────────────┘
                             │  POST /v1/chat/completions
                             │  GET  /v1/models
                             │  Authorization: Bearer <key>
                             │  images: data:image/...;base64 only
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  RUNTIME PLANE  (hardware + weights; interchangeable)       │
│  Laptop A / venue GPU / plant vLLM / IndiaAI node           │
│                                                             │
│  OpenAI-compatible server                                   │
│  Local staged weights                                       │
│  Hardware probe (nvidia-smi / vendor ps) — NOT in OpenAI    │
│  Fit / recommend from local catalog                         │
└─────────────────────────────────────────────────────────────┘

SANDBOX (code exec) is a third plane: isolated, network=none.
It is NOT the inference server. Do not wrap the GPU runtime in
the same isolation boundary as untrusted generated code.
```

**Why two planes:** the problem statement requires “not locked to one model” and “addable later without redesign.” Hardware at the venue is unknown. Continue.dev, OpenHands, LM Studio, Ollama, vLLM, and llama-server all use the same three client fields: `base_url`, `api_key`, `model`.

---

## 2. OpenAI contract we actually depend on (lowest common denominator)

Verified against vendor docs (Ollama, vLLM, LM Studio, llama-server), not assumed:

| Use | Depend? | Evidence |
|---|---|---|
| `POST /v1/chat/completions` | **Yes** | All four servers |
| `GET /v1/models` | **Yes** (liveness / names only) | All four; returns **ids**, not capabilities |
| `messages` text | **Yes** | Spec |
| `tools` + `tool_calls` round-trip | **Yes, with fallback parser** | Supported on paper; small local models + unconstrained servers often emit malformed calls |
| `stream` | Prefer | Supported; do not require streaming+tools together |
| `temperature`, `max_tokens` | **Yes** | Spec |
| Vision as `image_url` **data URI / base64** | **Yes for multimodal** | Ollama: remote HTTP image URLs **not** supported. Air-gap forbids fetch anyway |
| `Authorization: Bearer` | **Always send** | Ollama: key required by SDK, **ignored**. LM Studio/vLLM/llama-server: optional or required depending on flags |
| `tool_choice` | **No** | Ollama documents it unsupported |
| Remote `https://...` image URLs | **No** | Breaks Ollama + air-gap |
| `POST /v1/responses` | **No** | Newer, uneven (Ollama vision on Responses was a gap) |
| `GET /v1/models` as capability discovery | **No** | Official Model object is `id`, `object`, `created`, `owned_by` only — **no vision/tools/VRAM** |
| Hardware / VRAM endpoint | **Does not exist in OpenAI** | Probe is **our** sidecar or `nvidia-smi` on the runtime host |

**Implication (this is the red-team correction):** “OpenAI-compatible keys for any model” is true for **transport**. It is **false** for **routing**. Routing needs **our Model Cards**.

---

## 3. Model Cards (software, lives in the workbench plane)

A card is config, not weights. Adding a model = add a card + stage weights on some runtime. No redesign.

```yaml
id: qwen2.5-14b-instruct          # string we send as `model`
display_name: Qwen 2.5 14B
roles: [draft, classify, code]    # what we MAY route here
capabilities:
  chat: true
  tools: true                     # claimed; still probe at runtime
  vision: false
  embeddings: false
constraints:
  min_vram_mb: 10000              # estimate, Q4, ~8k ctx, ~20% headroom
  context_tokens: 8192
  sequential_only: true           # mid-range: one active model
endpoint_profile: default         # which base_url/api_key
```

**Probe sequence (runtime-agnostic):**

1. Workbench reads cards (local YAML/SQLite).
2. `GET {base_url}/models` → intersection: card.id must be **listed or loadable**.
3. If the runtime exposes a **non-OpenAI** hardware sidecar (optional), filter by VRAM. If not, trust the card + fail if the server 500s on load.
4. Task classifier asks for required capabilities (`vision` vs `code` vs `draft`).
5. Pick the first card that matches role + capabilities + is staged. If none: **fail closed** (human message), never send a PDF to a text-only 8B.

Hardware suggestion (“Ollama-like”) is a **runtime-plane** job: `nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv` plus a local catalog. Ollama `/api/ps` `size_vram` is a **reservation**, often ≠ `nvidia-smi`. Do not treat vendor `ps` as gospel.

---

## 4. Workbench components (logical, no framework)

| Component | Job | Must not do |
|---|---|---|
| **UI** | HITL: ingest, approve, edit, export | Call cloud; hide citations |
| **Orchestrator / agent loop** | Plan → tool calls → iterate → stop | Assume one model; write DCS/SIS/PLC |
| **InferenceClient** | OpenAI LCD only | Vendor SDKs as the only path |
| **Router** | Task class → card → model id | Fake routing logs with one model |
| **Policy** | Classification badge, no-write to OT, HITL gates | Pretend production ACL inheritance |
| **Tool host** | file r/w, OCR, spreadsheet, KB search, sandbox exec, docx/xlsx/pptx | Network egress |
| **OCR tool** | Deterministic on-device OCR (PS says OCR **and** vision) | Cloud OCR |
| **Vision path** | If card.vision: attach base64 image to chat | HTTP image URLs |
| **Deliverable builders** | python-docx / openpyxl / pptx from **structured fields** | Paste chat into .docx |
| **Local KB** | Folder / index of manuals, SOPs (mock OK) | External search |
| **Egress monitor** | Visible log: dest, deny, zero WAN | “We were offline” without proof |
| **Audit** | Prompts, tools, model id, hashes, HITL | |

**Agent loop honesty:** local tool-calling is **not** uniform. Same weights can succeed on llama.cpp (grammar-constrained) and fail on unconstrained parsers (Ollama-class). Workbench must: (a) prefer structured `tool_calls`; (b) fallback-parse common text formats; (c) retry once; (d) HITL if still invalid. Do not claim “any model is an agent.”

---

## 5. Runtime components (logical)

| Component | Job |
|---|---|
| OpenAI-compatible HTTP server | `/v1/chat/completions`, `/v1/models` |
| Staged weights directory | USB / local disk; **no internet pull in demo** |
| Hardware probe | GPU name, VRAM total/used, CPU fallback |
| Fit table | Catalog ∩ VRAM → recommended roles |
| Load / unload | Sequential on mid-range VRAM |

“Pull any model” in the jury script means **load from local disk**, not `ollama pull` from the WAN.

---

## 6. Expected Solution mapped to planes

| PS bullet | Who | How |
|---|---|---|
| Mid-range GPU / smaller model if 120B absent | Runtime | Cards for 8B/14B/32B-class; venue = change `base_url` |
| Auto-select ≥2 task types | Workbench router | e.g. vision/extract card vs code/draft card; logs show `model` |
| Scan → findings → Word approval | Both | OCR tool ± VLM → structured JSON → python-docx; HITL |
| Coding verified in sandbox | Workbench + sandbox plane | Generate → `network=none` run tests → show output |
| Multimodal | Workbench + vision card | Base64 image; fail closed if no vision card staged |
| Zero external calls | Egress monitor + air-gap LAN | Pre-stage everything |

Two-laptop mapping: A = runtime plane, B = workbench plane. One-box: both planes on one compose/profile. Same software.

---

## 7. Org-scale (design, not build)

Same workbench. Runtime becomes plant vLLM/TGI/LiteLLM gateway. Cards point at named endpoints (`ocr-vlm`, `coder`, `drafter`). Policy inherits plant classification later. Mock connectors stay labelled mocks until real EAM/ERP exists. **Never** write DCS/SIS/PLC.

---

## 8. Explicitly not locked

- Ollama vs vLLM vs LM Studio vs llama-server vs LiteLLM gateway
- Exact three GGUFs (needs measured VRAM)
- Orchestrator library (LangGraph etc.)
- OCR engine (Tesseract / Paddle / EasyOCR)
- Vector DB vs folder grep for prototype KB

---

## 9. Red-team findings that changed the design

1. **OpenAI does not carry hardware or capability metadata.** Cards are mandatory.
2. **Ollama vision requires base64; remote URLs unsupported.** LCD = data URIs.
3. **`api_key` is not “OpenAI cloud.”** Dummy on Ollama; real token if the server enables auth.
4. **Tool calling is model+server dependent.** Agent loop needs a parser fallback; coding sandbox remains the verifier.
5. **Vendor VRAM stats disagree with nvidia-smi.** Probe nvidia-smi as source of truth when present.
6. **SIH venue GPU is still unverified.** Architecture does not depend on it.
