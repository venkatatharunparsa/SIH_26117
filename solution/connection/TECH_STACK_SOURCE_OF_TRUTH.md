# KWB — Tech stack (source of truth)

**Date:** 2026-09-18  
**Status:** **OPEN FOR VERIFY** — **brands not locked**. Interfaces and policies **are** locked by freezes.  
**Companion diagram:** `ARCHITECTURE_HIGH_LEVEL.md`  
**Rule:** Prefer a **SoT row** over inventing a library. If no SoT → mark **HYPOTHESIS** and do not treat as binding.

---

## 0. How to read this document

| Status | Meaning | May ship as “decided”? |
|---|---|---|
| **LOCKED** | Interface / policy from binding freeze or Official PS | Yes — brand may still vary |
| **PATTERN** | Adopted *shape* from repo map / freeze; not a fork | Use pattern; check license later |
| **CANDIDATE** | Named brand allowed as interchangeable option | **No** until DM lock + overlay |
| **REFUSED** | Explicitly out | Never for must-work |
| **HYPOTHESIS** | Convenient default for SIH build; **not** a freeze | Needs explicit DM accept |

### Source-of-truth rank (highest wins)

| Rank | Source | Examples |
|---|---|---|
| **1 Official** | SIH Expected Solution / Description / Title | Mid-range GPU local; Word path; WAN=0 |
| **2 Binding freeze** | `solution/WP-*_FREEZE.md` | Gateway `/v1`; k=5; de-Docker |
| **3 Design input** | `DESIGN_REPO_MAP_v1.md`, agendas | Adopt/refuse patterns |
| **4 Research** | `sih_research/`, `agentic_research/` | Feasibility notes |
| **5 Hypothesis** | This file’s SIH-leaning picks | FastAPI, SQLite, … |

Conflict rule: **Official + Freeze beat this file.** Update this file when a freeze changes.

---

## 1. LOCKED contracts (brand-agnostic)

These must be true in any implementation.

| Layer | Locked contract | SoT |
|---|---|---|
| Planes | Workbench **≠** runtime **≠** sandbox; no weights in workbench | WP-00, WP-10, WP-16 |
| Client API | Workbench is **OpenAI-compatible client** to local `/v1` only | WP-00, WP-09, WP-10 |
| Wire shape | `POST /v1/chat/completions`; `GET /v1/models` = **liveness only** (not Model Cards) | WP-09, WP-24 |
| Gateway | **Only** gateway opens runtime socket; verify auth/schema/card/local endpoint/params/size/timeout/`grant_id`/vision | WP-09, WP-20 F3 |
| Runtime shape | One local `/v1`, many `model` ids, **one** API key multiplex; quant OK; pre-load 2 demo; LRU; **enable ≠ loaded**; org GPU-only | WP-10 |
| Cards | Model Card catalog; UI model-agnostic; OCR+LLM kinds required; fail closed if id not on card | WP-24 |
| Doc artefact | Must-work = **`.docx`**; PDF when possible; deliverable ≠ chat transcript | WP-00, WP-01 |
| Plant I/O | Pluggable **read-only** connectors; never write DCS/EAM/ERP/DMS SoR; outputs only in KWB store | WP-00, WP-02 |
| Ingest | Pre-LLM path; H1 before KB; drafter gets **normalized extract** (not raw binary); no auto-promote to org index | WP-03, WP-11 |
| Images | **`data:` / local only**; deny `http(s)` image URLs | WP-00, WP-03, WP-09 |
| Grants | Session ≠ task grant; TTL; ceiling; revoke | WP-04 |
| HITL | H1–H12 + stale re-approval; human ultimate verifier; no auto DRAFT→record | WP-00, WP-05 |
| Orch | Software brain of **app loop**; not plant Approver | WP-06, WP-20 F7 |
| RAG | Authz-**first**; lexical/MOCK must-work; top-k=**5** demo; cite source+revision/`revision_unknown`; index ≠ SoR | WP-11 |
| Claims | Three-source + H7 (file / user / policy) | WP-00, WP-22 |
| Pack / trust | Packer + T0–T4 untrusted content classes | WP-21, WP-23 |
| Gates | Before unmasked view / export | WP-12, WP-20 F2 |
| MCP | stdio / 127.0.0.1; Admin allowlist; **grant ∩ allowlist**; egress default deny; no public registry at runtime | WP-08 |
| Sandbox | Network **none**; 60s default; no pip/WAN; ≠ GPU process; calc-in-jail; pass/fail = evidence (H9); **de-Docker** | WP-16 |
| Monitors | A = host evidence pack / snapshot (not CERT); B = operator page | WP-13 |
| Audit | Append-only; fail-closed on write fail | WP-17 |
| Offline | USB stage; no cloud LLM / public `base_url` / HF-in-UI | WP-19, WP-00 Never |
| Done bar | **G1–G10** / `eval/` spine before org ambition | WP-18, WP-20 F6 |
| Air-gap claim | Controls **help**; not CERT-In / plant certification badge | WP-20 F5 |

