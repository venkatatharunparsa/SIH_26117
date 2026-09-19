# Idea PPT fill spec — SIH26117 (discuss first, do not upload)

**Date:** 2026-09-16 (portal lock)  
**Status:** Spec only. Official idea **template** = reference. Portal listing = `Downloads/Smart India Hackathon.pdf` (sih.gov.in/sih2026PS, printed 16/09/2026 21:21).  
**Placeholders (do not invent):** `[TEAM_ID]` · `[TEAM_NAME]` · `[PRODUCT_NAME]`  
**Do not upload** `SIH26117_IDEA_WORKING.pptx`.

---

## 0. Portal PDF vs your paste vs our KB

| Field | Portal PDF (`Smart India Hackathon.pdf`) | Your paste / KB | For the PPT |
|---|---|---|---|
| Org | Mangalore Refinery and Petrochemicals Limited (MRPL) | Same | Slide 1 context only (not an official pointer) |
| Title | Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work | Same | **Exact string** |
| Category | Software | Same | **Software** |
| Theme | Smart Automation | Same | **Smart Automation** |
| ID on detail card | **26117** | — | See note below |
| PS Number in table | **SIH26117** | SIH26117 | Use **`SIH26117`** on slide 1 (table column). Optionally add `26117` if the portal form wants digits only — we follow whatever the idea form shows when you register |
| Ideas | 34/500 | — | **Not on slides** |
| Idea deadline | **30 September 2026** | — | **Not on slides** (ops fact only) |
| Dataset | Open-source models + **public sample scanned PDFs / sample P&IDs**; **no proprietary data required** | Not in your paste; **new** | Prototype may use public samples. Still **no fake screenshot** on the idea PPT |
| Background / Description / Expected Solution | PDF OCR **truncated** mid-sentence | Your paste = full text; **matches our KB verbatim** | Map uniqueness to **your paste**. Do not use SIHONE paraphrases |

**PS typo (official, do not “fix” on slide 1):** “manually resulting in productivity **gain**” — intent is loss/pain. We do not quote that sentence on the PPT.

**Your paste is the binding PS body** (Background, Description, Expected Solution). Confirmed same as `01-problem-statement.md`.

---

**Playbook rules we must follow (Official + Observed keep):**  
6 slides including title · PDF upload · **do not rename pointers** · points/diagrams not paragraphs · named product · one flowchart · Layer/Tech/Purpose table · Real vs Mock · Challenge|Risk|Mitigation · one sourced KPI labelled estimate · competitor ticks only if true · no fake URL · no crore / no 14B / no PPT-in-36h.

---

## A. Adversarial: do we have enough to fill the PPT?

**Enough to write a content spec for slides 2–6: YES.**  
**Enough to produce a portal-ready PDF: NO.**

| Datum | Have? | Source grade | On which slide | If missing |
|---|---|---|---|---|
| PS ID **SIH26117** / **26117** | Yes | **Portal PDF** 16/09/2026 | 1 | Use `SIH26117` unless the idea form shows 26117 |
| Full PS title | Yes | **Portal PDF** + your paste | 1 | Wrap so it misses the brain graphic |
| Theme Smart Automation · Category Software · Org MRPL | Yes | **Portal PDF** | 1 | Locked |
| Team ID | Placeholder `[TEAM_ID]` | You | 1, oval | Keep placeholder |
| Registered team name | Placeholder `[TEAM_NAME]` | You | 1, oval | Keep placeholder |
| Product name | Placeholder `[PRODUCT_NAME]` | You | 2 title | Keep placeholder |
| Scan for demo | Portal **allows public** sample PDFs/P&IDs | Portal dataset line | Prototype later | Not a screenshot on this PPT |
| Official 2026 idea deadline | **30 September 2026** | Portal table | nowhere | Do not print on slides |
| Prize | Still **not** on this PDF | — | nowhere | Do not print |

**Cross-check vs playbook §3 “how software teams die”:** generic chatbot · wall of text · no 36h honesty · no difference vs ChatGPT · wrong template. The discarded PPTX failed **wall of text** and **no diagram**. Spec below is meant to fix that.

---

## B. Slide-by-slide: what to fill (layout + tables)

Stay **inside** the official white content area. SIH logo/graphic on the right of slide 1 — keep PS title in the **left** text box only.

### Slide 1 — TITLE PAGE (official pointers unchanged)

| Field | Fill | Status |
|---|---|---|
| Problem Statement ID – | `SIH26117` | Portal table; detail card also shows `26117` |
| Problem Statement Title- | `Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work` | Portal exact; wrap 2 lines, stay left of graphic |
| Theme- | `Smart Automation` | Portal exact |
| PS Category- | `Software` | Portal exact |
| Team ID- | `[TEAM_ID]` | Placeholder |
| Team Name (Registered on portal)- | `[TEAM_NAME]` | Placeholder |
| Oval “Your Team Name” | `[TEAM_NAME]` | Placeholder |

