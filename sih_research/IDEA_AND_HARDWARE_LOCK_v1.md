# Hardware lock, Windows sandbox, idea-PDF draft

**Date:** 2026-09-16  
**User facts (this message):** internal SIH not done; idea/PDF/video not submitted; team criteria pass; RTX **4060 8 GB = runtime**, RTX **3050 6 GB = workbench**; both **Windows**; no NDT scan yet (do not generate now); no plant forms; selection extras will come later.

**Role:** Principal Solutions Architect / Harness Engineer / Research Engineer.

---

## 1. Hardware — locked for prototype and for the PDF (honest)

| Machine | GPU | Role |
|---|---|---|
| Laptop A | NVIDIA RTX **4060 8 GB** | **Runtime** — `/v1` server + staged weights |
| Laptop B | NVIDIA RTX **3050 6 GB** | **Workbench** — UI, gateway, OCR (CPU is enough), sandbox **client**, egress UI |

Workbench does **not** need the 3050 for the idea. Leave it idle or use it only if we later offload OCR; do **not** split two LLMs across two cards for SIH (driver/LAN pain, jury confusion).

**What 8 GB can actually do** (Q4, modest context ~4–8k; blogs/Ollama size cards, not our bench):

| Fits in 8 GB | Does not fit well |
|---|---|
| One **7B–8B** chat/coder at a time (~4.5–6 GB + KV) | Comfortable **14B** (~9 GB GGUF class) |
| Optional small **VLM 2B–7B Q4**, **instead of** the 7B chat, not with it | Two models **resident** at once |
| CPU **OCR** (Tesseract/Paddle) in parallel with the GPU model | 32B / 70B / 120B |

PS already allows smaller models if 120B hardware is absent. **8 GB is that case.** Sequential load: e.g. vision/extract model **unload** → drafter/coder model. Routing log shows **two model ids**. That is real auto-select, not two GPUs.

**Do not write on the PDF:** “we run 70B / multiple models at once / Claude-quality.”

---

## 2. What the PS means by “sandbox” (not Docker-the-product)

Expected Solution: *“A coding task run and **verified** in a sandbox.”* Description: *code execution in a sandbox.*

They mean: **untrusted generated code runs isolated, then tests actually execute.** They do **not** mean “put the LLM inside Docker.”

