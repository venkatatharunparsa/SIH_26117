# WP-06 orchestration — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-06_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Extra DM framing:** Orchestrator is the **ultimate brain** of the workbench — decides what to do; knows tools / specialists / MCP / cards / capabilities; schema-aware; drives development of the work-loop.  
**Against:** Official Description/Expected Solution; WP-00 (human ultimate decider; no safety autonomy; Intelligent layer); WP-04 grants; WP-05 HITL + stale; WP-07 matrix; WP-24 model-agnostic; WP-03 OCR≠draft path; agenda split WP-06≠WP-21≠WP-09.

**Mode:** Attack first. Overclaiming here breaks the whole product.

---

## 0. DM answers (as given)

| Q | Decision |
|---|---|
| **1** | **Demo:** approved job id **not** required (freestyle OK). **Org:** approved job id **required** |
| **2** | **Orchestrator-only** model selection (worker does not pick the card) |
| **3** | Route by **requirement vs card capability** — one capable LLM may cover many tasks; pick the card that fits the need (not forced always-two-cards-per-job) |
| **4** | Parallel vs sequential **depends on the task** (job template / plan) |
| **5** | **Auto-failover** to next eligible card |
| **6** | **Temporary rules** skeleton + **LLM corrects** the plan **with verification** |
| **R0** | Orchestrator = capability-aware **conductor / decision engine for the workbench work-loop** (tools, specialists, MCP, cards) |

---

## Verdict

| | |
|---|---|
| Missing | M1–M14 (brain bounds, schema split, catalog≠context, failover rails, plan verify, demo freestyle map, Expected Solution proof vs one-card-many-tasks) |
| Overhyped | Ultimate brain = human/plant decider; knows everything = loads everything; schema validator = replaces gateway; one LLM = skip multi-model demo; failover = silent success |
| Confidence after freeze | **~0.86** → GO WP-21 (residual: freestyle map quality; failover modality hop) |

---

## Attack A — “Ultimate brain” vs WP-00 human

| Attack | Why fatal | Fix (freeze) |
|---|---|---|
| **A1** Orchestrator decides plant safety / FFS / MOC / statutory | Contradicts WP-00 Never + HITL | Orchestrator is **ultimate brain of the workbench loop** only — **never** ultimate plant/business decision-maker |
| **A2** “Ultimate” ⇒ bypass HITL / stale approval | WP-05 void | Orchestrator **must pause** on H*; material plan/tool/artefact change → stale rules still apply |
| **A3** “Ultimate” ⇒ rewrite Never on user ask | WP-00 | Never list still wins; orchestrator cannot grant Never |
| **A4** Marketing “brain” = jury thinks unsupervised autonomy | Expected Solution is assist + draft | Language in freeze: **Workbench Conductor** — capability-aware planner/router; human remains **ultimate verifier** |

**Decision:** Adopt DM intent (**orchestrator decides what the workbench does next**) with hard ceiling: **no safety/statutory autonomy; HITL/grants/Never bind it.**

---

## Attack B — “Has all information” = standing super-context

| Attack | Why fatal | Fix |
|---|---|---|
| **B1** Catalog of all tools/MCP/skills dumped into every prompt | Burns context; standing privilege; WP-07 progressive load | Orchestrator holds a **capability index** (metadata: ids, tags, allow flags). **Runtime load stays narrow** (WP-07) |
| **B2** “Knows MCP” ⇒ auto-enable any server | WP-08 allowlist + grant | Awareness ≠ enable; use still `grant ∩ allowlist` |
| **B3** Specialists share one mega memory because brain knows all | WP-07 no shared super-context | Parallel/sequential runs keep **isolated packs** (WP-21) |

**Decision:** **Capability registry / index** inside orchestration — not “everything always in context.”

---

## Attack C — “Schema validator” eats WP-09

| Attack | Why fatal | Fix |
|---|---|---|
| **C1** Orchestrator validates `/v1` wire schema and talks to GPU directly | Bypasses gateway auth/timeout/fail-closed | Orchestrator owns **workbench route schema** (job → specialist → card → tools plan). **WP-09** still validates outbound `/v1` requests |
| **C2** Invalid tool args silently “fixed” by brain | Privilege escalation via tool confusion | Tool calls must pass **tool schema ∩ grant**; fail-closed or HITL — no silent widen |

**Decision:** Dual schema layers — **route/plan schema (WP-06)** + **gateway `/v1` schema (WP-09)**. Orchestrator **produces** valid intents; gateway **enforces** wire.

---

## Attack D — Q1 demo freestyle vs org job id

| Attack | Why | Fix |
|---|---|---|
| **D1** Freestyle invents new privileges (“open all SOPs + shell”) | Grant/skill bypass | Map NL → **nearest approved job** under role; if none → **clarify or fail-closed**; never invent tools outside catalog |
| **D2** Demo freestyle ≠ org; jury confuses slices | Honesty | Document demo vs org; org **must** pick approved `job_id` |
| **D3** Ambiguous NL → wrong specialist (code vs inspect) | Wrong tools | Low-confidence map → ask user to confirm job (demo) / force picker (org) |

**Decision:** **D1 as DM.** Demo: freestyle with **constrained map**. Org: **job id required**.

---

## Attack E — Q2/Q3 capability routing vs Expected Solution

