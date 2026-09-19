# WP-14 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-01 / WP-02 / WP-03 / WP-05 / WP-11 / WP-17 (WP-13 may display lineage snippets)  
**Status:** **SUPERSEDED by `WP-14_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-14_REDTEAM.md`. Verify: `WP-14_FREEZE_VERIFY.md`.  
**Job of WP-14:** **Task–version lineage store** — durable **relations** linking a **task** to **input versions** (attach/extract/SOP revision), **tool/plugin calls**, **model_id**, **DRAFT artefact versions**, **HITL accepts**, and **export packages** — so an engineer sees *what was built from what*, not a chat dump. **Engine not locked** (SQL / files+manifest / graph later).

**Sources:** User (“not a graph DB; clarity of what they are building”); Official (SOP grounding ⇒ revision identity); WP-02 designated store + versioning + lineage records; WP-05 artefact_version; WP-11 revision/revision_unknown; WP-17 event spine; follow-list WP-14.

---

## One sentence (proposed)

Every task has a **lineage record**: which **input revisions** and **model/tool steps** produced which **artefact versions** and which **HITL/export** outcomes — queryable without choosing Neo4j.

---

## 1. What lineage is (and is not)

| Is | Is not |
|---|---|
| Relation graph / join tables / manifests over ids | Mandatory Neo4j / property-graph product |
| Document-control clarity (which SOP rev cited) | Plant DMS versioning |
| Built from WP-17 events + store versions | Replacement for the audit log |
| Engineer-facing history | Chat transcript as SoR |

```
task_id
  ├─ inputs[]: {source_id, object_id, revision|revision_unknown, extract_version?}
  ├─ steps[]:  {event_id, model_id?, tool/plugin_id?, ts}
  ├─ artefacts[]: {artefact_id, artefact_version, kind}
  ├─ hitl[]: {gate_id, artefact_version, outcome, person_id}
  └─ exports[]: {package_ref, artefact_versions[], ts, outcome}
```

Exact persistence shape = implementation later; **fields above are contractual**.

---

## 2. Ownership

| Actor | Role |
|---|---|
| **WP-17** | Append events (spine) |
| **WP-14** | Materialize / query **task lineage view** from events + versioned store |
| **WP-02 store** | Bytes of DRAFT/code + version ids |
| **WP-13** | May show compact lineage strip (ambition/demo) |

If lineage write fails: align with audit integrity — **fail-closed** on privileged progress or mark lineage_degraded (open Q).

---

## 3. Must links (proposed)

| Link | Why |
|---|---|
| task → input attach hash / extract version | H1 chain |
| task → cited SOP/object **revision** or `revision_unknown` | WP-11 honesty |
| task → model_id(s) used | Auto-select proof + reconstruct |
| task → artefact_version chain | Stale HITL (WP-05) |
| artefact_version → H2/H3/H9 outcomes | Who accepted what |
| export package → frozen artefact_versions | G-pack (WP-12) |

---

## 4. Demo vs org

| | Demo | Org |
|---|---|---|
| Engine | File manifest JSON **or** simple SQL beside store | Same contract; scale later |
| UI | Task “History” list: inputs → versions → HITL → export | Richer graph UI ambition |
| Depth | Inspect-to-note + code path enough | All job types |
| Retention | Follow WP-17 demo (jury-day) for lineage rows | Follow org audit retention |

---

## 5. Must / ambition / deferred / never (proposed)

### Must-work

1. Per-task lineage record with §3 links (demo: inspect + code).  
2. Show **which revision** (or unknown) was cited when KB used.  
3. Artefact version chain visible for DRAFT edits / accepts.  
4. model_id(s) on the lineage for that task.  
5. Engine **not** brand-locked; PPT/docs say “lineage” not “Neo4j.”  
6. Lineage ≠ plant DMS.

### Org-ambition

- Interactive graph UI; cross-task compare; Auditor browse; export lineage certificate.

### Deferred

- Distributed lineage bus; W3C PROV-full profile as product.

### Never

- Graph DB mandatory.  
- Lineage stored only in chat.  
- Pretend revision known when `revision_unknown`.  
- Write lineage into plant SoR.

---

## 6. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Document-control *idea* (rev identity); event-sourced projection from WP-17 |
| **Add** | Contractual relation fields; demo History UI |
| **Refuse** | Neo4j lock-in; chat-as-lineage |

---

## 7. Boundaries

| Topic | Owner |
|---|---|
| Raw events | **WP-17** |
| Blob versions on disk | **WP-02** |
| Citation metadata | **WP-11** |
| Stale rules | **WP-05** |
| Monitor chrome | **WP-13** |

---

## 8. Open questions for decision maker

1. **Demo store:** **JSON/manifest beside files**, or **SQLite** (or equivalent) for must-work?  
2. **UI depth:** Must-work = **linear History list**, or must show a **simple node diagram**?  
3. **Lineage write fail:** **Fail-closed** (like audit), or allow continue with **lineage_degraded** flag?  
4. **Cross-task:** Demo needs **only current task** lineage, or also **link prior task ids** when user reuses an artefact?  
5. **Export bundle:** Should H3 package optionally include a **lineage snapshot** (read-only), or keep lineage **in-app only** (must-work)?  
6. **Unknown revision:** When `revision_unknown`, must History show an explicit **warning badge**, or plain text enough?

---

## 9. Next after your decisions

**Done.** Frozen as `WP-14_FREEZE.md` rev 1.0. Next: **WP-13**.
