# PPT fill kit — SUPERSEDED

**Do not use this file to fill the PPT.** It was too generic: it merged slide-2 “Proposed” with “Detailed explanation”, named almost no OSS, and had almost no sourced numbers.

**Use instead:** `sih_research/PPT_FILL_PACK_v2.md`

Kept below only as a historical outline.

---

# PPT fill kit — you fill, we do not touch the PPTX (v1, outdated)

**Date:** 2026-09-16  
**You:** paste into official `SIH2026-IDEA-Presentation-Format.pptx` → delete slide 7 → save **PDF**.  
**Me:** no PPTX edits.

Placeholders: `[TEAM_ID]` `[TEAM_NAME]` `[PRODUCT_NAME]`

---

## 1. Adversarial recheck — enough data?

**Yes, enough to fill a strong 6-slide idea PDF now** — if you use tables/diagrams, stay honest on 8 GB, and leave the three placeholders.

**Not enough** for: a live URL, a UI screenshot, a measured MRPL KPI, a locked product name, Team ID.

Those absences are **OK for screening** (playbook: PDF must stand alone; no fake URL). They are **not** OK to invent.

| Slide | Enough? | Weak spot | What to do |
|---|---|---|---|
| 1 | Yes | ID `SIH26117` vs card `26117` | Use **SIH26117** (portal table). Switch only if the idea form shows 26117 |
| 2 | Yes | Looks like a chatbot | Named `[PRODUCT_NAME]` + loop diagram + 3 uniqueness ticks |
| 3 | Yes | “Models at once” vs 8 GB | Use **wording A** below |
| 4 | Yes | Overclaim 36h | Real vs Mock table — mandatory |
| 5 | Yes | Fake hours | **Pick KPI A or B** below |
| 6 | Yes | Green-tick theatre | Matrix only where true; no PPT tick |

**Do not wait for prototype** to submit the idea PDF. Portal deadline from listing: **30 September 2026** (ops only — not a slide).

---

## 2. Strategy (playbook, compressed)

Official: 6 slides including title · don’t rename pointers · points/diagrams **not paragraphs** · unique vs prior events · PDF only.

Observed (steal craft, not “winner” claims):

- Left text, **right one diagram** (slide 2–3).
- **Tables:** Layer/Tech/Purpose · Real/Mock · Challenge|Risk|Mitigation · You vs tools.
- One **sourced** number, labelled estimate — or no number.
- Fill `[TEAM_ID]` later; blank ID is a known fail in sample decks — placeholder is fine in your working file.

**Landmines**

- Wall of bullets (last discarded deck).
- Logo salad (Ollama+vLLM+LangGraph+Flask+Django).
- “We run 120B / 14B / two models in VRAM.”
- Screenshot that isn’t ours.
- Claiming PPT in 36h (PS mentions PPT; **36h = Word+Excel only**).
- ₹crore, 99% OCR, prize money, 34/500.

---

## 3. What to put on each page (paste-ready)

### Slide 1 — Title

| Pointer | Paste |
|---|---|
| Problem Statement ID – | `SIH26117` |
| Problem Statement Title- | `Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work` (wrap; stay **left** of the brain graphic) |
| Theme- | `Smart Automation` |
| PS Category- | `Software` |
| Team ID- | `[TEAM_ID]` |
| Team Name (Registered on portal)- | `[TEAM_NAME]` |
| Oval | `[TEAM_NAME]` |

Skip: college logos, deadline, prize.

---

### Slide 2 — Idea (title chrome → `[PRODUCT_NAME]`)

**Keep the three official headers** in the body.

**Layout:** 2 columns. Left = three blocks. Right = **boxes**, not a paragraph of arrows.

**Left — Proposed Solution**

- `[PRODUCT_NAME]`: self-hosted workbench on the org GPU — **not a chatbot**.
- Loop 1: scan → on-device OCR → HITL → **Word + Excel**.
- Loop 2: code **run + tests** in a no-network sandbox.
- Proof: WAN off + visible log (PS: that *is* the sovereign claim).

**Left — How it addresses** (map the PS, don’t rewrite the PS)

- Claude/Codex forbidden → nothing leaves premises.
- Not locked to one model → **task** router; new models = new card, no redesign.
- Agent: files, sandbox, spreadsheet, local KB, iterate.
- Expected Solution: ≥2 task types, inspection→Word, sandbox coding, OCR/vision, zero external calls.

**Left — Uniqueness** (3 lines only)

- vs Open WebUI / Ollama / PrivateGPT: local chat already exists; we add **task route + template Word + sandbox calc + HITL + egress proof**.
- vs ChatGPT / Copilot: air-gap; **7B-class sequential on RTX 4060 8 GB** (PS allows smaller if 120B absent).
- Not DCS/SIS control. Not a new LLM.

**Right — draw**

`Scan → OCR → Gateway(task) → local /v1`  
`→ HITL JSON → sandbox CR → Word DRAFT`  
`+ code/pytest in Docker --network=none`

No URL.

---

### Slide 3 — Technical approach

**Header 1 — Technologies** → **this table** (not a logo row)