| Product | What *their* sandbox is | Use for us |
|---|---|---|
| **Cursor** ([Feb 2026 blog](https://cursor.com/blog/agent-sandboxing)) | OS-level jail: macOS Seatbelt, Linux Landlock+seccomp, **Windows = Linux sandbox inside WSL2**. Network off by default. Agent asks to escalate. | Pattern: isolate **commands**, not the GPU server |
| **Codex** | OS-level / container; network often off; on Windows it can **block Docker’s named pipe** | Do not nest “sandbox inside sandbox” with Docker Desktop |
| **Claude Code** | Mostly **permission prompts**; Docker Inc. also sells **Docker Sandboxes** (microVM) as a *product* | We do not need that product for SIH |
| **SIH / MRPL PS** | Prove generated code ran **offline**, did not roam the disk/WAN, and tests **passed or failed visibly** | Small Linux container **or** equivalent jail |

**Prototype choice (Windows laptops):**

1. **Primary:** Docker Desktop (WSL2 backend)  
   `docker run --rm --network=none --cpus=1 --memory=1g`  
   mount **only** a temp workspace (generated .py + tests).  
   **Never** run Ollama/vLLM inside this container.
2. **Fallback if Docker Desktop is banned/broken at venue:** WSL2 Ubuntu + `unshare`/firejail-class, or a Python subprocess with cwd jail + Windows firewall block for that process. **Weaker.** Say so if we use it.
3. **Not a sandbox:** “run pytest on the host.” Jury can call that unverified.

Calc (`corrosion.py`) can use the **same** sandbox so LLM math never runs.

---

## 3. Scan / synthetic — parked

No real NDT, no generate-now. For **idea PDF**: workflow diagram + **labelled mock fields**, not a fake screenshot of a working app.

When we build (later): photograph a **printed thickness table** (you can type 15 rows in Word, print, snap). That is more honest than a digital PDF pretending to be a scan.

---

## 4. Idea PDF — format facts vs drafts

**Official SIH 2026 Guidelines (our PDF):** experts score nine **named** criteria; **no marks**. Mentors exist to make a **working prototype**. Ideas must be **new**.

**Circulated 2026 “IDEA Presentation Format” (Scribd/Studylib, not the same as college 10-slide blogs):**

- Max **6 slides including title**
- **Do not change** the official pointers
- Upload **PDF only** (not PPT/DOCX)
- Delete the “instructions” slide before upload

**Playbook:** `judging_sources/SIH_SOFTWARE_PLAYBOOK.md` graded keep/drop in `PLAYBOOK_KEEP_DROP_v1.md`. Official 6-slide craft **approved**. College tactics, fake winner decks, PPT-in-36h, DMS-as-demo **dropped**.

**Internal hackathon** may also want video / GitHub. Some 2026 writeups claim software edition needs PPT + **non-AI** team-narrated video + GitHub with **partial** code. **Treat as unconfirmed until you paste the college circular.** If true, we need a thin repo *before* national upload — that is a later build, not this PDF draft.

---

## 5. Six-slide content (paste into official template)

Idea title (working): **Sovereign On-Prem Agentic Workbench for Confidential Industrial Documents**

PS: **SIH26117** · Theme: Smart Automation · Category: **Software** · Org: MRPL  
Team ID / name: *fill from portal*

### Slide 1 — Title

- PS ID, title, theme, category, team ID/name, college  
- One line: *Air-gapped workbench that drafts inspection notes and verified code on the organisation’s GPU — nothing leaves the premises.*

### Slide 2 — Proposed solution (this is novelty + problem fit)

**What:** Not a chatbot. An **evidence workbench**: ingest scan → on-device OCR/vision → **task-routed** open-weight models → HITL → **Word/Excel** + sandbox-verified code. Visible **zero-WAN** log.

**Addresses PS:** shadow-AI / cannot use Claude; own GPU; multi-model by **task**; agent + tools; multimodal; real deliverables; local KB; air-gap **proof**.

**Uniqueness (honest):** Open WebUI/Ollama already chat locally. We add **task gateway + Model Cards**, **controlled templates**, **sandbox calc (no LLM arithmetic)**, **draft/HITL**, **egress monitor**. Not a new LLM. Not plant DCS control.

Diagram (boxes): Workbench laptop → Gateway (route/auth) → Runtime 8 GB GPU · OCR/tools/sandbox beside · NEVER DCS.

### Slide 3 — Technical approach

**Hardware we already have:** Runtime RTX 4060 **8 GB**; workbench RTX 3050 6 GB (UI only). Sequential **7B-class** open-weight (+ optional small VLM); CPU OCR.

**Software (logical, not a locked brand):** Python workbench; OpenAI-compatible `/v1` (Ollama / vLLM / llama-server — pick at build); Model Cards; OCR; python-docx/openpyxl; Docker **`--network=none`** for generated code only; local JSON KB; audit + packet/host log.

**Method:** 1 ingest 2 OCR 3 `vision_extract` 4 HITL fact sheet 5 sandbox CR 6 `draft_note` → Word 7 separate `code_sandbox` + tests 8 show routing log + zero egress.

**36h/finale:** same architecture, pre-staged weights, two-laptop LAN, WAN unplugged.

### Slide 4 — Feasibility and viability

**Feasible:** PS allows mid-GPU / smaller models. 8 GB = one 7B at a time — matches PS. Mocks: EAM as JSON **same schema**. No SAP needed for demo.

**Risks:** small-model tool-calling; OCR on bad scans; Docker Desktop on locked-down venue PCs; fake-looking routing.

**Mitigations:** sequential two model ids; OCR confidence + `NOT FOUND`; calc in sandbox; Docker primary + WSL fallback; WAN unplug + monitor; **draft** watermark; no OT writes.

### Slide 5 — Impact and benefits

**User:** inspection / integrity engineer (then other PSU knowledge work).  
**Benefit:** cut **assemble-and-type** time; keep P&IDs/financials off cloud; audit trail.  
**KPI (illustrative, not measured):** time-to-**draft** note, not autonomous FFS.  
**Scale:** same workbench, swap runtime URL (laptop → plant GPU). Other PSUs: same spine, new templates.  
**Social/economic:** reduce shadow AI in confidential orgs. **Environmental:** reuse existing GPUs; no extra training claim.

### Slide 6 — Research and references (links, not an essay)

- SIH26117 Expected Solution (verbatim bullets)  
- OISD-STD-128 (catalogue, not pasted) · API 510-class report **fields**  
- OpenAI-compatible local serving (Ollama/vLLM/llama.cpp docs)  
- Cursor agent sandboxing (isolate **code**, WSL2 on Windows)  
- Agent Skills format (on-disk skills, no cloud hub)  
- Adjacent: Open WebUI, PrivateGPT — **gap** = industrial deliverable + proof of sovereignty  

No fake papers. No “we benchmarked 120B.”

---

## 6. How this maps to the nine official criteria (selection)

Evaluators skim. Every slide must hit a criterion **in a diagram or 5 bullets**, not a paragraph.

| Criterion | Where it lives |
|---|---|
| Novelty | Slide 2: gap vs chat-RAG |
| Complexity | Slide 3: OCR + route + sandbox + air-gap |
| Clarity / format | Stay inside **6-slide official** template |
| Feasibility | Slide 4 + **8 GB honestly** |
| Practicability | Inspection → Word, HITL |
| Sustainability | Model cards; USB update; plant URL later |
| Impact | Slide 5, illustrative KPI |
| UX | HITL fact sheet → download Word (describe; no fake UI shot) |
| Future | Org scale on paper; prototype = 1/100th |

**Video (when college requires it):** team voices only, no AI voice. Show **whiteboard or slides** until code exists. Do not fake a product demo.

**GitHub (if required):** empty README + architecture is weak; they often want **partial implementation**. Wait for your circular. If mandatory, first code = gateway + OCR→JSON stub, not a 20-box platform.

---

## 7. What I still need from you (do not invent)

1. Official **idea PPTX** from SPOC/portal (or a screenshot of the six headings).  
Until the official PPTX is here, this file is the **content spine**, not the upload file. Team ID still blank until you send it.
