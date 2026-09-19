# WP-14 Task–version lineage store — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-01 / WP-02 / WP-05 / WP-11 / WP-17 (and WP-12 export pack).  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-14_ARCHITECT_PERSPECTIVE.md`, `WP-14_REDTEAM.md`, **DM 2026-09-18** (JSON/manifest; node diagram; lineage_degraded; current-task only; H3 snapshot; revision_unknown badge).  
**Findings SoT:** `WP-14_REDTEAM.md`  
**Verify SoT:** `WP-14_FREEZE_VERIFY.md`  
**Product:** **KWB**

**Engine brand:** not locked (manifest now; SQL/graph later under same contract).

---

## 1. One-sentence contract

Each **task** has a **lineage** (JSON/manifest beside the designated store) relating **input revisions**, **model/tool steps**, **artefact versions**, **HITL**, and **exports**, shown as a **simple node diagram**; `revision_unknown` gets a **warning badge**; H3 may ship a **minimized lineage snapshot**; lineage materialize failure sets **`lineage_degraded`** (visible) without weakening **WP-17 audit fail-closed**.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Lineage = relations + diagram **view** | Neo4j / graph DB mandatory |
| JSON/manifest must-work | Manifest is Worker-editable SoR |
| `lineage_degraded` continues task | Audit write may be dropped (WP-17 still fail-closes) |
| Current task only | Must-work cross-task graph |
| H3 lineage snapshot | Snapshot with secret bodies / re-importable SoR |
| Warning badge for unknown rev | Silent “current SOP” look |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Persist demo lineage as **JSON/manifest beside files** in designated KWB store |
| **D2** | Must-work UI = **simple node diagram** (linear list alone insufficient) |
| **D3** | Lineage materialize fail → continue with **`lineage_degraded`** + visible banner + audit event; **audit append** still fail-closes (WP-17) |
| **D4** | Must-work scope = **current task only** |
| **D5** | H3 allow → package includes **read-only minimized lineage snapshot** |
| **D6** | `revision_unknown` → **explicit warning badge** on citation and on diagram node |

---

## 4. Contractual shape (engine-free)

```
task_id
  inputs[]:     source_id, object_id, revision|revision_unknown, extract_version?, content_hash?
  steps[]:      event_id ref, model_id?, tool/plugin_id?, ts  (summarized)
  artefacts[]:  artefact_id, artefact_version, kind, content_hash
  hitl[]:       gate_id, artefact_version, outcome, person_id
  exports[]:    package_ref, artefact_versions[], ts, outcome
  flags:        lineage_degraded?
```

Projection preferably from **WP-17 events** + store versions; manifest is the durable demo projection.

---

## 5. Rules

| Rule | Must |
|---|---|
| Worker | Read-only lineage UI; no hand-edit of manifest as product path |
| Hash | Artefact version hash mismatch → degraded + warn |
| Reuse prior DRAFT | **Copy** into current task → **new** artefact_version under this task_id |
| Diagram | Cap/summary nodes (not per-keystroke); redact like audit |
| Snapshot | Ids, revisions, model_ids, gate outcomes, hashes — **no** raw secrets/tool dumps |
| Snapshot | Not re-imported as live lineage authority |
| Unknown rev | Badge always visible when present |
| Plant DMS | Never write lineage there |

---

## 6. Demo vs org

| | Demo | Org |
|---|---|---|
| Store | JSON/manifest | Same contract; SQL/graph OK later |
| Jobs | inspect-to-note + code-sandbox | All jobs |
| Retention | Align WP-17 demo window | Align org audit retention |
| UI | Simple node diagram | Richer ambition |

---

## 7. Must / ambition / deferred / never

### Must-work

1. Manifest lineage per task with §4 fields.  
2. Simple node diagram UI.  
3. model_id(s), artefact version chain, HITL, export links.  
4. revision or revision_unknown + **badge**.  
5. H3 minimized snapshot.  
6. lineage_degraded visible path; audit fail-closed unchanged.  
7. Current-task scope; engine not brand-locked.

### Org-ambition

- Cross-task links; interactive graph; Auditor browse; SQL backend; derived_from links.

### Deferred

- Full W3C PROV product; distributed lineage bus.

### Never

- Neo4j mandatory.  
- Chat-as-only-lineage.  
- Pretend known revision.  
- Worker-mutable history.  
- Snapshot as editable SoR.  
- Weaken WP-17 fail-closed.

---

## 8. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Event-sourced projection; doc-control rev identity | User / WP-02/11 |
| **Add** | Manifest+diagram; degraded flag; H3 snapshot; unknown badge | DM / red-team |
| **Refuse** | Graph-DB lock; silent unknown rev |

---

## 9. Demo acceptance

1. Inspect task diagram shows attach/extract → model → DRAFT versions → H2 → (optional) H3.  
2. KB cite with unknown rev → **badge** on node and cite chrome.  
3. Code path shows sandbox + model_id nodes.  
4. H3 zip/folder contains lineage snapshot file (minimized).  
5. Inject lineage write fail → banner `lineage_degraded`; privileged path still requires audit success.  
6. No Neo4j required to pass.

---

## 10. Next

**WP-13** — Monitors (sovereign + operator).

---

## 11. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial degraded/snapshot/diagram pass |

**Confidence:** **0.87**
