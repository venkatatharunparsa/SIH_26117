# WP-19 offline update — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-19_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** Official add-models + no external calls; WP-00 offline media; WP-08 H5; WP-10/24 stage+card; WP-13 Audience A; WP-18 no-HF.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Media = **USB only** (must) |
| **2** | Demo integrity = **size + Admin eyeball** (SHA-256 = org-ambition) |
| **3** | **Operator may copy**; **Admin enables** (card/H5) |
| **4** | Demo shows **visible import UI** |
| **5** | Must-work payloads = **weights + plugins only** (skills later) |
| **6** | Demo = **direct stage OK** (quarantine = org-ambition) |

---

## Verdict

| | |
|---|---|
| Missing | M1–M10 (USB malware; operator stage abuse; eyeball≠integrity; import UI WAN; direct stage overwrite; org SHA; Audience A during import) |
| Overhyped | Eyeball = supply-chain secure; USB = always safe; import UI = download |
| Confidence | **~0.87** → GO WP-20 |

---

## Attack A — USB only (Q1)

| Attack | Fix |
|---|---|
| **A1** USB as malware vector | Org runbook: scan on connected island if policy; KWB still no WAN. Demo: labelled clean MOCK media |
| **A2** “USB only” blocks approved air-gap share forever | Freeze: **must-work channel = USB**; org-ambition may add Admin on-prem share later without redesign |
| **A3** Auto-run from USB | Import UI copies files — no auto-execute of payloads |

---

## Attack B — Size+eyeball (Q2)

| Attack | Fix |
|---|---|
| **B1** Tampered weights, wrong size coincidence | Org **must** move to checksum; demo honesty Limits: eyeball ≠ crypto verify |
| **B2** Skip eyeball | Admin enable requires recorded “reviewed” ack in audit |

---

## Attack C — Operator copy + Admin enable (Q3)

| Attack | Fix |
|---|---|
| **C1** Operator enables card themselves | Enable/H5 = **Admin only** (WP-24/08) |
| **C2** Operator stages to production runtime path unchecked | Import UI writes to **stage area**; Admin promote-to-runtime/enable |
| **C3** Worker uses unstaged path | Gateway/card still require enabled card |

**Reconcile D6 direct stage:** Demo may stage directly into runtime dirs **only after Admin enable action** or Admin-supervised import — operator alone cannot flip `enabled`.

---

## Attack D — Visible import UI (Q4)

| Attack | Fix |
|---|---|
| **D1** UI has “Download from HF” | **Never** — UI = pick local/USB path only |
| **D2** UI triggers curl | Fail-closed; A monitor during import |
| **D3** Import without audit | Log who imported, path, size, Admin enable |

---

## Attack E — Weights+plugins only (Q5)

| Attack | Fix |
|---|---|
| **E1** Skills smuggled as plugin | Plugin H5 capability review; skills path deferred |
| **E2** Templates forgotten | Ambition / Admin offline copy outside this must |

---

## Attack F — Direct stage demo (Q6)

| Attack | Fix |
|---|---|
| **F1** Overwrite live warm models mid-demo | Import to new dir/version; enable switches card `endpoint_ref`/path |
| **F2** Org skips quarantine forever | Quarantine **org-must-ambition**; demo direct OK |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | USB must-work channel |
| **M2** | Demo size+eyeball + Admin reviewed ack |
| **M3** | Operator import; Admin enable only |
| **M4** | Import UI local/USB only — no WAN |
| **M5** | Weights+plugins must; skills deferred |
| **M6** | Demo direct stage; org quarantine ambition |
| **M7** | Audit import+enable |
| **M8** | No auto-exec from media |
| **M9** | Audience A during import |
| **M10** | SHA-256 org-ambition |

---

## 2. Disposition

**Applied.** → `WP-19_FREEZE.md` + `WP-19_FREEZE_VERIFY.md`. Confidence **0.87**. **GO** → **WP-20**.