| Attack | Why | Fix |
|---|---|---|
| **E1** “One LLM does many tasks” ⇒ only one `model_id` forever | Fails Expected Solution auto-select proof | Catalog still ≥2 cards (WP-24). **Proof script** runs ≥2 task types that **select different** eligible cards. Day-to-day may reuse one capable card when tags allow |
| **E2** General LLM selected for OCR-only step | Bad extracts / WP-03 | Eligibility: modalities + `kind`/`task_tags` must match **step need**; OCR step prefers `ocr`/`vlm` when present |
| **E3** Worker cannot override bad route | Ops stuck | No worker override (DM). **Admin** card priority / disable. Failover (Q5). HITL stop |
| **E4** Capability score invented / opaque | Un-auditable | Selection = **deterministic policy** over card fields + step requirements; **reason string logged** (H10) |

**Decision:** Capability-based selection **yes**; specialized cards **preferred when eligible**; multi-model proof **preserved** via task-type diversity, not “force two cards every job.”

---

## Attack F — Q4 task-dependent parallel

| Attack | Why | Fix |
|---|---|---|
| **F1** “Depends on task” with no template = ad-hoc swarm | Super-context creep | Each approved job declares **topology**: `solo` \| `sequential` \| `parallel_join` |
| **F2** Parallel join merges secrets across grants | Leak | Join only **allowed artefact refs** under each grant; no raw shared brain |
| **F3** Demo accidentally parallel | WP-07 demo = one specialist | Demo topology forced **solo** |

**Decision:** Topology is a **job-template field** (rules), not free LLM whim. LLM may refine steps **inside** that topology (Q6).

---

## Attack G — Q5 auto-failover (high risk)

| Attack | Why | Fix |
|---|---|---|
| **G1** Failover to wrong modality (OCR → plain LLM) | Silent quality lie | Next card must remain **eligible for same step** (kind/modalities/tags) |
| **G2** Infinite failover hop | Latency / confusion | Cap **N** failovers per step (recommend **2**); then fail-closed |
| **G3** Failover hides outage from operator | Audience B | Log every attempt: from_id, to_id, error, reason |
| **G4** Failover mid-HITL bypasses stale | WP-05 | Failover that changes extract/draft path = **material** → re-HITL if gated artefact already accepted |
| **G5** Failover to cloud/HF | Never | Eligible = local enabled cards only |
| **G6** Failover changes params into unsafe range | | Params still ∩ task allow-list |

**Decision:** **Auto-failover yes**, with **same-step eligibility**, **cap**, **full log**, **HITL/stale respect**, **no cloud**.

---

## Attack H — Q6 rules + LLM correct + verification

| Attack | Why | Fix |
|---|---|---|
| **H1** LLM rewrites plan to add forbidden tools | Privilege | Verify plan against **job template rails**: allowed specialists/tools/skills only; reject illegal steps |
| **H2** “Verification” = another LLM saying OK | Circular | **Machine verify** = schema/rails check; **human verify** where HITL requires (plan material change ambition) |
| **H3** No temporary rules ⇒ pure LLM plan | Non-reproducible demo | Must-work: **rule/template skeleton first**; LLM may **amend** within rails |
| **H4** LLM “corrects” away OCR H1 or citations | WP-03/05/22 | Rails include mandatory gates (e.g. H1 before KB-as-truth); cannot strip |

**Decision:** **Rules-first skeleton + LLM refine + rails verification** (fail reject/re-ask). Human HITL unchanged for artefact gates.

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Brain ceiling | Workbench conductor ≠ plant decider |
| **M2** | Capability index vs context dump | Metadata index; narrow load |
| **M3** | Schema split | Route schema WP-06; `/v1` WP-09 |
| **M4** | Demo freestyle map rails | Map or clarify/fail-closed |
| **M5** | Org job id required | Hard |
| **M6** | Orchestrator-only card pick | Admin priority only |
| **M7** | Capability routing + proof script | One card many tasks OK; ≥2 ids when proving ≥2 types |
| **M8** | Step-level card eligibility | OCR/vision vs draft |
| **M9** | Job topology field | solo/sequential/parallel_join |
| **M10** | Failover rails | Same eligibility, cap, log, HITL |
| **M11** | Plan verify | Rails machine-check |
| **M12** | Grant revoke mid-loop | Stop / fail-closed |
| **M13** | Pass model_id+params | WP-24 D7 |
| **M14** | No packer bypass | WP-21 owns tokens |

---

## 2. Overhyped

| ID | Claim | Reality |
|---|---|---|
| **O1** Ultimate brain | **Software brain of KWB** (conductor); **human = ultimate verifier** (DM confirmed) |
| **O2** Knows all capabilities | Index, not full bodies |
| **O3** Schema validator | Route/plan + tool intent; not GPU wire alone |
| **O4** One LLM enough for PS | Enough for many runs; **not** enough to skip multi-model proof |
| **O5** Auto-failover = resilience done | Only with eligibility + cap + log |
| **O6** LLM verifies itself | Rails + HITL; not self-signed |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Capability-aware orchestrator as work-loop brain | Safety/FFS autonomy |
| Rules skeleton + LLM refine + rails verify | Unbounded LLM planner |
| Auto-failover within eligible set | Cross-modality silent hop; cloud failover |
| Demo freestyle → constrained map | Freestyle privilege invent |
| Org mandatory job id | Org freestyle as must-work |
| Deterministic logged card policy | Opaque “model vibes” routing |

---

## 4. Disposition

**Applied.** → `WP-06_FREEZE.md` rev **1.0a** (DM: software brain ≠ human verifier). Confidence **0.88**. **GO** → **WP-21**.

