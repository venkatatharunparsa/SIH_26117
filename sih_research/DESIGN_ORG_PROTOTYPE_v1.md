# Org design → prototype overlay — SIH26117

**Date:** 2026-09-16 (patched same day: red-team fixes merged; official-portal target)  
**Status:** Design lock for *shape*. Red-team kill items below are **closed on paper**. Stack still **not** locked. Code when user asks.  
**Target:** Official SIH **portal** idea PDF + a **portal-level prototype** (Expected Solution spine that can be shown). Not college-internal rounds.  
**Rule:** One architecture. Prototype is the same system at 1/100th scale, with mocks labelled.

**Roles:** User = decision maker. Assistant = Principal Solutions Architect + Principal Harness Engineer + Principal Research Engineer.

---

## 0. What we are doing

| Layer | Job |
|---|---|
| **Paper (org)** | Full industrial workbench: same boxes a plant would run |
| **Labels** | Every box is **REAL** / **MOCK** / **LATER** |
| **Build (later)** | Only the Expected Solution spine, as REAL boxes |
| **Show** | Working prototype + this diagram. Do not show a second architecture |

Jury line: *“Same logic as production. Demo is one GPU, small models, mock connectors. Scaling is GPUs, larger staged models, real APIs — not a rewrite.”*

---

## 1. Org-scale logical system (paper)

```
 IDENT / POLICY          INGEST              RETRIEVE           ACT                    DELIVER
 ┌──────────┐      ┌──────────────┐    ┌─────────────┐   ┌──────────────┐      ┌─────────────┐
 │ Identity │      │ OCR tool     │    │ Local KB    │   │ Agent loop   │      │ Word/Excel  │
 │ Policy   │─────▶│ VLM (vision) │───▶│ Entity tags │──▶│ Tool host    │─────▶│ PPT (later) │
 │ HITL     │      │ File ingest  │    │ Citations   │   │ Sandbox      │      │ Code+tests  │
 └──────────┘      └──────────────┘    └─────────────┘   └──────┬───────┘      └─────────────┘
                                                                │
                         LLM GATEWAY (software)                 │
                         task route · auth · timeout            │
                         Model Cards (not OpenAI spec)          │
                                          │ POST /v1/*          │
                                          ▼                     │
                         RUNTIME (weights + GPU)                │
                         OpenAI-compatible server               │
                         hardware probe · staged catalog        │
                                                                │
                         EGRESS MONITOR + AUDIT  (wraps all)    │
                         NEVER write DCS / SIS / PLC / permits  │
```

Connectors to plant systems sit **behind** ingest/retrieve as **read-only** sockets. They are not the workbench.

---

## 2. Prototype overlay (same boxes)

| Org box | Two-laptop prototype | One-box fallback |
|---|---|---|
| Analyst workstation | **Laptop B — RTX 3050 6 GB** — UI, agent, gateway, OCR(CPU), monitor. GPU **not** used for LLM | Same processes on one machine |
| GPU server | **Laptop A — RTX 4060 8 GB** — `/v1` + staged **one** 7B-class (or small VLM) at a time | Same runtime on localhost |
| Plant LAN / air-gap | Private LAN, **WAN unplugged**, plus host/packet log (not app-only) | Same |
| SAP / EAM / historian | JSON/CSV folders, **same schema as future API** | Same mocks |
| Venue mid-range GPU | Change gateway `base_url` only | Same |

Software on B does not know if A is a laptop, a venue GPU, or a plant vLLM. That is the industrial pattern.

---

## 3. REAL / MOCK / LATER

### REAL in prototype (must work, must not be theatre)

| Box | Why (PS) |
|---|---|
| Local inference via OpenAI-compatible `/v1` | Own GPU server; not locked to one model |
| Task router + **visible** routing log (≥2 task types) | Auto-select coding vs summary vs vision |
| Agent loop (plan → tools → iterate → stop) | “Act like an agent” |
| On-device OCR | Scanned PDFs / notes |
| Vision path (base64 images) **or fail closed** | Multimodal on-device |
| File read/write, spreadsheet tool | Listed tools |
| Sandbox code **run and verified** (`network=none`, separate from GPU server) | Coding task |
| python-docx from **structured fields** | Approval note as Word, not chat paste |
| Deterministic calc in sandbox (e.g. corrosion rate) | “Calculations with steps shown” |
| Local KB (folder or small index) + citations | Manuals/SOPs, nothing external |
| Classification + **draft** badges | HITL; not a decision-maker |
| Audit log (prompts, model id, tools, HITL) | Governance |
| Visible egress monitor, zero WAN | “Actual proof of the sovereign claim” |
| Air-gap demo (pre-staged weights; no pull) | Nothing leaves premises |

