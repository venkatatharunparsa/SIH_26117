# WP-12 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-04 / WP-05 / WP-07 / WP-16 / WP-22 / WP-23 (WP-11 citations; WP-17 consumes gate events)  
**Status:** **SUPERSEDED by `WP-12_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-12_REDTEAM.md`. Verify: `WP-12_FREEZE_VERIFY.md`.  
**Job of WP-12:** **Validation + security gates (output-side)** — before the user **sees** record-facing content or **downloads** off KWB: enforce **citation/claim readiness**, **classification ceiling**, **secret scan**, **sandbox verdict binding**, and **export package integrity** — machine checks that **block or warn**; humans still own H2/H3/H9 (WP-05).

**Sources:** User “gates before information reaches the user”; Official Background (confidential); Expected Solution deliverable = export control point; WP-05 H2/H3/H9; WP-22 claim/H7; WP-23 light secret scan; WP-16 sandbox evidence≠authority; WP-04 classification ceiling; follow-list WP-12.

---

## One sentence (proposed)

Nothing **record-facing** or **off-box** leaves the happy path until **output gates** pass (or hard-fail): citations/conflicts clean enough for H2, secrets scanned, classification respected, sandbox report attached when required — **HITL still decides**; gates do not replace Approvers.

---

## 1. Input-side vs output-side (do not confuse)

| Side | WP | Example |
|---|---|---|
| **Input / trust** | WP-23, WP-03, WP-04 | Delimit T3; H1 extract; grant allowlist |
| **Claim truth** | WP-22 | S1/S2/S3; H7; `NOT FOUND` |
| **Human decision** | WP-05 | H2 / H3 / H9 accepts |
| **Output validation** | **WP-12** | Pre-view / pre-export **machine** checklist that **enables or blocks** those steps |

**Risk if skipped:** Approver clicks H2 on a doc that already flashed secrets on screen, or export zip omits citation fail.

---

## 2. Gate catalogue (proposed)

| Gate id | When | Machine check | On fail |
|---|---|---|---|
| **G-cite** | Before record-facing H2 (KB path) | Required citations present when KB grant used; no cite to non-packed chunks | Block H2 |
| **G-claim** | Before record-facing H2 | Open required H7 conflicts resolved; `NOT FOUND` labelled not invented (WP-22) | Block H2 |
| **G-class** | Before view of org-high content / before H3 | Artefact classification ≤ grant ceiling; segregation respected | Block / redact path |
| **G-secret** | Before H3 export | Light local secret heuristics (WP-23 D6) | Block H3 or force re-HITL |
| **G-sandbox** | Before H9 / code H3 | Sandbox report exists when code job requires verify; fail≠auto-approve | Block H9 accept as “greenwash” without report; H9 still human |
| **G-fresh** | Before H3 | Upstream H1/H2/H9 not stale (WP-05) | Block H3 |
| **G-pack** | Before H3 | Export package membership = approved artefact versions only | Block |

**Preview vs download:** In-place PDF preview ≠ export (WP-05 D6). G-secret/G-fresh/G-pack bind **download/export**. Org may also gate **first screen** of high class (open Q).

---

## 3. Pipeline (proposed)

```
Artefact ready for human
  → run output gate set for that job type
  → emit GateReport {gate_id, pass/fail/warn, details}
  → UI: show blockers before H2/H3/H9 controls enable
  → human HITL (WP-05)
  → on H3: re-run G-secret + G-fresh + G-pack at click time (live)
  → audit events → WP-17
```

Gates are **re-checked** at export click (not only once at draft time).

---

## 4. Demo vs org

| | Demo | Org |
|---|---|---|
| Must show | G-secret block; G-fresh/H3; G-cite or G-claim on inspect path; sandbox report before “verified” story | Full gate set |
| Classification | MOCK ceiling enough | Real taxonomy ambition |
| Redaction | Ambition | Org may redact-on-view |
| Performance | Slow OK | Same honesty |

---

## 5. Must / ambition / deferred / never (proposed)

### Must-work

1. GateReport before enabling record-facing H2 / H3 where applicable.  
2. G-secret pre-H3 (WP-23).  
3. G-fresh + G-pack on export.  
4. G-cite when KB grant used; G-claim respects H7 block.  
5. G-sandbox: no “verified” export story without report when job requires sandbox.  
6. Live re-check at H3 click.  
7. Gates assist — **do not** auto-approve plant outcomes.

### Org-ambition

- On-screen high-class gate before first paint; DLP packs; Approver gate dashboard; auto-redact.

### Deferred

- Certified DLP; full DPDP programme claim.

### Never

- Gate pass = statutory/FFS safe.  
- Skip H3 because G-secret passed.  
- Silent strip secrets without log.  
- Export with stale H2.  
- Treat chat preview leak as “not export” for org-high (open Q).

---

## 6. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Pre-export scan *idea*; approve-before-download (already H3) |
| **Add** | Named G-* catalogue; GateReport; live re-check; cite/claim/class/sandbox binding |
| **Refuse** | Gates replace HITL; full DLP as must-work demo |

---

## 7. Boundaries

| Topic | Owner |
|---|---|
| Which human clicks | **WP-05** |
| Claim matrix / H7 | **WP-22** |
| Secret heuristic patterns | **WP-23** (WP-12 invokes) |
| Sandbox execution | **WP-16** |
| Audit fields | **WP-17** |
| Grant ceiling values | **WP-04** |

---

## 8. Open questions for decision maker

1. **On-screen gate:** For demo, is **blocking download (H3)** enough, or must **high-class / secret-hit content also be blocked from first full-screen view**?  
2. **G-cite strictness (attach-only):** Attach-only inspect (no KB) — skip G-cite, or still require **file-level** evidence labels?  
3. **Secret hit:** **Hard-block H3** until cleaned, or **warn + Approver override** (audited) allowed for must-work?  
4. **Sandbox red:** If sandbox **fails**, may H9 still **accept with caveat** (human), or must code export stay blocked until green?  
5. **GateReport visibility:** Jury must see GateReport in **UI**, or **log/inspect only** (like PackManifest demo)?  
6. **Re-run cost:** On every H3 click, re-run **all** applicable gates, or only **G-secret + G-fresh + G-pack** (cite/claim assumed held unless artefact version changed)?

---

## 9. Next after your decisions

**Done.** Frozen as `WP-12_FREEZE.md` rev 1.0. Next: **WP-17**.
