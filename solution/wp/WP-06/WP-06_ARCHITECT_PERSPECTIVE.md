# WP-06 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-01 / WP-04 / WP-05 / WP-07 / WP-03 / WP-24 (and WP-16/08 as tool/host slots already frozen)  
**Status:** **SUPERSEDED by `WP-06_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-06_REDTEAM.md`.  
**Job of WP-06:** **Orchestration + task routing** — classify/map the user job → specialist(s) + skill(s) + **registered Model Card**; **plan** multi-step work; **iterate** within WP-07 limits; **pass `model_id` + params** into the gateway path; **never** exercise safety/FFS/statutory autonomy; leave **what tokens enter the model** to WP-21.

**Sources:** Official Description (auto-pick model; plan; iterate) + Expected Solution (≥2 task types → auto-select proof); WP-00 Intelligent layer; WP-07 orchestrator/specialist split + D3/D4/D6/D7; WP-24 D7 model-agnostic + card selection; WP-04 grants; WP-05 HITL; WP-03 OCR≠draft model; User “smart routing”; agenda red-team (route ≠ pack).

---

## One sentence (proposed)

The **orchestrator** owns the job loop: map task → **role×skill×specialist×card**, plan steps, call tools under the **grant**, iterate until stop/HITL/fail-closed, and **always** emit `model_id` (+ params) so the rest of KWB stays **model-agnostic** — it does **not** decide plant safety and does **not** assemble the full prompt (WP-21).

---

## 1. Ownership split (critical)

| Concern | Owner | Not owner |
|---|---|---|
| Job accept / plan / iterate / stop | **WP-06 orchestrator** | Specialist inventing plant policy |
| Role×task → skill → tools | **WP-07** matrix (orchestrator **applies**) | Free-form “any skill” |
| Which **Model Card** | **WP-06** using WP-24 catalog | UI feature forks per brand |
| What **tokens / citations / tool blobs** enter request | **WP-21** | Orchestrator dumping whole files |
| Schema-valid `/v1` call | **WP-09** | Orchestrator talking CUDA |
| Load/unload VRAM | **WP-10** | Orchestrator |
| Safety / FFS / statutory “approve as safe” | **Human + HITL (WP-05)** | Orchestrator / model |

**WP-00:** Intelligent layer = route by task + decide what data to pass. Agenda split already: **route here; pack in WP-21**. Orchestrator may **request** minimize-to-grant; packer enforces.

---

## 2. Control loop (proposed)

```
User job (typed or selected job id)
  → grant check (WP-04) — fail closed if missing
  → task map: job_id / task_type → skill(s) + specialist(s)  [WP-07 D7]
  → card select: enabled cards ∩ task_tags ∩ modalities  [WP-24]
  → emit route record: {job_id, specialist_id, skill_ids, model_id, param_defaults…}
  → plan steps (structured, logged)
  → loop (≤ max_iterations, WP-07 D3):
        pack context (WP-21) → gateway (WP-09) with model_id+params
        → tool calls under grant ∩ skill ∩ allowlist
        → HITL pause if H* triggered (WP-05) — material change may need re-approve
        → stop on done / deny / fail-closed / iteration cap
  → artefact in workspace DRAFT (WP-01) — human owns plant record
```

**Demo slice (WP-07):** one task → one specialist; single `model_id` OK **except** when the script is proving Expected Solution auto-select (≥2 task types → ≥2 ids in log).

**Org:** may dispatch **parallel specialists** (WP-07 D6) with **no shared super-context** — each run has its own grant-scoped pack.

---

## 3. Task mapping (proposed)

| Input | Behaviour |
|---|---|
| User selects **approved job id** (e.g. `inspect-to-note`, `code-sandbox`) | Prefer — deterministic map via WP-07 matrix |
| Freestyle natural language | Map to nearest approved job **or fail-closed** / ask clarify (align WP-07 D7) — **not** invent new privilege |
| Unknown / out-of-catalog | Fail-closed or HITL “request new job” — no silent elevate |

Classifier for **sensitivity** already exists as WP-00/04 concern; WP-06 must **not** treat classifier output as “approved to run dangerous tools.”

---

## 4. Model card selection (implements WP-24 D7)

| Rule | Must |
|---|---|
| Eligible set | `status=enabled` ∧ `open_weight` ∧ local `endpoint_ref` ∧ modalities match task |
| Preference | Card `task_tags` ∩ job needs (e.g. `coding`, `ocr`, `summary`, `vision`) |
| OCR / ingest path | Prefer **`ocr` / `vlm`** kind for understand steps (WP-03) |
| Draft / agent LLM path | Prefer **`llm`** (≠ OCR card) when writing notes/code |
| Tie-break | Deterministic policy (Admin order / priority field) — **logged** |
| No eligible card | **Fail closed** — no cloud rewrite |
| User override dropdown | Optional UX; **not** the Expected Solution proof |
| Workbench UI | **Unchanged** by which card wins (WP-24) |

Orchestrator **passes** at least: `model_id`, generation params from card `param_defaults` ∩ task policy allow-list. Exact allow-list not brand-locked.

