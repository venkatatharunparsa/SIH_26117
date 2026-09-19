# WP-00 Product contract — FREEZE (rev 2.0)

**Date:** 2026-09-19  
**Status:** **FROZEN rev 2.0** — reopened for role + G1 honesty alignment with WP-05/WP-01 rev 2.0  
**Prior:** rev 1.1 (2026-09-17)  
**Product name:** **KWB** (Knowledge Workbench)  
**Official PS:** `../sih_research/sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`  
**Aligns:** WP-05 rev 2.0 · WP-01 rev 2.0 · WP-18 rev 1.1 (G1) · no-pull Ollama adopt policy  

**Stack:** not locked. No app code / PPT fill required by this freeze.

---

## 1. One-sentence product

**KWB** is a **self-hosted, fully offline software workbench** for confidential industrial **knowledge work**: it assists people the way Claude/Codex would on their desk, using **open-weight** models that software only **references** (weights stay on hardware), **grounds** work in org knowledge with **three-level citations**, **drafts** real deliverables from **templates**, and **never** replaces the human as final decision-maker or **writes** to existing plant/business systems.

Not a chatbot. Not a GPU optimiser. Not a refinery operator. Not ChatGPT with a skin. Not Open WebUI.

Chat may exist as a **UI for interaction**; the **product deliverable** is always an artefact (docx / PDF when possible / code / later Excel·PPT·calc), never the chat transcript alone.

---

## 2. Buckets (do not mix)

| Bucket | Meaning |
|---|---|
| **Must-work** | Expected Solution + Software category. If missing, SIH26117 is not solved. |
| **Org-ambition** | Full organisation KWB on paper. Same architecture; more depth. |
| **Deferred** | In ambition; not required for the binding demo until explicitly promoted. |
| **Never** | Forbidden even for the demo. |

**Two scales, one contract:** Organisation design assumes suitable org hardware. Demonstration shows what KWB can build under Expected Solution constraints (workstation or server, mid-range GPU, smaller open-weight model OK).

---

## 3. Planes (hardware vs software)

| Plane | Owns | Does not own |
|---|---|---|
| **Workbench (software)** | UI, orchestrator, specialist agents, tools, HITL, templates, KB connector/RAG, local plugin/skill host, **model references (cards)**, task routing, context packing, grants, gateway client, audit, monitors | Weight files, CUDA, VRAM |
| **Runtime (hardware)** | GPU/CPU, staged **open-weight** files, local `/v1` server, load/unload | Deliverable policy, plant ACL, HITL rules |
| **Sandbox (code)** | Isolated run/verify of generated code/tests | Inference server (**never** wrap GPU in the code jail) |

- Software requests inference by **model id** + **schema-valid** local request — it does **not** pass weight files.  
- Add/remove model = stage/unload weights on runtime + register/drop card — **no workbench redesign**.  
- Change machine (laptop ↔ org GPU) = point `base_url` / refresh catalog — **no workbench redesign**.  
- Gateway is **software** (auth, timeout, validity, card check). It is **not** CUDA. Invalid requests fail closed; no rewrite to a public `base_url`.

---

## 4. Human–AI role

| Actor | May | May not |
|---|---|---|
| **KWB** | Plan; retrieve under grant; draft full artefacts; sandbox checks; propose template-based updates; ask verification; run internal checks | Approve as **plant record**; decide safety/FFS/statutory/legal/commercial outcomes; write plant SoR |
| **Human (in-app knowledge worker)** | Ultimate **own-work** verifier: self-HITL accept/edit/reject DRAFT; export leave; grant-sensitive access under policy; stop the task | Instruct KWB to break **Never**; act as in-app plant Approver |
| **Human (org paper Approver / officer)** | Record-facing / plant acceptance **outside** KWB using exported pack | In-app H2/H3 clicker |

**Assist:** KWB drafts the deliverable; worker self-checks; **export leave** ends the KWB solution path.  
**Does not complete the plant job:** **record / plant decision** stays with humans **outside** KWB (paper).  

