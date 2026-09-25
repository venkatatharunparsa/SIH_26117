# Repo pull map — clone → extract → compose KWB

**Date:** 2026-09-19  
**Status:** **ACTIVE** — see also **`REPO_EXTRACT_VERIFY.md`** (one-page verify for desk build)  
**Product:** Knowledge Work Bench  
**SoT:** `REPO_EXTRACT_VERIFY.md` · `OPENHANDS_EXTRACT.md` · `../freezes/` · `DEMO_TECH_STACK.md`

**Rule:** We **clone for study and slice**. We do **not** fork an agent OS as the product. License check before pasting code.

---

## Method

```text
1. Map each REAL box → repo / library
2. Clone shallow into vendor/ (study) OR pip install (runtime dep)
3. Extract only the needed pattern/file into backend/
4. Wrap with OUR grants / HITL / gateway / Word / WAN=0
5. Prove with G1–G10
```

---

## Global refuse (do not clone-as-product)

| Repo class | Examples | Why |
|---|---|---|
| Agent OS fork | OpenHands, DeerFlow, Hermes, OpenClaw | Wrong product job |
| Chat+RAG UI | Open WebUI, AnythingLLM, PrivateGPT | Not Word/HITL/WAN proof |
| Cloud brain | NabhiPersona sync, LiteLLM public providers | Breaks air-gap |
| Browser/computer-use | Browser Use, Open Interpreter | WAN + shadow IT |
| Graph-as-product | Neo4j, Graphiti, Cognee | Not Expected Solution |

---

## Map: demo need → source → extract → ours

| KWB need (REAL) | G# | Source | How we take it | We add |
|---|---|---|---|---|
| Local `/v1` client triad | G1,G8 | **Continue** / OpenHands client pattern | Study; write thin `httpx` client | Card check, grant_id, deny WAN |
| Runtime serve | G1 | **Ollama** *or* **llama.cpp** server | Install binary (not fork into app) | Model Cards; sequential load |
| Word DRAFT | G2 | **python-docx** (PyPI) | `pip` | Templates + DRAFT badge + HITL |
| OCR | G4 | **Demo framework:** **Tesseract** + `pytesseract` (+ pypdf). **Org SoT:** OCR model (later) | System + pip | H1 gate; fail closed; fixture stub if binary missing |
| Sandbox ≠ GPU | G3,G10 | **OpenHands** jail idea; Docker/`network=none` or process jail | Study OpenHands sandbox docs; implement thin runner | de-Docker; calc-in-jail; H9 |
| MCP host (MOCK later) | — | **MCP Python SDK** + **FastMCP** | Clone SDK; write one local server | Allowlist; egress deny |
| Secret/PII gate | G9 | **Presidio** (idea + pip) | `pip` analyzer or light regex first | Bind to export gates |
| HITL interrupt | G2,H* | **LangGraph** interrupt *pattern* | Pattern only (optional dep later) | H1–H3/H9 hard gates |
| Authz retrieve MOCK | G6 | Local files; Onyx *intent* | No Onyx fork | Grant filter; NOT FOUND |
| Audit JSONL | G5+ | Langfuse *self-host pattern* | Already have `audit.py` | grant, model_id, HITL fields |
| Skills on disk | — | **Agent Skills** spec | Folder layout `SKILL.md` | Progressive load under grant |
| Egress proof | G5 | Host snapshot (ours) | Write script | Audience A start/stop |

---

## Clone waves

### Wave 0 — no clone (pip / system) — start immediately

```text
pip: fastapi uvicorn httpx pydantic-settings pyyaml python-docx python-multipart pytesseract
optional later: mcp presidio-analyzer
system: Tesseract OCR (if G4 REAL)
runtime: DEFERRED — workbench uses configurable local /v1 URL (hardware later)
```

### Wave 1 — done (shallow clones in `vendor/`)

| Repo | Path | Status |
|---|---|---|
| MCP Python SDK | `vendor/python-sdk/` | Cloned (MIT) |
| FastMCP | `vendor/fastmcp/` | Cloned (Apache-2.0) |
| OpenHands Agent Canvas | `vendor/OpenHands/` | Cloned (MIT) — **UI study only** |
| OpenHands **software-agent-sdk** | `vendor/software-agent-sdk/` | Cloned (MIT) — **primary extract** |

Detail: `OPENHANDS_EXTRACT.md` (workbench first; hardware later).  
**Required slices copied to:** `KWB/required/` (see `KWB/README.md`).

### Wave 2 — pulled via web into `KWB/` (not vendor clones)

Study-only slices; do **not** vendor-merge. Index: `KWB/PULL_INDEX.md`.

| Repo | KWB folder | Why look | Extract limit |
|---|---|---|---|
| Continue | `KWB/from_continue_web/` | `base_url`+`model` client | Notes only; we write thin httpx gateway |
| Onyx | `KWB/from_onyx_web/` | Connector/ACL intent | MOCK JSON schema only; **`ee/` blocked** |
| Haystack | `KWB/from_haystack_web/` | Pipeline shape | Function outline, not product UI |
| LlamaIndex | `KWB/from_llamaindex_web/` | Citation shape | Function outline, not product UI |
| Presidio | `KWB/from_presidio_web/` | PII patterns | Or pip package |
| LangGraph | `KWB/from_langgraph_web/` | interrupt/resume HITL *pattern* | Notes only |

**Still refuse / missing:** DeerFlow (product refuse) · GBrain (not extracted this pass).

### Wave 3 — never clone for product

DeerFlow, Open WebUI, AnythingLLM, LiteLLM-with-cloud-providers, Browser Use, Graphiti-as-core.  
Do **not** ship Agent Canvas as KWB UI.

---

## Folder layout after pull

```text
SIH26/
  KWB/                      ← required OpenHands slices + Wave 2 web study
    required/01_…06_
    from_*_web/             ← Continue / Onyx / Haystack / LlamaIndex / Presidio / LangGraph
  vendor/
    python-sdk/
    fastmcp/
    OpenHands/              ← Agent Canvas (study)
    software-agent-sdk/     ← full SDK (source of KWB copies)
  backend/                  ← OUR product (compose here)
  solution/                 ← freezes + this map
```

---

## Compose order (workbench first)

| Day focus | Pull | Build in `backend/` |
|---|---|---|
| 1 | Wave 1 done | sandbox · gateway stub · audit (hardware deferred) |
| 2 | — | grants · cards · router G1 · deny G8 |
| 3 | — | Word G2 · OCR G4 · H1 |
| 4 | — | calc-in-jail G3/G10 · gates G9 · NOT FOUND G6 · revoke G7 |
| 5 | Runtime pick | Point gateway `base_url` at chosen local `/v1` |
| 6 | MCP if time | MOCK MCP · Monitor A G5 · eval/ |

---

## License gate (before copy-paste)

| Source | Typical license | Action |
|---|---|---|
| python-docx, httpx, fastapi | permissive | OK via pip |
| MCP SDK / FastMCP | MIT / Apache-2.0 | OK; attribute |
| OpenHands / software-agent-sdk | MIT | Prefer reimplement thin slice; attribute if copy |
| OpenViking | AGPL | **Pattern only** — do not embed |

---

## Next actions

1. ~~Clone Wave 1~~ done.  
2. Compose `sandbox.py` + `gateway.py` (workbench).  
3. Grants · cards · G1–G10 spine.  
4. **Later:** pick Ollama / llama.cpp / vLLM and set `llm_base_url`.
