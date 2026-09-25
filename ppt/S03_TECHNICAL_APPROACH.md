# Slide 3 — Technical Approach

**Official pointers:**  
• Technologies to be used  
• Methodology / process (flowchart / images / working prototype)  

**Narrative job:** Show **component diagram** + Layer/Tech/Purpose.  
**Mandatory line:** Multiple open-weight **roles**; auto-pick by task; on mid-GPU **load one at a time**.  
**Layout:** Top = **Diagram 2 — Components** (`D02_COMPONENT_DIAGRAM.md`) · Bottom = tech table.

---

## 0. Primary visual — Component / planes diagram (architecture O2 + O3)

**Full spec:** [`D02_COMPONENT_DIAGRAM.md`](./D02_COMPONENT_DIAGRAM.md)  
• Planes (top): **§2** drawing or Mermaid **§3 (O2)**  
• Assist→export strip (**use on slide**): **§4 O3 slide-fit** — ASCII + Mermaid LR · PNG ~960×160–220 · ~25–35% height

**O2 caption (planes):**  
Desk → Workbench (grants · confirm extract · retrieve · packer · Word · audit) → **Gateway only** → Runtime (Cards · weights) · Sandbox ≠ GPU · Monitor A ≠ CERT · Export leave ends path.

**O3 caption (strip — one line):**  
Desk → Session → Grant → Orch → Cards · Confirm extract · Review citations → Pack → **Gateway only** · Word → Secrets → Self-check DRAFT → Export leave → Store · Spec/MCP · Sandbox

**Planes (must be readable):**

| Plane | Contains |
|---|---|
| Desk | Task desk · Task monitor · Admin console |
| Workbench | API · Session≠Grant · Orch · Ingest · Retrieve · Packer · Word · Secrets · Store · Audit · MCP · Sandbox API · Monitor A |
| Gateway | Card · schema · grant · loopback — **only** model path |
| Runtime | Stage/SHA · Cards enable · `/v1` · GPU weights |
| Sandbox | Calc/code · network-none · ≠ GPU |

**O3 flow strip under figure** (from D02 §4 — plain words):  
`Confirm extract → Retrieve → Review citations → Pack → Gateway only · Word → Secrets → Self-check DRAFT → Export leave → Store`

---

## 1. On-slide paste

### Technologies — Layer / Tech / Purpose

*(Keep ≤6 rows on the PDF; full table in inventory below.)*

| Layer | Tech (candidate / demo) | Purpose |
|---|---|---|
| Desk | Electron + Vite + React | Operator workbench window |
| Workbench API | Python · FastAPI | Grants, routes, human checkpoints, gates, audit |
| Gateway | OpenAI-compat → local `/v1` only | Card/grant check; only path to runtime |
| Runtime | Ollama `/v1` (demo) · vLLM/llama.cpp (org) | Serve open-weight; sequential load |
| Files | **python-docx** | Word **DRAFT** (must) |
| Jail + Proof | Sandbox network-none · Monitor A/B | Verify calc/code · evidence pack ≠ CERT |

**Hardware:** Mid-range GPU; smaller/quant OK (PS). Demo: single laptop + adopted tag.

### Methodology

Primary = **O2 planes** (§2/§3).  
Secondary = **O3 slide-fit strip** ([`D02` §4](./D02_COMPONENT_DIAGRAM.md) — use on slide):  
`Desk → Session → Grant → Orch → Cards · Confirm extract · Review citations → Pack → Gateway only · Word → Secrets → Self-check DRAFT → Export leave → Store · Spec/MCP · Sandbox`

### Prototype proof (tiny strip)

Inspection walk + coding sandbox + fail-closed denies + Electron desk.
---

## 2. Full inventory

### 2.0 Full Layer / Tech / Purpose (overflow)

| Layer | Tech (candidate / demo) | Purpose |
|---|---|---|
| Desk | Electron + Vite + React (`apps/kwb-app`) | Operator workbench window |
| Workbench API | Python · FastAPI | Grants, routes, human checkpoints, gates, audit |
| Gateway | OpenAI-compat client → local `/v1` only | Card/grant check; **only** path to runtime |
| Runtime | Ollama **/v1** (demo) · vLLM/llama.cpp (org) | Serve open-weight; quant; sequential load |
| Model policy | Model Cards (`config/models.yaml`) | Pluggable ids; task families |
| Ingest | **Demo:** OCR *framework* (pypdf + Tesseract) + fixture stub. **Org later:** OCR *model* | Pre-LLM extract → **Confirm extract** |
| Retrieve | Authz-first local packs | Cite or abstain; k small |
| Files | **python-docx** | Word **DRAFT** (must). Excel Later |
| Jail | Process / container `--network=none` | Verify calc/code; **≠ GPU** |
| Proof | Audit chain + Monitor A/B | Reconstruct + evidence pack (≠ CERT) |

### 2.1 Demo stack (what we actually run today)

| Piece | Value |
|---|---|
| API | `127.0.0.1:8080` FastAPI |
| Desk | `apps/kwb-app` Electron |
| Model | `llama3.2:3b` (two task cards · one tag) |
| Cards | `inspect-draft` · `code-assist` |
| Start | `scripts/start_demo.ps1` |
| Evidence | `eval/evidence/*` · `MANUAL_TEST_REPORT.md` |

### 2.2 Org scale (same sockets)

| Scale lever | Change |
|---|---|
| More GPUs | Behind same `/v1` |
| More models | New Model Cards — no redesign |
| Connectors | Read-only EAM/DMS Later |
| Auth | SSO Later — Admin=IT outside engineer UI |

### 2.3 Interfaces locked (do not salad)

- Do **not** list Flask + Django + FastAPI together.  
- Do **not** wrap GPU inside the sandbox.  
- Do **not** claim Excel/PPT as must on this slide.

### 2.4 Optional visual

Electron window screenshot (real) — caption: *Knowledge Work Bench desk · DRAFT ≠ CERT*.

---

## 3. Speaker notes (~1:00)

“Three planes: the **workbench** owns grants and human checkpoints; the **gateway** is the only path to models; the **runtime** serves open-weight weights. Sandbox is separate — network-none — for calc and code. Desk is Electron. Files are Word DRAFT via python-docx. On mid-range GPU we load **one** model at a time and route by **model card**.”

---

## 4. Adversarial check

| Risk | Fix |
|---|---|
| Brand salad | One runtime brand on demo line; candidates labelled |
| Claiming dual-load | Explicit sequential load |
| Showing code walls | Diagram > code |
| Fake live URL | Omit; demo is local |
