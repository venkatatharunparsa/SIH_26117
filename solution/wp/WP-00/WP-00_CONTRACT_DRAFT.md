# WP-00 Product contract — DRAFT (complete discussion capture)

**Date:** 2026-09-17  
**Status:** **SUPERSEDED.** Answers closed; binding file is `WP-00_FREEZE.md`.  
**Product working name:** KWB (Knowledge Workbench) — rename later if you want.  
**Official PS:** `../sih_research/sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`  
**Backing:** architect perspective, hardware clarity, red-team, your A1–A10 / G1–G11 answers.

**Rule:** Later WPs may not contradict this page once locked. Stack brands are **not** in this contract.

---

## 1. One-sentence product

KWB is a **self-hosted, air-gapped software workbench** for confidential industrial **knowledge work**: it assists people the way Claude/Codex would on their desk, using **open-weight** models referenced (not bundled) by software, **grounds** work in org knowledge with citations, **drafts** real deliverables from **templates**, and **never** replaces the human as final decision-maker or writes plant control systems.

Not a chatbot. Not a GPU optimiser. Not a refinery operator. Not ChatGPT with a skin. Not Open WebUI.

---

## 2. Buckets (do not mix)

| Bucket | Meaning |
|---|---|
| **Must-work** | Expected Solution + Software category. Demo/acceptance. If missing, we did not solve SIH26117. |
| **Org-ambition** | Full organisation workbench on paper (Description + Background + agreed User lines). Same architecture; more connectors/roles/artefacts. |
| **Deferred** | In ambition, **not** required for the binding demo until you promote them. |
| **Never** | Forbidden even “for the demo.” |

**Two scales, one contract:** Org design assumes suitable org hardware. Demonstration shows what the workbench can build within Expected Solution constraints (workstation/server, mid-range GPU, smaller model OK).

---

## 3. Planes (hardware vs software) — agreed

| Plane | Owns | Does not own |
|---|---|---|
| **Workbench (software)** | UI, agents, tools, HITL, templates, RAG/connector, plugins/skills host, **model references (cards)**, routing, grants, audit | Weight files, CUDA, VRAM |
| **Runtime (hardware)** | GPU/CPU, staged open-weight files, `/v1` server, load/unload | Word policy, plant ACL, HITL rules |
| **Sandbox (code)** | Isolated run/verify of generated code/tests/calc engines | Inference server (never wrap GPU in the code jail) |

- Software talks to runtime by **model id + valid request**, not by shipping weights.  
- Add/remove model = stage/unload weights on runtime + register/drop card in software — **no workbench redesign**.  
- Change machine (laptop ↔ org GPU server) = change `base_url` / catalog — **no workbench redesign**.

---

## 4. Human–AI role (A1, G1, G3, G11)

| Actor | May | May not |
|---|---|---|
| **KWB** | Plan, retrieve (under grant), draft full artefacts, run sandbox checks, propose updates from user requirements, ask for verification | Approve, sign, file as **record**, decide safety/FFS/statutory/legal/commercial outcomes |
| **Human** | Ultimate verifier and **decision-maker** for the task; accept / edit / reject draft; grant or deny sensitive access; stop the task | — |

**Assist means:** KWB produces a **draft deliverable** (not chat-only) and asks for **human verification**.  
**Does not complete the job means:** the **record / decision** stays human. Draft may be end-to-end complete as a file.

**Internal checks:** KWB may run automated checks (OCR confidence flags, sandbox pass/fail, citation presence). **Ultimate verifier** is the human with domain knowledge.

**G11 clarified for freeze intent:** Human is ultimate decider **inside KWB’s product boundaries** (see Never). “Whatever they want” = full control of drafts, grants, accept/reject — **not** authority for KWB to write DCS or call the internet because a user asked.

---

## 5. Deliverables and templates (A1)

- Outputs are **real artefacts**: documents, calculations (where in scope), code — **not chat as the product**.  
- Prefer **company predefined templates** when available.  
- Else use a **KWB base template**.  
- Flow: template → base generation → update from user requirements → show **DRAFT** → human verifies / edits → only then can it become a record (human action).  
- HITL sits on this draft gate.

**Must-work demo artefact (Official Expected Solution):** approval note as a **Word** file from the inspection path.  
**Org-ambition formats:** Word/Doc, PDF export, Excel, PPT, calc packs — see Deferred.

---

## 6. Must-work (acceptance)

From **Official Expected Solution** + Title/category + agreed planes:

1. **Software workbench** (not a hardware product).  
2. Local deploy on **workstation or server**, **mid-range GPU**; **smaller open-weight** model if 120B absent.  
3. **Model auto-select ≥2 task types** with **two different model ids** in the log (not a manual dropdown as the “proof”).  
4. Agentic path: scanned inspection → key findings → **Word** approval note as **DRAFT** for human verification.  
5. Coding path: generate + **run and verify** in sandbox.  
6. Multimodal: image or scan understood **on-device**.  
7. Sovereign proof: logs or **visible** network monitor — **no external (internet) calls at any point**, including model/plugin/skill install.  
8. **Not locked to one model**; add **and remove** via catalog/reference without redesigning the workbench.  
9. Human draft verification on the Word path (A1/A8 principles applied to the demo spine).

---

## 7. Org-ambition

### 7.1 From Official Description / Background

- Air-gapped workbench on org infrastructure; nothing leaves premises.  
- Multiple open-weight models; task-based routing (coding ≠ summary ≠ vision).  
- Agent: plan, **iterate**, local file read/write, sandbox, spreadsheet work, internal search.  
- Inputs: scanned PDFs, handwritten notes, drawings, photographs; on-device OCR/vision (models as plugs).  
- Outputs: approval notes, PPT/Word/Excel, working code, calculations with steps — not chat-only.  
- **Local knowledge base connector** to manuals, SOPs, **past correspondence**.  
- Claude/Codex-class UX so staff stop pasting confidential material into public tools.  
- Same product shape for refinery / PSU / defence-linked / government knowledge work; **MRPL is sponsor**, not the only sector in Background.  
- Complements existing **process** AI; KWB is **knowledge-work** AI.

### 7.2 Agreed promotions (User)

| Item | Contract line |
|---|---|
| **Plugin / MCP host** | Connect **local** MCP already on the machine (offline). Integration via proper host wiring / local config — not a workbench rewrite per plugin. **Never** internet MCP. Org may advise users to **download offline** packs for efficient work; install stays air-gap. |
| **Skill library** | On-disk catalog. Skills give agents **better context** for how to do a task efficiently. Load by task / role — not every skill on every tool. Org / plugin / personal shelves; promotion to org = HITL. |
| **Role classes** | Base roles with allowed activities; **role-linked skills** to distinguish work. |
| **Classifier** | Keep a **sensitivity / access classifier**. Rule-based vs model = **research later** (WP-04); presence of classifier is in the contract. |
| **Permission for sensitive access** | Ask before expanding access; risk-based friction (A10). |
| **KB + three-source citation** | First-class. Connector to existing systems; efficient retrieve; **three-level citation** for KWB (file / user claim / company policy — confirm in open Q). |
| **OCR then human then KB** | After every OCR/scan extract: **user verifies** correct vs assumed data; **then** system checks against company knowledge base. |
| **Audit / tracking** | Track who did what and what changed (ambition; detail WP-17). |
| **Company policy** | Retention / personal data / handling follow **company policy** (detail WP-04/17; do not invent MRPL text). |
| **Boundaries** | Explicit product limits; beyond them KWB does not go (G10). |
| **Fail closed** | Missing model/plugin/permission → stop or degrade safely; **no** internet fallback. |

### 7.3 Org vs demo (A9)

- **Organisation paper:** full KWB assuming proper org hardware and governance.  
- **Demonstration:** what we can build in the workbench under Expected Solution (one focused deliverable path, mid-GPU, smaller models OK).

---

## 8. Deferred (explicit park rules)

| Item | Status | Rule |
|---|---|---|
| **Excel** | Org-ambition; deferred for demo focus | Do not silently promote to must-work |
| **PPT / board pack** | Org-ambition; deferred | Same |
| **Calc-with-steps / rule-book calcs** | **Org-ambition:** users can perform calculations **step-by-step following the application rule book**. Prototype: focus on **one** primary deliverable path; sandbox **code verify** remains must-work (separate). Exact “must calc in prototype” = open Q |
| **SSO / plant IdP** | Later | MOCK identity OK for demo |
| **Live EAM/DMS write APIs** | Never write; read connectors later | MOCK JSON schemas OK |
| **Classifier implementation (rules vs model)** | Research in WP-04 | Classifier **exists** in contract |

---

## 9. Never

- Decide safety / FFS / statutory / legal / commercial / isolation / MOC outcomes.  
- **Write** DCS / SIS / PLC / EAM / ERP / permits; act as an **OT / control-network agent**.  
- Cloud LLM brain (OpenAI / Anthropic / OpenRouter / etc.) or `/v1` to a public `base_url`.  
- **Internet** MCP, skill hub, or weight pull at runtime (`npx`, registry, HF/Ollama pull on stage).  
- Product identity = Open WebUI / OpenHands / DeerFlow / GPU tuner.  
- Unsupervised **weight training** on plant data as “self-learning.”  
- Treat grants/revoke or classifiers as **complete security**.  
- Claim certified plant deployment, industrial P&ID vision SLA, or invented MRPL KPI hours.  
- Fail-open to WAN when something is missing.  
- Present chat transcript as the official deliverable.  
- Auto-promote DRAFT → plant **record** without human.  
- Auto-promote personal skill → org skill without HITL.

