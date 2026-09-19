# WP-22 Three-source claim verification — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-01 / WP-05 / WP-11 / WP-23. Reopen only if the decision maker explicitly says so.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-22_ARCHITECT_PERSPECTIVE.md`, `WP-22_REDTEAM.md`, **DM 2026-09-18** (H2 block on S1↔S3 until H7; policy↔user demo; NOT FOUND demo; material+cited scope; H7+audit user override; attach-only optional).  
**Findings SoT:** `WP-22_REDTEAM.md`  
**Product:** **KWB**

**Stack:** not locked. No runtime Ragas dependency.

---

## 1. One-sentence contract

Material grounded assertions in KWB are labelled by support from **file/evidence (S1)**, **user claim (S2)**, and **company policy (S3)**; **conflicts** and **`NOT FOUND`** are first-class; unresolved fights go to **H7** — the model must **not** silently reconcile — and **record-facing H2** stays blocked until conflicts required by this contract are resolved.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Three-source labels + H7 | LLM silent reconciler |
| `NOT FOUND` is success-path honesty | `NOT FOUND` = product failure |
| H7+audit user override of file | Override writes plant SoR |
| Material + cited spans | Every chat token scored |
| Attach-only may skip three-level | Fake policy cites without KB grant |
| Policy = corpus (WP-11) | Policy = system-prompt footer only |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | **S1↔S3 conflict** → block **record-facing H2** until **H7** resolves |
| **D2** | Must-work demo includes **policy vs user** conflict → H7 |
| **D3** | Must-work shows **`NOT FOUND`** |
| **D4** | Claim scope = **material findings + any cited assertion** |
| **D5** | User may prefer claim over file **only via H7 + audit**; **not** SoR write |
| **D6** | Attach-only / no KB grant → three-level **optional** (WP-01) |

---

## 4. Three sources

| ID | Source | Trust | Origin |
|---|---|---|---|
| **S1** | File / evidence | T2 extract and/or T3 file chunk | WP-03 / WP-11 |
| **S2** | User claim | T1 claim | Chat / form |
| **S3** | Company policy | T3 policy chunk | WP-11 `mock_policy` / org policy |

**Never list / system policy engine ≠ S3 corpus.** S3 must be citable policy text.

---

## 5. Claim unit & record

**In scope:** findings fields; any draft span that is a grounded plant/policy assertion; any span that carries a citation.

**Out of scope (default):** pure boilerplate template chrome; uncited chit-chat.

Minimum claim record fields:

| Field | Purpose |
|---|---|
| `claim_id` / span | Assertion |
| `support_S1` / `S2` / `S3` | Refs or null |
| `status` | `supported` \| `conflict` \| `not_found` \| `user_only` \| `human_resolved_*` |
| `conflict_pair` | When conflicting |
| `human_resolution` | H7 outcome + audit pointer |

---

## 6. Contradiction matrix (frozen)

| Situation | Behaviour |
|---|---|
| S1 ∧ S2 agree | Cite S1; S2 optional note |
| S1 ∧ S2 disagree | Surface conflict; default prefer **S1** for plant facts; user may win only via **H7+audit** (D5) → status `human_resolved_prefer_user` (file disagreement retained) |
| S3 ∧ S2 disagree | **H7 hard**; default prefer **S3** until human acts (D2 demo) |
| S1 ∧ S3 disagree | Surface; **no auto-pick**; **H7**; **H2 record-facing blocked** until resolved (D1) |
| Needed S1 missing | **`not_found`** (file) — do not invent |
| Needed S3 missing | **`not_found`** (policy) — do not invent |
| Only S2 | `user_only` — not file/policy grounded |

**Never:** silent friendliest-sentence merge across S1/S2/S3.

---

## 7. H2 / H7 binding

- Open `conflict` that this matrix marks as requiring H7 → **H7** must run.  
- While such conflict unresolved → **record-facing H2 accept denied**.  
- Worker may still edit DRAFT (H4b); accept stays blocked.  
- H7 audit: `person_id`, `role_class`, `claim_id`, source refs, choice, timestamp (WP-17 shape).

---

## 8. `NOT FOUND`

- Valid status and demo-required (D3).  
- Draft may continue with gap labels; must not fabricate S1/S3 text.  
- Prefer `NOT FOUND` over a wrong friendly sentence (WP-00 accuracy over speed).

---

## 9. Must / ambition / deferred / never

### Must-work

1. Three-source model + statuses.  
2. Matrix §6 + H2 block (D1).  
3. Policy↔user conflict demo + H7 (D2).  
4. `NOT FOUND` demo (D3).  
5. Scope = material + cited (D4).  
6. H7+audit override path (D5); no SoR write.  
7. Attach-only optional three-level (D6).  
8. No LLM-as-reconciler. Offline; slow OK.

### Org-ambition

- Full claim-pack export; richer support scoring; Approver queue for S1↔S3 at scale.

### Deferred

- Formal NLI prover; Ragas as runtime; legal discovery grade.

### Never

- Silent reconcile.  
- Invent file/policy on miss.  
- Policy-only-in-prompt as S3.  
- User claim as SoR.  
- H2 accept over open required conflict.  
- Override without H7/audit.

---

## 10. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | GBrain citation+gap *idea*; Atlas source/contradict/approve questions | Honesty |
| **Add** | Matrix; H2 block; demo conflicts; claim scope; audit fields | KWB / DM |
| **Refuse** | LLM reconciler gate; Ragas runtime must; fake cites on attach-only |

---

## 11. Demo acceptance

1. KB+policy path: file cite + policy cite + user claim labelled.  
2. Forced **policy vs user** conflict → H7 → resolution logged.  
3. **`NOT FOUND`** shown when evidence missing.  
4. S1↔S3 conflict → H2 accept **blocked** until H7.  
5. Attach-only run without three-level still allowed if labelled.

---

## 12. Boundary

| Topic | Later |
|---|---|
| Retrieve chunks | WP-11 (done) |
| Output filter polish | WP-12 |
| Eval suites | WP-18 |
| Context pack strings | WP-21 |
| Audit retention | WP-17 |

---

## 13. Next

**WP-07** — Tools, prompts, specialist agents.

---

## 14. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze from architect + red-team + DM answers |

**Confidence:** **0.88**
