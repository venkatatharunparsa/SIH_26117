# Org-level design agenda — SIH26117 workbench

**Date:** 2026-09-17 (rev 3 — pluggable models + PS completeness)  
**Mode:** Organisation design first. Prototype narrow is **after** this list is walked.  
**Stack:** not locked.  
**Red-team:** `DESIGN_AGENDA_REDTEAM_v1.md`  
**PS clause check:** `DESIGN_PS_COMPLETENESS_v1.md`  
**PPT / code:** paused until this agenda is done.

User = decision maker. Assistant = Principal Solutions Architect / Harness Engineer / Research Engineer.

---

## User intent (2026-09-17) — product meaning, not a freeze

These are how **you** defined the layers. Each still gets a WP freeze (must / may / never). They are no longer “optional fashion” questions.

| Topic | Meaning we will design to | Explicitly not |
|---|---|---|
| Workbench | Claude/Codex-class **host**: user can **add MCP or plugins** and use them; **separate agents** for defined tasks | Cloud Claude connectors; public MCP directory; one mega-agent with standing full access |
| Models | **Pluggable entity** on the workbench: add **or remove** without changing workbench code. Cards + catalog, not hardcoded names | Weights baked into the app; cloud `/v1` as a “model”; Hugging Face fetch at runtime |
| Self-learning | Workbench adapts to **daily tasks** by writing/updating personal **`.md` files** | Unsupervised weight training on plant data |
| “Graph” | **Relations** between **data versions** and **tasks** so the user sees what they are building | Neo4j (or any graph engine) as a default |
| Intelligent layer | **Route** the right model for the task; decide **what data to pass**; related packing/timeouts | Model as safety / FFS / statutory decision-maker |
| Session | **Not** whole-system data access; **revoke after the task**. Helps safety; **not complete security** | Standing full-plant tokens; “revoke” while copies remain in chat/`.md` |
| RAG | Verify claims against **file, user, company policy**; slower retrieval is acceptable | Fast uncited chat; vectors as the plant system of record |
| Gateway | Software that sends **valid** requests to the runtime | CUDA; silent rewrite to a cloud `base_url` |
| Monitors | Satisfy **users** (routing, citations, HITL, grants, plugins) **and** PS air-gap proof | App-only WAN badge with OS still egressing |

---

## How we will work (every item)

1. Discuss **one work package (WP)** only.  
2. Adversarial pass: what the PS actually requires, what exists in industry/OSS, what would be fake.  
3. You decide. We freeze that WP in a short contract (must / may / never).  
4. Next WP may **use** frozen contracts; it may not reopen them without you saying so.  
5. After all org WPs: one connection diagram. **Then** narrow to prototype.

Do not pick FastAPI, Ollama, Neo4j, LangGraph, or a GitHub fork inside a WP unless that WP’s job is “candidate list” and the freeze is still “not locked.”

---

## Your 11 parts — mapped, not discarded

| Your # | You called it | Agenda WP | Note |
|---|---|---|---|
| 1 | Orchestration + intelligent layer that decides from requirements | **WP-06** + **WP-21** | Route ≠ pack context. Neither is allowed to decide safety. |
| 2 | Tools, system prompt, agents | **WP-07** | PS local tools. Specialist agents behind one orchestrator. |
| 3 | MCP servers available for tasks | **WP-08** | **Host product.** Freeze = air-gap install, allowlist, isolation — not “skip MCP.” |
| 4 | Self-learning harness that adopts to workflow | **WP-15** | Personal `.md` + HITL promotion to org skill. |
| 5 | LLM gateway to server | **WP-09** | Valid `/v1` requests. Not CUDA. Pair with **WP-10**. |
| 6 | Session management / data access | **WP-04** | Person session + **task grant** + revoke. |
| 7 | Validation and security gates before information reaches the user | **WP-12** + **WP-22** | Output filter + three-source claim check. |
| 8 | HITL: critical spots and engineering weak spots | **WP-05** | Includes plugin install and skill promotion. |
| 9 | Efficient RAG vs how plant systems store data | **WP-11** | Revision-aware, ACL-aware. Slow OK. |
| 10 | Store generated workbench data; graph needed? | **WP-14** | **Lineage** of versions ↔ tasks. Engine undecided. |
| 11 | How we show air-gap; which monitors | **WP-13** | Audience A: WAN=0. Audience B: operator. |

