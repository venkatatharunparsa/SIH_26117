# Follow list — SIH26117 org design (walk this)

**Date:** 2026-09-17  
**Status:** Binding **queue**. Individual WP contracts freeze only when you decide that WP.  
**Stack:** not locked. **PPT / app code:** paused until WP-20 is done, then prototype overlay.

This file is what we follow. Agenda, red-team, and PS completeness are the backing notes.

| File | Role |
|---|---|
| **This file** | Queue + why + significance + source of truth |
| `DESIGN_REPO_MAP_v1.md` | **Before WP-00:** adopt / add / refuse vs existing repos (not a fork lock) |
| `DESIGN_AGENDA_ORG_v1.md` | Order, dependencies, adversarial flags |
| `DESIGN_AGENDA_REDTEAM_v1.md` | Attacks, MCP/HITL/session research |
| `DESIGN_PS_COMPLETENESS_v1.md` | Every PS sentence mapped |
| `sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md` | **Official** PS text |

---

## How to read a row

**Source grade**

| Grade | Means |
|---|---|
| **Official** | SIH26117 Title / Background / Description / Expected Solution, verbatim in the KB file |
| **User** | Your 2026-09-17 meanings (MCP host, `.md` harness, lineage, grants, citation RAG, valid gateway, operator monitors, pluggable **remove**) |
| **Spec** | Named public spec or paper (MCP, Agent Skills, NIST SP 800-53 AC-6, Lewis et al. RAG 2020, IETF MCP security draft) |
| **Prior paper** | Our architecture notes (OpenAI LCD, Model Cards). Re-confirm at the WP; not a freeze |

**PS split (do not mix)**

- **Expected Solution** = acceptance test (what must work to claim the PS).  
- **Description** = org ambition (full workbench).  
- **Background** = why it exists (confidential work, no Claude/Codex on P&IDs).

Walk **one WP**. Freeze must / may / never. Do not pick a stack brand inside a freeze.

---

## Queue (25 org WPs, then prototype overlay)

---

### 1 — WP-00 Product contract

**Job.** One page: must-work / org-ambition / never.

**Why required.** Without this, later WPs invent a chatbot, a GPU tuner, a DCS writer, or a cloud-plugin clone.

**Significance.** Every other freeze is illegal if it contradicts this page. Expected Solution is must-work. Description (PPT, Excel, multi-model catalog, plugin host) is ambition unless you promote a line. Never: safety/FFS/statutory/commercial decisions; write to DCS/SIS/PLC; WAN install of models or MCP.

**Source of truth.** **Official** — full PS. **User** — industrial evidence workbench, HITL forever. Category **Official**: Software, not hardware optimiser.

**If skipped.** Routing, plugins, and PPT will each define a different product.

**Depends on.** PS only.

---

### 2 — WP-01 Users, jobs, artefacts

**Job.** Who uses it; jobs; artefact classes: **plant-controlled** vs **workbench-generated** vs **personal `.md`**. Must vs ambition for Word / Excel / PPT / **calculations with steps** / code.

**Why required.** PS is about **deliverables**, not chat. Mixing personal notes with SOPs makes fake plant truth.

**Significance.** Inspection demo is **Word** (**Official** Expected Solution). PPT, Excel, calc-with-steps are **Official** Description. Board presentations and engineering calculations are **Official** Background. Sectors (PSU, defence-linked, government offices) are **Official** Background — not MRPL-only ambition.

**Source of truth.** **Official** Background + Description + Expected Solution (Word example). **User** — personal `.md` as a third class.

**If skipped.** We will demo a chatbot and call Excel “later” with no contract.

**Depends on.** WP-00.

---

### 3 — WP-02 Surrounding plant systems

**Job.** What we are **not**: EAM, DMS, historian, IdP, DCS. What we may **read** via a connector.

**Why required.** Description asks for a local **knowledge base connector** and internal search — connector to org stores, not a second ERP.

**Significance.** Stops “we replaced SAP.” Read-only + declared destination. Mail/correspondence lives here as a store type, not as a PDF dump.

**Source of truth.** **Official** Description: manuals, SOPs, **past correspondence**, KB **connector**. No MRPL interface is verified — freeze “not our job” vs “read-only later,” do not invent APIs.

**If skipped.** MCP will be aimed at write-capable plant systems.

**Depends on.** WP-01.

---

### 4 — WP-04 Identity, session, task grants, revoke

