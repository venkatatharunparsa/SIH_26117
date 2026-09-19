# WP-00 — Adversarial red-team of perspectives (pre-lock)

**Date:** 2026-09-17  
**Status:** Findings only. **WP-00 is not frozen.** Lock after you review this and we decide line-by-line.  
**Inputs:** Architect draft (`WP-00_ARCHITECT_PERSPECTIVE.md`) + your perspective + hardware clarity (`WP-00_HARDWARE_SOFTWARE_CLARITY.md`) + Official PS.

---

## Combined perspective under test (as agreed so far)

| # | Claim | Source |
|---|---|---|
| P1 | Software workbench for confidential industrial knowledge work; Claude/Codex-class on-prem; open-weight; artefacts not chat | Architect + you |
| P2 | Weights on hardware; software = model **reference** / catalog; hardware change without software redesign | You + clarity note |
| P3 | Must-work = Expected Solution (2-task auto-select, scan→Word, sandbox verify, multimodal, WAN=0) | Architect (Official) |
| P4 | Plugin host + skill library = **org-ambition** (not Expected Solution must) | **You** |
| P5 | Assist humans; do **not** fully complete their job; **verify**; **ask permission** for sensitive information access | **You** |
| P6 | Excel / calc-with-steps = **decide later** | **You** |
| P7 | Design the workbench **for the organisation** (not a single-laptop toy only) | **You** |
| P8 | Never: DCS write, safety/statutory decide, cloud brain, WAN marketplace, fake certified plant AI | Architect |

---

## Verdict (short)

The direction is **right for SIH26117 and for an org knowledge workbench**.  
It is **not lockable yet**: “assist / ask permission / for the organisation” are correct **intent** but underspecified as a **product contract**. Adversaries (jury, CISO, plant document control) will ask *who*, *what is sensitive*, *what happens if the human says no*, and *what “done” means vs the PS Word demo*.

Fill the gaps below **in the WP-00 freeze**, or park them as named open questions that later WPs must answer.

---

## What survives red-team (keep)