KWB may run internal checks (OCR flags, sandbox pass/fail, citation presence). **Ultimate in-app verifier** = operating worker (WP-05). **Plant Approver** = outside.

---

## 5. Deliverables and templates

- Product outputs are **artefacts**, not chat.  
- Prefer **company templates**. Else **KWB base templates**.  
- Flow: template → base generation → update from user requirements → **DRAFT** → **self-HITL** (WP-05) → **export leave** → human may promote to plant record **outside KWB** (paper Approver; KWB does not auto-file).  
- **Templates ownership (Q6):**  
  - **Admin (IT)** owns and manages organisation / higher-tier templates.  
  - **Users** may use those templates **or** a **freestyle** option based on company-allowed template policy.  
- **Must-work format (Q1):** **Word `.docx`** is required for the Expected Solution path. **Also produce PDF when possible** (same content). **If PDF fails, must-work still passes when `.docx` DRAFT + HITL path succeeds.**  
- HITL sits on extract / draft / export-leave gates (**self-HITL** in-app).

### 5.1 Artefact classes (principle — detail WP-01)

| Class | Meaning |
|---|---|
| **Plant-controlled** | Org SOPs/manuals/records KWB may **read** (not write) |
| **Workbench-generated** | DRAFT docx/PDF/code/exports produced by KWB |
| **Personal** | User `.md` / personal skills — not plant truth until **Admin** promotion (WP-05 H6) |

Do not store personal files as if they were controlled SOPs.

---

## 6. Must-work (acceptance)

1. **Software** workbench (not a hardware product).  
2. Local deploy on **workstation or server**, **mid-range GPU**; smaller **open-weight** model if 120B absent.  
3. **Auto-select ≥2 task types** with routing log `task_type → card_id → model_id` (not a user dropdown as the proof).  
   - **Full G1:** ≥2 **distinct** `model_id`s when ≥2 chat models are **locally staged** (offline adopt; **never pull** to satisfy G1).  
   - **Floor G1 (honest):** if only one chat tag is adopted, ≥2 task→card routes may share that `model_id` — eval/PPT must label **single-tag adopt**.  
4. Agentic path: scanned inspection → findings → **Word `.docx`** note as **DRAFT** for **self-HITL** (**PDF also if possible**; see §5) → **export leave**.  
5. Coding path: generate + **run and verify** in sandbox (jail ≠ GPU) + **H9**.  
6. Multimodal: image or scan on-device (images as local/`data:` content only — no remote URL fetch).  
7. Sovereign proof: Monitor A **evidence pack** / snapshots — **no public internet** (Q2); **not CERT**. Models/plugins via offline media only.  
8. Not locked to one model; **add and remove** via catalog (local stage) without redesigning KWB — **no registry pull from workbench**.  
9. Human **self-HITL** on the inspection→Word spine; plant approval **outside**.  
10. Fail closed if required model/card/permission is missing — **no** internet fallback.

---

## 7. Org-ambition

### 7.1 Official Description / Background

- Fully offline on org infrastructure.  
- Multiple open-weight models; task-based routing (coding ≠ summary ≠ vision).  
- Plan, **iterate** (not one-shot); local file read/write **inside KWB workspace only**; sandbox; spreadsheet; internal search.  
- Scanned PDFs, handwritten notes, drawings, photographs; on-device OCR/vision (**pluggable** models).  
- Approval notes, PPT/Word/Excel, code, calculations with steps — not chat-only.  
- **Local KB connector** to manuals, SOPs, past correspondence.  
- Claude/Codex-class host so staff stop pasting confidential data into public tools.  
- Shape fits refinery / PSU / defence-linked / government knowledge work; MRPL is **sponsor**.  
- Complements existing **process** AI; KWB is **knowledge-work** AI.

**KWB workspace write ≠ plant write:** agents may create/update files **inside KWB’s workspace** (drafts, exports). That is **not** editing EAM/ERP/DCS/DMS systems of record.

### 7.2 Agreed promotions

