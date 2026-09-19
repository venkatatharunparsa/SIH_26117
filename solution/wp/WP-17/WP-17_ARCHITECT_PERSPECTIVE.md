# WP-17 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-04 / WP-05 / WP-06 / WP-08 / WP-09 / WP-11 / WP-12 / WP-21 / WP-24 (WP-14 consumes this log; WP-13 displays subsets)  
**Status:** **SUPERSEDED by `WP-17_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-17_REDTEAM.md`. Verify: `WP-17_FREEZE_VERIFY.md`.  
**Job of WP-17:** **Audit and evidence log** — append-only record of **who / what task / which grant / which model card / which tools·plugins / what was retrieved (revisions) / HITL / gates / export**, with **retention** and **who may read** — enough to prove auto-select, reconstruct incidents, and feed lineage (WP-14). Not plant SoR. Not a SIEM product brand lock.

**Sources:** Official Expected Solution (logs or visible monitor; model auto-select in log); WP-00 Audit + two-model log proof; WP-04 grant events; WP-05 gate audit fields; WP-09 `request_id` + deny codes; WP-12 GateReport; WP-21 PackManifest; follow-list (cite CERT-In at freeze).  
**Spec cite (for freeze — verify against PDF):** CERT-In Directions **No. 20(3)/2022-CERT-In** (28 Apr 2022) § enabling ICT logs, secure retention **rolling 180 days**, Indian jurisdiction / producible to CERT-In — **shape** for org retention; **not** a claim that KWB is CERT-In certified. FAQ May 2022: successful **and** unsuccessful events; log types indicative.  
**DPDP:** Digital Personal Data Protection Act, 2023 — org data-handling for personal data in logs = **ambition/compliance track**; demo MOCK users OK; do not invent MRPL DPIA here.

---

## One sentence (proposed)

KWB writes an **append-only evidence log** so every consequential action is reconstructible: **person, task, grant, model_id, tools, retrieve revisions, HITL, gates, export** — retained per org policy (**180-day-shaped** minimum for org ICT-style logs), readable only by allowed roles, and **never** treated as the plant system of record.

---

## 1. Why this WP exists

| Without it | Failure |
|---|---|
| “We auto-selected models” | Slideware — Expected Solution wants **ids in the log** |
| HITL / export dispute | No who-approved-which-version |
| Incident / revoke | Cannot prove deny-after-revoke |
| WP-14 lineage | No event spine to hang versions on |

---

## 2. Log vs monitor vs SoR

| Artefact | Role |
|---|---|
| **Audit / evidence log (WP-17)** | Durable append-only events |
| **Monitors (WP-13)** | Live / visible subset for Audience A/B |
| **Plant SoR** | Never — log is KWB evidence only |
| **Chat transcript** | Not a substitute for structured events |

---

## 3. Minimum event families (proposed must)

| Family | Examples (ids brand-free) |
|---|---|
| **Identity / session** | login, logout, idle_timeout |
| **Grant** | grant_created / expanded / denied / revoked / expired; action_allowed / action_denied (WP-04) |
| **Route** | job_id, specialist_id, skill_ids, **model_id**, selection reason, failover (WP-06) |
| **Gateway** | request_id, allow/deny + reason code (WP-09) |
| **Pack** | PackManifest summary refs (WP-21) — not full secret bodies |
| **Retrieve** | chunk_id, source_id, revision/revision_unknown, grant_id (WP-11) |
| **HITL** | gate_id, accept/reject/stale/re-approve, person_id, role_class, artefact_version (WP-05) |
| **Gates** | GateReport pass/fail per gate_id (WP-12) |
| **Tools / MCP** | tool/plugin id, allow/deny, grant_id (WP-08) |
| **Sandbox** | job id, pass/fail, report ref (WP-16) |
| **Export** | H3 allow/deny, package hash / artefact versions |
| **Card admin** | card add/enable/disable/remove (WP-24) |
| **Air-gap evidence** | optional pointer to host monitor snapshot id (WP-13) |

