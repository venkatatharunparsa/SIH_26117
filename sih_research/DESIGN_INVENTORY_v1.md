# What we have vs what we do not — SIH26117

**Date:** 2026-09-17  
**Purpose:** Inventory only. No new product decision in this file. PPT redesign is paused.  
**Rule:** User = decision maker. Assistant = Principal Solutions Architect / Harness Engineer / Research Engineer. Stack not locked. No app code until asked.

---

## Honest status

We have a **research corpus** and a **paper architecture**. We do **not** have a validated product.  
The 6-slide DALL-E work assumed the paper architecture was the solution. That is the gap you named: **slides were filled from research, not from a decided, validated design.**

| Layer | Status |
|---|---|
| Problem statement (verbatim) | **Have** |
| Expected Solution as acceptance test | **Have** (on paper) |
| Org-scale logical boxes | **Have as a hypothesis** (`DESIGN_ORG_PROTOTYPE_v1.md`) |
| Prototype overlay REAL/MOCK/LATER | **Have as a hypothesis** — not run |
| Hardware facts (4060 8 GB / 3050 6 GB, Windows) | **Have** (user-stated) |
| Internal stack (runtime, OCR, UI, orchestrator) | **Not locked** (working rule) |
| Adopt from existing repos | **Patterns named, nothing adopted** |
| Running workbench | **Do not have** |
| Validation (OCR on a scan, two model ids, WAN log, pytest jail, Word from JSON) | **Do not have** |
| Official idea PDF | **Not submitted** |

Treat every previous “lock” below as **revisitable** in the next step-by-step pass. Do not treat them as proven.

---

## 1. Binding input (this is not our invention)

**PS:** SIH26117 — Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work.  
**Org:** MRPL. **Category:** Software. **Theme:** Smart Automation.

**Expected Solution (acceptance test, not optional flavour):**

1. Local deploy on mid-range GPU; smaller open-weight model OK if 120B absent  
2. Model auto-select across **≥2 task types**  
3. Agentic path: scanned inspection → findings → **Word** approval note  
4. Coding task **run and verified** in a sandbox  
5. Multimodal: image or scanned document  
6. Logs or visible network monitor: **no external calls** (the sovereign proof)

Description (air-gap GPU server, not locked to one model, agent+tools, OCR/vision, Word/Excel/PPT, local KB) is the **org ambition**. PPT is in Description, **not** in Expected Solution.

File: `sih_research/sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`

---

## 2. What exists in the workspace

### Research (large, mixed grade)

| Location | What it is | Use now |
|---|---|---|
| `sih_research/sovereign-ai-workbench-kb/` | MRPL-type workflows, templates, policy, competitors, feasibility estimates | Domain **input**. Time KPIs are **estimates**, not MRPL SLAs |
| `sih_research/SYNTHESIS_v1_adversarial.md` | First prune of the KB | Background |
| `sih_research/ADVERSARIAL_READINESS_CHECK.md` | Fake-demo traps | Keep as a checklist when we validate |
| `agentic_research/*.md` | OSS agent atlas (OpenHands, Continue, skills, sandboxes, …) | **Catalogue**. Not a decision to fork |
| `sih_research/judging_sources/` | Official 6-slide template extract + software playbook | PPT **later**, after product design |

### Paper design (hypotheses, written as “locks”)

| File | Claimed lock | What is actually true |
|---|---|---|
| `ARCHITECTURE_LOGICAL_v1.md` | Workbench plane vs runtime plane; OpenAI `/v1` LCD; Model Cards | Logical split is a **proposal**. Runtime binary not chosen. `/v1` LCD was checked against docs, **not** against our laptops |
| `DESIGN_ORG_PROTOTYPE_v1.md` | Org boxes + prototype overlay; REAL/MOCK/LATER; inspection spine; 5 skills | Shape on paper. **No software.** Red-team items closed on paper only |
| `IDEA_AND_HARDWARE_LOCK_v1.md` | 4060 = runtime, 3050 = UI; Docker jail for code only; sequential 7B | Hardware is a **user fact**. Docker on these Windows machines is **untested** |
| `DESIGN_REDTEAM_SKILLS_JUDGING_v1.md` | Five on-disk skills; HITL JSON gate | Spec only |

### PPT track (pause)