| Item | Freeze line |
|---|---|
| **Local MCP / plugin host** | Connect MCP **already present on the machine**. Proper local integration. **Never** internet MCP. Packs may be brought in **outside KWB** on **approved offline media**; KWB only allowlists/connects local servers. |
| **Skill library** | On-disk catalog; **task-scoped and role-scoped** load (not every skill on every tool); progressive disclosure. Better context for how to do work efficiently. Shelves: **org / plugin / personal**; org promotion = **Admin** HITL (H6). |
| **Specialist agents** | One orchestrator; **separate agents** for defined tasks; no shared super-context / standing full access. |
| **Task grants + revoke** | Session authenticates the person; **task** opens a time-bounded grant (sources, tools, plugins, classification ceiling). Task end / abort / timeout → grant **revoked**. Helps safety; **not complete security**. Copies in chat/personal `.md` are in scope for design (WP-04). |
| **Intelligent layer** | Route by task to **registered** cards; decide **what data to pass** (minimize to grant); no safety autonomy. |
| **Valid gateway** | Schema-valid local `/v1` only; model id must exist on a card; fail closed. |
| **Role classes** | **In-app:** Knowledge worker / Admin (IT). **Org paper (outside):** Approver/officer. Detail **WP-01 / WP-05**. |
| **Classifier** | Sensitivity/access classifier exists. Rules vs model = research in WP-04. |
| **Sensitive access** | Ask permission; risk-based friction (easy inside grant; harder on expand/export). |
| **KB + three-level citation (Q4)** | **(1) file/evidence (2) user claim (3) company policy.** Conflict/`NOT FOUND` handled honestly (detail WP-22); do not silently pick the friendliest sentence. |
| **OCR pipeline** | After every OCR/scan extract: **human verifies** correct vs assumed → **then** company KB check with citations. |
| **Version–task lineage** | Relations between **data versions** and **tasks** / drafts so users see what they are building. **Not** “must use a graph database.” Engine later (WP-14). |
| **Personal `.md` harness** | Adapt to daily work via personal markdown; HITL before org skill. **Not** weight training. |
| **Monitors** | **Audience A:** offline evidence pack (snapshots) — **not CERT**. **Audience B:** card + why, citations, own HITL state, grant, plugin allow/deny. |
| **Audit** | Track who did what and what changed (detail WP-17; CERT-In-shaped fields at that WP). |
| **Company policy** | Retention / personal data per company policy (detail WP-04/17). |
| **Read-only to existing systems (Q3)** | KWB **reads** existing plant/business systems when connected. It does **not** edit or write them. |
| **Fail closed** | No internet fallback; missing card/plugin/permission stops or degrades safely. |

### 7.3 Org vs demo

- **Org paper:** full KWB, proper hardware assumed.  
- **Demo:** focused path under Expected Solution (docx + sandbox code + multimodal + two-model log + offline proof).

---

## 8. Deferred

| Item | Rule |
|---|---|
| **Excel** | Org-ambition; not must-work until promoted |
| **PPT** | Org-ambition; not must-work until promoted |
| **Calc-with-steps / rule-book calcs (Q5)** | **Organisation only.** Demo does not require a calc artefact. Sandbox **code verify** remains must-work (separate). |
| **SSO / plant IdP** | Later; MOCK OK for demo |
| **Live read connectors to EAM/DMS** | Ambition; MOCK schemas OK; **never write** |
| **Classifier algorithm** | WP-04 research |
| **Lineage storage engine** | WP-14 (SQL/files/graph undecided) |

---

## 9. Never