---

## 10. Role classes (A3, G4) — base set for later detail

Names are **generic** (not MRPL HR titles). Activities refined in WP-01/04/05/07.

| Role | Intent (activities) | Skills |
|---|---|---|
| **Knowledge worker** | Run assigned tasks; attach files; verify OCR/drafts; request grants | Role skill pack for their job type |
| **Approver** | Accept/reject DRAFT as record-facing; override/deny | Approver skill pack |
| **Admin** | Register/remove model cards; allowlist local MCP/skills; templates; air-gap ops | Admin skill pack |

One human may hold multiple roles in a small deployment; org paper still distinguishes them.

---

## 11. Sensitivity & permission (A2, G2) — principles

- KWB **keeps a classifier** for sensitive handling.  
- Define **what is sensitive for KWB** and **how to react** (classes written in WP-04; PS Background seeds: P&ID, financials, vendor negotiations, unreleased designs, correspondence, strategy).  
- Permission moments (minimum):

| Class | Friction |
|---|---|
| User-attached file for this task | Low (already chosen) |
| Org corpus retrieve | Grant / confirm by class or source |
| Write / export download | HITL |
| Local MCP/skill that expands access | Install allowlist + task gate |

- Easy to use, **less friction** inside an already-granted task (A10); harder when expanding access or exporting.  
- Retrieval respects ACL **before** chunks reach the model.

---

## 12. Verify kinds (A8, G5)

| Kind | When |
|---|---|
| **Permission** | Before sensitive retrieve / expand access |
| **OCR / extract** | After every scan: human confirms correct vs assumed |
| **Knowledge** | After human OCR OK: check company KB; **three-level citation** |
| **Execution** | Sandbox pass/fail for code (must-work) |
| **Human draft** | Before DRAFT can be treated as finished work / record |

---

## 13. Knowledge connector & citation (A7, G5)

- First-class for a knowledge workbench: connect **existing** org systems (as available); retrieve efficiently.  
- **Three-level citation** required for KWB development (intended: **file evidence**, **user claim**, **company policy** — confirm open Q).  
- `NOT FOUND` / conflict handling detailed in WP-22; contradiction does not silently prefer the friendliest sentence.

---

## 14. Local MCP & skill library (A4, A5, G6)

- **Local MCP only:** already present on the laptop/org host; connect through host integration.  
- Suggest offline download of useful connectors for efficient work; **no internet call** to fetch MCP at runtime.  
- Skills: provide task procedure/context so agents work efficiently; bound to task and **role**.  
- Everything required for production posture is **offline-capable**. “Online” in discussion = **on-prem / LAN to local runtime**, not public internet (confirm open Q).

---

## 15. Audit & policy (G8, G9)

- Track who did what and what changed (ambition → WP-17).  
- Handle personal/sensitive data **according to company policy** (→ WP-04/17). Do not invent MRPL legal text in WP-00.

---

## 16. What WP-00 deliberately does not lock

Stack (Ollama/vLLM/llama.cpp, OCR engine, orchestrator library, vector DB, Neo4j). Exact model names. Exact MRPL forms/IdP/DMS APIs. Classifier algorithm (rules vs model). Full sensitivity taxonomy text. Exact role–activity matrix.

---

## 17. Open questions — answer these to lock

Reply with short answers; then we write `WP-00_FREEZE.md` as the binding file for later stages.

| ID | Doubt | Why it matters |
|---|---|---|
| **Q1** | Must-work deliverable format: PS says **Word**. You also said PDF/Doc. Confirm: **must-work = Word (docx)**; PDF = export ambition? | Jury Expected Solution wording |
| **Q2** | “Offline online” (G6): confirm you mean **works fully offline / on-prem LAN**, and **never** depends on public internet? | Sovereign proof |
| **Q3** | G11 “human can do whatever”: confirm human is ultimate on **drafts/grants/accept-reject**, but **cannot** instruct KWB to break Never (DCS write, internet MCP, cloud LLM)? | Boundary vs chaos |
| **Q4** | Three-level citation = **(1) file/evidence (2) user claim (3) company policy**? | WP-22 design |
| **Q5** | Prototype calc: **(a)** org-ambition only (demo = Word + sandbox code), or **(b)** prototype must also show one rule-book calc-with-steps? | Scope creep vs your A6 |
| **Q6** | Company templates: who owns them in role terms — **Admin** uploads org templates; workers only use? | WP-01/05 |
| **Q7** | Working product name for freeze: keep **KWB** or placeholder only? | Docs consistency |

---

## 18. After lock

1. Save answers into `WP-00_FREEZE.md` (binding).  
2. Update follow-list pointer.  
3. Start **WP-01** (users, jobs, artefacts) under this contract.
