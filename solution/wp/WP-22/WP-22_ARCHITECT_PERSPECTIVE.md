# WP-22 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-01 / WP-05 / WP-11 / WP-23  
**Status:** **SUPERSEDED by `WP-22_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-22_REDTEAM.md`.  
**Job of WP-22:** For grounded claims, require honest use of **three sources** — **(1) file/evidence**, **(2) user claim**, **(3) company policy** — with **contradiction** handling and valid **`NOT FOUND`**. Accuracy over speed. The LLM must **not** silently pick the friendliest sentence or act as the conflict gate.

**Sources:** WP-00 Q4; User three-level citation; Official Description grounding; WP-11 chunks + policy MOCK; WP-23 T1 claim / T3 file+policy; WP-05 H7; repo map GBrain citation+gap; Lewis 2020 (retrieve ≠ verify).

---

## One sentence (proposed)

Every important grounded statement in a KWB draft is labelled by **which of the three sources support it** (file, user claim, policy), surfaces **conflicts** and **gaps** (`NOT FOUND`), and sends unresolved policy↔user fights to **H7** — never “the model decided.”

---

## 1. Three sources (do not collapse)

| # | Source | What it is | Trust (WP-23) | Comes from |
|---|---|---|---|---|
| **S1 File / evidence** | Controlled or task evidence text with citation | T2 extract and/or T3 retrieved chunk | WP-03 H1 extract; WP-11 retrieve |
| **S2 User claim** | What the human asserted in chat / form | **T1 claim** — not plant fact | User utterance |
| **S3 Company policy** | Policy corpus chunk + citation | T3 | WP-11 `mock_policy` / org policy |

**System prompt / Never list ≠ S3.** Policy is a **corpus**, not a footer.

---

## 2. What WP-22 owns vs not

| Owns | Does not own |
|---|---|
| Claim labelling rules; conflict matrix; `NOT FOUND` / gap artefacts | Authz-first retrieve (**WP-11**) |
| When to raise **H7** | H7 UI gate mechanics (**WP-05**) |
| Demo three-level pack structure | Full Ragas runtime eval (**WP-18**) |
| Refusal to silent-reconcile | Output security filter polish (**WP-12**) |

---

## 3. Claim record (proposed shape — brand-free)

For each material claim in a draft (or claim pack):

| Field | Purpose |
|---|---|
| `claim_id` / text span | What was asserted |
| `support_S1` | chunk_ids / extract refs or null |
| `support_S2` | user utterance refs or null |
| `support_S3` | policy chunk_ids or null |
| `status` | `supported` \| `conflict` \| `not_found` \| `user_only` \| `policy_blocked` |
| `conflict_pair` | Which sources disagree |
| `human_resolution` | H7 outcome when required |

Bare Expected Solution without KB grant may omit full three-level (WP-01); **when KB + policy path active**, three-level applies.

---

## 4. Contradiction policy (proposed defaults — decide)

| Situation | Proposed behaviour |
|---|---|
| S1 present, S2 agrees | OK — cite file; user claim optional note |
| S1 present, S2 disagrees | Surface conflict; **prefer S1 for plant facts**; do not silently adopt S2; H7 if user insists |
| S3 vs S2 disagree | **H7 hard** (WP-05); default prefer **policy** until human chooses/escalates |
| S3 vs S1 disagree | Surface conflict; **do not auto-pick**; H7 / Approver if record-facing |
| Needed S1 missing | **`NOT FOUND`** (file) — do not invent SOP text |
| Needed S3 missing | **`NOT FOUND`** (policy) — do not invent policy |
| Only S2 | Label **user_only** — not file/policy grounded |

**Never:** “LLM reconciles conflicts” as the gate (repo map refuse).

---

## 5. `NOT FOUND` (valid output)

- First-class status, not a failure of the product.  
- Shown in UI / citation pack / draft footnote as appropriate.  
- Accuracy over speed: better `NOT FOUND` than a friendly wrong sentence (WP-00).

---

## 6. Must-work demo path

When KB grant + policy MOCK active (WP-11):

1. Retrieve file chunk + policy chunk (T3).  
2. Include a user claim (T1) that **agrees** or **conflicts** (MOCK).  
3. Show labels: file cite, policy cite, user claim.  
4. On conflict → **H7** MOCK banner / choose-escalate.  
5. On missing file evidence → **`NOT FOUND`**.  
6. No silent friendliest-sentence merge.

Attach-only inspect-to-note without KB grant: three-level not required (WP-01).

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Three-source model + claim status vocabulary.  
2. Conflict surfacing; no silent reconcile.  
3. `NOT FOUND` valid.  
4. H7 on policy↔user (and S3↔S1 when record-facing / demo conflict).  
5. Prefer file over user for plant facts until human overrides via H7.  
6. Prefer policy over user until H7.  
7. Demo with MOCK file+policy+claim when KB path on.  
8. Slow OK; offline.

### Org-ambition

- Rich claim pack export; Approver queue for S1↔S3; automated support scoring; Ragas-style eval suites (WP-18).

### Deferred

- Formal logic prover; legal e-discovery grade.

### Never

- LLM as silent conflict decider.  
- Policy only in system prompt (no corpus).  
- Invent file/policy when `NOT FOUND`.  
- Treat user claim as SoR.  
- Collapse three sources into one “context” blob without labels.

---

## 8. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | GBrain citation + gap *idea*; Atlas “what source / contradict / who approves” |
| **Add** | Status vocabulary; conflict matrix; H7 binding; `NOT FOUND`; demo path |
| **Refuse** | LLM-as-reconciler gate; Ragas as runtime dependency |

---

## 9. Open questions for decision maker

1. **S1 vs S3 conflict default:** hold draft + **H7 always**, or allow draft with dual cites + warning until H2? (Recommend: **block record-facing accept until H7**.)  
2. **Must-work conflict demo:** force one **policy vs user** conflict in jury script — **yes**?  
3. **`NOT FOUND` demo:** required showable in must-work — **yes**?  
4. **Claim packing:** every sentence vs only **material findings** / flagged spans? (Recommend: **material findings + any cited assertion**.)  
5. **User overrides file (S2 wins) after H7:** allowed with audit, or **Never** for plant facts? (Recommend: **allowed only via H7 + audit**, still not SoR write.)  
6. **Attach-only path:** keep three-level **optional** (WP-01) — confirm **yes**?

---

## 10. Next after your decisions

**Done.** Frozen as `WP-22_FREEZE.md` rev 1.0. Next: **WP-07**.