### MOCK (connector placeholders — honest in the pitch)

| Box | Prototype stand-in | Production socket |
|---|---|---|
| ERP / EAM / LIMS / historian / DMS / PTW / MOC | JSON/CSV with **same fields** | Read-only APIs |
| Identity | Local user + role | Plant IdP / AD |
| ACL | Role gate (engineer vs manager) | Source-system ACL inheritance |
| Audit sink | App log file | SIEM |
| Model quality | **7B–8B Q4 sequential** (8 GB fact). 14B is not the prototype plan | Larger staged open-weight |
| Template library | **One** inspection Word + one Excel | Plant template set |

Pitch sentence: *“In production this connector is read-only SAP EAM. Here it is a JSON folder with the same schema. The workbench does not care.”*

### LATER (on the org diagram, not built)

- Full RBAC inheritance, document classification workflow beyond a badge  
- PPT generation (Description lists it; Expected Solution does not require it)  
- Industrial P&ID symbol AI, handwriting as stretch  
- Multi-model **simultaneous** VRAM occupancy  
- Enterprise rate-limit farm, SSO, HA, multi-site DR  
- Any write to DCS / SIS / PLC / SCADA / F&G / live permits  

**Never**, even later on paper as an implemented feature: autonomous safety / commercial / statutory **decisions**. HITL stays.

---

## 4. Task taxonomy (router — this is the PS “auto selection”)

Routing is by **task**, not by VRAM. VRAM only **filters** which cards are legal.

| `task_type` | When | Needs | Typical role |
|---|---|---|---|
| `vision_extract` | Scan, photo, drawing page | `vision` and/or OCR tool | VLM **or** OCR then text model |
| `draft_note` | Approval note, summary | `chat` + tools | Drafter |
| `code_sandbox` | Generate/repair code | `tools` + sandbox | Coder |
| `calc` | Thickness, rates, units | **No LLM math** — sandbox Python | (router may skip LLM) |
| `kb_search` | Ground in SOP/manual | local retrieve tool | Any chat model |

**8 GB routing (closed):** cannot keep two LLMs loaded. **Unload / load.** Minimum legal auto-select for the PS:

- `vision_extract` = **CPU OCR** (+ optional small VLM if we unload the chat model first)
- `code_sandbox` = **different** 7B-class **coder** GGUF  
Log must show **two distinct `model` ids**. Using one 7B with two prompt labels is **rejected** (fake routing).

`draft_note` may reuse the coder or a second 7B instruct **after** unload; if VRAM allows only two cards total, prefer **OCR + instruct** then **coder**.

Fail closed: no VLM **and** OCR unusable → human message, do not hallucinate the scan.

---

## 5. LLM gateway contract (software socket)

Not the product. Not CUDA. Connects **workbench → OpenAI-compatible runtime**.

**In (from orchestrator)**

```
task_type, classification, user_role
messages[], optional images[] (already base64)
tools[] allowed for this step
timeout_s
```

**Gateway does**

1. Authorize: `Authorization: Bearer <api_key>` toward the runtime (dummy if the server ignores it).  
2. Load Model Cards ∩ `GET /v1/models`.  
3. Pick `model` for `task_type` (and optional classification).  
4. Timeout / max concurrent (thin; full rate-limit is LATER).  
5. `POST /v1/chat/completions` — LCD only (no `tool_choice`, no remote image URLs, no `/v1/responses`).  
6. Log: `{task_type, model, endpoint, tokens, tool_calls}`.

**Out:** completion or `tool_calls` back to the agent loop.

Hardware probe stays on the **runtime host** (`nvidia-smi`). Gateway may *read* “which models are staged”; it does not drive the GPU.

---

## 6. Binding spine — inspection → Word (do not lose this)

This is the workflow the rest of the design must serve.