Do **not** add college collage, extra logos, prize, 34/500, or deadline.

---

### Slide 2 — replace chrome “IDEA TITLE” with **product name**; **keep the three official pointers** as section headers

**Product name:** `[PRODUCT_NAME]` (placeholder). Oval/title use this string when you choose it.

**Layout (playbook Observed):** 2-column. Left = three short blocks. Right = **one** loop diagram (boxes). No screenshot until we have a real UI.

#### Left — Proposed Solution (≤4 bullets)

- `[PRODUCT_NAME]` — air-gapped agentic workbench on the org GPU (not a chat bubble).
- Demo loop: scanned inspection → OCR → HITL → **Word note + Excel CR**.
- Second loop: code **run and tested** in a no-network sandbox.
- Proof: WAN unplugged + visible log (PS “sovereign claim”).

#### Left — How it addresses the problem (map PS, ≤4 bullets)

- Data cannot go to Claude/Codex → nothing leaves the GPU box.
- Not locked to one model → **task** router + Model Cards + `/v1`.
- Agent + tools → file, OCR, sandbox, spreadsheet, local KB.
- Expected Solution: two task types, Word file, verified code, multimodal OCR.

#### Left — Uniqueness (only true ticks — 3 lines)

- vs Open WebUI / Ollama / PrivateGPT: they chat locally; we **route by task**, **template Word**, **sandbox math**, **HITL**, **egress proof**.
- vs ChatGPT / Copilot: air-gap; 7B-class on **8 GB** (PS allows smaller than 120B).
- Not DCS control. Not a new LLM.

#### Right — diagram (draw this; do not paste ASCII walls)

```
Scan PDF → OCR (CPU) → Gateway[task] → 7B /v1 (4060 8GB)
                ↓
         HITL fact sheet
                ↓
     sandbox CR  →  Word DRAFT
                +
     code + pytest in Docker --network=none
```

**No URL box** until a link loads.

---

### Slide 3 — TECHNICAL APPROACH

**Keep both official sentences as headers.** Then a **table**, then a **flow**, not a logo salad.

#### Table — Layer / Tech / Purpose (playbook Observed)

| Layer | Tech | Purpose |
|---|---|---|
| Workbench (Laptop B, 3050 unused for LLM) | Python UI + gateway | Task route, HITL, audit |
| Ingest | CPU OCR; optional small VLM sequential | Scan/photo → text/JSON |
| Runtime (Laptop A, RTX 4060 **8 GB**) | OpenAI-compat `/v1` (Ollama **or** vLLM **or** llama-server — **not locked**) | One 7B-class at a time |
| Calc / code | Docker `--network=none` (WSL2) | CR formula + pytest; **not** the GPU server |
| Deliverable | python-docx, openpyxl | Word note, thickness sheet |
| KB | JSON/CSV, same schema as future EAM | Mock connector, real lookup |
| Skills | 5 on-disk Agent Skills | extract / calc / draft / code / policy |
| Proof | Host/packet log + WAN unplug | Zero external calls |

**Do not list** Flask+Django+FastAPI. **Do not list** python-pptx. **Do not list** LangGraph unless we lock it.

#### Methodology (one flow, two PS loops)

1. Upload scan → OCR → `vision_extract` → JSON → **HITL gate**  
2. `calc` in sandbox: `CR = (t_prev − t_curr) / Δt` (print inputs)  
3. `draft_note` **different model id** (unload/load) → `.docx` DRAFT  
4. Parallel: `code_sandbox` → pytest in jail → pass/fail  

**36h / portal prototype phase:** this loop only.  
**Org phase (not on this slide as a product claim):** plant GPU URL, real EAM API, more templates.

---

### Slide 4 — FEASIBILITY AND VIABILITY

Three official pointers → **three tables**. No adjectives (“highly scalable”).

#### Feasibility

| Slice | In 36h / portal prototype | Later / org paper |
|---|---|---|
| OCR → JSON → HITL → Word | **REAL** | — |
| Excel CR from sandbox | **REAL** | — |
| Two model ids sequential on 8 GB | **REAL** | Larger GPU = same gateway |
| Coding pytest in Docker jail | **REAL** | — |
| WAN off + log | **REAL** | Certified air-gap LATER |
| EAM / historian / LIMS | JSON **same schema** | Read-only API |
| SAP, PPT pack, 14B, two LLMs in VRAM | **Not claimed** | LATER or never |

One line: PS already allows smaller models if 120B hardware is absent.

#### Challenges / risks / mitigations (playbook table)