PS-first-class, not in the original 11: **models as plugs** → **WP-24** (workbench registry) + **WP-10** (runtime load). Same host pattern as MCP: swap the pack, not the workbench.

---

## Missing parts (org paper)

Required at **org paper** even if the prototype later mocks them.

| WP | Why it was missing |
|---|---|
| **WP-00** Product contract | Must / ambition / never. Stops chatbot vs GPU-optimiser vs DCS-writer vs cloud-plugin clone |
| **WP-01** Users, jobs, artefacts | Who uses it; Word/Excel/code; **plant vs generated vs personal `.md`** |
| **WP-02** Plant systems around us | EAM, DMS, historian, IdP — workbench is **not** those systems |
| **WP-03** Ingest / multimodal | OCR, vision, scans, drawings — PS Description + Expected Solution |
| **WP-10** Runtime plane | GPU / `/v1` server, **load/unload** weights that the registry already named |  
| **WP-24** Model registry | Workbench-side **pluggable models** (LLM/VLM/OCR cards). Add/remove = catalog, not a rebuild |
| **WP-16** Code sandbox plane | PS: verified execution. Must **not** be the same box as the GPU |
| **WP-17** Audit / lineage log | Prompts, model id, tools/plugins, HITL, exports — CERT-In-shaped |
| **WP-18** Fail-closed + evaluation | OCR/tools/models/plugins/grants fail; golden tasks |
| **WP-19** Ops: offline update | Weights **and plugins**; no silent WAN pull |
| **WP-20** Connection map | After all WPs: one org diagram |
| **WP-21** Context assembly | **What data to pass** to which model (from intelligent-layer split) |
| **WP-22** Three-source verification | File vs user vs policy; contradiction policy |
| **WP-23** Untrusted content | Prompt injection via OCR, RAG, MCP, personal `.md` |

---

## Ordered list to follow (this is the queue)

Discuss in this order. Dependencies are why.

