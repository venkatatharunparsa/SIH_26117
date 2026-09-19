# WP-06 Orchestration + task routing — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0a**). Binding with WP-00 / WP-04 / WP-05 / WP-07 / WP-24 (and WP-03 path split).  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-06_ARCHITECT_PERSPECTIVE.md`, `WP-06_REDTEAM.md`, **DM 2026-09-18** (demo freestyle / org job id; orchestrator-only model pick; capability-based routing; task-dependent topology; auto-failover; rules+LLM+verify; orchestrator as workbench conductor).  
**Findings SoT:** `WP-06_REDTEAM.md`  
**Product:** **KWB**

**Stack / agent framework:** not locked.

---

## 1. One-sentence contract

The **orchestrator** is the **software brain of KWB**: the capability-aware **Workbench Conductor** that decides **what the application does next** (jobs → specialists → skills → tools/MCP → **Model Cards** → plan/iterate/stop) and alone chooses which **`model_id` + params** to pass — bound by **grants, HITL, Never, and rails**. The **human** remains the **ultimate verifier** and plant/business decision-maker (WP-00 / WP-05). Orchestration is **not** a bypass of WP-09 gateway or WP-21 packing.


---

## 2. Limits (anti-overclaim)

| True | False / refuse |
|---|---|
| **Software brain** of the KWB application / work-loop | **Ultimate verifier** of plant safety / FFS / statutory / commercial outcomes (that is the **human**) |
| Holds **capability index** (tools, specialists, MCP, cards, job templates) | Loads **all** skill/tool bodies into every context |
| Owns **route/plan schema** + tool-intent checks | Replaces WP-09 `/v1` wire validation |
| May refine plans with LLM | Unbounded planner that adds forbidden tools |
| Auto-failover within eligible cards | Silent hop to wrong modality or cloud |
| One capable card may serve many steps | Skip Expected Solution ≥2-model proof |

---

## 3. Closed decisions (DM + red-team)

| ID | Decision |
|---|---|
| **D1** | **Demo:** freestyle NL allowed → **constrained map** to approved jobs (clarify or fail-closed if unknown). **Org:** **approved `job_id` required** |
| **D2** | **Orchestrator-only** Model Card selection; workers do not override; Admin sets priorities / enablement (WP-24) |
| **D3** | **Capability-based** routing: match **step requirements** to card `kind` / `modalities` / `task_tags`; a strong multimodal LLM may cover multiple steps **when eligible** — specialized `ocr`/`vlm` preferred for understand steps when present |
| **D4** | Parallel vs sequential is **task-dependent** via job-template **topology**: `solo` \| `sequential` \| `parallel_join` |
| **D5** | **Auto-failover** to next **same-step-eligible** card; **cap 2** failovers per step; then fail-closed; full log; no cloud; respect HITL/stale |
| **D6** | **Rules/template skeleton first**; LLM may **correct/refine** plan; **rails verification** must pass before execute |
| **D7** | Orchestrator = **software brain** of KWB (Workbench Conductor); **human = ultimate verifier** — red-team M1–M14 ceilings apply |
| **D8** | Expected Solution proof: when demonstrating auto-select, run **≥2 task types** that yield **≥2 distinct `model_id`s** in the log (catalog ≥2 — WP-24) |
| **D9** | DM confirm 2026-09-18: red-team split is correct — software brain ≠ human verifier |

---

## 4. Conductor vs everyone else

| Layer | Orchestrator does | Does not |
|---|---|---|
| **Human (WP-00/05)** | Pause for H*; honour stale/re-approve | Replace Approver/Admin — **human is ultimate verifier** |
| **WP-07** | Apply role×task → skill → specialist matrix | Invent skills/tools outside catalog |
| **WP-24** | Select enabled card; pass `model_id`+params | Fork UI per brand; embed weights |
| **WP-21** | Request minimize-to-grant / step needs | Assemble raw token soup itself |
| **WP-09** | Emit intended `/v1` call params | Skip gateway; rewrite public `base_url` |
| **WP-08/16** | Dispatch allowed tool/MCP/sandbox calls | Auto-allowlist new MCP; escape jail |
| **WP-04** | Run only under active grant; stop on revoke | Treat session login as standing grant |

---

## 5. Capability index (not super-context)

Orchestration maintains (or queries) a **capability index**:

- Approved **job templates** (id, topology, rails, mandatory gates)  
- **Specialists** + **skill** metadata (not full bodies until load)  
- **Built-in tools** + **MCP** ids from allowlist (not all descriptions always in prompt)  
- **Model Cards** (WP-24 fields)  

**Runtime** still progressive-loads skill bodies and packs context per WP-07 / WP-21. Awareness ≠ privilege.

---

## 6. Control loop (frozen)

