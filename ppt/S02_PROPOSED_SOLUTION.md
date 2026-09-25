# Slide 2 — Proposed Solution

**Official pointers (keep all four):**  
• Detailed explanation of the proposed solution  
• How it addresses the problem  
• Innovation and uniqueness of the solution  

**Chrome title:** Knowledge Work Bench  
**Narrative job:** Name the product, map PS pains, three uniqueness ticks, **context diagram on the bottom band**.  
**Layout:** **Top ~62%** = text (Proposed / How / Addresses / Uniqueness) · **Bottom ~35%** = Context diagram — gen **920×420** empty-top from [`prompt/DALLE_S02_CONTEXT.md`](./prompt/DALLE_S02_CONTEXT.md), **crop ~920×200** (topology also in `D01_CONTEXT_DIAGRAM.md`).

---

## 0. Primary visual — Context diagram (bottom of slide)

**Image prompt (canonical):** [`prompt/DALLE_S02_CONTEXT.md`](./prompt/DALLE_S02_CONTEXT.md) · gen **920×420** (empty top) → crop **~920×200**  
**Topology / Mermaid:** [`D01_CONTEXT_DIAGRAM.md`](./D01_CONTEXT_DIAGRAM.md) — use **§2 bottom-band** or **§5 single-row Mermaid** if drawing by hand.

**One-line caption under the band:**  
Worker assisted → exports DRAFT · Admin stages USB (quarantine/SHA) → enables Model Cards → local runtime · Gateway only · Monitor A ≠ CERT · Plant read-only · Public net blocked

**Bottom-band mini (designer paste):**

```
USB→Stage→Admin─┬─enable→Cards→Runtime
Worker⇄Desk→Core┴─prompts→Gateway→Runtime
              ├→ DRAFT ←export← Worker
              └→ MonA≠CERT · Plant RO · Net BLOCKED
```

---

## 1. On-slide paste (dense — preferred)

### A. Proposed solution

- **Knowledge Work Bench (KWB)** — fully offline industrial workbench for confidential knowledge work.  
- Delivers **DRAFT Word (`.docx`)** from inspection extracts + **sandbox-verified** calc/code.  
- **Pluggable open-weight models** behind a local OpenAI-shape `/v1` socket; workbench = client.  
- **Task grants**, **human checkpoints** (engineer confirms), audit, and **Monitor A evidence pack** (start–stop snapshot — **≠ CERT**).  
- Same architecture for demo laptop and org GPU server — scale cards and connectors, not a rewrite.

### B. Detailed explanation (how it works)

```
Start task → Open task grant → Pick task model card
  → Load / paste extract → Confirm extract (human)
  → Retrieve knowledge (cite or abstain)
  → Review citations (human)
  → Pack → Local gateway → Runtime (one model)
  → Tools / sandbox (isolated calc/code)
  → Output checks → Generate DRAFT Word
  → Self-check DRAFT (human) → Export leave → Audit
```

- **Auto-select:** task type → model card (inspection ≠ coding).  
- Mid-GPU: **load one model at a time**; honest demo = two task types / one adopted model tag.  
- Org later: more cards + read-only connectors — **never** write DCS / EAM / ERP.

### C. How it addresses the problem

| PS pain | KWB mechanism |
|---|---|
| Cloud assistants forbidden; shadow paste risk | Premises-only path; gateway deny; evidence pack |
| Slow manual inspection packs | Guided walk → **DRAFT Word** in hours (**estimate**) |
| Locked to one model forever | Task model cards; add tags without redesign |
| Need agent + real files | Multi-step tools + sandbox + **docx** |
| Mid-range GPU / no 120B | Smaller open-weight; sequential load (PS allows) |
| Must prove sovereignty | Logs + Monitor A evidence pack |

### D. Uniqueness (exactly 3 ticks)

