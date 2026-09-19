# WP-14 lineage — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-14_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** User “not a graph DB; clarity of what they are building”; Official SOP revision identity; WP-02 store+versioning; WP-05 artefact_version; WP-11 revision_unknown; WP-17 append-only + fail-closed audit; WP-12 G-pack / export.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Demo store = **JSON/manifest beside files** |
| **2** | UI must-work = **simple node diagram** (not list-only) |
| **3** | Lineage write fail → **continue with `lineage_degraded`** (not fail-closed) |
| **4** | Scope = **current task only** (no prior-task links must-work) |
| **5** | H3 package **includes lineage snapshot** |
| **6** | `revision_unknown` → explicit **warning badge** |

---

## Verdict

| | |
|---|---|
| Missing | M1–M12 (degraded vs audit fail-closed clash; snapshot secrets; diagram≠Neo4j; manifest tamper; current-task reuse hole; badge without block; H3 snapshot vs stale) |
| Overhyped | Node diagram = graph DB; degraded = fine forever; snapshot = full audit export |
| Confidence | **~0.87** → GO WP-13 |

---

## Attack A — lineage_degraded vs WP-17 fail-closed (Q3)

| Attack | Fix |
|---|---|
| **A1** Operators ignore degraded forever | **Audience B banner** + audit event `lineage_degraded`; Admin must clear |
| **A2** Contradicts audit fail-closed | Split: **audit event write** still fail-closes privileged I/O (WP-17). **Lineage projection/materialize** may degrade if secondary write fails after audit succeeded |
| **A3** Silent degrade | Never silent — visible badge + log |

**Decision:** D3 with A2 split locked.

---

## Attack B — JSON/manifest beside files (Q1)

| Attack | Fix |
|---|---|
| **B1** Manifest edited on disk | Treat as evidence; prefer regenerate from WP-17; Worker UI read-only; Admin-only raw file access |
| **B2** Manifest drifts from bytes | Store content hash per artefact_version; mismatch → degraded + warn |
| **B3** Path traversal in manifest | Ids only; paths under designated store |

---

## Attack C — Simple node diagram (Q2)

| Attack | Fix |
|---|---|
| **C1** Jury thinks Neo4j required | Limits: diagram = **view**; store = JSON/SQL later |
| **C2** Diagram too heavy for demo | Cap nodes (inputs, steps summary, artefact versions, HITL, export) — not every keystroke |
| **C3** Diagram shows secrets | Same redaction as WP-17 (ids/hashes/labels) |

---

## Attack D — Current task only (Q4)

| Attack | Fix |
|---|---|
| **D1** Reused DRAFT from prior task loses provenance | Must-work: copy-into-task creates **new** artefact_version under **current** task; optional “derived_from” string ambition |
| **D2** Org needs cross-task | Ambition only |

---

## Attack E — Lineage snapshot in H3 (Q5)

| Attack | Fix |
|---|---|
| **E1** Snapshot contains secrets / full tool stdout | Snapshot = **ids, revisions, model_ids, gate outcomes, hashes** — same minimization as audit |
| **E2** Snapshot editable after download | Read-only file in package; not re-importable as live lineage SoR |
| **E3** Stale snapshot vs last second edit | Snapshot taken at **H3 allow** time from current task lineage; G-fresh already required |
| **H3 deny** | No snapshot export |

---

## Attack F — revision_unknown badge (Q6)

| Attack | Fix |
|---|---|
| **F1** Badge only, still looks “current SOP” | Badge **and** citation chrome; cannot hide on node |
| **F2** Blocks all H2 | Warning ≠ automatic H2 block unless WP-22/12 require; honesty badge always |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | Audit fail-closed ≠ lineage degrade split |
| **M2** | Visible degraded banner + event |
| **M3** | Manifest+hash; read-only Worker |
| **M4** | Simple diagram view; not engine lock |
| **M5** | Current-task scope; copy = new version |
| **M6** | Minimized H3 lineage snapshot |
| **M7** | revision_unknown warning badge mandatory |
| **M8** | Node cap / summary steps |
| **M9** | Lineage ≠ plant DMS |
| **M10** | Built from WP-17 + store versions |
| **M11** | Demo inspect+code paths |
| **M12** | No chat-as-lineage |

---

## 2. Overhyped

| Claim | Reality |
|---|---|
| Node diagram | UI only |
| Degraded OK | Visible debt; audit still strict |
| Snapshot = full forensics | Minimized certificate |
| Current-task only | Reuse via copy, not silent merge |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Manifest lineage + simple diagram | Neo4j must |
| revision_unknown badge | Pretend known rev |
| Minimized export snapshot | Mutable lineage SoR |

---

## 4. Disposition

**Applied.** → `WP-14_FREEZE.md` + `WP-14_FREEZE_VERIFY.md`. Confidence **0.87**. **GO** → **WP-13**.
