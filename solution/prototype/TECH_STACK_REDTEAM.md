# KWB — Tech stack adversarial red-team + best picks

**Date:** 2026-09-19  
**Status:** **RESEARCH COMPLETE** · external critique **verified** in `TECH_STACK_VERIFY.md` · **NOT ultimate lock** until DM says Lock
**Attack surface:** SIH26117 Expected Solution + locked flow A→J + F1–F7 + Windows demo laptop + offline + Word + self-HITL + G1–G10  
**Rule:** Best = survives red-team for **must-work demo**, not “coolest in atlas.”

---

## Attack criteria (what we used to kill options)

| Attack ID | Kill if… |
|---|---|
| **A1 Offline** | Needs WAN / cloud API / HF-in-UI |
| **A2 Wrong product** | Becomes chat+RAG skin (Open WebUI class) |
| **A3 Windows demo** | Only works on Linux namespaces / K8s |
| **A4 de-Docker** | Must have Docker Desktop to pass G3 |
| **A5 Cite honesty** | Encourages fake citations / no abstain |
| **A6 Overbuild** | Blocks G1–G10 spine before jury |
| **A7 Plane mix** | Puts weights / GPU inside workbench or sandbox |
| **A8 Hierarchy** | Forces in-app Approver queue (contradicts T3) |

---

## Scoreboard — BEST vs killed

| Layer | **BEST (recommend lock)** | Strong runner-up | Killed / deferred | Why BEST survives |
|---|---|---|---|---|
| Workbench language | **Python 3.11+** | — | Node-only backend | docx, OCR, sandbox, MCP SDK live in Python; dual runtime = A6 |
| Workbench API | **FastAPI + Uvicorn (127.0.0.1)** | — | Flask (weak streaming); Django (A6); cloud API (A1) | Async agent loop + Pydantic + OpenAPI; industry default for local agent backends |
| Task-desk UI | **React + Vite SPA** (Claude artifact desk layout) | SvelteKit static SPA | Next.js SSR (needless server); Open WebUI skin (A2); Electron first (A6) | Internal tool / desk = Vite SPA; chat-left / **DRAFT canvas-right**; FastAPI separate |
| Word DRAFT | **docxtpl (Jinja in Word) + python-docx** | python-docx alone | Pandoc-as-primary; cloud doc APIs | Company templates = Word-maintained; Expected `.docx`; PDF via LibreOffice **optional later** |
| Audit | **JSONL append-only + SHA-256 prev_hash chain** | + SQLite index later | Cloud Langfuse; SQLite-only “truth” | Jury can open file; tamper-evident; research consensus JSONL=canonical stream |
| Session / grants store | **SQLite** | JSON files | Cloud IdP | Single-node offline; grant revoke G7 |
| OCR | **Tesseract primary + fixture fallback** | PaddleOCR if scans fail quality | Cloud Document AI (A1); EasyOCR as default (VRAM) | Cold-start + Windows-friendly; H1 still required; fixture keeps G4 alive |
| Retrieve (demo) | **Grant-filter → lexical (SQLite FTS5 / BM25) k≤5** | Hybrid later | Chroma-as-DMS theatre; live plant DMS | Authz-first; exact SOP tags; A5 less likely than pure vector |
| Knowledge verifier | **Rule cite-or-abstain** (claim↔chunk id or NOT FOUND) | — | “Second LLM says OK” alone | G6; CiteGuard-class; machine check ≠ HITL |
| Orchestrator | **Thin custom Python loop** | LangGraph interrupt *pattern* only | DeerFlow/OpenHands fork (A2/A6) | We own grants/HITL/Word; frameworks as ideas |
| Sandbox | **Process jail must-work** (timeout, cwd jail, strip secrets; Win Job Object when available) + **optional** Docker/Podman `--network=none` | WSL2 Docker optional | E2B/cloud (A1); bubblewrap-only (A3); Docker Desktop mandatory (A4) | WP-16 de-Docker; Windows demo survives |
| Gateway / runtime client | **httpx → local OpenAI `/v1` only** | — | Public base_url; LiteLLM public mesh | Cards + grant + deny WAN |
| Runtime server (demo) | **Ollama first** (ease) **or llama.cpp server** (control) — **pick at hardware phase** | vLLM if shared GPU | Cloud providers | Both expose `/v1`; workbench unchanged; **still deferred OK** |
| Secret gate | **Local regex + optional Presidio** | — | Cloud moderator | G9 |
| MCP | **One local FastMCP MOCK** after G1–G5 | — | Public registry | WP-08 |
| WAN proof | **Host snapshot script** (start/stop) | — | Continuous WAN product | G5 |