- Decide safety / FFS / statutory / legal / commercial / isolation / MOC outcomes.  
- **Write or edit** existing plant/business systems: DCS / SIS / PLC / EAM / ERP / permits / OT control paths / DMS-as-system-of-record. **Read-only** when connected.  
- Act as an OT/control-network agent.  
- Cloud LLM brain or public `/v1` `base_url`.  
- Non-**open-weight** / cloud-hosted weights as the product brain.  
- **Any internet access** for KWB operation (models, MCP, skills, telemetry, remote image URLs, package registries).  
- Internet MCP / skill hub / weight pull **through KWB** at runtime.  
- Product identity = Open WebUI / OpenHands / DeerFlow / GPU tuner.  
- Unsupervised weight training on plant data as “self-learning.”  
- Treat grants, revoke, or classifiers as complete security.  
- Claim certified plant deploy, industrial P&ID vision SLA, or invented MRPL KPI hours.  
- Fail-open to the internet.  
- Chat transcript as the official deliverable.  
- Auto-promote DRAFT → plant **record** without human.  
- Auto-promote personal skill → org skill without **Admin** HITL (H6).  
- In-app Approver / accept-for-forward queue.  
- Registry/`ollama pull` from workbench to “satisfy” G1.  
- Dump entire plant corpus into the model outside the **grant**.  
- Let a human instruction override these Never rules inside KWB.

---

## 10. Role classes (base)

| Role | Where | Intent | Skills |
|---|---|---|---|
| **Knowledge worker** | **In-app** | Run tasks; attach files; **self-HITL**; export leave; request grants; use org or allowed freestyle templates | Worker skill pack |
| **Admin (IT)** | **In-app** | Platform control: cards (local tags only), MCP/skill allowlist, org templates, offline intake, Audience A config | Admin skill pack |
| **Approver / officer** | **Org paper only (outside KWB)** | Record-facing / plant acceptance after export | Outside process — not in-app H2/H3 |

Detail matrices: **WP-01** · HITL map: **WP-05**.

---

## 11. Sensitivity & permission (principles)

- Classifier for sensitive handling; full class list and reactions in **WP-04** (seeded by PS: P&ID, financials, vendor negotiations, unreleased designs, correspondence, strategy).  
- Permission moments: user-attached (low friction) → org retrieve (grant) → write/export (HITL) → local MCP/skill expand (allowlist + task gate).  
- Easy to use; less friction inside an already-granted task.  
- ACL enforced **before** retrieval reaches the model.

---

## 12. Verify kinds

| Kind | When |
|---|---|
| Permission | Before sensitive retrieve / expand access |
| OCR / extract | After scan: **same-user H1** confirms correct vs assumed |
| Knowledge | After OCR OK: company KB + cite-or-abstain + **H7** when needed |
| Execution | Sandbox pass/fail + **H9** (code must-work) |
| Human draft / export | **H2** self-check; **H3** export leave; plant record **outside** |

---

## 13. Offline (Q2)

KWB and its required runtime path run **completely offline**. **No internet access anywhere** in normal or demo operation. Local LAN to an on-prem runtime is allowed only as **on-premises** connectivity, not as a path to the public internet.

Bringing new weights/plugins/skills into the org uses **approved offline media** and Admin allowlisting — **not** an in-app download from the public internet.

---

## 14. Closed open questions (Q1–Q7)

| ID | Decision |
|---|---|
| Q1 | Must-work = **`.docx`**; **also PDF when possible** (PDF failure ≠ must-work failure if docx OK) |
| Q2 | **Fully offline**; no internet anywhere |
| Q3 | Human accept/reject/grant freely; cannot break Never; **read-only** to existing systems (no edit/write) |
| Q4 | Three-level citation = **file / user claim / company policy** |
| Q5 | Calc = **organisation only** |
| Q6 | **Admin** owns org/higher templates; users may use them or **company-allowed freestyle** |
| Q7 | Product name **KWB** |

---

## 15. Explicitly not locked here

Runtime binary, OCR engine, orchestrator library, vector store, exact model ids, full sensitivity taxonomy text, exact role–activity matrix, MRPL IdP/DMS APIs, lineage engine brand, classifier rules-vs-model choice.

---

## 16. Next

GATE_90 remainders: **WP-20** freeze · design-info B-rows. WP-01/05 already rev 2.0.

---

## 17. Changelog

| Rev | Note |
|---|---|
| **1.0 / 1.1** | Original product contract + completeness red-team |
| **2.0** | **FROZEN** 2026-09-19: Approver = org paper only; Admin = IT; self-HITL + export leave; G1 floor/full honesty (no pull); Monitor A ≠ CERT; align WP-01/05/18 |