**Job.** Person authenticates. **Task** opens a grant (sources, tools, plugins, classification ceiling, TTL). Task end → grant revoked. Copies in chat/`.md` are in scope.

**Why required.** Full-system access for a session is the leak you named. PS confidential classes are not one bucket (P&IDs, financials, vendor negotiations, unreleased designs, mail, strategy).

**Significance.** Helps safety; **not complete security** (**User**). Standing tokens + “revoke theatre” while drafts still hold P&IDs = failure.

**Source of truth.** **Official** Background (confidential classes, on-prem policy). **User** (least privilege, revoke after task). **Spec** [NIST SP 800-53 Rev 5 AC-6](https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-6/) least privilege for the assigned task.

**If skipped.** RAG and plugins inherit the whole plant.

**Depends on.** WP-01.

---

### 5 — WP-05 HITL map

**Job.** Hard gates vs review-only vs none. Include: export, plugin install, org-skill promotion, file **write**, contradiction (policy vs user), Word/approval drafts.

**Why required.** Product is not an autonomous refinery operator. Description asks for approval notes and real deliverables — those are human-owned.

**Significance.** If HITL is only “approve the Word file,” plugins and `.md` bypass it.

**Source of truth.** **Official** Background (approval notes, confidential work). **User** / prior product definition: HITL forever; never safety/legal/financial/statutory decider.

**If skipped.** Intelligent layer will “decide” because no gate exists.

**Depends on.** WP-00, WP-01.

---

### 6 — WP-03 Ingest and multimodal

**Job.** Scanned PDFs, handwritten notes, engineering drawings, photographs → on-device OCR/vision. Fail closed.

**Why required.** Expected Solution: multimodal task + inspection scan → Word. Description: those four input types, on-device OCR and vision.

**Significance.** Vision/OCR **models** are plugs (WP-24), but the **path** (scan in → text/image out) is this WP. Handwritten is Official, not a stretch.

**Source of truth.** **Official** Description + Expected Solution.

**If skipped.** The inspection demo has nothing to read.

**Depends on.** WP-01, WP-05.

---

### 7 — WP-23 Untrusted content / injection

**Job.** Treat OCR text, retrieved chunks, MCP tool output, and personal `.md` as **untrusted instructions**.

**Why required.** Those channels can override system policy. Not in the PS as a sentence; it is what makes RAG, plugins, and `.md` survivable on confidential files.

**Significance.** Without this, citation RAG and MCP host are prompt-injection surfaces with plant data.