| Challenge | Risk | Mitigation |
|---|---|---|
| 8 GB VRAM | Fake “two models at once” | Sequential unload; two GGUF **ids** in the log |
| Small model tools | Broken JSON / tools | Schema + retry + HITL; sandbox verifies numbers |
| Bad scan | Hallucinated mm | OCR confidence; `NOT FOUND`; no invent |
| Docker Desktop blocked | Host pytest looks unverified | Primary Docker; WSL jail fallback **disclosed** |
| App-only “air-gap” | HF/Ollama still phones home | WAN unplug + host/packet log; pre-stage weights |

---

### Slide 5 — IMPACT AND BENEFITS

#### Audience table

| Who | What changes |
|---|---|
| **Primary:** inspection / integrity engineer | Draft note + thickness sheet from a scan; they still approve |
| Secondary: process / HSE / procurement (same product later) | Same workbench, new template (not in 36h) |
| Organisation | Less shadow ChatGPT on P&IDs / vendor / board files |

#### Benefits (social / economic / environmental) — **one sourced number**

| Benefit | Number | Source / honesty |
|---|---|---|
| Time-to-**DRAFT** (not approved FFS) | Scanned inspection **1–5 days** elapsed → **target 2–3 hours** for a draft pack | KB workflow study; **industry estimate, not MRPL SLA** |
| Social | Stops quiet paste into public AI | PS background (shadow AI) |
| Economic | Reuse existing 8 GB GPU; **no ₹crore** | Hardware fact |
| Environmental | No extra training run claimed | — |
| Policy (one line) | Logs usable for CERT-In-style retention; DPDP: data stays on-prem | Not a legal opinion |

If you refuse the 2–3 hour figure, use only: “majority of elapsed time is assemble-and-type (KB 50–70%) — we attack that, not the engineer’s judgement.”

---

### Slide 6 — RESEARCH AND REFERENCES

**No Scribd. No “Click here”. No End….**

#### Links / names (short)

- SIH26117 Expected Solution (inspection→Word, sandbox coding, multimodal, zero-egress).
- OISD-STD-128 — *Inspection of Unfired Pressure Vessels* (**name only**).
- API 510-class **report fields** (CML, thickness, CR) — not pasted code text.
- OpenAI-compat local serving (Ollama / vLLM / llama.cpp docs).
- Agent Skills spec (on-disk). Cursor sandboxing: isolate **code**, not the GPU.
- SIH 2026 Guidelines: six-slide PDF; nine criteria; **no published weights**.

#### Competitor matrix (ticks only where true)

| | Air-gap / no WAN | Citations / NOT FOUND | Code sandbox verified | HITL before Word | Word/Excel artefact |
|---|---|---|---|---|---|
| **[PRODUCT_NAME]** | Y | Y | Y | Y | Y |
| ChatGPT / Copilot / Claude | N | n/a | N (cloud) | n/a | chat / cloud docs |
| Open WebUI / Ollama chat | local optional | N | N | weak | chat |
| PrivateGPT-class RAG | often local | partial | N | weak | chat |

Do **not** tick PPT. Do **not** tick “better accuracy.” Do **not** tick every cell green.

---

### Slide 7 — DELETE before PDF export

Official instruction slide. Never in the upload.

---

## C. Phases (what the screener should see vs later)

| Phase | What exists | On PPT? |
|---|---|---|
| **Now (idea PDF)** | Design + this spec | Slides 1–6 only |
| **Portal / 36h prototype** | Same boxes: OCR, two 7B ids, Word, Excel CR, Docker tests, WAN log | Slide 4 “REAL” |
| **Org paper** | Plant GPU URL, real EAM, more templates, SSO | Slide 4 “Later” one column; slide 5 secondary audience |
| **Never** | DCS/SIS writes; autonomous FFS; fake 120B | Uniqueness line |

Finale (if shortlisted, Unverified 3 evals): leave a visible increment; do not freeze 100% before day-1.

---

## D. Highlights (max 8 — if it is not here, it is not on the PPT)

1. `[PRODUCT_NAME]` — a workbench, not “an AI platform”.  
2. PS owner constraint: **air-gap + confidential industrial files**.  
3. One demo spine: **scan → Word**.  
4. Second spine: **sandbox-verified code**.  
5. Task router + two **model ids** on **8 GB sequential**.  
6. HITL fact sheet **before** Word.  
7. REAL vs MOCK in one table.  
8. Honest KPI or no number.

---

## E. What’s still open

Placeholders stay until you send real strings: `[TEAM_ID]` `[TEAM_NAME]` `[PRODUCT_NAME]`.

**Decide (not a blocker for the spec):** Keep “1–5 days → target 2–3 hours **for a draft** (KB estimate, not MRPL SLA)”, or drop hours?

Portal screenshot: **done** (`Smart India Hackathon.pdf`). College logo: still **no**.

When you want to fill the official PPTX, we do it **from this spec**, placeholders first.