---

## 2. REFUSED (do not pick for must-work)

| Refuse | Why | SoT |
|---|---|---|
| Cloud OpenAI / Anthropic / openrouter.ai as brain | Nothing leaves | Official + WP-00 Never |
| Ollama / Open WebUI / AnythingLLM **as the KWB product** | Chat+RAG ≠ Expected Solution | WP-24, WP-11, Repo map |
| LiteLLM public provider mesh / WAN failover | Fail-open to internet | WP-09, WP-24 |
| HF download in UI | Offline Never | WP-24 |
| Docker Desktop as **only** sandbox path | de-Docker | WP-16 |
| E2B / cloud sandbox | WAN | WP-16 |
| Chroma-as-DMS / “indexed the plant” theatre | Index ≠ SoR | WP-11 |
| Graphiti / Neo4j as uniqueness / must | Not Expected Solution | WP-11, Repo map |
| Mem0 as plant KB | Conversation ≠ plant truth | WP-11 |
| Temporal/Camunda as SIH spine | Demo ≠ workflow cluster | Repo map |
| Fork DeerFlow / OpenHands / Nabhi as product | Wrong job | Repo map |
| PPT/Excel/live DMS as must until overlay REAL | Description overhang | WP-00, WP-20 §8 |

---

## 3. PATTERN adopts (shape only — not brand lock)

| Area | Pattern to copy | Not to fork | SoT |
|---|---|---|---|
| Word/Excel libs | `python-docx` / `openpyxl` as libraries | Chat→docx hacks | Repo map WP-01 |
| Connectors | Onyx-style connector + RBAC layer | Onyx actions that write plant | WP-02, Repo map |
| HITL | Interrupt / resume; human promotes drafts | Auto-merge to SOP | WP-05, Repo map |
| OCR engines | Tesseract and/or PaddleOCR **candidates** | Cloud Document AI | Repo map WP-03 |
| RAG pipeline | Haystack / LlamaIndex *pipeline shape* | Their product UI | WP-11 |
| Client triad | `base_url` + `api_key` + `model` (Continue/OpenHands class) | Cloud model defaults | WP-09/24 |
| MCP | Spec + local stdio/localhost SDK; FastMCP for *our* demo servers | Public MCP registry servers | WP-08 |
| Guardrails | Presidio / NeMo *ideas* offline | Cloud moderator APIs | WP-12, WP-23 |
| Traces | Self-host Langfuse/Phoenix *pattern* | Cloud upload | WP-17 |
| Isolation menu | Podman/Docker `--network=none` **or** non-Docker jail | K8s Agent Sandbox as must | WP-16 |

---

## 4. CANDIDATE brands (interchangeable — **OPEN**)

Pick **one** per row at lock time. Any choice must still satisfy §1.

| Slot | Candidates (any one) | Must satisfy | SoT |
|---|---|---|---|
| Runtime `/v1` server | **Demo: Ollama** · **Org: vLLM** (llama.cpp spare) | Local `/v1`; multi-id; quant; probe GPU/VRAM | WP-10 + DM 2026-09-19 |
| **Optional offline proxy** | LiteLLM / Envoy AI Gateway / Portkey **only if** offline + **empty** public provider list | Same gateway Never; else **REFUSED** | Repo map WP-09 + WP-09 refuse |
| **Sandbox jail** | Podman · Docker (not Desktop-mandatory) · OS job object / bubblewrap / nsjail | network-none; caps; ≠ GPU | WP-16 |
| **Org isolation (ambition)** | gVisor · Firecracker · nsjail | Same controls; not SIH must | WP-16, Repo map |
| **OCR** | Tesseract · PaddleOCR · (VLM card via same `/v1`) | Pre-LLM path; H1 before KB | WP-03 |
| **Vector index** | *Unset* — lexical/MOCK must-work; hybrid ambition. **Chroma is not a candidate as DMS** | Authz-first; k=5; not SoR | WP-11 |
| **Orch framework** | Thin custom loop · LangGraph *candidate* | Interrupts; no safety autonomy | WP-06 |
| **Secret/PII scan** | Presidio-class local · light regex | Honesty; block on hit | WP-12 |
| **MCP demo server** | FastMCP (or equivalent) for **our** MOCK stdio server | Local only | WP-08 |
| **UI shell** | *Unset* | Artefact-first (docx), not chat-as-product | WP-00, WP-01 |

---

## 5. SIH prototype lean (HYPOTHESIS only)

**Not binding.** Proposed defaults for a fast G1–G10 spine after REAL/MOCK/LATER. Replace freely if §1 holds.

