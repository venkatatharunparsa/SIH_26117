# WP-00 — Architect perspective (not frozen)

**Date:** 2026-09-17  
**Role:** Principal Solutions Architect (this page only)  
**Status:** **Draft for debate.** Freeze only after your perspective + PS/org check.

Official text: `../sih_research/sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`

---

## One sentence (proposed)

A **self-hosted, air-gapped software workbench** for confidential industrial **knowledge work**: it behaves like Claude/Codex on the user’s desk, runs **open-weight** models the org can **plug in or remove** without rebuilding the app, **grounds** drafts in org files/policy, produces **real artefacts**, and **proves** nothing left the premises. A human still **owns** every decision that matters.

Not a chatbot. Not a GPU tuner. Not a refinery operator. Not ChatGPT with a skin.

---

## Split I will not mix

| Bucket | Job |
|---|---|
| **Must-work** | Expected Solution + Software category. If we cannot show it, we did not solve SIH26117. |
| **Org-ambition** | Description + Background (and only the User lines you promote). Org paper and later phases. |
| **Never** | Illegal for every later WP, including “just for the demo.” |

---

## Must-work (my recommendation)

From **Official Expected Solution** + Title/category:

1. **Software workbench** — client + agent + tools + artefacts. Hardware/weights are a **runtime we talk to**, not the product.  
2. **Local deploy** on a **workstation or a server**, **mid-range GPU**; **smaller open-weight** model if 120B is absent.  
3. **Auto-select ≥2 task types**, with **two different model ids** visible in the log (not a dropdown the user clicks).  
4. **Agentic path:** scanned inspection report → key findings → **Word** approval note.  
5. **Coding path:** generate, **run and verify** in a **sandbox**.  
6. **Multimodal path:** image or scanned document understood **on-device**.  
7. **Sovereign proof:** logs **or** visible network monitor; **no external calls at any point** (including model/plugin/skill install).  
8. **Not locked to one model;** new **open-weight** models **addable without redesign** (catalog / cards). I treat **remove** as the same must, or “not locked” is add-only.

If we ship only chat+RAG locally, we failed (Open WebUI already does that).

---

## Org-ambition (my recommendation)

From **Official Description + Background**, unless you demote a line:

- Air-gap on the **organisation’s GPU server** (Expected still allows a single workstation — both must be true: same workbench, runtime may be laptop or server).  
- Multiple open-weight models; routing coding ≠ summary ≠ vision.  
- Agent: **plan, iterate**, local **file read and write**, sandbox, **spreadsheet**, **internal search**.  
- Inputs: scanned PDF, **handwritten**, **drawings**, photographs; OCR + vision **models** (also plugs).  
- Outputs: approval notes, **PPT / Word / Excel**, working code, **calculations with steps shown** — not chat as the deliverable.  
- **Local KB connector** to manuals, SOPs, **past correspondence**.  
- Claude/Codex-class **host** so people stop pasting P&IDs / financials / vendor files / unreleased designs into public tools.  
- Same product shape for **PSU / defence-linked / government** knowledge work, not a refinery-only gadget. MRPL is the **sponsor**, not the only user type in the Background.

**Proposed promotions (Official-adjacent, your earlier intent — you may reject):**

- **Plugin/MCP host**, local/offline only.  
- **Skill library** as a catalog; load by task, not all skills on all tools.  
- **Specialist agents** behind one orchestrator.  
- **Task grants + revoke** (helps safety; not complete security).  
- **Citation-first** grounding; file vs user vs policy.  
- **Version–task lineage** (not a graph-DB product).  
- HITL **forever** on exports that look like records.

**Phase inside ambition (so PPT does not hijack must-work):**

| Phase | Artefact |
|---|---|
| Must-work demo | Word + verified code + multimodal + two-model log + WAN=0 |
| Org near-term | Excel, calc-with-steps shown, KB connector to files |
| Org later | PPT/board pack, plant DMS/EAM **read** connectors, SSO |

You can move a row when you answer.

---

## Never (my recommendation)

- Decide **safety / FFS / statutory / legal / commercial / isolation** outcomes. Drafts only.  
- **Write** DCS / SIS / PLC / EAM / ERP / permits. Read-only connectors, later, if at all.  
- Cloud Claude / Codex / OpenAI / OpenRouter as the brain. `/v1` to a **cloud** `base_url` is still an external call.  
- Public **MCP / skill / weight** marketplace at runtime (`npx`, `ollama pull`, HF fetch on stage).  
- Product identity = **Open WebUI**, **OpenHands**, **DeerFlow**, or a GPU optimiser.  
- **Unsupervised training** on plant data as “self-learning.”  
- Treat session revoke as **complete security**.  
- Claim **certified** plant deployment, industrial P&ID vision, or MRPL SLA hours we do not have.  
- Silent fail-open to WAN when a model/plugin is missing.

---

## What I am **not** putting in WP-00

Stack brands. Exact 7B names. Neo4j. LangGraph. Docker vs other jail. Those are later WPs or prototype overlay.

MRPL-specific forms, IdP, DMS APIs — **unverified**. Org requirement we *do* have in the PS: **company policy keeps this data on premises**. Anything beyond that we mark **unknown** until you or a source supplies it.

MRPL already runs **process** AI (predictive/prescriptive units). This PS is the **knowledge-work** gap. Do not claim we invented plant AI.

---

## Open questions for your perspective

1. Promote plugin host + skill library into **org-ambition**, or keep them out of WP-00 until WP-07/08?  
2. Is **HITL forever** a Never-exception (always human on record exports) or only on named artefact types?  
3. Excel / calc-with-steps: ambition or must-work? (PS Description vs Expected Solution.)  
4. Primary user for the org paper: inspection engineer, all knowledge workers in Background, or both?

Do not freeze this file. After your perspective we score each line **Official / org-need / drop**.
