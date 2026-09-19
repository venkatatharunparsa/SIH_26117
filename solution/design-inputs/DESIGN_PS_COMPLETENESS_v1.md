# PS completeness pass — pluggable models and other buried clauses

**Date:** 2026-09-17  
**Trigger:** User: models add/remove must not change the workbench; model is a **pluggable entity**. Check for other PS items of the same kind.  
**Official text:** `sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`  
**Does not freeze stack.**

Grades: **Official** = PS wording. **User extension** = implied by Official, stated by user. **Prior paper** = architecture note, not a WP freeze.

---

## 1. You are right: model plugability was buried

PS Description (Official):

> The backend should not be locked to one model. It needs to support multiple open weight models at once and automatically pick the right one for a given task … New open weight models should be addable later without redesigning the system, since this space is moving fast.

Expected Solution (Official): auto-select across ≥2 task types; if 120B hardware is absent, use a smaller open-weight model.

Agenda v2 put this inside **WP-10 Runtime (GPU + weights)**. That is the wrong plane.

| Plane | Owns | Changes when a model is added/removed? |
|---|---|---|
| **Workbench** | UI, agents, tools, plugins, grants, RAG, gateway client, **Model Cards / registry** | **No code change.** Register or unregister a card. Routing reads the catalog. |
| **Runtime** | GPU, staged weights, `/v1` server | Weights appear or disappear. `GET /v1/models` changes. |

**Why it is required (not a nice-to-have):**

1. **PS says so.** Not locked; add without redesign; field moving fast. A hardcoded `if task==code: qwen-coder` *is* a redesign every time the org swaps weights.
2. **Remove is required even though PS only says add.** If you can only add, dead models stay in routes, UI, and eval. Unregister is the same plug as install, inverted. **User extension**, justified by “not locked.”
3. **Same pattern as MCP/plugins.** Plugins are user-addable packs. Models are operator-addable inference packs. Both are **entities the workbench consumes by catalog**, not by shipping a new workbench build.
4. **Transport ≠ policy.** OpenAI-compatible `/v1` is how we *talk* to a model. It does not say which models are allowed. Title + Description say **open-weight**, on-prem. A cloud `base_url` that speaks `/v1` still fails air-gap and fails “open weight.”
5. **`GET /v1/models` is not a Model Card.** Prior logical architecture: the OpenAI Models object is `id` only — no vision/tools/role. Routing needs **our** cards on the workbench. Adding a model = stage weights (offline, WP-19) + insert card (WP-24) + runtime lists the id. Removing = drop card first so the workbench never sends that `model` field; then unload weights.
6. **OCR / vision models are also plugs.** Description: “on device OCR and vision models.” A new VLM must not fork the ingest UI. Cards carry `capabilities.vision` / `roles`.

**Adversarial:**

- “Addable” by downloading from Hugging Face at demo time = **external call**. Fails Expected Solution “at any point.”
- “Multiple at once” on one mid-range GPU often means **catalog of many, one loaded**. Claiming simultaneous 70B+VLM on 8 GB is fake. Org paper: catalog + load policy. Prototype: sequential OK (already red-teamed).
- Workbench that embeds a GGUF path in source is **not** pluggable.
- Routing that ignores missing cards and “falls back” to a default model hides removal.

**Agenda fix:** **WP-24 Model registry (pluggable models)** on the workbench plane. WP-10 stays runtime (load/unload hardware). WP-06 routing **depends on WP-24**, not on GPU brand.

---

## 2. Clause-by-clause: what else was buried or missing

Every sentence of Title, Background, Description, Expected Solution. **Covered** = has a WP that will freeze it. **Buried** = exists but on the wrong WP or as a side note. **Gap** = no WP job line.