| Slot | Lean | Why | SoT rank |
|---|---|---|---|
| Workbench language | **Python 3.11+** | Docx, MCP Python SDK, sandbox calc | Hypothesis |
| Workbench API | **FastAPI** | Local service; **not named in any freeze** | Hypothesis |
| Session/grants store | **SQLite** (+ JSON grants) | Offline single-node demo | Hypothesis + WP-04 MOCK users |
| KWB artefact store | Filesystem versions + SQLite metadata | WP-02 store; no plant write | Hypothesis |
| Lexical retrieve | Whoosh / SQLite FTS5 / plain ranked files | WP-11 lexical must | Hypothesis |
| Embeddings / vector | **LATER** unless G-goldens need hybrid | WP-11 hybrid = ambition | Freeze |
| Runtime (demo) | **llama.cpp** *or* **Ollama** as `/v1` only | Shallow HW; quant; Windows-friendly | Candidate |
| Docx | **python-docx** | Expected Solution Word | Pattern |
| Sandbox (Windows demo) | Process jail / job object; Podman if available | de-Docker | WP-16 |
| MCP demo | One local **stdio** FastMCP server | WP-08 | Pattern |
| Frontend | Minimal local UI (framework **unset**) | Artefact + HITL pages | Hypothesis |
| Eval harness | Scripts under `eval/` | WP-18 | Freeze |

Lock rule: promote a lean row from **HYPOTHESIS → LOCKED brand** only by DM + short note in this file’s changelog.

---

## 6. Map: architecture box → stack slot

| Architecture box (`ARCHITECTURE_HIGH_LEVEL.md`) | Stack slot | Status |
|---|---|---|
| Workbench UI | Frontend | HYPOTHESIS unset |
| Session / Grant | SQLite + grant JSON | HYPOTHESIS |
| Orchestrator | Thin loop / LangGraph candidate | CANDIDATE |
| Specialists / skills | In-process + `.md` skills | LOCKED pattern (WP-07/15) |
| Templates | docx templates + python-docx | PATTERN |
| Ingest OCR/VLM | Tesseract/Paddle + VLM card | CANDIDATE |
| Authz-first RAG | Lexical must; vector later | LOCKED policy |
| Packer / Gates / Audit | Workbench modules | LOCKED behaviour |
| Gateway | OpenAI-shape client verify suite | LOCKED interface |
| Runtime | llama.cpp / vLLM / Ollama / … | CANDIDATE |
| Sandbox | Podman/Docker/non-Docker jail | CANDIDATE |
| MCP host | MCP SDK local | PATTERN |
| Monitors A/B | Host snapshot + UI page | LOCKED behaviour |
| Offline USB | Import UI + Admin enable | LOCKED behaviour |

---

## 7. Demo vs org stack posture

| Concern | Demo | Org |
|---|---|---|
| Runtime device | GPU+CPU OK; honest string on Monitors | GPU-only |
| Models | ≤3 cards; quant; pre-load 2 | More cards; LRU |
| Retrieve | Lexical MOCK packs | Hybrid ambition + live connectors |
| IdP/SSO | MOCK local users | Org ambition |
| Continuous WAN monitor | Snapshot A | Continuous A ambition |
| SHA/quarantine USB | Size + eyeball OK | Ambition |

---

## 8. Explicit “stack / brand not locked” (freeze quotes)

| Freeze | Statement |
|---|---|
| WP-00 | Stack not locked |
| WP-02 | Stack / vendor brands not locked |
| WP-03 | Stack / OCR / VLM brands not locked (candidates only) |
| WP-08 | Stack / MCP SDK brand not locked |
| WP-09 | Stack / proxy brand not locked |
| WP-10 | Runtime binary brand not locked |
| WP-11 | Stack / vector DB not locked |
| WP-16 | Isolation brand not locked (Docker/Podman or non-Docker jail) |
| WP-24 | Stack / serving brand not locked |
| DESIGN_REPO_MAP | Not a stack lock; candidates until DM says lock |

---

## 9. Verify checklist

1. §1 matches freezes (no brand smuggled in as LOCKED).  
2. §2 refuse list still matches WP-00 Never + repo map.  
3. §5 lean is acceptable as **hypothesis** only — or name replacements.  
4. Diagram file stays brand-free; this file owns brands.

Reply **stack verify OK** (or list fixes). Brand lock happens **after** WP-20 freeze + REAL/MOCK/LATER overlay unless you order otherwise.

---

## 10. Changelog

| Rev | Date | Change |
|---|---|---|
| **0.1** | 2026-09-18 | Initial SoT: locked contracts, refuse, candidates, SIH lean hypotheses |
| **0.2** | 2026-09-18 | Align with freeze audit: wire shape, ingest/images, MCP grant∩allowlist, sandbox 60s/no-pip, conditional offline proxy, Chroma-not-candidate, explicit “not locked” table |
