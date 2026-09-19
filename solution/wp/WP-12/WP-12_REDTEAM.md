# WP-12 output gates — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-12_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** Official Background (confidential); User “gates before user sees/downloads”; WP-05 H2/H3/H9 + stale; WP-22 H7/H2 block; WP-23 secret scan; WP-16 evidence≠authority; WP-04 ceiling; WP-01 attach-only cite rule.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Also **block first full-screen view** on secret / high-class hit (not download-only) |
| **2** | Attach-only still requires **file evidence labels** (≠ org KB citations) |
| **3** | Secret hit → **hard-block H3 until cleaned** (no Approver override of the scan) |
| **4** | Sandbox **red** → **export blocked until green** |
| **5** | GateReport = **log/inspect only** (demo) |
| **6** | H3 click re-runs **G-secret + G-fresh + G-pack** only; G-cite/G-claim held unless **artefact version** changed |

---

## Verdict

| | |
|---|---|
| Missing | M1–M12 (view vs edit path; false-positive clean path; H9 vs export-green; file-label ≠ KB cite; log-only ≠ silent deny; version trigger; high-class definition; screen-shot residue) |
| Overhyped | Gates = DLP complete; view-block = no residue; green sandbox = plant-safe |
| Confidence | **~0.87** → GO WP-17 |

---

## Attack A — Full-screen block (Q1)

| Attack | Fix |
|---|---|
| **A1** Block view but chat already streamed secrets | Gate **before** first paint of artefact body; stream hold until G-secret/G-class pass |
| **A2** Worker cannot fix secrets if fully blind | Allow **masked / placeholder** view + edit of non-secret regions, or “clean room” editor without revealing raw secret spans — not infinite blind deadlock |
| **A3** Screenshot / shoulder residue | Honesty: gates **help**; not complete security (WP-00/04) |
| **A4** High-class undefined | High-class = object/artefact class **> grant ceiling** OR seed high classes (P&ID/financials/bidder/…) per WP-04 — MOCK taxonomy OK in demo |

**Decision:** Block **unmasked full-screen** of failing content; provide **remediation path** without Approver secret-override.

---

## Attack B — File evidence labels (Q2) vs WP-01

| Attack | Fix |
|---|---|
| **B1** Force org KB citations on attach-only | **Refuse** — labels = **file/evidence** (source file id, page/region, extract version) — not WP-11 org cites |
| **B2** Empty labels → invented findings | G-file (attach path): material findings need **file evidence labels** or `NOT FOUND` / blocked H2 |

**Decision:** Attach-only **G-file** must-work; G-cite (org KB) only when KB grant active.

---

## Attack C — Hard-block secret / no override (Q3)

| Attack | Fix |
|---|---|
| **C1** False positive permanent stuck | **Clean paths:** edit artefact (material → stale); Admin extends heuristic allowlist; **not** Approver “export anyway” |
| **C2** Silent auto-redact then export | Forbidden without log; prefer block until human removes/rewrites |
| **C3** WP-23 said warn+HITL for FP | DM **tightens** for H3: hard-block; warn-only may remain for non-export side-effects |

**Decision:** **Hard-block H3** until G-secret pass after clean.

---

## Attack D — Export until sandbox green (Q4) vs H9 human

| Attack | Fix |
|---|---|
| **D1** Contradicts “H9 decides / sandbox ≠ authority” | Split: **H9** = human may **acknowledge** red report; **G-sandbox** = **H3 export** of code package **blocked until green** |
| **D2** Impossible green on flaky test | Re-run sandbox; fix code; Admin may mark job type non-sandbox — not “export red” |
| **D3** Greenwash by skipping sandbox job | Jobs that require verify (WP-16) must have green report for H3 |

**Decision:** Export blocked until green; H9 remains human review of evidence — cannot unlock H3 while red.

---

## Attack E — Log-only GateReport (Q5)

| Attack | Fix |
|---|---|
| **E1** User sees deny with no reason | UI shows **short deny reason** (gate_id + one line); full GateReport = log |
| **E2** Skip writing GateReport | Always emit log (like PackManifest) |

---

## Attack F — Partial re-run (Q6)

| Attack | Fix |
|---|---|
| **F1** Cite/claim drift without version bump | Any material edit / claim-matrix change / new retrieve → **artefact_version** bump → full gate set including G-cite/G-claim/G-file |
| **F2** Stale H7 resolved in parallel without version | Resolving H7 updates claim state → version bump |

**Decision:** H3 hot path = secret+fresh+pack; **version change** invalidates cite/claim/file cache.

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | Unmasked view block + remediation path |
| **M2** | G-file for attach-only labels |
| **M3** | Hard-block H3; no secret override |
| **M4** | Clean paths for FP |
| **M5** | H9 ack ≠ H3 unlock while red |
| **M6** | Short UI deny; full report log-only |
| **M7** | Version-triggered full re-gate |
| **M8** | Live secret+fresh+pack on H3 |
| **M9** | Stream hold before first paint |
| **M10** | Gates ≠ plant safety |
| **M11** | G-class vs ceiling |
| **M12** | Preview ≠ export still holds; view-gate is separate |

---

## 2. Overhyped

| Claim | Reality |
|---|---|
| View-block = no leak | Residue/screenshot remain |
| Hard secret block = DLP | Light heuristics only |
| Green sandbox = safe to run in plant | Evidence only |
| Log-only = no user feedback | Short deny still required |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Output gate catalogue + GateReport log | Approver override of G-secret |
| File evidence labels on attach-only | Org cites required without KB grant |
| Export blocked while sandbox red | Export red “with caveat” |
| Version-scoped cite/claim cache | Skip GateReport write |

---

## 4. Disposition

**Applied.** → `WP-12_FREEZE.md` + `WP-12_FREEZE_VERIFY.md`. Confidence **0.87**. **GO** → **WP-17**.