| # | PS clause | Status | Why it is required | Where it lives now |
|---|---|---|---|---|
| T1 | Title: **open-weight** multimodal LLMs | **Buried** in WP-10 | Closed/cloud weights contradict title + air-gap even if `/v1` works | WP-00 never-list + **WP-24** allowlist = open-weight staged on-prem |
| T2 | Title: **multimodal** | Covered | Expected Solution multimodal task | WP-03 |
| T3 | Software / Smart Automation | Covered | Category is software, not a GPU tuner | WP-00 |
| B1 | Sectors: refineries, **PSUs, defence-linked, government offices** | **Gap** | Product is not MRPL-only; classification and HITL differ by sector | WP-00 / WP-01 (org-ambition users) |
| B2 | Work: approval notes, **board presentations**, **engineering calculations**, internal tools code, scan/drawing review | **Buried** | Calculations-with-steps and PPT are Description deliverables; WP-01 listed Word/Excel/code more than calc/PPT | WP-01 artefact types |
| B3 | Confidential classes: P&ID, financials, vendor negotiations, unreleased designs, mail, strategy | **Buried** | Session grants must be **classification-scoped**, not “engineer vs admin” only | WP-04 |
| B4 | Policy keeps data on premises; people either go slow or **paste into public tools** | Covered as why | Sovereign proof is the product; shadow-IT is the competitor | WP-00, WP-13 |
| B5 | Claude/Codex-class UX missing on-prem | Covered | Plugin host + agents | WP-08, WP-07 |
| D1 | Self-hosted, **org’s own GPU server**, nothing leaves | Covered | Two planes; air-gap | WP-10, WP-13 |
| D2 | Backend **not locked to one model** | **Buried** → **WP-24** | See §1 | WP-24 |
| D3 | **Multiple** open-weight models **at once** | **Buried** | Catalog vs simultaneous load is a freeze, not a slogan | WP-24 + WP-10 load policy |
| D4 | **Auto-pick** by task (coding ≠ summary) | Covered | Intelligent layer | WP-06 |
| D5 | **Add later without redesign** | **Buried** → **WP-24** | See §1 | WP-24 |
| D6 | **Remove** without redesign | **User extension** | Catalog hygiene; otherwise “not locked” is add-only | WP-24 |
| D7 | Agent: **plan** multi-step | Covered | Orchestration | WP-06, WP-07 |
| D8 | Tools: file **read and write** | **Buried** | Write is a HITL/grant class; agenda said “file” | WP-07 + WP-04 + WP-05 |
| D9 | Sandbox **code execution** | Covered | | WP-16 |
| D10 | **Spreadsheet work** | Covered as tool | Excel is Description + Expected-adjacent | WP-07, WP-01 |
| D11 | **Internal document search** | Covered | | WP-11 |
| D12 | **Iterate**, not answer once | **Buried** | One-shot chat fails Description | WP-06 freeze: loop until tool/HITL stop |
| D13 | Scanned PDF, **handwritten**, drawings, photographs | Covered | | WP-03 |
| D14 | **On-device OCR and vision models** | **Buried** | These are **pluggable models** too, not a hardcoded Tesseract button | WP-24 roles + WP-03 |
| D15 | Deliverables: approval notes, **PPT/Word/Excel**, working code, **calculations with steps shown**, not just chat | **Buried** (calc + PPT) | Expected Solution binds **Word** for the inspection demo; Description still requires calc-with-steps and PPT as org ambition | WP-01: must vs ambition |
| D16 | Ground in manuals, SOPs, **past correspondence** | **Buried** | Correspondence ≠ PDF SOP; mail/DMS connector | WP-11, WP-02 |
| D17 | **Local knowledge base connector** | **Buried** | Connector to org store, not “Chroma is the KB” | WP-11 |
| D18 | Nothing external (KB path) | Covered | | WP-13, WP-19 |
| E1 | Working **local** deployment | Covered | | prototype overlay after WP-20 |
| E2 | **Single workstation or server** | **Gap** | Org paper must allow laptop-only demo; GPU server is Description, not the only Expected box | WP-00 / WP-10: runtime may be the same machine |
| E3 | **Mid-range GPU**; smaller model if **120B** absent | Covered as venue | Must not become a uniqueness claim | WP-10, prototype overlay |
| E4 | Auto-select **≥2 task types** | Covered | Acceptance test | WP-06, WP-18 |
| E5 | Inspection scan → findings → **Word** | Covered | | WP-01, WP-03, WP-07 |
| E6 | Coding **run and verified** in sandbox | Covered | Verify ≠ print code | WP-16 |
| E7 | Multimodal image or scan | Covered | | WP-03 |
| E8 | Logs **or** visible network monitor; **no external calls at any point**; that is the sovereign proof | Covered | “At any point” includes model/plugin fetch | WP-13, WP-19 |

---

## 3. Same *kind* of miss as pluggable models

These share the pattern: **the workbench is a host; X is a catalogued entity; swapping X must not ship a new workbench.**

| Entity | PS hook | Swap without workbench rebuild? |
|---|---|---|
| **LLM / VLM / OCR model** | not locked; add without redesign; on-device OCR/vision | **Yes — WP-24** |
| **MCP / plugin pack** | Claude/Codex-like (Background) + local tools (Description) | Yes — WP-08 |
| **Runtime `/v1` server** | own GPU server; workstation or server; 120B optional | Yes — change `base_url` (prior lock, confirm in WP-09/10) |
| **KB connector target** | “local knowledge base **connector**” | Yes — WP-11 points at DMS/EAM; not baked-in files only |
| **Skill / personal `.md`** | user intent, not PS | Yes — WP-15 |
| **Sandbox engine** | code verified in sandbox | May swap Docker/other later; not PS-explicit. Do not freeze in WP-00. |

Not pluggable (must stay in the workbench contract): HITL policy, air-gap, classification, “never write DCS,” claim verification. Those are product, not packs.

---

## 4. Queue bug this pass also fixes

WP-06 (routing) listed a dependency on WP-10 Model Cards while WP-10 sat **after** WP-06. Cards belong on the workbench (**WP-24**) and must be frozen **before** routing.

---

## 5. Honest limits

- PS does not use the word “plugin” for models. The **requirement** is add-without-redesign; **plugin-shaped registry** is the design that satisfies it.
- PS does not say “remove.” Remove is the operational inverse of add.
- “At once” is ambiguous (catalog vs VRAM-resident). Freeze in WP-24/WP-10; do not print simultaneous-70B.
