# WP-17 audit log — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-17_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** Official Expected Solution (logs; model ids); WP-00 Audit; WP-04/05/09/12 event producers; CERT-In Directions No. 20(3)/2022-CERT-In (28 Apr 2022) § ICT logs rolling **180 days**; CERT-In FAQ May 2022 (success + fail events); DPDP 2023 (org track — no fake compliance claim).

---

## 0. DM answers (as given + adversarial parse)

| Q | Raw | **Freeze interpretation** |
|---|---|---|
| **1** | Jury-day only | Demo retention = **jury window only** (start→end of demo day). Org still **180-day-shaped** |
| **2** | Full own-task event list | Workers see **full structured events for own tasks** |
| **3** | in-app view only for must-work **and** downloaded and editable | **Must-work:** in-app view. **Download:** Admin read-only bundle = **ambition** (not must). **Editable:** UI filter/search only — **Never** mutate/delete audit events |
| **4** | yes | Ambiguous → **person_id required**; **display_name allowed** for MOCK demo jury; org may hide names |
| **5** | Runbook trusted clock | Org/demo **runbook**: sync trusted time before jury; events store timestamps from host after sync |
| **6** | Fail-closed the action | If audit append fails → **privileged action fails closed** |

---

## Verdict

| | |
|---|---|
| Missing | M1–M12 (editable≠tamper; jury-day vs reconstruct; cross-task leak; download off-box; CERT-In shape≠badge; fail-closed loops; clock lie; secret bodies in log) |
| Overhyped | CERT-In compliant; chat=audit; jury-day=org retention |
| Confidence | **~0.88** → GO WP-14 |

---

## Attack A — “Downloaded and editable” (Q3)

| Attack | Why fatal | Fix |
|---|---|---|
| **A1** Worker edits audit history | Erases deny-after-revoke / HITL proof | Append-only; **no update/delete** API for Workers |
| **A2** Downloaded CSV edited offline, re-imported as truth | Fake trail | Download (if any) = **evidence export copy**, not re-importable as SoR |
| **A3** Must-work download contradicts air-gap / H3 | Off-box copy | Must-work = **in-app only**; gated Admin download = ambition + WP-12-style control |
| **A4** “Editable” meant filter UI | OK | Freeze: editable = **query/filter/sort view**, not event mutation |

**Decision:** D3 as interpreted in §0.

---

## Attack B — Jury-day only (Q1)

| Attack | Fix |
|---|---|
| **B1** Cannot reconstruct after laptop sleep overnight | Jury-day = retain until **demo session officially ends**; document wipe after |
| **B2** Org thinks jury-day is enough forever | Org profile **≥180 rolling days** (CERT-In-shaped) |
| **B3** Auto-select proof lost if log rotated mid-demo | No rotation during active demo window |

---

## Attack C — Full own-task list (Q2)

| Attack | Fix |
|---|---|
| **C1** Worker sees other users’ tasks | Scope = **own person_id ∩ own task_ids** only |
| **C2** High-class payload in event detail | Log **ids/hashes/reason codes**; not raw secret spans / full tool stdout |
| **C3** Grant allowlist dumped into UI | Summaries OK; full allowlist = Admin |

---

## Attack D — PII “yes” (Q4)

| Attack | Fix |
|---|---|
| **D1** Ambiguous yes → accidental Aadhaar etc. | Only **MOCK display_name** + opaque **person_id**; no government IDs |
| **D2** DPDP overclaim | Cite DPDP as **org track**; demo MOCK ≠ compliance badge |

---

## Attack E — Trusted clock (Q5)

| Attack | Fix |
|---|---|
| **E1** NTP to public internet mid-demo | Runbook: sync **before** air-gap / use **local** time source; no WAN during operation |
| **E2** Backdated HITL | Fail-closed if clock step detected (ambition); demo: runbook discipline |

---

## Attack F — Fail-closed on audit write (Q6)

| Attack | Fix |
|---|---|
| **F1** Disk full → total denial of service | Alarm + Admin; still fail-closed privileged I/O; read-only UI may continue |
| **F2** Audit fail on read-only view | Viewing log does not require new privileged append |
| **F3** Recursive fail (logging the fail-closed) | Best-effort **last-resort local file** for audit_subsystem_error; if even that fails, stop privileged ops |

---

## Attack G — CERT-In / Expected Solution

| Attack | Fix |
|---|---|
| **G1** “We are CERT-In compliant” | **Never** without legal review — only **shaped** by 180-day / enable logs / success+fail |
| **G2** Skip model_id in log | Violates Expected Solution + WP-00 proof |
| **G3** Only success events | Log denials too (FAQ flavour) |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | Append-only; no worker edit/delete |
| **M2** | Jury-day demo vs 180d org |
| **M3** | Own-task full list; no cross-user |
| **M4** | In-app must-work; download ambition read-only |
| **M5** | person_id + optional MOCK display_name |
| **M6** | Trusted clock runbook; no WAN NTP in-op |
| **M7** | Fail-closed privileged actions |
| **M8** | model_id on route/gateway events |
| **M9** | GateReport / PackManifest refs not secret bodies |
| **M10** | Success + fail events |
| **M11** | CERT-In cite as shape not badge |
| **M12** | WP-14 consumes event spine |

---

## 2. Overhyped

| Claim | Reality |
|---|---|
| Editable audit | Filter UI only |
| Jury-day = compliance retention | Org 180d separate |
| CERT-In certified | Shape only |
| Full task list = full payloads | Redacted fields |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Append-only evidence log; 180d org shape | Worker-mutable history |
| model_id + deny events must | Chat-as-sole-audit |
| Fail-closed on audit I/O fail | Silent drop of audit |

---

## 4. Disposition

**Applied.** → `WP-17_FREEZE.md` + `WP-17_FREEZE_VERIFY.md`. Confidence **0.88**. **GO** → **WP-14**.
