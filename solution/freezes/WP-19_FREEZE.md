# WP-19 Offline update (models + plugins) — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-08 / WP-10 / WP-13 / WP-24.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-19_ARCHITECT_PERSPECTIVE.md`, `WP-19_REDTEAM.md`, **DM 2026-09-18** (USB; size+eyeball demo; operator copy + Admin enable; import UI; weights+plugins; direct stage demo).  
**Findings SoT:** `WP-19_REDTEAM.md`  
**Verify SoT:** `WP-19_FREEZE_VERIFY.md`  
**Product:** **KWB**

---

## 1. One-sentence contract

Weights and plugins enter KWB only via **USB offline media** through a **visible import UI** (operator may copy; **Admin alone enables**), with **demo** integrity = **size + eyeball + reviewed ack**, **direct stage** allowed for demo, **no** in-app HF/npm/MCP-hub fetch, and **skills-on-media** deferred.

---

## 2. Limits

| True | False / refuse |
|---|---|
| USB must-work intake channel | In-app internet download |
| Size+eyeball OK for **demo** | Demo = supply-chain certified |
| Operator copy / Admin enable | Operator self-enable cards/H5 |
| Visible import UI | HF download button |
| Weights + plugins must-work | Skills packs must on media |
| Direct stage OK for demo | Org forever without quarantine ambition |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Must-work media = **USB** (on-prem share = org-ambition later) |
| **D2** | Demo integrity = **size + Admin eyeball** + recorded **reviewed** ack; **SHA-256 manifest** = org-ambition |
| **D3** | **Operator** may run import/copy; **Admin** only **enables** (card enable / H5) |
| **D4** | Must-work **visible import UI** (local/USB path picker only) |
| **D5** | Must-work payloads = **weights + plugins**; skill packs = deferred/ambition |
| **D6** | Demo **direct stage** into runtime/plugin dirs OK; **quarantine dir** = org-ambition |

---

## 4. Pipeline (frozen)

```
USB (approved)
  → Import UI (operator or Admin): copy to stage/runtime or plugin stage paths
  → record size + Admin eyeball/reviewed (demo) 
  → Admin enables Model Card (WP-24) or H5 allowlist (WP-08)
  → audit: import + enable events (WP-17)
  → no WAN fetch at any step
```

**Never in UI:** Hugging Face, npm, public MCP registry, Skills Hub URLs.

---

## 5. Role split

| Role | May | May not |
|---|---|---|
| Operator / Knowledge worker | Import UI copy from USB | Enable card; H5 allowlist; self-install WAN |
| Admin | Import + **enable** + H5 + disable/remove | Skip air-gap for convenience |
| System | No background public updater | — |

---

## 6. Demo vs org

| | Demo | Org |
|---|---|---|
| Media | USB (MOCK labelled drop OK) | USB (+ share ambition) |
| Integrity | Size + eyeball + ack | SHA-256 (+ signed packs ambition) |
| Stage | Direct OK | Quarantine then promote ambition |
| Proof | Import UI + no public peers on A during import | Same |

---

## 7. Must / ambition / deferred / never

### Must-work

1. USB offline intake for weights + plugins.  
2. Visible import UI (local/USB only).  
3. Operator copy; Admin enable only.  
4. Demo size+eyeball+reviewed ack.  
5. No in-app public registry pull.  
6. Audit import/enable; A-compatible (no WAN).  
7. No auto-execute of media payloads.

### Org-ambition

- SHA-256/SBOM; quarantine; on-prem Admin share; dual control; skill packs on media.

### Deferred

- Continuous offline mirror product; CVE auto-patch farm.

### Never

- HF/npm/MCP-hub in-app download.  
- Silent WAN updater.  
- Operator enable without Admin.  
- “Advise download” as air-gap.

---

## 8. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Stage-then-register air-gap pattern | WP-00/08/24 |
| **Add** | USB+import UI; operator/Admin split; demo eyeball honesty | DM |
| **Refuse** | Public fetch buttons; auto-enable on copy |

---

## 9. Demo acceptance

1. Import UI copies from USB/MOCK path — no network fetch.  
2. Operator cannot enable new card without Admin.  
3. Admin enable after size/eyeball ack.  
4. Audience A during import: no public peers.  
5. Plugin path uses H5, not self-install.

---

## 10. Next

**WP-20** — Org connection diagram.

---

## 11. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze USB/import/Admin-enable/demo eyeball |

**Confidence:** **0.87**