**Org (WP-07 D4):** when ≥2 suitable cards exist, prefer **distinct** ids across different task types in the routing log.  
**Demo:** single id OK unless running the auto-select proof script.

---

## 5. Plan + iterate (not one-shot)

| | Must-work |
|---|---|
| Plan | Multi-step plan object logged before/during run |
| Iterate | Tool → observe → continue within **max_iterations** (default **5**, editable ≤ Admin max — WP-07 D3) |
| Stop reasons | Success; HITL deny; grant revoke; iteration cap; missing card/tool; gateway fail-closed |
| Re-plan | Allowed on tool failure / HITL amend; **material change → re-HITL** (WP-05) |
| Safety autonomy | **Never** — no “plant is safe / approve MOC / clear FFS” as a machine decision |

---

## 6. What WP-06 must log (demo + org)

For Expected Solution / Audience B monitors:

| Field | Why |
|---|---|
| `job_id` / `task_type` | Prove coding ≠ summary ≠ vision routes |
| `specialist_id` | WP-07 |
| `skill_ids` | Progressive load proof |
| `model_id` | Auto-select proof (≥2 task types → ≥2 ids when demonstrating) |
| `iteration` / stop reason | Agentic, not one-shot |
| `grant_id` | WP-04 |

Dropdown clicks ≠ proof. Log is proof (WP-00 / WP-24).

---

## 7. Boundaries (do not steal)

| Topic | Later / other WP |
|---|---|
| Token packing, citation injection, tool-result truncation | **WP-21** |
| `/v1` schema, timeout, auth | **WP-09** |
| VRAM load policy | **WP-10** |
| Exact HITL gate list | **WP-05** (orchestrator only **honours** pauses) |
| Sandbox internals | **WP-16** |
| MCP host install | **WP-08** |
| Eval golden tasks for routing | **WP-18** |

---

## 8. Must / ambition / deferred / never (proposed)

### Must-work

1. Task → specialist + skill(s) via WP-07 matrix (fail-closed unknown).  
2. Card selection from WP-24 catalog; pass `model_id` + params; workbench stays agnostic.  
3. Plan + iterate ≤ max_iterations; stop reasons logged.  
4. Auto-select **demonstrable**: ≥2 task types → ≥2 `model_id`s in log when proof script runs.  
5. OCR/understand vs draft LLM can be different cards on one job (multi-step route).  
6. Honour grant revoke mid-loop; honour HITL pauses; no safety autonomy.  
7. Demo: one specialist path; org: parallel specialists allowed without shared super-context.

### Org-ambition

- Richer planner (DAG); learned routing weights; Admin priority UI; multi-card A/B.

### Deferred

- Fully autonomous multi-day workflows; self-modifying orchestrator code.

### Never

- Safety / FFS / statutory decision autonomy.  
- Cloud / HF fallback on missing card.  
- Dump whole corpus past grant (pack is WP-21; orchestrator must not bypass).  
- Per-model workbench forks.  
- Treat user dropdown as the auto-select proof.  
- Unlock tools outside skill ∩ grant ∩ allowlist.

---

## 9. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Thin orchestrator + specialists (OpenHands/DeerFlow *pattern*) | Fits WP-07 |
| **Adopt** | Logged route record as product proof | Expected Solution |
| **Add** | Explicit card selector + param pass; job-id map; OCR≠draft route | WP-24 / WP-03 |
| **Refuse** | Single mega-agent with standing full tool access; swarm super-context; model-as-safety-officer |

Stack / framework brand **not** locked.

---

## 10. Demo vs org (routing)

| | Demo | Org |
|---|---|---|
| Specialists | One per run | Parallel OK |
| Models | Single OK; **proof script** uses ≥2 cards / ≥2 task types | Prefer distinct ids when eligible |
| Freestyle NL | Narrow or force job picker | Map or fail-closed |
| Planner depth | Short plan OK | Richer ambition |

---

## 11. Open questions for decision maker

1. **Task intake:** Must users **pick an approved job id** for must-work, or may freestyle NL auto-map (with fail-closed on unknown)?  
2. **Card override:** Allow worker **manual model override** (logged), or **orchestrator-only** selection (Admin may still set priorities)?  
3. **Same job, two cards:** On `inspect-to-note`, must OCR/VLM step and draft-LLM step use **different cards when available** (recommended for proof), or one card for whole job OK?  
4. **Parallel org runs:** When two specialists run, is orchestration **fan-out then join** (barrier before final draft) or **sequential handoff** only for must-work?  
5. **Re-route mid-job:** If first card fails (unserveable), **auto-failover** to next eligible card (logged) or **fail-closed** immediately?  
6. **Planner authority:** Is the plan **rules/template-first** (deterministic steps per job id) with LLM only filling step content, or may the **LLM propose the plan** under rails?

---

## 12. Next after your decisions

**Done.** Frozen as `WP-06_FREEZE.md` rev 1.0. Next at freeze time: **WP-21** (now frozen). **Current walk:** **WP-09**.