| Item | Why it survives | Source grade |
|---|---|---|
| Must vs ambition vs never split | Stops Description from becoming a fake Expected Solution demo | **Official** PS structure |
| Software ≠ weights; catalog/reference | Matches “add without redesign”; Software category | **Official** Description + Title |
| Plugin host + skill library in **ambition** | Claude/Codex metaphor (**Background**) without claiming Expected Solution needs a marketplace | **Official** Background + **User** |
| Assist / do not decide safety-commercial outcomes | Aligns NIST AI RMF: support vs replace human decision; define human-AI roles ([NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) GOVERN 3.2, MAP 1.1, MAP 3.5) | **Spec** + **User** |
| Ask permission for sensitive access | Least privilege / task grant (**NIST AC-6**); air-gapped RAG must not become ACL bypass ([air-gap RAG practice](https://vdf.ai/air-gapped-rag/): filter at retrieve, not after answer) | **Spec** + **User** |
| Excel/calc parked | Expected Solution binds **Word** + sandbox code, not Excel/PPT | **Official** Expected vs Description |
| Org-level design first | Background lists refineries, PSUs, defence-linked, government offices; MRPL is sponsor | **Official** Background |
| Never write DCS / never cloud brain | Process AI ≠ knowledge work; company policy on-prem | **Official** + prior product definition |

---

## Attacks on the perspective (where it is weak)

### A1 — “Assist, don’t complete” vs Expected Solution agentic Word

**Attack.** Jury: “Your PS asks for an end-to-end agentic task: scan → findings → Word. You say you don’t complete the task. Which is it?”

**Finding.** Without a precise definition, “don’t complete” sounds like a **chatbot that stops early** — which **fails** Expected Solution.

**Required fill (for WP-00).** Define **assist** as:

- Workbench may **draft** the full artefact (Word, code, findings).  
- Workbench may **not** **approve**, **sign**, **file as record**, or **act as the decision**.  
- “Complete” = human accountability / plant record. “Draft complete” = allowed and required for the demo.

**Source.** **Official** Expected Solution (Word path) + NIST MAP (support vs replace decision-making).

---

### A2 — “Ask permission for sensitive information” with no sensitivity model

**Attack.** What is sensitive? All plant data? Only financials? User’s own upload? A P&ID the user already opened? If everything needs a click, engineers hate it and bypass. If nothing does, CISO rejects it.

**Finding.** Org knowledge workbenches need a **classification + permission moment** contract, not a slogan.

**Required fill (for WP-00 or park → WP-04/05).** At minimum name these classes (names can change later):

| Class (example) | Permission moment |
|---|---|
| User-attached file for this task | Low friction (they already chose it) |
| Org corpus retrieve (SOP / correspondence / P&ID) | Grant / confirm by classification or source |
| File **write** / export download | HITL |
| Plugin / skill that expands access | Install + per-call or per-task gate |

State explicitly: permission is **not** complete security (your earlier line). Retrieval must respect ACL **before** the model sees chunks (air-gap RAG anti-pattern: redacted answer but full chunk still retrieved).

**Source.** **Official** Background confidential classes; **User** grants; NIST AC-6; air-gap RAG ACL-at-retrieve.

---

### A3 — “Design for the organisation” without org roles

**Attack.** Org product without roles becomes “one engineer laptop.” PSU/defence/gov Background users need **document control**: who may draft, who may approve, who may install plugins, who may register models.

**Finding.** WP-00 should state **role classes** at product level (even if IdP is LATER):

- Operator / knowledge worker (runs tasks)  
- Approver (HITL on records)  
- Admin (models, plugins, skills, air-gap ops)  

MRPL-specific org chart = **unknown** until supplied. Do not invent titles.

**Source.** **Official** Background multi-sector; NIST GOVERN 3.2 human roles; maker-checker practice for enterprise approvals (**Observed** governance patterns, not MRPL policy).

---

### A4 — Plugin host + skill library in ambition without a Never for WAN install

**Attack.** Ambition slides say “MCP like Claude.” Implementers ship `npx` / registry. Expected Solution “no external calls **at any point**” dies on first plugin add.

**Finding.** Ambition is fine. WP-00 **Never** must include: no public marketplace / runtime pull for models, plugins, or skills. Offline allowlist only.

**Source.** **Official** Expected Solution + Description nothing external.

---

### A5 — Skill library + “assist” without promotion control

**Attack.** Personal `.md` becomes fake SOP; agent “completes” work from poisoned skills.

**Finding.** Org-ambition skill library must say: org shelf vs personal shelf; promotion = human; skill text is not a security boundary.

**Source.** **User** WP-15 intent; Agent Skills spec; atlas caution.

---

### A6 — Parking Excel/calc without parking **rules**

**Attack.** Description lists Excel and calculations with steps. If we only say “decide later,” a later WP will silently promote them to must-work and break the prototype contract.

**Finding.** WP-00 should **park with rules**:

- Excel / PPT / calc-with-steps = **org-ambition**, status **deferred** (not must-work).  
- Sandbox **code verify** remains must-work (separate from spreadsheet).  
- If calc appears in org paper, steps shown + sandbox/deterministic path preferred over LLM arithmetic (prior design intent — confirm at WP-07/16, not invent MRPL formula).

**Source.** **Official** Description vs Expected Solution; **User** decide later.

---

### A7 — Org KB connector missing as a first-class ambition line in your short list

**Attack.** You stressed assist + org + plugins. Org knowledge work without **grounding in manuals/SOPs/correspondence** is a writing assistant — competitors exist; PS Description requires the connector.

**Finding.** Keep **local KB connector + citation** in org-ambition explicitly in the freeze (architect had it; your short note did not repeat it).

**Source.** **Official** Description.

---

### A8 — “Verify” is overloaded

**Attack.** Verify OCR? Verify claim vs SOP? Verify sandbox tests? Verify user permission? One word, four layers.

**Finding.** WP-00 should list **verify kinds** (one line each), detail later:

1. Permission verify (may we access this?).  
2. Grounding verify (claim vs file/policy — ambition).  
3. Execution verify (sandbox pass/fail — must-work for code).  
4. Human verify (HITL before record/export).

**Source.** **User** + **Official** sandbox + Description grounding.

---

### A9 — Organisation vs SIH venue honesty

**Attack.** Org design on paper; demo on mid-range GPU. If WP-00 only says “for the organisation,” jury thinks you promised plant SSO + DMS on day one.

**Finding.** WP-00 must keep: **one product contract**, two scales — org paper (ambition) vs demonstrable Expected Solution (must-work). Same boxes; MOCK/LATER later.

**Source.** **Official** Expected Solution workstation/server mid-GPU.

---

### A10 — Sensitive permission fatigue → shadow IT again

**Attack.** Background problem is people pasting into Claude because policy is hard. If our workbench is *harder* than Claude (constant prompts) without being *safer* in a clear way, users revert to paste.

**Finding.** Org product needs **risk-based** friction: high on expand-access and export; low on continuing a granted task. That principle belongs in WP-00 one sentence; mechanics in WP-04/05.

**Source.** **Official** Background (shadow IT); **User** assist + permission.

---

## Org-level knowledge workbench — requirement gaps to fill before / in WP-00

These are what a real org (MRPL-class / PSU / defence-linked / gov office from Background) will expect beyond a hackathon demo. Grade: **fill in WP-00** | **park named open Q** | **later WP**.

| ID | Gap | Why org needs it | Fill now? |
|---|---|---|---|
| G1 | **Human-AI role:** assist vs decide vs draft-complete | NIST MAP 1.1; jury Word demo | **Fill in WP-00** (A1) |
| G2 | **Sensitive access** definition + permission moments | Confidential classes in Background; ACL-at-retrieve | **Fill principle in WP-00**; detail WP-04/05 |
| G3 | **DRAFT vs record** (cannot become plant truth without human) | Document control; maker-checker | **Fill in WP-00** |
| G4 | **Role classes** (worker / approver / admin) | Org deployment; plugin/model install authority | **Fill in WP-00** (names generic) |
| G5 | **KB connector + citations** in ambition | Official Description | **Fill in WP-00** (reaffirm) |
| G6 | **Plugin/skill Never:** offline only | Sovereign proof | **Fill in WP-00 Never** |
| G7 | **Excel/calc/PPT** deferred with explicit status | Avoid silent promotion | **Fill park rule in WP-00** |
| G8 | **Audit trail** of who approved what | CERT-In-shaped logging (**Observed** org need; cite directive at WP-17) | **Park → WP-17**; one line in ambition |
| G9 | **Retention / personal data** in correspondence & prompts | DPDP-oriented governance (**Observed** India AI governance practice) | **Park → WP-04/17**; do not invent MRPL DPO |
| G10 | **OT/IT boundary** (never touch control network) | Refinery reality; CERT-In least privilege / segmentation themes | **Fill in Never** (no DCS/OT write already; add “not an OT agent”) |
| G11 | **Override / reject / stop** path | NIST oversight; user said ask permission | **Fill in WP-00**: human can deny access and reject draft |
| G12 | **Primary jobs for org paper** | Inspection note is demo spine; org has more knowledge jobs | **Park → WP-01**; WP-00 may say “knowledge workers in Background sectors” |
| G13 | **Model remove** + open-weight only | Completes “not locked” | **Fill in WP-00** (must/ambition) |
| G14 | **Fail closed** when model/plugin/permission missing | No WAN fallback | **Fill in Never / must** |
| G15 | **MRPL process AI complementarity** | Honesty vs existing plant AI | **Fill one Never/ambition line** |

---

## PS cross-check (Official only)

| PS demand | Covered by perspectives? | Gap? |
|---|---|---|
| Software, on-prem, air-gap | Yes | Proof = must-work |
| Open-weight, not locked, add without redesign | Yes (weights on HW) | State **remove** |
| Auto-select ≥2 tasks | Must-work | Keep |
| Agent scan→Word | Must-work | Resolve A1 assist wording |
| Sandbox code verified | Must-work | Keep |
| Multimodal on-device | Must-work | Keep |
| WAN=0 proof | Must-work | Tie to plugin/skill install Never |
| File R/W, spreadsheet, search, iterate | Ambition | Spreadsheet deferred per you — **park rule** |
| PPT/Word/Excel/calc steps | Ambition | Excel/calc deferred; Word must |
| KB connector | Ambition | Reaffirm (G5) |
| Claude/Codex-class | Ambition (plugins/skills) | Offline host only (A4) |

---

## Honest limits of this red-team

- No MRPL written AI policy, IdP, or DMS API was provided — mark **unknown**, do not invent.  
- CERT-In / DPDP: org-shaped needs are **Observed** from public guidance; exact obligations freeze at WP-17 with the statute/advisory in hand.  
- NIST AI RMF is voluntary **Spec** for role design, not Indian law.

---

## Recommended WP-00 freeze shape (for the decision meeting — not locked yet)

When you are ready to lock, the freeze page should contain only:

1. One-sentence product  
2. Must-work (Expected Solution + software/runtime split + model reference)  
3. Org-ambition (incl. **plugin host, skill library, KB connector, org roles, assist/draft**)  
4. Deferred (Excel, calc-with-steps, PPT — decide later)  
5. Never (incl. OT write, cloud, WAN marketplace, decide-for-human, fail-open)  
6. Named open questions handed to WP-01+ (primary personas, sensitivity taxonomy detail)

---

## Next step

You review these gaps. We adjust any line you reject. **Then** we write `WP-00_FREEZE.md` and move to WP-01.