---

## Red-team detail (attacks that changed the pick)

### API — why FastAPI wins
- **Attack:** Flask + long sandbox/LLM waits → streaming/concurrency pain.  
- **Attack:** Django → auth/admin tax, wrong shape for agent loop (A6).  
- **Attack:** Node API + Python tools → two stacks for SIH (A6).  
- **Survive:** FastAPI stays local 127.0.0.1; no cloud.

### UI — why React+Vite, not Next, not Open WebUI
- **Attack:** Next.js SSR assumes a Node server you do not need offline (A6).  
- Research: dashboards / internal tools → **Vite SPA**.  
- **Attack:** Open WebUI = chat product identity (A2) — refuse even if “pretty.”  
- **Claude-like** = layout pattern (artifact canvas + side evidence), **not** Anthropic cloud.

### Word — why docxtpl + python-docx
- **Attack:** python-docx alone fights company template layout.  
- **Attack:** Pandoc weak on exact corporate Word.  
- **Survive:** Admin/designer edits `.docx` template; app fills Jinja; DRAFT badge via python-docx post-pass.

### Audit — why JSONL + hash chain
- **Attack:** “Pretty dashboard only” without exportable file → jury cannot take evidence.  
- **Attack:** SQLite alone is queryable but **not** the evidence story; can be silently edited.  
- Research (AI audit trails / AIAuditLog class): **JSONL canonical** + optional hash chain; SQLite index optional.  
- **Honest limit:** hash chain is tamper-**evident**, not immutable if attacker rewrites whole file — still enough for SIH honesty + G-pack.

### OCR — why Tesseract first
- **Attack:** PaddleOCR accuracy win but heavier install / framework risk on demo day (A6).  
- **Attack:** VLM-only OCR couples extract to GPU runtime (A7 risk if miswired).  
- **Survive:** Tesseract path + **H1**; fixture fallback so G4 never dies; upgrade to Paddle if scans demand.

### Retrieve — why lexical+grant, not Chroma-as-hero
- **Attack:** Vector-only misses equipment tags / clause numbers → wrong cites (A5).  
- **Attack:** Chroma marketed as “plant memory” → SoR theatre.  
- Research: hybrid BM25+vector better; for **must-work** lexical+authz+k=5+verifier is enough; hybrid = ambition.

### Verifier — why rules beat “LLM judge”
- **Attack:** LLM-as-judge can rubber-stamp hallucinations.  
- **Survive:** Every material claim must map to retrieved `chunk_id` or **NOT FOUND**; human still self-HITL.

### Sandbox — why process jail is BEST for *your* machine
- Demo OS = **Windows**. bubblewrap/Firejail are Linux (A3).  
- Docker Desktop as **only** path fails WP-16 (A4).  
- **BEST:** subprocess jail + timeout + secret strip; tighten with **Job Objects** when feasible; Docker `--network=none` **optional** evidence boost.  
- **Honest:** not Firecracker-grade — do not claim CERT-level isolation.

### Runtime — why not lock brand yet
- Ollama = fastest laptop path; llama.cpp = tighter GGUF control; vLLM = GPU serving.  
- Workbench is client-only → **BEST process:** lock client now; pick server when hardware phase opens.  
- **Recommend demo lean:** Ollama if team wants speed; llama.cpp if team wants “we own the binary.”

---

## Proposed LOCK set (say YES to adopt)

```text
Python 3.11+ · FastAPI · React+Vite (Claude-like artifact desk)
docxtpl + python-docx · JSONL audit + hash chain · SQLite grants/session
Tesseract + fixture fallback · grant→lexical k≤5 · cite-or-abstain verifier
thin orch loop · process-jail sandbox (+ optional Docker network=none)
httpx local /v1 gateway · runtime brand DEFERRED (Ollama|llama.cpp later)
```

---

## Explicitly NOT best for must-work

Open WebUI, AnythingLLM, DeerFlow/OpenHands as product, E2B, cloud OCR, Next.js as required shell, Chroma-as-DMS, LangGraph as identity, Docker Desktop mandatory, in-app Approver workflow engine.

---

## DM

Reply: **Lock BEST set** / **change row X to Y** / **need more attack on row Z**.