| Order | WP | Title | We freeze | Depends on |
|---|---|---|---|---|
| 1 | **WP-00** | Product contract | Must-work / org-ambition / never | PS only |
| 2 | **WP-01** | Users, jobs, deliverable artefacts | Primary user; plant / generated / personal; **Word vs PPT vs calc-with-steps** (must vs ambition) | WP-00 |
| 3 | **WP-02** | Surrounding plant systems | Read-only connectors vs “not our job” | WP-01 |
| 4 | **WP-04** | Identity, session, **task grants**, revoke | Who can request what; grant TTL; copies after revoke | WP-01 |
| 5 | **WP-05** | HITL map (critical + weak spots) | Hard gates vs review-only; plugin + skill promotion | WP-01, WP-00 |
| 6 | **WP-03** | Ingest and multimodal | Scan/photo/drawing path; fail-closed | WP-01, WP-05 |
| 7 | **WP-23** | Untrusted content / injection | How OCR, RAG, MCP, `.md` are sandboxed as text | WP-03, WP-05 |
| 8 | **WP-11** | Retrieve / RAG / plant storage | How manuals, EAM, mail, scans are fetched; revision + ACL | WP-02, WP-03, WP-04 |
| 9 | **WP-22** | Three-source claim verification | File vs user vs policy; `NOT FOUND`; slow OK | WP-11, WP-05 |
| 10 | **WP-07** | Tools, prompts, specialist agent(s) | Tool list; orchestrator vs specialists; system policy | WP-05, WP-11 |
| 11 | **WP-16** | Execution sandbox | Isolated code/tests; never wraps GPU | WP-07 |
| 12 | **WP-08** | Plugin host (MCP + skills packs) | Local install; allowlist; per-plugin egress deny | WP-07, WP-16, WP-23 |
| 13 | **WP-24** | Model registry (pluggable models) | Card schema; add/remove without workbench rebuild; open-weight only | WP-00 |
| 14 | **WP-06** | Orchestration + task routing | Task type → **registered** model; plan/**iterate**; **no safety autonomy** | WP-07, WP-24 |
| 15 | **WP-21** | Context assembly / data-to-pass | What tokens, citations, tool results enter the request | WP-06, WP-04, WP-11 |
| 16 | **WP-09** | LLM gateway | Schema-valid `/v1`, auth, timeout; `model` id must exist on a card | WP-06, WP-21, WP-24 |
| 17 | **WP-10** | Runtime (GPU + weights) | Serve ids the registry named; load policy for “at once” vs sequential | WP-09, WP-24 |
| 18 | **WP-12** | Validation + security gates | Before user sees or downloads | WP-05, WP-22, WP-07 |
| 19 | **WP-17** | Audit and evidence log | What is logged, retained, shown; **model id from card** | WP-09, WP-12, WP-08 |
| 20 | **WP-14** | Task–version lineage store | Relations: task ↔ versions ↔ artefacts; engine later | WP-01, WP-17 |
| 21 | **WP-13** | Monitors (sovereign + operator) | WAN=0 proof; user-facing routing/HITL/grant/plugin/**which model card** | WP-10, WP-16, WP-17, WP-04 |
| 22 | **WP-15** | Personal `.md` harness | Daily adaptation; promotion HITL; no weight training | WP-07, WP-14, WP-23 |
| 23 | **WP-18** | Fail-closed + eval suite | Org quality bar including routing and grants | WP-03, WP-12, WP-21, WP-24 |
| 24 | **WP-19** | Offline update (models + plugins) | USB/approved media; no silent HF/registry pull | WP-10, WP-08, WP-24, WP-13 |
| 25 | **WP-20** | Org connection diagram | One picture of all frozen WPs | All above |

After **WP-20**, we open a **prototype overlay** pass (REAL / MOCK / LATER + tests). Not before.

---

## Adversarial flags (do not skip when that WP starts)

| Topic | Risk if we assume it |
|---|---|
| MCP / plugins | Industry host pattern is real. **Public install + remote HTTPS MCP** fails Expected Solution. Design **offline allowlisted host**. |
| Self-learning | Retraining on plant data is a policy hole. Personal `.md` is the surviving meaning; still injectable and not an SOP. |
| Graph database | Need is **version–task lineage**. A graph engine is optional later. |
| Intelligent layer “taking decisions” | PS wants routing and drafting. **Safety, FFS, commercial, statutory stay human** (WP-05). |
| Session = security | Session without **grant + classification + revoke-of-copies** is a leak. Revoke is not complete security. |
| RAG = Chroma | Plant truth lives in EAM/DMS **revisions** and in **policy**. User speech is a claim. |
| Fast RAG | You chose **accuracy over speed**. Do not “optimise” by dropping citations. |
| Gateway = GPU | Gateway is software. Invalid request must fail closed. |
| Monitor in the app only | PS wants **visible** sovereign proof; operators also need grant/plugin/HITL views. |
| One agent, all plugins | Standing privilege. Specialists inherit **task grants**, not the whole catalog. |
| Personal `.md` next to SOPs | Document-control failure. |
| Model hardcoded in workbench | Violates PS “add without redesign.” Models are **catalog entities** (WP-24), weights are **runtime**. |
| `/v1` = allowed model | Transport is not policy. Open-weight + on-prem + card. Cloud OpenAI-compat is still forbidden. |
| “Multiple at once” = many weights in VRAM | Catalog of many; load policy is WP-10. Simultaneous 70B+VLM on mid-GPU is fake. |
| File **write** as an ordinary tool | Description lists write. Grant + HITL class, not the same as read. |
| Iterate as one-shot chat | Description: do not answer once and stop. |
| KB = files inside the app | Description: **connector** to manuals/SOPs/**correspondence**. |
| PPT / calc-with-steps forgotten | Description deliverables. Expected Solution demo binds **Word** for inspection. WP-01 must vs ambition. |

---

## What each WP discussion must produce

A freeze note, max one page:

- **Job** of this layer at org  
- **Inputs / outputs**  
- **What it must never do**  
- **Interfaces** to already-frozen WPs  
- **Open questions** parked (not solved with a stack brand)  
- **Prototype hint** (one line only, not a build plan)

---

## Next

**Follow:** `DESIGN_FOLLOW_LIST_v1.md` (walk list). **Repo map before any WP:** `DESIGN_REPO_MAP_v1.md` (adopt / add / refuse; not a fork lock).

Queue starts at **WP-00 Product contract** when you say go.

WP-00 must state **plugin host + local-only install** and **models as pluggable catalog entities** (add/remove without workbench redesign), or WP-08/WP-24 will smuggle a WAN marketplace and hardcoded weights.