```
1. HITL: engineer drops scanned inspection PDF
2. Policy: badge Confidential + Draft; no OT write
3. Ingest: rasterize pages
4. OCR tool (REAL, on-device) → text + confidence
5. Router: task_type=vision_extract
   - if VLM card staged: send page images as data:image/...;base64
   - else: OCR text only
6. Agent: extract structured findings
   {equipment_tag, points[], thicknesses[], units, date, source_page}
7. Entity resolve: **tool call** into mock EAM JSON (must actually query; no hardcoded tag in the prompt)
8. If numbers needed: task_type=calc → **same code sandbox**
   CR = (t_prev - t_curr) / Δt   print inputs; LLM does not invent CR
9. HITL: engineer sees **JSON fact sheet**, edits, **approves** — **hard gate**; draft cannot start without this
10. Router: `draft_note` → **different model id** than extract/coder pair as per 8 GB rule
11. Drafter fills template from **approved** fields only; missing = `NOT FOUND`
12. python-docx / openpyxl from those fields only — never paste raw chat
13. Citations: file / page / tag
14. HITL: download Word; still labelled DRAFT
15. Egress monitor: zero external destinations for 1–14
16. Audit: models used at 5 and 10 are different (or logged as two roles if sequential load)
```

**Coding spine (second PS bullet, same gateway):** user asks for a script → `code_sandbox` → generate → sandbox run tests → show pass/fail. Separate from inspection, same workbench.

---

## 7. Harness borrow (patterns only — no repo lock)

From `agentic_research/` and prior Mem0: **compose a thin orchestrator**. Steal workflows, do not fork a cloud laptop-agent as the SIH product.

| Pattern | Source class | Use in *our* loop |
|---|---|---|
| `base_url` + `api_key` + `model` | Continue / OpenHands / Cursor | Gateway LCD |
| Tools sealed; model cannot open raw network | Nabhi-style boundary | Tool host allow-list |
| Sandbox ≠ inference process | OpenHands / Cursor (WSL2 jail) | Docker Desktop `--network=none` for **generated code + tests + calc only** |
| HITL before sensitive write | Hermes-class | Fact-sheet gate (step 9) and Word download (step 14) |
| Plan → act → observe → iterate | Generic agent | Orchestrator |
| On-disk skills, progressive load | [agentskills.io](https://agentskills.io/specification) | **Prototype: 5 skills** (not LATER): `inspect-extract`, `inspect-calc`, `inspect-draft`, `code-sandbox`, `sovereign-policy` |

Reject as product: OpenRouter, always-on OS/browser control, “company brain” that syncs off-prem.

Licenses: only copy code after a named, OSI-compatible file is chosen. Not now.

---

## 8. Still not locked

- Runtime binary (Ollama vs vLLM vs LM Studio vs llama-server)  
- Exact 7B GGUF names (candidates only: instruct + coder + optional tiny VLM)  
- OCR engine, vector DB, orchestrator library  
- Official portal PPTX (user will share playbook/template)

---

## 9. Build order (portal-level prototype — when user says build)

Must be enough to support **official PDF** (diagrams from real boxes) and a **partial running spine** (portal/video/GitHub if the playbook requires it):

1. Gateway + **two** Model Cards + routing log with two model ids  
2. OCR → JSON fact sheet → HITL → Word (one template)  
3. Docker `--network=none` coding task **verified** (pytest visible)  
4. WAN unplug + host/packet egress view  
5. One-box fallback  

Do not build a platform before step 2 works. Do **not** put the GPU server inside the sandbox container.

---

## 10. Red-team issues — closed vs still open

You were right: they were **listed**, not **merged**. Merged now:

| Issue | Status |
|---|---|
| Fake routing (one model, two labels) | **Closed** — two GGUF ids, sequential unload on 8 GB |
| Chat pasted into Word | **Closed** — fact-sheet HITL gate → python-docx |
| LLM invents CR | **Closed** — calc in code sandbox |
| App-only egress monitor | **Closed** — WAN unplug **and** host/packet log |
| Mock EAM never queried | **Closed** — mandatory lookup tool |
| Vision HTTP URLs | **Closed** — base64 only (already) |
| Sandbox wraps GPU / host pytest | **Closed** — Docker jail for code only |
| Two models in 8 GB VRAM | **Closed** — sequential; 14B not prototype |
| Skills sprawl / skills marked LATER | **Closed** — five skills in prototype |
| “Nothing exists” uniqueness | **Closed** — gap vs Open WebUI stated |
| Official 6-slide PPTX filled | **Open** — waiting template + playbook |
| Running code / scan photograph | **Open** — not built; scan parked |
| Playbook keep/drop | **Open** — you will share; we will accept/reject rows |
| Venue Docker blocked | **Parked** — WSL fallback, weaker, disclose |

Paper can close process bugs. It cannot close “software does not exist yet.” That is the next build, not another red-team list.
