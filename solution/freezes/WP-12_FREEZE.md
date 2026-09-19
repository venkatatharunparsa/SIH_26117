# WP-12 Validation + security gates — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-04 / WP-05 / WP-16 / WP-22 / WP-23 (and WP-01 attach-only; WP-11 when KB).  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-12_ARCHITECT_PERSPECTIVE.md`, `WP-12_REDTEAM.md`, **DM 2026-09-18** (block unmasked first view; file evidence labels; hard-block H3 on secrets; export until sandbox green; GateReport log-only; H3 re-run secret+fresh+pack unless version changed).  
**Findings SoT:** `WP-12_REDTEAM.md`  
**Verify SoT:** `WP-12_FREEZE_VERIFY.md`  
**Product:** **KWB**

**DLP/scanner brand:** not locked.

---

## 1. One-sentence contract

**Output gates** run before **unmasked view** and before **off-box download**: classification/secret/file-or-cite/claim/sandbox/fresh/pack checks emit a **GateReport** (log) and **block** unsafe paths — including **first full-screen** on secret/high-class hits and **H3 until secrets cleaned and sandbox green** — while **HITL** still owns accepts; gates **never** mean plant-safe.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Block **unmasked** first view on secret/high-class hit | Complete anti-shoulder / anti-screenshot security |
| File **evidence labels** on attach-only | Org KB citations without KB grant |
| Hard-block H3 until G-secret pass | Approver “export anyway” override of secrets |
| Code **export** blocked while sandbox red | Green sandbox = FFS/statutory OK |
| GateReport **log-only** (demo) | Silent deny with zero UI reason |
| H3 hot re-check secret+fresh+pack | Skip re-check if version unchanged for those three |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Secret or **high-class** fail → block **unmasked full-screen** of that artefact (stream/first paint held); remediation path without revealing raw secrets unchecked |
| **D2** | Attach-only → **G-file** requires **file evidence labels** on material findings (not WP-11 org cites) |
| **D3** | G-secret fail → **hard-block H3** until cleaned; **no** Approver override of the scan |
| **D4** | Sandbox **red** → **H3 export blocked until green** (H9 may review red report; cannot unlock export while red) |
| **D5** | Full GateReport = **log/inspect only** (demo); UI shows **short deny** (`gate_id` + one line) |
| **D6** | On H3 click: re-run **G-secret + G-fresh + G-pack**; re-run G-cite/G-claim/G-file only if **artefact_version** changed since last pass |

---

## 4. Input vs output

| Side | Owner |
|---|---|
| Ingest trust / grants | WP-03/04/23 |
| Claims / H7 | WP-22 |
| Human clicks | WP-05 |
| **Machine output checklist** | **WP-12** |

---

## 5. Gate catalogue (frozen)

| Gate | When | Check | Fail |
|---|---|---|---|
| **G-secret** | Before unmasked view + before H3 | Light local secret heuristics (WP-23) | Block unmasked view; **hard-block H3** |
| **G-class** | Before unmasked view + before H3 | Class ≤ grant ceiling; segregation; unknown org class fail-closed (WP-04) | Block unmasked view / H3 |
| **G-file** | Before record-facing H2 (attach-only / file path) | Material findings have **file evidence labels** (file id, page/region, extract version) or honest gap | Block H2 |
| **G-cite** | Before H2 when **KB grant** active | ≥1 valid cite bound to packed chunks (WP-11) | Block H2 |
| **G-claim** | Before record-facing H2 | Required H7 resolved; no silent invent over `NOT FOUND` (WP-22) | Block H2 |
| **G-sandbox** | Before code H3 | Required sandbox job has **green** report | **Block H3** until green |
| **G-fresh** | Before H3 | Upstream H1/H2/H9 not stale (WP-05) | Block H3 |
| **G-pack** | Before H3 | Package = approved artefact versions only | Block H3 |

In-place PDF **preview** ≠ export (WP-05). Preview must still respect **G-secret/G-class** for unmasked body.

---

## 6. Pipeline

```
Artefact version V
  → run applicable gates → GateReport (log) + short UI denies
  → unmasked view only if G-secret ∧ G-class pass
  → H2 enabled only if G-file/G-cite/G-claim pass as applicable
  → H9: human may review sandbox report (red or green)
  → H3 click: live G-secret + G-fresh + G-pack
       + if V changed since cite/claim/file pass → re-run those too
       + G-sandbox green required for code package export
  → events → WP-17
```

**Remediation (secrets FP):** edit content (bumps version / stale HITL); or Admin updates heuristic allowlist — **not** export override.

---

## 7. High-class (for D1)

Treat as high-class hit when:

- Artefact/object classification **>** grant `classification_ceiling`, or  
- Seed high classes per WP-04 (P&ID, financials, vendor/bidder, strategy, unreleased designs) when labelled — MOCK labels OK in demo.

---

## 8. Must / ambition / deferred / never

### Must-work

1. G-* catalogue above; GateReport always logged.  
2. Unmasked view block on secret/high-class fail.  
3. G-file labels on attach-only; G-cite when KB.  
4. Hard-block H3 on secrets; export blocked while sandbox red.  
5. H3 live secret+fresh+pack; version-triggered cite/claim/file.  
6. Short UI deny reasons.  
7. Gates do not replace HITL or mean plant-safe.

### Org-ambition

- GateReport UI; auto-redact; richer DLP; Approver dashboards.

### Deferred

- Certified DLP / full DPDP programme claim.

### Never

- Approver override of G-secret.  
- H3 while sandbox red (for required verify jobs).  
- Org KB cites mandatory without KB grant.  
- Gate pass = statutory/FFS safe.  
- Silent secret strip without log.  
- Skip GateReport write.

---

## 9. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Pre-export scan + approve-before-download patterns | WP-05/23 |
| **Add** | View-gate; G-file; hard secret; export-until-green; versioned re-gate | DM / red-team |
| **Refuse** | Secret export override; DLP-as-complete-security |

---

## 10. Demo acceptance

1. Secret pattern in DRAFT → unmasked view blocked; H3 denied; after clean → pass.  
2. Attach-only findings without file labels → H2 blocked.  
3. Sandbox red → H3 denied; green → H3 allowed if fresh.  
4. Stale H2 → H3 denied (G-fresh).  
5. GateReport lines in log; UI shows short reason.  
6. Edit after cite pass → version bump → cite/file re-checked before H2/H3 as applicable.

---

## 11. Next

**WP-17** — Audit and evidence log.

---

## 12. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial view/secret/sandbox/version decisions |

**Confidence:** **0.87**
