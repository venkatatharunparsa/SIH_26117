# WP-17 Audit and evidence log — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-04 / WP-05 / WP-06 / WP-08 / WP-09 / WP-11 / WP-12 / WP-21 / WP-24.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-17_ARCHITECT_PERSPECTIVE.md`, `WP-17_REDTEAM.md`, **DM 2026-09-18** (jury-day demo retention; full own-task list; in-app must-work; download/edit parsed; PII yes→id+MOCK name; trusted clock runbook; fail-closed).  
**Findings SoT:** `WP-17_REDTEAM.md`  
**Verify SoT:** `WP-17_FREEZE_VERIFY.md`  
**Product:** **KWB**

**SIEM / DB brand:** not locked.

**Spec cites (shape, not certification):**  
- CERT-In Directions **No. 20(3)/2022-CERT-In** (28 April 2022): enable ICT logs; retain securely **rolling 180 days**; maintain within Indian jurisdiction / producible to CERT-In.  
- CERT-In FAQs on Cyber Security Directions (May 2022): record **successful and unsuccessful** events; indicative log types.  
- DPDP Act, 2023: org personal-data handling = **compliance track** — demo MOCK ≠ “DPDP certified.”

---

## 1. One-sentence contract

KWB keeps an **append-only evidence log** of consequential actions (**person, task, grant, model_id, tools/MCP, retrieve revisions, HITL, gates, export**) so auto-select and approvals are **reconstructible**; Workers may **view full own-task events in-app**; **nobody edits history**; audit write failure **fail-closes** privileged actions; org retention is **180-day-shaped**; demo may keep **jury-day only**.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Append-only evidence | Worker-editable audit history |
| In-app view must-work | Must-work off-box log download |
| “Editable” = filter/search UI | Mutate/delete/re-import events as truth |
| Jury-day demo retention | Jury-day = org CERT-In retention |
| CERT-In-**shaped** 180d org | “CERT-In compliant” badge without legal review |
| person_id + optional MOCK display_name | Government ID / secrets in event bodies |
| Fail-closed on audit I/O fail | Drop audit and continue privileged I/O |

---

## 3. Closed decisions (DM + red-team parse)

| ID | Decision |
|---|---|
| **D1** | **Demo retention:** jury-day window only. **Org:** ≥ **rolling 180 days** (CERT-In-shaped) |
| **D2** | Workers see **full own-task** structured event list (scoped to self) |
| **D3** | **Must-work access:** in-app view only. Admin **read-only download** = ambition. **Never** editable events — only query/filter UI |
| **D4** | Every event has **person_id** (or `system`); demo may show **MOCK display_name**; no gov IDs / raw secrets in bodies |
| **D5** | **Runbook trusted clock** before operation/jury; no public NTP **during** air-gapped run |
| **D6** | Audit append failure → **fail-closed** privileged action (+ Admin alarm) |
| **D7** | Log **success and failure**; **model_id** mandatory on route/gateway inference events |

---

## 4. Log vs monitor vs SoR

| | Role |
|---|---|
| **WP-17 log** | Durable append-only events |
| **WP-13 monitors** | Live visible subset |
| **Plant SoR** | Never |
| **Chat** | Not a substitute |

---

## 5. Minimum event families (must)

| Family | Must include |
|---|---|
| Session | login / logout / idle_timeout |
| Grant | created / expanded / denied / revoked / expired; action_allowed / action_denied |
| Route | job_id, specialist_id, skill_ids, **model_id**, reason, failover chain |
| Gateway | request_id, allow/deny, reason code |
| Pack | PackManifest **refs** (sizes/ids/flags — not secret bodies) |
| Retrieve | chunk_id, source_id, revision or revision_unknown, grant_id |
| HITL | gate_id, accept/reject/stale/re-approve, role_class, artefact_id+version |
| Gates | gate_id, pass/fail (GateReport) |
| Tools/MCP | plugin/tool id, allow/deny, grant_id |
| Sandbox | report ref, pass/fail |
| Export | H3 allow/deny, package/artefact version refs |
| Card admin | add/enable/disable/remove |
| Audit health | audit_write_failed (best-effort) |

**Common fields:** `event_id`, `ts`, `person_id`, `task_id?`, `grant_id?`, `outcome`.

---

## 6. Retention & access

| | Demo | Org |
|---|---|---|
| Retain | **Jury-day** (no mid-demo wipe) | **≥180 days rolling** |
| Worker | Full **own-task** events in-app | Same + class minimization |
| Approver | Tasks they act on | Same |
| Admin | Full demo log in-app | Full + incident export ambition |
| Download | Not must-work | Read-only bundle ambition; **not** re-importable as log SoR |

---

## 7. Integrity & failure

- Append-only store; Worker has **no** update/delete.  
- Privileged action path: write audit event(s) **or fail closed**.  
- View/filter existing log does not require a new privileged grant action.  
- Hash-chain = org-ambition.

---

## 8. Must / ambition / deferred / never

### Must-work

1. Append-only log with §5 families (thin MOCK OK except **model_id**, HITL, grant, gateway deny).  
2. Auto-select: ≥2 task types → ≥2 model_ids queryable.  
3. Own-task full list in-app; role scope enforced.  
4. Jury-day demo retention; org 180d shape in design.  
5. Trusted-clock runbook; fail-closed on audit write fail.  
6. Success + fail events; no raw secrets in bodies.  
7. CERT-In cited as **shape only**.

### Org-ambition

- Admin read-only download; hash-chain; SIEM; Auditor role; DPDP operationalization; >180d cold store.

### Deferred

- Automated CERT-In incident filing; ISO packs.

### Never

- Editable/deletable audit by Workers.  
- Re-import downloaded file as authoritative log.  
- Cloud log ship as must-work.  
- “CERT-In/DPDP certified” marketing without legal review.  
- Log as plant SoR.  
- Skip model_id on inference route events.

---

## 9. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Append-only audit; CERT-In 180d **shape**; success+fail | Spec + Expected Solution |
| **Add** | Event catalogue; fail-closed; own-task UI; jury vs org retention | DM / red-team |
| **Refuse** | Mutable history; chat-only audit; compliance badge theatre |

---

## 10. Demo acceptance

1. Run two task types → log shows **two model_ids**.  
2. Revoke grant → deny event present; Worker sees it on own task.  
3. H2 accept + H3 deny (secret) both logged.  
4. Stop audit disk / inject write fail → privileged action **blocked**.  
5. Worker cannot edit/delete events; can filter view.  
6. No public NTP call during air-gapped demo run.

---

## 11. Next

**WP-14** — Task–version lineage store.

---

## 12. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze + CERT-In cite + Q3 editable parsed as filter-only |

**Confidence:** **0.88**