```
Intake
  Demo: NL and/or job id → map to approved job (clarify / fail-closed)
  Org:  job_id required
  → grant check (WP-04)
  → load job template: topology + rails + default specialist/skills
  → build plan skeleton (rules)
  → optional LLM refine → rails verify (reject illegal steps)
  → for each step:
        select card (capability match) → log reason
        pack (WP-21) → gateway (WP-09) with model_id+params
        tools under grant ∩ skill ∩ allowlist
        on unserveable/fail: failover ≤2 eligible cards else fail-closed
        HITL pauses as required; material change → stale (WP-05)
  → stop: success | deny | revoke | iteration cap | fail-closed
  → workspace DRAFT only — human owns plant record
```

**Demo topology:** force **`solo`** (one specialist) even if org templates allow parallel.  
**Org:** honour template topology; `parallel_join` merges only allowed artefact refs — **no shared super-context**.

---

## 7. Card selection + failover

### 7.1 Selection

1. Eligible = enabled ∧ open_weight ∧ local endpoint ∧ modalities/kind match **this step**.  
2. Score/order by `task_tags` ∩ step need + Admin priority.  
3. Deterministic tie-break; **reason logged** (H10).  
4. Pass `model_id` + `param_defaults` ∩ task allow-list.

### 7.2 Failover (D5)

| Rule | Must |
|---|---|
| Trigger | Unserveable, gateway fail-closed for that id, or hard runtime error — **not** “I disliked the answer” without policy |
| Next card | Must be eligible for **same step** |
| Cap | **2** failovers / step; then fail-closed |
| Log | `from_id`, `to_id`, error, reason |
| HITL | If failover changes a gated artefact path after accept → **stale / re-approve** |
| Never | Cloud/HF; cross-modality silent substitute when tagged specialist card exists and is enabled |

---

## 8. Plan: rules + LLM + verification (D6)

| Stage | Owner |
|---|---|
| Skeleton | Job template / temporary rules (deterministic) |
| Refine | LLM **may** amend steps, wording, order **within rails** |
| Verify | **Machine:** schema + allowed specialists/tools/skills + mandatory gates (e.g. cannot strip H1 before KB-as-truth). Fail → reject refine / revert skeleton |
| Human | Unchanged HITL on artefacts (WP-05); plan-only HITL = ambition unless material |

**Never:** LLM self-approves illegal plan; “verification” = another unchecked LLM rubber-stamp alone.

---

## 9. Intake (D1)

| Scale | Rule |
|---|---|
| **Demo** | Freestyle OK → map to approved job; low confidence → ask confirm; cannot invent tools/sources |
| **Org** | UI/API requires **approved `job_id`**; freestyle alone is not must-work |

Mapped `job_id` / `task_type` always written to the route log (even when user typed NL).

---

## 10. Logging (must-work)

| Field | Required |
|---|---|
| `job_id` / `task_type` | Yes |
| `topology` | Yes |
| `specialist_id` / `skill_ids` | Yes |
| `model_id` + selection reason | Yes |
| failover chain | If any |
| `grant_id` | Yes |
| iteration + stop reason | Yes |
| plan version / verify result | Yes |

Dropdown ≠ auto-select proof. **Log** is proof.

---

## 11. Must / ambition / deferred / never

### Must-work

1. Conductor loop with D1–D8.  
2. Capability index + narrow runtime load.  
3. Orchestrator-only card select + param pass (model-agnostic workbench).  
4. Rules skeleton + LLM refine + rails verify.  
5. Auto-failover with eligibility, cap 2, log.  
6. Honour grant revoke + HITL/stale; no safety autonomy.  
7. Auto-select demonstrable per D8.  
8. Demo solo specialist; org topology per template.

### Org-ambition

- Learned routing weights; richer DAG planner; explicit plan HITL; Admin simulation of routes.

### Deferred

- Multi-day unsupervised campaigns; self-modifying orchestrator code.

### Never

- Safety / FFS / statutory / legal / commercial autonomy.  
- Bypass Never / HITL / grants because “brain decided.”  
- Cloud/HF failover.  
- Standing full-tool super-context.  
- Skip WP-09 or WP-21.  
- Freestyle privilege invention.  
- Treat one general LLM as excuse to omit multi-model proof.

---

## 12. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Thin conductor + specialists pattern | WP-07 |
| **Add** | Capability index; job topology; failover rails; rules+LLM+verify | DM / red-team |
| **Refuse** | Mega-agent safety officer; swarm shared brain; gateway bypass; opaque vibe routing |

---

## 13. Demo acceptance

1. Freestyle demo maps to a known job without granting extra tools.  
2. Org path rejects missing `job_id`.  
3. Proof script: ≥2 task types → ≥2 `model_id`s logged with reasons.  
4. Kill primary card mid-step → failover ≤2 → success or fail-closed; log shows chain.  
5. LLM plan refine that adds forbidden tool → **rejected** by rails.  
6. HITL pause still blocks; revoke stops loop.  
7. No public `base_url` / HF.

---

## 14. Next

**WP-21** — Context assembly / data-to-pass (orchestrator requests; packer enforces).

---

## 15. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial pass on conductor / failover / plan-verify |
| **1.0a** | DM confirm: orchestrator = **software brain**; human = **ultimate verifier** |

**Confidence:** **0.88**