1. **vs cloud assistants (Claude / Copilot / ChatGPT):** air-gapped open-weight path, grants, audit — P&IDs stay on site.  
2. **vs local inference front-ends (e.g. Open WebUI + Ollama):** we add **task routing + human checkpoints + sandbox verify + template Word + evidence pack**.  
3. **vs coding-agent harnesses (OpenHands / Continue-class):** we are an **inspection-document workbench** that also runs a jail — patterns studied, not a fork as the product.

### Right-side visual

Use **Context diagram** (`DALLE_S02` gen **920×420** → crop **~920×200** / `D01`) — not a second competing flowchart.  
Keep this **plain** process strip if space remains:

`Confirm extract → Retrieve → Review citations → DRAFT Word → Self-check → Export leave`---

## 2. Full inventory (overflow / denser layouts / Q&A)

### 2.1 One-line pitch (speaker)

Knowledge Work Bench is an offline industrial workbench that routes open-weight models by task, gates human verification, and delivers cited DRAFT Word plus sandbox-verified calc/code — with grants, audit, and a Monitor A evidence pack — on mid-range GPU hardware.

### 2.2 Expected Solution coverage (screener checklist)

| Expected Solution clause | Where on this slide |
|---|---|
| Mid-range GPU / smaller model OK | Addresses table + uniqueness |
| Auto-select ≥2 task types | Detailed + auto-select bullet |
| Scan → findings → Word | Loop + proposed |
| Coding + sandbox verify | Proposed + uniqueness #3 |
| Multimodal / scanned doc | Loop “Scan/extract” + addresses |
| Logs / network monitor proof | Monitor A evidence pack |

### 2.3 Demo walk (plain words — align with Electron desk)

`Start → Confirm extract → Retrieve → Review citations → Generate DRAFT → Self-check DRAFT → Export leave`  
Fail-closed demos: block secrets · block public model · revoke grant · block leave after failed sandbox.

### 2.4 What we provide / hold (honesty strip — optional footer)

| Provide (day-1) | Hold / Later |
|---|---|
| Word DRAFT · grants · human checkpoints · sandbox · Monitor A | Live plant OCR engine · Excel/PPT artefacts · SSO · installer |
| Two task types · one adopted model tag | Second offline chat tag when staged |
| Fixture / paste extract + confirm | Full VLM plant drawings |

### 2.5 Personas (one line each — Q&A)

- **Primary:** inspection / integrity engineer — DRAFT recommendation note.  
- **Secondary:** process / HSE / maintenance — same workbench, more skills later.  
- **IT / Admin:** runtime + cards + policy — outside the engineer UI.

### 2.6 Boundaries (never claim)

- Autonomous FFS / permit / DCS decisions  
- CERT-In certificate  
- In-app Approver replacing paper dual-control  

---

## 3. Diagram notes for designer

- Primary art = **D01 / DALL·E S2** bottom band (crop **~920×200** from **920×420**, full width, ~1/3 height) — not a tall right column.  
- Same navy `#1F497D` · accent `#0070C0` · warn `#C0504D` for blocked net.  
- Keep Admin / Stage / Cards / Gateway — do not drop for space; shorten labels instead.  
- No robot / neural-net clipart.  
---

## 4. Speaker notes (~1:10)

“Industrial sites generate inspection packs and notes that cannot leave the premises. Knowledge Work Bench opens a **task grant**, picks a **model card** by task, runs retrieve and draft under **human checkpoints**, and leaves a **DRAFT Word** soft copy. Coding tasks go through the **sandbox**. **Monitor A** is an evidence pack — not a CERT badge. Three differences: we stay offline versus cloud assistants; we add gates and Word versus a bare local model UI; we centre inspection artefacts versus a pure coding agent.”

---

## 5. Adversarial check

| Risk | Fix |
|---|---|
| “Chatbot” language | Use **workbench / DRAFT Word** only |
| H1/H2/H3 jargon on PDF | Use **Confirm extract / Self-check DRAFT / Export leave** — see `00_PLAIN_LANGUAGE.md` |
| Loop too jargon-heavy | Prefer labels above; expand in speaker notes |
| Missing coding spine | Keep sandbox in proposed + uniqueness #3 |
| Claiming CERT | Always “evidence pack ≠ CERT” |
