# Red team, skills, templates, SIH criteria — v1

**Date:** 2026-09-16  
**Role:** Principal Solutions Architect / Harness Engineer / Research Engineer  
**Target:** `DESIGN_ORG_PROTOTYPE_v1.md`  
**Honesty rule:** no self-scores. Official SIH 2026 PDF lists **nine named criteria and no marks**. Any “100 marks / weights” from college sites is **not** national fact.

---

## A. Verdict in one paragraph

The design is **the right product shape** for SIH26117 (workbench + task gateway + REAL/MOCK/LATER + inspection→Word). It will **fail judging** if we (1) look like Open WebUI + Ollama, (2) fake routing with one model, (3) paste chat into Word, (4) skip a visible egress proof, or (5) ship a 40-skill “industry OS” instead of three working skills. Skills and templates **help small models**; they are not novelty by themselves. We have **no running prototype**, so feasibility / UX / practicability are **unproven**. I will not guess a rank.

---

## B. Adversarial attack on the design

### B1. Attacks that can kill the demo (fix before build)

| # | Attack | Why it is real | Required defence |
|---|---|---|---|
| 1 | **Fake routing** | PS: auto-select ≥2 task types. One 8B with two log lines that say `vision` / `draft` is theatre. | Two **different** `model` strings in the log **or** sequential load of two cards, with timestamps. Jury may ask to swap the scan. |
| 2 | **Chat pasted into .docx** | Expected Solution is a Word **file**. Judges open it. | `python-docx` from a **JSON fact sheet** after HITL. Empty fields stay `NOT FOUND`, never invented. |
| 3 | **LLM invents corrosion rate** | API 510 / plant practice: CR = (t_prev − t_curr) / Δt. Hallucinated mm/y is an engineering lie. | `task_type=calc` → sandbox Python; print inputs. Skill must **forbid** mental arithmetic. |
| 4 | **Egress monitor watches only the app** | Ollama/HF/Windows update can still phone home. PS wants proof **no external calls**. | Physical WAN unplug **plus** a monitor that shows destinations (host firewall / packet log). Pre-stage weights. |
| 5 | **OCR only on a clean digital PDF** | Real inspection packs are image-only, skewed, mixed units. | Hold-out **scan** (even synthetic photograph of a table). Show OCR confidence. Tolerate errors. |
| 6 | **Mock EAM never queried** | “Connector placeholder” with a hardcoded tag in the prompt is fake integration. | Agent must `kb_search` / `eam_lookup` the JSON. If miss → `UNRESOLVED_TAG`. |
| 7 | **Vision URL fetch** | Ollama OpenAI compat: remote image URLs unsupported; air-gap forbids fetch. | Only `data:image/...;base64`. |
| 8 | **Sandbox wraps the GPU server** | Windows + Docker `network=none` on Ollama breaks inference. | Sandbox = **code only**. Runtime stays a normal local server. |
| 9 | **“Models at once” on 8 GB** | Mid-range VRAM usually one active model. | Sequential load. Do not claim simultaneous 70B+VLM. |
| 10 | **Skills as the product** | 11 document types × full OISD in context = token sludge and a toy that never finishes the spine. | Prototype: **≤5 skills**, progressive disclosure ([Agent Skills](https://agentskills.io/specification) / Hermes-class). Rest stay on the **org paper**. |

### B2. Attacks that kill novelty (slides, not code)

| # | Attack | Honest answer |
|---|---|---|
| 11 | “This is PrivateGPT / Open WebUI / AnythingLLM.” | Those chat a local model. We must **show** template Word, sandbox calc, task router log, draft badge, zero egress. If the demo is a chat box, they are right. |
| 12 | “Ollama already routes models.” | Ollama is a **runtime**. PS routing is by **task**. If our gateway is a dropdown the user picks, we failed auto-select. |
| 13 | “MRPL already has AI.” | Process/APC AI ≠ knowledge-work workbench. Say that once; do not claim we invented plant AI. |
| 14 | “Nothing like this exists.” | **False.** Adjacent OSS and vendors exist. Novelty = **integration for confidential industrial deliverables + proof of sovereignty**, not a new LLM. |
| 15 | “Air-gap” on hotel Wi-Fi with HF pulls. | Isolated LAN ≠ certified air-gap. Call the demo **offline / no WAN**. Certified air-gap is LATER. |

### B3. Attacks on skills + prompts (your new proposal)

| # | Attack | Defence |
|---|---|---|
| 16 | Skill says “you are a senior API 510 inspector” → model **decides** remaining life. | Skills instruct **procedure**. Remaining life / FFS / shutdown = HITL. Draft badge forever in prototype. |
| 17 | Skill dumps full OISD-STD-128 into the prompt. | **Copyright + tokens.** Cite *edition name* in a KB stub. Do not paste standard body. Field lists only. |
| 18 | Prompt asks for JSON but small model emits prose. | Schema + retry + fallback parser; HITL if invalid. Same as tool-calling fragility (server-dependent). |
| 19 | Eleven templates in the prototype. | Org paper: 11 types already in `06-document-templates/`. **Build 1** (inspection recommendation). Optional 2nd: tiny code-result note. |

### B4. What still stands (do not throw away)

- Workbench ≠ GPU optimiser  
- Gateway = OpenAI LCD + **task** cards  
- Org paper / prototype overlay / REAL-MOCK-LATER  
- Inspection spine as the thing we cannot lose  
- Never write DCS/SIS/PLC  

---

## C. Skills library (effective, not decorative)

**Standard to copy (format, not Hermes-the-product):** [agentskills.io](https://agentskills.io/specification) — directory + `SKILL.md` YAML `name`/`description`, progressive disclosure (list → body → `references/` / `assets/`). Hermes documents the same pattern. Air-gap: skills live **on disk**, no Skills Hub.

**How they plug in:** router picks `task_type` → agent may `skill_view(name)` → tools in `allowed-tools` only → model never gets a web tool.

### Prototype set (build these)

| Skill `name` | When | Must force | Must forbid |
|---|---|---|---|
| `inspect-extract` | Scanned NDT / thickness pack | OCR then optional VLM; output **only** the JSON schema; units + page; confidence | Inventing missing mm; mixing in/mm silently |
| `inspect-calc` | Thickness / CR / remaining life **if** formula inputs exist | Call sandbox; show formula + inputs | LLM arithmetic; dropping outliers without a flag |
| `inspect-draft` | After HITL on fact sheet | Fill **controlled** Word sections; every number cited | Changing numbers; sounding approved |
| `code-sandbox` | Coding task | Write file → run tests in sandbox → return stdout | Network, host FS outside workspace |
| `sovereign-policy` | Always-on short | Draft + classification badge; no OT writes; no WAN | “I’ll look this up online” |

`sovereign-policy` is a **system preamble** (~400 tokens), not a 20-page skill.

### Org paper only (do not build for SIH demo)

`deviation-note`, `rca-report`, `moc-checklist`, `tbe-matrix`, `shift-handover`, `capex-nfa`, `incident-report`, `board-pack` — structures already in the KB. Skills for those = post-SIH.

### Skill file skeleton (prototype)

```
skills/
  inspect-extract/SKILL.md
  inspect-extract/references/extract-schema.json
  inspect-calc/SKILL.md
  inspect-calc/scripts/corrosion.py      # deterministic
  inspect-draft/SKILL.md
  inspect-draft/assets/inspection-recommendation.docx  # our fields, not MRPL letterhead
  code-sandbox/SKILL.md
  sovereign-policy/SKILL.md
```

---

## D. Prompt templates (short; tools do the work)

**Global system (always)**  
You are a **drafting** assistant inside an air-gapped industrial workbench. You do not approve, derate, or shut down equipment. If a value is missing, write `NOT FOUND`. Never call the network. Use only listed tools. Label every user-visible document `AI-generated draft — technical review required`.

**`vision_extract` / inspect-extract**  
Extract measurements into JSON. Do not recommend. If OCR confidence is low, still extract and set `confidence`. Do not convert units unless the source unit is explicit.

```json
{
  "equipment_tag_raw": "",
  "inspection_date": "",
  "method": "",
  "points": [
    {"cml_or_location": "", "t_mm": null, "unit_as_written": "", "page": null, "confidence": 0}
  ],
  "unreadable": [],
  "warnings": []
}
```

**`calc` / inspect-calc**  
Do not compute in prose. Call `sandbox_run` on `corrosion.py` with `t_prev`, `t_curr`, `delta_years`. If any input is `NOT FOUND`, skip calc.

**`draft_note` / inspect-draft**  
Fill template sections 1–5, 8–9 only if facts exist. Section “recommendation” must be **options for the engineer**, not a decision. Copy numbers **verbatim** from the approved fact sheet.

**`code_sandbox`**  
Implement the asked function. Run tests. If tests fail, patch once, re-run, then stop for HITL.

These prompts are **useless** without tools + HITL. That is the honest bound for 7B–14B models.

---

## E. Industry templates we can actually use

**We do not have MRPL letterhead or controlled forms.** KB already says internal templates are not public (`11-reference/05-sources.md`). Using a real PSU form verbatim is **copyright / identity** risk. We use **field structures** from public practice + our KB, branded as **“industry-typical, not MRPL official.”**

### E1. Use in prototype (one Word + one Excel)

From public API 510-class inspection practice (report contents summarised, **not** the standard text) and our `01-inspection-recommendation-note.md`:

**Word — Inspection recommendation (DRAFT)**  
Cover control block · 1.0 Requested decision (placeholder, HITL) · 2.0 Equipment ID · 3.0 Degradation · 4.0 Inspection evidence · 5.0 Calculation basis (sandbox output pasted) · 6.0 Codes **cited by name/edition only** (e.g. OISD-STD-128 *Inspection of Unfired Pressure Vessels*; API 510) · 8.0 Options · 9.0 Monitoring · 12.0 Approvals (blank signature lines) · DRAFT watermark.

**Excel — CML / thickness table**  
Tag · CML · component · t_nominal · t_previous · t_current · date_prev · date_now · CR (sandbox) · t_min (from mock datasheet JSON) · remaining life **only if t_min present** · flags (negative CR, mixed units, low OCR).

**Sandbox formula (public engineering, not a copied standard paragraph):**  
`CR = (t_previous − t_current) / Δt`  
Remaining life only if `t_min` is supplied by **data**, not by the LLM.

### E2. On org paper (already in KB — do not build all)

| KB file | Industrial analogue |
|---|---|
| `01-inspection-recommendation-note.md` | Integrity / inspection recommendation |
| `02-deviation-investigation-note.md` | Process deviation |
| `03-rca-report.md` | RCA |
| `04-moc-review-checklist.md` | MOC |
| `05-technical-bid-evaluation.md` | TBE |
| `06-shift-handover-note.md` | Shift log |
| `08-capex-approval-note.md` | PSU **note for approval** / NFA-style capex |
| `10-incident-investigation-report.md` | Incident |
| `12-ppt-board-pack-template.md` | Board pack — **LATER** |

Official catalogues (cite, don’t paste): [OISD standards list](https://www.oisd.gov.in/en-in/oisd-standards-list) (STD-128 vessels, 129 tanks, 130 piping).

### E3. What I will not do

- Paste OISD/API/ASME body text into the repo  
- Fake an MRPL document number / logo  
- Claim FFS per API 579 in the prototype (that is specialist; HITL)

---

## F. SIH 2026 criteria — where we **actually** stand

**Primary source:** official Guidelines p.20 (our extract): experts evaluate **novelty, complexity, clarity and details in the prescribed format, feasibility, practicability, sustainability, scale of impact, user experience, potential for future work progression.** Ideas must be **new** vs prior events (p.24). Mentors exist to turn ideas into a **working prototype** at the finale.

**Not fact:** numerical weights for 2026. MIC 2024 20/30/50 = historical rehearsal bias only. A college site saying “100 marks / nine parameters” is **unverified**.

**Today’s artefact:** architecture paper. **Not** a working prototype. Scores below are **gap ratings**, not jury marks.

| Official criterion | Paper (now) | If we ship the spine as designed | How we die |
|---|---|---|---|
| **Novelty** | Medium. Integration story is real; “local LLM” is not new. | Medium-high **only if** Word+router+egress+HITL are visible. | Chat UI demo. |
| **Complexity** | High on paper (OCR, route, sandbox, air-gap). | High if those parts **run**. | Diagram of 20 boxes, 1 chat. |
| **Clarity / format** | Strong if idea PDF follows user, workflow, real vs mock. | Strong. | “AI platform for India.” |
| **Feasibility** | Honest: mid-GPU, mocks, small models (PS allows). **Unproven until it runs.** | High if E2E works offline on two laptops. | Depends on venue 120B or real SAP. |
| **Practicability** | Spine matches inspection engineer. | High if a stranger can upload→Word in minutes. | Developer CLI only. |
| **Sustainability** | Weak until model cards + offline update + who owns it after SIH. | Medium with a 6–12 month pilot slide (Inspection + IT). | One-off GGUF. |
| **Scale of impact** | Beachhead MRPL inspection → other PSUs. Must stay **illustrative** on time saved. | Medium. | Fake ₹crore savings. |
| **UX** | Not demonstrated. | The whole game at finale. | Pretty Figma, broken OCR. |
| **Future progression** | Org diagram + LATER list is exactly this axis. | Strong if we don’t pretend LATER is built. | Blockchain / “then we connect DCS.” |

**Idea-submission vs finale:** if the idea is not yet submitted, **clarity + novelty write-up** matter *now*. Finale historically overweight **live demo**. We should still build as if the prototype is mandatory (mentor text).

**Where we stand in one line:** *conceptually aligned with the PS and with the nine criteria; competitively average until the spine runs; currently losing on UX/feasibility-as-evidence because there is no software.*

---

## G. What to change in the design (small, concrete)

1. Promote skills from “Hermes LATER” to **prototype: 5 skills**, org: the rest.  
2. Add **extract JSON schema + HITL** as a hard gate before `inspect-draft`.  
3. Add **sustainability/future** one-pager (cards, USB model update, MRPL Innovation Centre as *hoped* owner — not a claimed deal).  
4. Jury script: competitor table (Open WebUI, PrivateGPT, process AI) — we already know uniqueness theatre is a trap.

---

## H. Questions I need from you (data I do not have)

Answer in any form. If unknown, say unknown.

1. **SIH stage:** internal college hackathon done? Idea submitted on sih.gov.in? Deadlines?  
2. **Team:** 6 members, ≥1 female, same college? Domain mix (mech/inspection vs only CSE)?  
3. **Hardware:** `nvidia-smi` on both demo laptops (or “no NVIDIA”).  
4. **Sample scan:** do you have a real (even dummy) thickness/NDT PDF, or generate synthetic?  
5. **OS for sandbox:** Windows-only or a Linux box/WSL2 for `network=none`?  
6. **Can anyone get a plant note** (anonymized inspection recommendation / NFA) for field names? If no, we stay on KB structures.  
7. **Idea PDF:** do you want the next artefact to be the **official submission write-up** mapped to the nine criteria, or still design-only?

I will not invent answers for 1–6.