| Layer | Tech | Purpose |
|---|---|---|
| Workbench (Laptop B) | Python UI + gateway | Route, HITL, audit. 3050 **not** for LLM |
| Runtime (Laptop A) | OpenAI-compat `/v1` | One 7B-class on **RTX 4060 8 GB** |
| Ingest | CPU OCR | Scan/photo → text (portal allows public sample PDFs) |
| Calc / code | Docker `--network=none` | CR formula + pytest. **Not** the GPU container |
| Files | python-docx, openpyxl | Word note, thickness sheet |
| KB | JSON = future EAM schema | Mock socket, real lookup |

Stack brands (Ollama vs vLLM): write **“OpenAI-compat /v1”**. Pick the binary later.

**Header 2 — Methodology** → same flow as slide 2, plus:

**Wording A (recommended) for “models at once”**  
*Support multiple open-weight roles in one system; auto-pick by task; on 8 GB **load one at a time** (two model ids in the log).*

**Wording B (weaker)**  
*Two models available; router selects.* — drop this; sounds like simultaneous VRAM.

**36h vs later on this slide:** one loop only. Plant GPU = change `base_url`.

---

### Slide 4 — Feasibility

**Table 1 — 36h honesty**

| | REAL now | MOCK / LATER |
|---|---|---|
| OCR → HITL → Word | REAL | — |
| Excel CR in sandbox | REAL | — |
| Two task types, two model **ids** | REAL (sequential) | Two LLMs in VRAM = LATER |
| Sandbox pytest | REAL | — |
| WAN off + log | REAL | Certified air-gap LATER |
| EAM / historian | JSON same schema | Live API LATER |
| PPT pack, SAP, 14B | **Not claimed** | PPT = LATER (PS lists it; 36h does not) |

**Table 2 — risks**

| Challenge | Risk | Mitigation |
|---|---|---|
| 8 GB | Fake dual-load | Unload/load; log two ids |
| Small model | Bad tools/JSON | Schema + HITL; numbers only in sandbox |
| Bad scan | Invented mm | Confidence; `NOT FOUND` |
| No Docker at venue | Host pytest | Docker first; WSL jail fallback **said on the slide** |
| “Air-gap” app-only | Model pull on WAN | Pre-stage weights; unplug + packet/host log |

---

### Slide 5 — Impact

**Audience**

| Who | Change |
|---|---|
| Primary: inspection engineer | Draft note + sheet from a scan; **they** approve |
| Org | Less shadow paste of P&IDs into public AI |

**KPI — pick one (do not mix)**

**A (recommended if you want a number)**  
Scanned inspection pack today **1–5 days** elapsed → **target 2–3 hours to a DRAFT** (industry estimate from our workflow study; **not an MRPL SLA**). Judgement still human.

**B (safer, no hours)**  
Most elapsed time is **find-and-type** (about 50–70% in the same study). We cut that. We do **not** auto-approve FFS / shutdown.

**Social / economic / env (one line each)**  
Social: stop shadow Claude on confidential files.  
Economic: reuse the 8 GB card; **no crore claim**.  
Env: no extra training run claimed.  
Policy: one line — data stays on-prem (DPDP-shaped); logs kept (CERT-In-shaped). Not a legal opinion.

---

### Slide 6 — References

- SIH26117 Expected Solution (Word path, sandbox, OCR, zero-egress).
- OISD-STD-128 (name only). API 510-class **fields** (CML, thickness, CR).
- OpenAI-compat local serving. Agent Skills on disk. Code jail ≠ GPU.
- SIH 2026: 6-slide PDF; nine criteria; **no published weights**.

**Matrix**

| | Air-gap | Cite / NOT FOUND | Sandbox tests | HITL before Word | Word/Excel |
|---|---|---|---|---|---|
| `[PRODUCT_NAME]` | Y | Y | Y | Y | Y |
| ChatGPT / Copilot / Claude | N | — | N | — | cloud |
| Open WebUI / Ollama chat | maybe local | N | N | weak | chat |
| PrivateGPT-class | often local | partial | N | weak | chat |

No PPT column. No accuracy %.

---

### Slide 7

Delete before PDF.

---

## 4. Two “possibilities” that change the PPT (choose, don’t blend)

| Choice | PPT effect | When to pick |
|---|---|---|
| KPI A vs B | Slide 5 has a number or not | A if you can say “estimate” out loud; B if a screener will ask “who timed it?” |
| Wording A on multi-model | Slide 3 survives an 8 GB question | Always A |
| Diagram-heavy vs table-heavy | 2–3 more visual; 4–6 more tables | Playbook wants **both**: diagram on 2–3, tables on 3–4–6 |
| Mention public sample PDFs | One line on 3 or 4 | Yes — portal dataset line; proves we don’t need MRPL files |

---

## 5. What we will collect later (prototype mode — not this PDF)

- `[TEAM_ID]` `[TEAM_NAME]` `[PRODUCT_NAME]` real strings  
- Public sample scan (portal allows)  
- Running OCR→Word + sandbox pytest + two model ids + WAN log  
- Then: optional screenshot **of our UI only** for a **finale** deck, not required for this portal PDF  

---

## 6. Recheck answer

We have **enough validated data to fill the idea PPT ourselves** using this kit + placeholders.  
We do **not** have enough to pretend the product is already running. Screening does not require that if the loop and 36h honesty are clear.

If a slide still feels empty, it is a **layout** problem (draw the boxes / make the table), not a missing research problem.