**Common fields (every event):** `event_id`, `ts`, `person_id` (or system), `task_id` (if any), `grant_id` (if any), `severity`/`outcome`.

**Successful and unsuccessful** both logged (align CERT-In FAQ flavour).

---

## 4. Retention & storage (proposed)

| Scale | Retention | Location |
|---|---|---|
| **Demo** | Retain through jury day + short window (e.g. days–weeks) — enough to show reconstruct | Local disk under KWB data dir |
| **Org** | **≥ rolling 180 days** for ICT/application evidence logs (**CERT-In-shaped**); longer if org policy | On-prem / India-producible; encrypted at rest ambition |

Overwrite/delete of audit history by Worker = **Never**. Admin purge only under dual-control ambition + still retain legally required copies if applicable.

---

## 5. Who may read

| Role | Demo | Org |
|---|---|---|
| **Knowledge worker** | Own task events (Audience B) | Own task; not others’ high-class |
| **Approver** | Tasks they gate | Same + queue |
| **Admin** | Full demo log | Full org log + export for incident |
| **Auditor** (if used) | Read-only ambition | Read-only org |

Log export off-box = **H3-class control** / Admin + policy (open Q).

---

## 6. Integrity (proposed)

- Append-only file or table; no silent rewrite.  
- Optional hash-chain / signed batches = **org-ambition**.  
- Demo: tamper-evident enough = append-only + Admin-only raw access.

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Append-only evidence log with families in §3 (demo may MOCK thin fields but **model_id** + HITL + grant + gateway deny must be real).  
2. Auto-select proof: ≥2 task types → ≥2 **model_id**s queryable in log.  
3. Deny paths logged (grant revoke, gateway, gates, export).  
4. Role-scoped read (own task vs Admin).  
5. Org retention **180-day-shaped** in design; demo shorter OK.  
6. Cite CERT-In Directions as **shape**, not certification claim.  
7. No full secret/PII dump in log bodies — ids, hashes, reason codes.

### Org-ambition

- Hash-chain; SIEM ship; Auditor role UI; 180+ day cold storage; DPDP rosters.

### Deferred

- Full CERT-In incident reporting automation; ISO audit pack.

### Never

- Log = plant SoR.  
- Worker erase of audit trail.  
- Cloud log ship as must-work.  
- Claim “CERT-In compliant” without legal review.  
- Store raw PEM/private keys in events.

---

## 8. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Append-only audit *pattern*; CERT-In **180-day** retention *shape* |
| **Add** | Event family catalogue; model_id mandatory on route/gateway; GateReport ingest |
| **Refuse** | Chat-as-only-audit; cloud-only logging SaaS as brain |

---

## 9. Boundaries

| Topic | Owner |
|---|---|
| Live WAN=0 widget | **WP-13** |
| Task↔version graph UX | **WP-14** |
| Exact SIEM product | Not locked |
| Personal data lawful basis | Org legal / DPDP track |

---

## 10. Open questions for decision maker

1. **Demo retention:** Keep logs **jury-day only**, or **≥30 days** local for reconstruct demos?  
2. **Worker visibility:** Workers see **full own-task event list**, or only **Audience B summary** (model, grant, HITL) with Admin holding raw log?  
3. **Log export:** May Admin **download** audit bundle off KWB in demo (with H3-like gate), or **view in-app only** for must-work?  
4. **PII in logs:** Store **display name**, or **opaque person_id only** in must-work demo?  
5. **Clock sync:** Require **NTP/local trusted time** note in runbook, or accept host clock as-is for demo?  
6. **Failure mode:** If audit write fails, **fail-closed** the privileged action, or **allow action + alarm** (org preference)?

---

## 11. Next after your decisions

**Done.** Frozen as `WP-17_FREEZE.md` rev 1.0. Next: **WP-14**.
