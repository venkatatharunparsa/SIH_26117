# PPT fill pack v2 — data + strategy (you fill; we do not touch PPTX)

**Date:** 2026-09-16  
**Role:** Principal Solutions Architect / Harness Engineer / Research Engineer  
**Grade key (playbook):** Official / Observed / Unverified / Invalidated  
**Placeholders stay:** `[TEAM_ID]` `[TEAM_NAME]` `[PRODUCT_NAME]`

This file supersedes `PPT_FILL_KIT.md` for content. The old kit was a screening outline. This pack is what you actually paste from.

---

## 0. Adversarial verdict — do we have enough?

**Enough to fill a non-generic 6-slide idea PDF now**, if you use the **four official slide-2 pointers**, named OSS with a *purpose*, sourced numbers with a *grade*, and the org→prototype overlay.

**Not enough** to print as *our measured result*: OCR %, tokens/s on *this* 4060, MRPL SLA hours, plant ₹ savings, carbon kg saved vs ChatGPT, “we already built it.”

| Need (your complaint) | Status | What to put on the PDF |
|---|---|---|
| Slide 2 **detailed** solution (not a chatbot sentence) | **Yes** — design lock | 8-step spine + org vs prototype one line |
| Industry solution vs 36h prototype vs later phases | **Yes** | Slide 2 one line + slide 4 REAL/MOCK/LATER |
| Named tech + OSS | **Yes** as **candidates** (stack not locked) | Layer / Tech / Purpose table |
| Numeric metrics | **Partial** | Use **ledger §3**; never mix grades |
| Workflows | **Yes** | One loop on 2–3; rest = “same boxes, more skills” |
| Technical innovation | **Yes, integration not a new LLM** | vs named products, not “AI/ML” |
| Feasibility + risks | **Yes** | 8 GB sequential; Docker WSL2; HITL |
| Audience / impact | **Yes** with **org facts**; time KPI is **our estimate** | MRPL 15 MMTPA / 2,530 staff as *context*, not users of our app |
| Market size | **Enough as ecosystem, not TAM of this product** | IndiaAI ₹ + NASSCOM AI market on **slide 6**, not as our revenue |
| Env impact | **Enough to be honest** | Reuse existing GPU; **do not claim greener than cloud** |
| References / papers / govt / OSS | **Yes** | URLs in §9 |
| Similar products + difference | **Yes** | Matrix §8 |

**If a slide still looks empty:** shrink this pack into tables. Do not wait for a prototype.

---

## 1. Playbook patterns this pack obeys

Official pointers (do **not** rename): Title · Idea · Technical · Feasibility · Impact · References.

| Pattern | Where | What we steal | What we refuse |
|---|---|---|---|
| Named product in slide-2 chrome | 2 | `[PRODUCT_NAME]` | “IDEA TITLE” |
| **Four** idea pointers (template has four, not three) | 2 | Proposed · **Detailed** · Addresses · Uniqueness | Merging proposed+detailed (v1 kit mistake) |
| Left words, right one loop | 2–3 | Boxes, not a paragraph of arrows | Logo salad |
| Layer / Tech / **Purpose** | 3 | Each library has a job | Flask+Django+FastAPI |
| REAL vs MOCK vs LATER | 4 | 36h honesty | “highly scalable” adjectives |
| Challenge \| Risk \| Mitigation | 4 | High/Med/Low | Only “OSS so cheap” |
| Audience \| change \| **sourced** number | 5 | One number + grade | “billions of users” |
| You vs **named** tools | 6 | Ticks only where true | Every cell green |

Screening criteria (Official, **no %**): novelty, complexity, clarity in this format, feasibility, practicability, sustainability, scale of impact, UX, future work.

---

## 2. What we are actually proposing (lock this in your head before drawing)

**Product (org paper):** a **self-hosted workbench** that behaves like Claude/Codex for confidential industrial work: task-routed open-weight models, local tools, HITL, Word/Excel, visible zero-egress. Software is an **OpenAI-compatible client**. Hardware/weights live on the org GPU server.

**Not the product:** a new LLM, a GPU optimiser, DCS/SIS control, ChatGPT with a skin, Open WebUI fork.