`PPT_FILL_PACK_v2.md`, `chatgpt_slide_prompts/`. Working name **KWB** appeared in image prompts. It is **not** a product-design lock. Do not redesign the PPTX until the solution walkthrough below is done.

### Code

No workbench application. Filling scripts for PPT only. That is correct given the working rule.

---

## 3. Decisions that were treated as locked (to re-open one by one)

These were **user-confirmed in chat / Mem0**, not validated on a machine:

1. Software workbench **≠** hardware/runtime. Client stores `base_url` + key + model id.  
2. Org paper first, then same boxes at prototype scale.  
3. Binding demo spine = inspection scan → Word, plus sandbox coding, plus WAN log.  
4. Borrow **patterns** from repos; do not fork OpenHands/Continue as the product.  
5. No stack lock; no build until asked.  
6. Portal PDF + portal-level prototype; skip college-round tactics.

**Not decided / not validated:**

- Product name (KWB vs other)  
- Exact user journey screens (workbench UX)  
- Which repo patterns to copy vs ignore (only a table of *classes*)  
- OCR engine, serving binary, UI toolkit, orchestrator library  
- Whether two laptops are required or one-box is the product  
- Whether 7B sequential on 8 GB is good enough **in use** (only community VRAM tables)  
- Inspection JSON schema field list as a signed contract  
- KPI hours (1–5 days → 2–3 h) — study estimate only  

---

## 4. What “adopt from existing repos” currently means

We listed **patterns**, we did **not** pick a codebase:

| Pattern | Source class | Adopted? |
|---|---|---|
| `base_url` + `api_key` + `model` | Continue / OpenHands / local servers | Named only |
| Tool allow-list; model has no raw WAN | “Nabhi-style” / policy agents | Named only |
| Code jail ≠ GPU process | OpenHands / Cursor WSL | Named only |
| HITL before a file becomes a record | Hermes-class | Named only |
| Plan → tool → observe | Generic ReAct | Named only |
| On-disk `SKILL.md` | agentskills.io | Named only |

**Rejected on paper (not re-tested):** fork OpenHands as the SIH product; OpenRouter; always-on OS/browser agent; company-brain that syncs off-prem.

Next design pass must say for each: **ignore / read-and-steal / optional later** — still without locking a framework.

---

## 5. Validation gap (why the solution is not “done”)

Nothing below has been executed as a test:

- OCR on a real or printed thickness table  
- Two different model ids in one audit log  
- JSON HITL then Word that contains **only** approved fields  
- `CR = (t_prev − t_curr) / Δt` in an isolated process  
- pytest of generated code with `--network=none`  
- WAN unplug + host log = 0  
- `GET /v1/models` against a runtime on Laptop A  

Until those exist, uniqueness vs Open WebUI is an **argument**, not a demonstration.

---

## 6. Proposed sequence after you accept this inventory

Do **not** skip ahead to stack or PPT.

| Step | Decision | Output | Stop if |
|---|---|---|---|
| **A** | Restate the **product contract** from Expected Solution only | One page: must-work / org-ambition / never | We argue Description vs Expected |
| **B** | Org-level product: who, job, artefact, systems around it, non-goals | Org workbench definition | We design a chatbot or a GPU optimiser |
| **C** | Org logical components (re-decide each box; may match or replace v1) | Org diagram + data/control flow | A box has no owner or no artefact |
| **D** | Narrow to prototype: REAL / MOCK / LATER + **test** for each REAL | Prototype contract | REAL cannot be tested on 8 GB Windows |
| **E** | Harness: for each capability, ignore / steal pattern / later | Adopt table, still no framework lock | We start forking a full agent OS |
| **F** | Only then: candidate internals (still optional until build) | Shortlist, not lock | We pick Ollama “because everyone uses it” |
| **G** | Only then: PPT from the decided contract | 6 slides | We fill from KB estimates again |

---

## 7. What we will not do in the next message unless you say so

- Redesign the PPTX  
- Lock FastAPI / Ollama / Tesseract / LangGraph  
- Write application code  
- Invent measured KPIs  
- Treat `DESIGN_ORG_PROTOTYPE_v1.md` as frozen truth  

**Wait for you:** accept or correct this inventory, then start **Step A** (product contract) only.