**Source of truth.** **Spec** [IETF draft MCP security](https://www.ietf.org/archive/id/draft-mohiuddin-mcp-security-considerations-00.html); [arXiv 2509.24272](https://arxiv.org/html/2509.24272v1) (malicious MCP / tool poisoning). **User** — `.md` harness and MCP host make this mandatory.

**If skipped.** A scan or a plugin description becomes the real system prompt.

**Depends on.** WP-03, WP-05.

---

### 8 — WP-11 Retrieve / RAG / plant storage

**Job.** How manuals, SOPs, correspondence, EAM/DMS revisions are fetched. Revision-aware. ACL = **grant**, not role dump. Slow is acceptable.

**Why required.** Description: ground in org manuals/SOPs/correspondence via local KB connector; nothing external. Expected Solution does not name a vector DB.

**Significance.** Vectors are an index, not the system of record. Correspondence ≠ SOP PDF.

**Source of truth.** **Official** Description (grounding + connector). **User** (verify vs files; slower OK). **Spec** Lewis et al., *RAG*, NeurIPS 2020 (retrieval grounds generation; retrieval quality ≠ generation quality).

**If skipped.** Model invents plant facts; or we paste whole manuals (WP-21 then fails).

**Depends on.** WP-02, WP-03, WP-04.

---

### 9 — WP-22 Three-source claim verification

**Job.** Every grounded claim checked against **file**, **user utterance**, **company policy**. Contradiction policy. `NOT FOUND` is valid. Accuracy over speed.

**Why required.** You made this the RAG bar. PS says ground in org knowledge; it does not say “user is always right.”

**Significance.** Stops the model picking the friendliest of three sentences. Policy is a corpus, not a footer in the system prompt.

**Source of truth.** **User** (file / user / policy). **Official** Description (ground in manuals/SOPs). **Spec** Lewis et al. 2020.

**If skipped.** WP-11 retrieves; WP-12 never knows which source won.

**Depends on.** WP-11, WP-05.

---

### 10 — WP-07 Tools, prompts, specialist agents

**Job.** Official local tools. System policy vs skills. **One orchestrator**, **separate agents** for defined tasks. File **write** is a gated tool.

**Why required.** Description: act like an agent; plan; call local tools (file R/W, sandbox, spreadsheet, internal search); **iterate**. Background: Claude/Codex-class work.

**Significance.** Swarm with shared full access = standing privilege. Specialists inherit **task grants**.

**Source of truth.** **Official** Description tool list + iterate. **User** — separate agents for defined tasks.

**If skipped.** Either a chatbot or one mega-agent with every plugin.

**Depends on.** WP-05, WP-11.

---

### 11 — WP-16 Execution sandbox

**Job.** Isolated run **and verify** of generated code/tests. Not the GPU box. Network none at org intent.

**Why required.** Expected Solution: coding task **run and verified** in a sandbox. Description: code execution in a sandbox.

**Significance.** Verify ≠ print code. Wrapping the GPU in the same jail as untrusted code kills inference or leaks the model server.

**Source of truth.** **Official** Description + Expected Solution.

**If skipped.** Coding demo is a lie.

**Depends on.** WP-07.

---

### 12 — WP-08 Plugin host (MCP + skill packs)

**Job.** Users **add** MCP/plugins and use them. Local/offline install, allowlist, default-deny egress per plugin, audit, HITL on install/call as mapped in WP-05.

**Why required.** Background: work **the way they use Claude or Codex**. That industry host is MCP + skills. Expected Solution: **no external calls at any point** — so the host cannot be a public directory or Anthropic’s public-HTTPS MCP connector.

**Significance.** Product is a **host**. Freeze is *how* (air-gap), not *whether*. Prototype may ship one local demo server and still be a host.

**Source of truth.** **Official** Background (Claude/Codex-class). **User** (add MCP/plugins). **Spec** [MCP transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports); [Agent Skills](https://agentskills.io/specification); Claude/Cursor host docs (**Spec/Observed**). **Spec** MCP security draft + Docker allowlist/isolation. Anthropic Messages MCP connector = public HTTPS, **not** our pattern.

**If skipped.** Either no extensibility (fails the metaphor) or WAN plugins (fails sovereign proof).

**Depends on.** WP-07, WP-16, WP-23.

---

### 13 — WP-24 Model registry (pluggable models)

**Job.** Workbench catalog of **Model Cards** (LLM / VLM / OCR). Add **and remove** without changing workbench code. Open-weight, staged on-prem only.

**Why required.** Description: not locked to one model; multiple open-weight; **addable later without redesigning**; field moving fast. Expected Solution: smaller model if 120B absent; auto-select still works. **Remove** (**User**) is the inverse of add — otherwise the catalog is add-only lock-in.

**Significance.** Models are the same *kind* of entity as plugins: packs the host consumes. Weights are not in the workbench. `GET /v1/models` is not a card (no vision/tools/roles). Hardcoded `qwen-coder` *is* a redesign.

**Source of truth.** **Official** Title (open-weight multimodal); Description (not locked, at once, add without redesign, on-device OCR/vision models); Expected Solution (swap smaller model). **User** (remove; plug entity). **Prior paper** Model Cards / OpenAI LCD — re-confirm at freeze.

**If skipped.** Every new weight is a software project. Venue 120B fallback cannot happen.

**Depends on.** WP-00.

---

### 14 — WP-06 Orchestration + task routing

**Job.** Task type → **registered** card. Plan multi-step. **Iterate**. Never: safety/FFS/statutory autonomy.

**Why required.** Description: automatically pick the right model (coding ≠ summary). Expected Solution: show auto-select on **≥2 task types**. Description: plan; iterate, do not answer once.

**Significance.** Routing without WP-24 hardcodes models. Routing without WP-21 dumps whole files. Routing is not “the model decided the plant is safe.”

**Source of truth.** **Official** Description + Expected Solution. **User** (smart routing by task).

**If skipped.** No PS auto-select demo; one-shot chat.

**Depends on.** WP-07, WP-24.

---

### 15 — WP-21 Context assembly / data-to-pass

**Job.** What tokens, citations, tool results, and plugin outputs actually enter the request. Minimize to the **grant**.

**Why required.** **User**: intelligent layer decides **what data to pass**, not only which model. AC-6: only access needed for the task. Mid-range GPU context is finite (prototype fact, not org uniqueness).

**Significance.** This is the difference between a 7B that cites two SOP clauses and a 7B that swallows a P&ID binder.

**Source of truth.** **User**. **Spec** NIST AC-6. **Official** (indirect): confidential data must not go to cloud — same logic: do not over-send even locally.

**If skipped.** Grants and RAG are bypassed by “paste everything into the prompt.”

**Depends on.** WP-06, WP-04, WP-11.

---

### 16 — WP-09 LLM gateway

**Job.** Software socket: **valid** `/v1` requests only. Auth, timeout, size. `model` id must exist on a **card**. Fail closed. Never rewrite to a cloud `base_url`.

**Why required.** Description: workbench on org GPU **server** — there is a network hop. Invalid or capability-mismatched requests waste the runtime or break air-gap (remote image URLs).

**Significance.** Gateway ≠ CUDA. Gateway ≠ MCP bus.

**Source of truth.** **Official** Description (own GPU server; nothing leaves). **User** (valid requests). **Prior paper** LCD: `POST /v1/chat/completions`, `GET /v1/models`, Bearer, vision as `data:` base64 only — re-confirm at freeze.

**If skipped.** Workbench talks to GPU “somehow”; jury cannot see a contract.

**Depends on.** WP-06, WP-21, WP-24.

---

### 17 — WP-10 Runtime (GPU + weights)

**Job.** Serve ids the registry named. Load/unload policy for “multiple at once” (catalog vs VRAM-resident). Hardware probe lives here, not in OpenAI. Workstation **or** server.

**Why required.** Description: org GPU server; multiple models. Expected Solution: mid-range GPU; smaller model if 120B absent; **workstation or server**.

**Significance.** Changing runtime (`base_url`) must not redesign the workbench. Simultaneous 70B+VLM on mid-GPU is fake; freeze load policy honestly.

**Source of truth.** **Official** Description + Expected Solution. **Prior paper** two planes.

**If skipped.** Workbench bundles weights; venue GPU change is a rewrite.

**Depends on.** WP-09, WP-24.

---

### 18 — WP-12 Validation + security gates

**Job.** Before the user **sees or downloads**: citations, classification, export control, secret scan, sandbox verdict.

**Why required.** **User**: gates before information reaches the user. Expected Solution Word file is a deliverable — export is a control point. Confidential classes in Background.

**Significance.** Slow pass with citations beats fast uncited chat. This is output-side; WP-22 is claim-side; both needed.

**Source of truth.** **User**. **Official** Background (confidential; on-prem policy).

**If skipped.** HITL reviews a document that already leaked on screen.

**Depends on.** WP-05, WP-22, WP-07.

---

### 19 — WP-17 Audit and evidence log

**Job.** Log person, task, grant, **model card id**, tools/plugins, retrieval revisions, HITL, export. Retention and who may see logs.

**Why required.** Org / CERT-In-shaped accountability. Lineage (WP-14) is built from this log. Jury: which model ran.

**Significance.** Without model id and plugin id, “we auto-selected” is a slide.

**Source of truth.** **Official** Expected Solution (logs or visible monitor). **Spec/Observed** CERT-In logging expectations — **cite the advisory at freeze**, do not quote from memory. DPDP: freeze data-handling in this WP or WP-04, with the statute in hand.

**If skipped.** No approval trail; no incident reconstruction.

**Depends on.** WP-09, WP-12, WP-08.

---

### 20 — WP-14 Task–version lineage store

**Job.** Relations: task ↔ **input versions** ↔ tool/plugin calls ↔ model ↔ draft artefact versions ↔ HITL ↔ export. Engine **not** chosen here.

**Why required.** **User**: not a graph database; clarity of **what they are building**. Document control: which SOP revision was cited.

**Significance.** This is how an engineer sees history. SQL, files+manifest, or a graph engine are later. PPT must say lineage until an engine is frozen.

**Source of truth.** **User**. **Official** (indirect): grounding in SOPs implies revision identity. **Spec** none that forces Neo4j.

**If skipped.** RAG cites “the manual”; nobody knows which file version; tasks are a chat dump.

**Depends on.** WP-01, WP-17.

---

### 21 — WP-13 Monitors (sovereign + operator)

**Job.** **Audience A:** visible proof WAN/external = 0 (**Official**). **Audience B:** live task, selected **card** and why, citations, HITL queue, sandbox, **active grant**, plugin allow/deny (**User**). Prefer host/OS evidence, not only an in-app widget.

**Why required.** Expected Solution: logs **or visible network monitor**; no external calls **at any point**; that **is** the sovereign proof. You asked monitors that satisfy **users**.

**Significance.** App-only badge while OS still egresses is fake. Operator blank screen is an unusable Claude-class tool.

**Source of truth.** **Official** Expected Solution. **User** (operator needs).

**If skipped.** Sovereign claim is a README.

**Depends on.** WP-10, WP-16, WP-17, WP-04.

---

### 22 — WP-15 Personal `.md` harness

**Job.** From daily tasks, write/update personal markdown (templates, conventions). Promotion to org skill = HITL. No weight training. `compatibility: internet` skills unloadable.

**Why required.** **User** meaning of “self-learning.” Matches how Claude/Cursor-class tools persist workflow (skills as markdown).

**Significance.** Personalization without poisoning plant SOPs. Injected `.md` is WP-23.

**Source of truth.** **User**. **Spec** [Agent Skills](https://agentskills.io/specification) (`SKILL.md`, progressive disclosure). **Not Official PS** — do not claim the PS required “self-learning.”

**If skipped.** Either no adaptation (weaker host) or fake ML “self-train on plant data.”

**Depends on.** WP-07, WP-14, WP-23.

---

### 23 — WP-18 Fail-closed + eval suite

**Job.** What happens when OCR, retrieve, model, plugin, grant, or gateway fails. Golden tasks: ≥2-type routing, scan→Word, sandbox verify, multimodal, WAN=0, missing citation, expired grant, unregistered model.

**Why required.** Expected Solution is a **demonstrable** working deployment. Fail-open to cloud or to a default model hides removal and breaks air-gap.

**Significance.** This is the org quality bar and later the prototype test list.

**Source of truth.** **Official** Expected Solution (the demo list). **User** (grants, citations, plugins).

**If skipped.** We will call a happy-path video “done.”

**Depends on.** WP-03, WP-12, WP-21, WP-24.

---

### 24 — WP-19 Offline update (models + plugins)

**Job.** Weights and plugins arrive on approved media. No silent Hugging Face / npm / MCP directory pull. Staging then register (WP-24 / WP-08).

**Why required.** Expected Solution: no external calls **at any point**. Description: add models later — that later cannot be a WAN fetch in production or on stage.

**Significance.** Plugability without breaking sovereign proof.

**Source of truth.** **Official** Expected Solution + Description (add models; nothing external). **Spec/Observed** [air-gapped MCP is not default](https://connector.zone/guides/air-gapped-and-self-hosted-mcp/).

**If skipped.** First “add a model” demo phones home.

**Depends on.** WP-10, WP-08, WP-24, WP-13.

---

### 25 — WP-20 Org connection diagram

**Job.** One picture of all frozen WPs: person → session → **grant** → orchestrator → specialist → (tools | plugin host) → **context pack** → gateway → runtime; retrieve + WP-22; lineage; monitors A/B; HITL; **model registry**.

**Why required.** Layers designed in isolation will not meet. This is the org paper you asked for before prototype.

**Significance.** After this, we may narrow REAL / MOCK / LATER. Not before.

**Source of truth.** All frozen WPs + **Official** PS as the caption test: does this picture still match Expected Solution?

**If skipped.** Prototype will skip gates that only existed in separate notes.

**Depends on.** All above.

---

### After WP-20 — Prototype overlay (not a WP number)

**Job.** Mark each box REAL / MOCK / LATER. Bind tests to Expected Solution. Hardware honesty (mid-GPU, sequential load if needed).

**Why required.** **Official** Expected Solution is a working local demo on workstation or server, mid-range GPU, smaller model allowed.

**Source of truth.** **Official** Expected Solution. Do not start this pass until WP-20 exists.

---

## Pluggable entities (same pattern — do not rebuild the workbench)

| Entity | WP | Official hook |
|---|---|---|
| Models (LLM/VLM/OCR) | WP-24 + WP-10 | Not locked; add without redesign; on-device OCR/vision |
| MCP / plugins | WP-08 | Claude/Codex-class + local tools |
| Runtime `/v1` | WP-09 + WP-10 | Own GPU server; workstation or server |
| KB connector target | WP-11 + WP-02 | Local KB **connector** |
| Personal / org skills | WP-15 | **User** (not PS) |

**Not plugs:** HITL policy, air-gap, classification, never-write-DCS, claim-verification rules.

---

## How we use this list

1. You say go → **WP-00** only.  
2. Freeze note (one page) per WP.  
3. Next WP may use frozen contracts only.  
4. After **WP-20**, prototype overlay.  
5. No stack lock, no PPT fill, no app code until you ask after the overlay.