**Prototype (same boxes, 1/100 scale):** two Windows laptops; runtime = RTX **4060 8 GB**; UI = RTX **3050 6 GB unused for LLM**; one 7B-class GGUF loaded at a time; CPU OCR; Docker `--network=none` for generated code/tests/CR; mock EAM JSON; WAN unplugged + host log.

**Jury line:** *Same logic as production. Demo is one GPU, small models, mock connectors. Scaling is GPUs, larger staged models, real APIs — not a rewrite.*

### 2.1 Org vs prototype vs later (phases — put a 3-row strip on slide 4 or tiny on 2)

| Phase | When | What is real |
|---|---|---|
| **P0 — Idea PDF (now)** | Screening | Architecture + honesty. No fake screenshot. |
| **P1 — Portal prototype (after you ask to build)** | Pre-finale / 36h spine | Scan→OCR→JSON HITL→sandbox CR→Word DRAFT; second task = pytest in jail; two model **ids** in log; WAN log = 0 |
| **P2 — Pilot (post-SIH)** | 3–12 months | Read-only EAM/DMS APIs, SSO, SIEM sink, more skills (MOC, RCA, TBE), plant templates |
| **P3 — Org scale** | After pilot | Dedicated inference cluster, larger staged models, HA, classification workflow. **Never:** write to DCS/SIS/PLC |

**36h vs PS Description:** Description lists PPT. Expected Solution does **not**. **36h = Word + Excel.** PPT = P2/P3.

### 2.2 Binding inspection workflow (this is the “detailed explanation”)

```
1 Engineer drops scanned inspection PDF (public sample OK; portal allows)
2 Badge: Confidential + DRAFT; no OT write
3 Rasterize pages → CPU OCR (Tesseract or PaddleOCR) ± optional VLM after unload
4 Task router: vision_extract → 7B-class extract GGUF  (model id A in log)
5 Agent fills JSON: {tag, points[], thicknesses[], units, date, source_page, confidence}
6 Tool: lookup mock EAM JSON (same schema as future SAP/Maximo) — not a hardcoded tag in the prompt
7 Task calc: Docker --network=none runs CR = (t_prev − t_curr) / Δt   (LLM does not invent mm or CR)
8 HITL hard gate: engineer edits/approves JSON  — Word cannot start without this
9 Unload A, load B: draft_note → different model id  (PS auto-select; 8 GB cannot dual-load)
10 python-docx / openpyxl from approved fields only; missing = NOT FOUND
11 Second PS loop (same gateway): code_sandbox → write .py → pytest in same jail → pass/fail
12 Egress monitor: zero WAN destinations for 1–11
```

**Five on-disk Agent Skills** ([agentskills.io](https://agentskills.io/specification)): `inspect-extract` · `inspect-calc` · `inspect-draft` · `code-sandbox` · `sovereign-policy`. Org-only skills (MOC, RCA, TBE, handover, capex) stay **off** the 36h demo.

**Formula (public engineering practice, not a secret):** long-term corrosion rate  
`CR_LT = (t_previous − t_current) / (d_current − d_previous)`  
Same form as inspection/RBI practice in our KB; we do **not** quote a paid API 510 clause on the slide.

---

## 3. Metrics ledger — what is numeric, what is not

Print **at most one time-KPI and one policy/ecosystem number** on slides 5–6. Everything else is backup for Q&A.

| Metric | Number | Grade | May we print it? | Honest caption |
|---|---|---|---|---|
| PS ID / theme | SIH26117 · Smart Automation · Software | **Official** (portal) | Yes, slide 1 | Exact portal strings |
| Screening criteria | 9 named, **no weights** | **Official** | Slide 6 one line | Do not invent 25/20/15% |
| MRPL capacity | **15.0 MMTPA** installed | **Official** org (mrpl.co.in / MoPNG) | Slide 5 *context* | Not “our users” |
| MRPL FY24–25 throughput | **18.18 MMT** gross crude (company: highest ever) | **Observed** (BSE/board note) | Optional Q&A | Do not put on idea PDF (space) |
| MRPL staff 31 Mar 2025 | **2,530** (1,162 mgmt + 1,368 non-mgmt; 226 women) | **Observed** (Directors’ report) | Slide 5 secondary | Audience *at the org*, not claimed MAU |
| Inspection pack elapsed | **1–5 days** | **Unverified** (our workflow study, **not MRPL SLA**) | Slide 5 **only if labelled estimate** | Finding/typing share **50–70%** same study |
| AI target for that pack | **2–3 hours to a DRAFT** | **Unverified** (same study) | Same cell | Engineer still approves; not FFS/shutdown |
| 8 GB / 7B Q4 VRAM | ~**4.5–5.5 GB** weights+KV at 4–8k ctx; **one** model | **Unverified** (llama.cpp community tables, not our `nvidia-smi`) | Slide 3/4 | “Fits 7B-class Q4; we will measure on 4060” |
| Typical 7B Q4 speed on 8 GB class | ~**25–40 tok/s** (blogs) | **Unverified** | Q&A only | Do **not** print as our benchmark |
| Shadow ChatGPT accounts | **73.8%** workplace ChatGPT = non-corporate | Vendor **Observed** (Cyberhaven Q2 2024, 3M workers) | Slide 5 uniqueness *or* 6 | “Vendor telemetry, not India PSU census” |
| Sensitive share to AI tools | **27.4%** (2024) → **34.8%** (2025 report) | Vendor **Observed** (Cyberhaven) | Optional | Don’t mix years in one cell |
| Employees paste non-public data | **48%** of orgs admit it; **27%** banned GenAI for a time | Vendor **Observed** (Cisco 2024 Privacy Benchmark, n=2,600, 12 countries) | Slide 5 social | Not an MRPL survey |
| IndiaAI Mission | **₹10,371.92 crore**; **10,000+ GPUs** compute pillar | **Official** PIB 07 Mar 2024 PRID **2012355** | Slide 6 | We **complement** this; we are not the Mission |
| India AI market | **USD 8 bn (2025)** → ~**32 bn (2031)** @26% CAGR | **Observed** (NASSCOM CXO playbook citing that series) | Slide 6 *ecosystem* | **Not our TAM / revenue** |
| India GenAI market | IMARC **USD 1.5 bn (2025)** vs M&M **USD 2.23 bn (2025)** | **Invalidated as a single number** (vendors disagree) | **Do not print** | Conflict |
| India GenAI startups | **890+** by H1 2025; **USD 990 mn** cumulative funding | **Observed** (NASSCOM GenAI landscape 2025) | Slide 6 optional | Shows crowded apps; we are industrial air-gap |
| CERT-In logs | Rolling **180 days**; produce to CERT-In | **Official** Direction 20(3)/2022 | Slide 4/5 one word “180-day logs” | FAQ: copies *may* sit abroad if producible — we still keep logs **on-prem** by design |
| DPDP 2023 | Personal data duties; **not** a universal air-gap law | **Official** | Slide 5 “DPDP-shaped: no external processor” | Do not say “DPDP requires air-gap” |
| OCR accuracy | DocLayNet = **layout** dataset (80,863 pages, **scanned kept to a minimum**) | Paper **Official** as a *citation*, not a % for us | Slide 6 paper | **Do not write 99% OCR** |
| ICDAR 2023 layout mAP | Top ensemble **70.0 mAP** (WeLayout) | Paper | Q&A | Layout ≠ thickness transcription |
| Env: kWh/query | BLOOMz-7B ~**1.0×10⁻⁴ kWh**/inference (Luccioni et al. 2023, A100 cloud) | Paper | **Do not convert to “we save X kg”** | On-device can use **more** client energy than remote (CAIN 2025) |
| Prize / 34/500 / ₹crore | — | Drop | **Never on PDF** | Year-mix / theatre |

**KB correction:** do **not** print “38,000 GPUs”. PIB 2012355 says **10,000 or more**. Later MeitY figures, if any, need their own URL.

---

## 4. Slide-by-slide paste (playbook density)

### Slide 1 — Title

| Pointer | Paste |
|---|---|
| Problem Statement ID – | `SIH26117` |
| Problem Statement Title- | `Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work` (wrap left of brain graphic) |
| Theme- | `Smart Automation` |
| PS Category- | `Software` |
| Team ID- | `[TEAM_ID]` |
| Team Name- | `[TEAM_NAME]` |
| Oval | `[TEAM_NAME]` |

---

### Slide 2 — Idea (chrome → `[PRODUCT_NAME]`)

**Layout:** 2×2 or left stack + right loop. **Four official headers. Do not drop “Detailed explanation”.**

#### A. Proposed Solution (what it is)

- `[PRODUCT_NAME]` = **on-prem agentic workbench** for inspection/process knowledge work. **Not a chatbot. Not a new model.**
- Engineer gets **Word recommendation note + Excel thickness sheet** from a **scan**, plus **code that actually ran tests**.
- Backend = any staged **OpenAI-compatible `/v1`** on **org GPU**; workbench stores `base_url` + key + Model Cards.
- Proof of “sovereign” = **WAN unplug + visible log = 0 external calls** (PS Expected Solution).

#### B. Detailed explanation (how it works — this is the missing block)

**Prototype spine (P1):**  
Scan → Tesseract/Paddle OCR → gateway `task_type` → `/v1` 7B → JSON fact sheet → **HITL** → sandbox `CR=(t1−t2)/Δt` → `python-docx` DRAFT → audit.

**Org (P2–P3, same boxes):** replace JSON folder with **read-only EAM**; add SSO/SIEM; load larger staged models; **never** write PLC/DCS.

**Auto-select (PS):** router picks by **task** (`vision_extract` ≠ `code_sandbox` ≠ `draft_note`). On **8 GB**: **unload/load**; log shows **two model ids**. Not two 70Bs in VRAM.

**Agent:** plan → tools (file, OCR, EAM lookup, sandbox, spreadsheet) → iterate → stop. Skills on disk, no Skills Hub.

#### C. How it addresses the problem (map PS → mechanism)

| PS pain (verbatim idea) | Our mechanism |
|---|---|
| Claude/Codex forbidden; people paste P&IDs anyway | Nothing leaves LAN; egress log is the demo |
| Manual 1–5 day assemble of inspection packs | Cut **find/type** (estimate 50–70%); judgement stays human |
| Locked to one model; space moves fast | Model Cards + `GET /v1/models`; new GGUF = new card |
| Must act like an agent + real files | Skills + sandbox + docx/xlsx, not a chat bubble |
| Mid-range GPU / no 120B at venue | Sequential **7B-class Q4** on RTX 4060 8 GB (PS allows this) |

#### D. Innovation / uniqueness (3 ticks only — vs *named* software)

1. **vs ChatGPT / Copilot / Claude:** air-gap + audit; they cannot take P&IDs (Cisco: 48% already paste non-public data).  
2. **vs Open WebUI / Ollama / PrivateGPT / AnythingLLM:** local chat+RAG already exists; we add **task router + HITL JSON gate + sandbox-verified calc/code + template Word**.  
3. **vs OpenHands / Continue:** coding agents; we are an **inspection-document workbench** that *also* has a jail. We **borrow patterns, we do not fork them**.

**Right-side boxes to draw:**

`Scan → OCR → Gateway(task) → /v1 (one 7B)`  
`→ HITL JSON → Docker --network=none (CR + pytest)`  
`→ Word/Excel DRAFT`  
`WAN log = 0`

No URL. No fake UI shot.

---

### Slide 3 — Technical approach

#### Technologies (table, not logos)

| Layer | Candidate tech (pick at build) | Purpose |
|---|---|---|
| Workbench UI + gateway | Python 3 · FastAPI (or equivalent) | Task route, auth, timeout, HITL, audit. Laptop B **3050 not for LLM** |
| Runtime | OpenAI-compat `POST /v1/chat/completions` + `GET /v1/models` via **llama.cpp server** or **Ollama** or **vLLM** | One 7B-class on **RTX 4060 8 GB** |
| OCR | **Tesseract** and/or **PaddleOCR** (CPU) | Scan/photo → text; fail closed if unusable |
| Agent skills | On-disk `SKILL.md` ([agentskills.io](https://agentskills.io/specification)) | extract / calc / draft / code / policy |
| Calc + code jail | **Docker Desktop WSL2** `docker run --network=none --cpus=1 --memory=1g` | CR script + pytest. **Never** wrap the GPU |
| Files | **python-docx**, **openpyxl** | Word note, thickness sheet |
| Schema / validation | JSON Schema (+ Pydantic at build) | Fact sheet; `NOT FOUND` |
| KB / EAM | Folder JSON **same fields as future API** | Mock now, connector later |
| Egress | Host/packet log + WAN unplug | PS “actual proof” |
| Fallback | WSL jail if Docker banned | **Weaker — say so** |

**Do not lock** Ollama vs vLLM vs llama.cpp on the PDF. Write **OpenAI-compat `/v1`**. Stars (this fetch, order-of-magnitude): Open WebUI ~152k · llama.cpp ~128k · vLLM ~92k · Tesseract ~77k — popularity ≠ industrial fit.

**Hardware line:** Laptop A 4060 8 GB = runtime. Laptop B 3050 6 GB = UI. Venue GPU = change `base_url` only.

#### Methodology (same loop as slide 2, plus)

**Wording (mandatory):** *Multiple open-weight **roles** in one system; auto-pick by task; on 8 GB **load one at a time**; two ids in the log.*

**LCD (why we are not “full OpenAI”):** no `tool_choice`, no remote image URLs, no `/v1/responses` as a requirement. Vision = `data:image` base64. Capability = **Model Cards**.

---

### Slide 4 — Feasibility and viability

#### Feasibility (three facts)

1. **PS already allows** smaller models if 120B hardware is absent. 8 GB Q4 7B is that case (~4.5–5.5 GB class, community tables).  
2. **36h / P1 is one loop**, not SAP. Portal allows **public sample PDFs/P&IDs**.  
3. **Viability:** OSS + existing GPU → no new H100 for demo; org scale = add GPUs behind the **same** socket. Sustainability = Model Cards + USB/offline weight update + HITL forever.

#### Table — REAL / MOCK / LATER

| | REAL (P1) | MOCK | LATER (P2–P3) |
|---|---|---|---|
| OCR → HITL JSON → Word | Y | | |
| Excel CR in sandbox | Y | | |
| Two task types, two model ids | Y sequential | | Dual-load VRAM |
| pytest in Docker none | Y | | |
| WAN off + log | Y | | Certified air-gap |
| EAM / historian / SAP | | JSON same schema | Read-only API |
| PPT, 14B, SSO, SIEM | | | Y |
| DCS / SIS write | **Never** | | **Never** |

#### Challenges | Risk | Mitigation

| Challenge | Risk | Mitigation |
|---|---|---|
| 8 GB | Dual-load theatre | Unload/load; log two ids |
| 7B JSON/tools | Bad mm / bad CR | Schema + HITL; math **only** in sandbox |
| Bad scan / handwriting | Invented readings | Confidence; `NOT FOUND`; fail closed |
| Docker on Windows venue | Jail missing | Docker first; WSL fallback **on the slide** |
| “Air-gap” that still pulls weights | WAN on first run | Pre-stage GGUF; unplug; host log |
| Hallucinated approvals | Engineer trusts draft | DRAFT badge; no statutory decision |
| CERT-In / DPDP | Logs/prompts as personal or ICT data | On-prem 180-day logs; no cloud processor |
| OCR literature ≠ plant scans | Fake 99% | Cite DocLayNet as **layout** research only; we measure later |

---

### Slide 5 — Impact and benefits

#### Target audience

| Who | What changes |
|---|---|
| **Primary:** inspection / integrity engineer | Draft note + sheet from scan; **they** approve |
| **Secondary:** process, HSE, maintenance, IT security | Same workbench, more skills later |
| **Org (MRPL-class):** 15 MMTPA CPSE, ~2,530 staff | Stop shadow paste of P&IDs; reuse mid-range GPU |
| **Replication:** other PSUs / defence-linked plants | Same socket; different templates |

Do **not** write “2,530 users of our app.”

#### Benefits (one line each + one sourced KPI)

**Social:** Reduce shadow AI on confidential drawings. Cisco 2024: **48%** of orgs admit pasting non-public data into GenAI; **27%** banned GenAI for a period (survey, not MRPL). Cyberhaven: **73.8%** of workplace ChatGPT accounts were non-corporate.

**Economic (honest):** Cut elapsed **find-and-type**, not headcount. Reuse **8 GB** card. **No ₹crore / no prize.** IndiaAI ₹10,371.92 cr is **national compute**, not our P&L — put rupees on **slide 6**.

**Environmental (honest):** No extra **training** run. Inference energy is **not automatically lower** on-prem (Luccioni 2023; CAIN 2025 on-device vs remote). Claim: **no cloud round-trip of P&IDs**; reuse hardware already bought.

**Policy alignment (one line):** On-prem prompts/logs (DPDP-shaped processor control) + 180-day ICT logs (CERT-In-shaped). Not a legal opinion.

**KPI — pick one caption, don’t mix:**

- **A (time, labelled):** Scanned inspection pack today **1–5 days** elapsed → **target 2–3 h to a DRAFT** (our industry workflow study; **not an MRPL SLA**).  
- **B (safer):** Most elapsed time is find-and-type (**50–70%**, same study). We attack that. We do **not** auto-approve FFS.

---

### Slide 6 — Research and references

**Do not write “Click here”.** Tiny URLs / arXiv ids.

**Gov / org / PS**

- SIH26117 Expected Solution (Word path, sandbox, OCR, zero-egress) — portal  
- MRPL profile: 15 MMTPA — https://www.mrpl.co.in/Content/Profile  
- MoPNG MRPL page — https://mopng.gov.in/en/refining/mrpl  
- OISD-STD-128 *Inspection of Unfired Pressure Vessels* — name + https://www.oisd.gov.in/en-in/oisd-standards-list (do not dump standard text)  
- DPDP Act, 2023  
- CERT-In Direction 20(3)/2022 — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf  
- IndiaAI Mission Cabinet 07 Mar 2024, **₹10,371.92 crore**, 10,000+ GPUs — PIB PRID **2012355** https://www.pib.gov.in/PressReleasePage.aspx?PRID=2012355  
- NIST AI 600-1 Generative AI Profile (Jul 2024) — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf  

**Papers (we use the idea, we did not re-run the experiment)**

- Yao et al., **ReAct**, 2022 — arXiv:2210.03629 (plan–act–observe)  
- Schick et al., **Toolformer**, 2023 — arXiv:2302.04761 (when to call tools; not our multi-step loop by itself)  
- Lewis et al., **RAG**, 2020 — arXiv:2005.11401 (grounding; we cite pages, not Wikipedia)  
- Pfitzmann et al., **DocLayNet**, KDD 2022 — arXiv:2206.01062 (corporate layout; **not** our OCR %)  
- Luccioni et al., **Power Hungry Processing**, 2023 — arXiv:2311.16863 (inference energy; **no fake kg saved**)  

**OSS we compose (patterns, not forks)**

- llama.cpp — https://github.com/ggerganov/llama.cpp  
- vLLM — https://github.com/vllm-project/vllm  
- Tesseract — https://github.com/tesseract-ocr/tesseract  
- Agent Skills spec — https://agentskills.io/specification  
- python-docx / openpyxl / Docker  

**Market (ecosystem, not our sales)**

- NASSCOM: India AI ~USD 8 bn (2025) → ~32 bn (2031)  
- NASSCOM GenAI landscape 2025: 890+ startups — crowded **chat apps**; gap is **air-gapped industrial deliverables**

#### Competitor matrix (ticks only where true)

| | Air-gap proof | Task auto-select | Sandbox tests | HITL before Word | Word/Excel from fields | Inspection CR in jail |
|---|---|---|---|---|---|---|
| `[PRODUCT_NAME]` | Y (WAN log) | Y (2 ids) | Y | Y | Y | Y |
| ChatGPT / Copilot / Claude | N | cloud | N | weak | cloud files | N |
| Open WebUI + Ollama | possible local | weak/manual | N | weak | chat | N |
| PrivateGPT / AnythingLLM | often local | N | N | weak | chat/RAG | N |
| Continue.dev | local possible | coding | IDE | N | N | N |
| OpenHands | local *possible*; cloud features common | coding agent | Y (dev jail) | N | N | N |
| Azure Local / GDC Air-Gap | infra | N | N | N | N | N |
| IBM watsonx.governance | governance | N | N | N | N | N |

**Difference in one sentence:** others give **chat, infra, or coding agents**; we give **PSU inspection artefacts + cited numbers + a visible sovereign proof** on mid-range GPU.

---

### Slide 7

Delete before PDF.

---

## 5. Similar existing solutions — what is true vs theatre

**They exist.** Anyone who says “nothing exists” is wrong. The PS itself says Claude-class UX does not exist *for this constraint set*.

| Class | Examples | What they already do | Gap we fill |
|---|---|---|---|
| Cloud assistants | ChatGPT, Copilot, Claude, Gemini | Best UX/agent | Confidential P&IDs cannot go there |
| Local chat/RAG | Open WebUI, Ollama, LM Studio, Jan, GPT4All, PrivateGPT, AnythingLLM | Offline chat, some RAG/OCR plugins | No HITL fact-sheet, no plant Word, no CR jail, no PS-style routing proof |
| Coding agents | Continue, Aider, OpenHands, Cursor (pattern only) | Sandboxed code | Not inspection notes; some **phone home** |
| Serving | llama.cpp, vLLM, LocalAI, Ollama | `/v1` | Not the workbench |
| Frameworks | LangChain, LlamaIndex, Haystack | Glue | Not a governed product |
| Cloud air-gap infra | Google Distributed Cloud Air-Gapped, Azure Local disconnected, watsonx.governance | Rack/governance | Still need the **application** |
| Plant software | SAP PM / Maximo / RBI tools | Assets, WO, thickness databases | Not agentic Word from **scans** on air-gap LLM |
| India models | Sarvam, Krutrim, BharatGen, AIKosh, Bhashini | Indic models/data | Model ≠ workbench |

**Innovation we can defend:** system integration (task route + Model Cards + HITL + sandbox calc + template docs + egress proof) on **open weights**.  
**Innovation we cannot defend:** new architecture paper, 99% OCR, first entity-resolution product in the world.

---

## 6. Technical innovations (precise list for Q&A)

1. **Software/hardware split:** workbench never owns CUDA; runtime swap = `base_url`.  
2. **Task router + Model Cards** because OpenAI `/v1` does not expose “this GGUF can see images.”  
3. **HITL JSON as a hard gate** before `python-docx` (stops chat-paste “approval notes”).  
4. **Deterministic engineering math in the same jail as pytest** (LLM never computes CR).  
5. **Sequential multi-model** as a first-class 8 GB design, not an apology.  
6. **Skills on disk** (air-gap), five prototype skills, rest of KB workflows as **future skills not fake modules**.  
7. **Egress as a product feature**, not a README claim.

---

## 7. What is still missing (collect next — does **not** block filling)

| Missing | Effect on PDF | Collect how |
|---|---|---|
| Real `[PRODUCT_NAME]` | Slide 2 chrome | You name it |
| Team ID / registered name | Slide 1 | Portal |
| `nvidia-smi` on 4060 | Speed/VRAM as **ours** | One screenshot later, finale |
| Public sample scan | Demo, not idea PDF | Portal dataset / printed table photo |
| Serving binary choice | Slide 3 already says `/v1` | At build |
| Plant letterhead | Never on SIH | Use our field names |

---

## 8. How to shrink this into six slides (craft)

- Slide 2: four headers + **one** loop. If it overflows, **cut adjectives**, not the detailed 8-step.  
- Slide 3: **one** table + **one** flow (copy slide 2).  
- Slide 4: REAL/MOCK + 5-row risk table.  
- Slide 5: audience 3 rows + KPI A **or** B + 3 impact lines.  
- Slide 6: 8 bullets with URLs + **small** matrix (5 columns, 5 rows).  
- If a screener only remembers one thing: **scan → HITL JSON → sandbox CR → Word, WAN=0, two model ids.**
