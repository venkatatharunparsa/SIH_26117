# WP-13 Monitors (sovereign + operator) — FREEZE

**Date:** 2026-09-19  
**Status:** **FROZEN** (rev **1.1**) — GATE_90 **A5** evidence-pack language.  
**Prior:** rev 1.0 (2026-09-18).  
**Depends on:** those freezes (must not contradict).  
**Aligns:** WP-00/20 · org D2 Monitor A contract · demo start/stop snapshot.  
**Inputs:** `WP-13_ARCHITECT_PERSPECTIVE.md`, `WP-13_REDTEAM.md`, **DM 2026-09-18** (OS view + firewall log; start/stop snapshots; Monitors page; green local hop; block claim without host evidence; Worker own-task B).  
**Findings SoT:** `WP-13_REDTEAM.md`  
**Verify SoT:** `WP-13_FREEZE_VERIFY.md`  
**Product:** **KWB**

**Host tool brands:** not locked (OS connection UI / firewall log as classes).

---

## 1. One-sentence contract

KWB proves sovereignty with **Audience A** host-backed **evidence pack** (org: egress attempts + deny; demo: **start/stop snapshot** via OS connection view and/or firewall log) showing **no public-internet egress** in the capture window, while labelling an explicit **green local runtime hop**; **Audience B** is a **Monitors page** for the Worker’s **own task**. Without host evidence the product **must not** claim Audience A pass — and **must not** claim CERT / accreditation.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Host/OS evidence pack for A | In-app “SECURE” / CERT badge alone |
| On-prem LAN to allowlisted runtime = **local hop** | Any LAN = PS “external call” |
| Start/stop snapshot pair (demo) / continuous ambition (org) | Verbal “WAN=0” without artefact |
| Block A claim if no host evidence | Log-only unlocks A green badge |
| B = Monitors page, own task | B shows all users’ secrets |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | A toolbox = **OS connection view** + **firewall log** (≥1 host artifact required; both preferred) |
| **D2** | A capture mode = **start/stop snapshot pair** + timing runbook |
| **D3** | B UI = dedicated **Monitors page** |
| **D4** | Explicit **green LOCAL RUNTIME** hop for WP-09 allowlisted endpoint |
| **D5** | No host evidence → **block Audience A / sovereign-monitor claim** (no fake badge) |
| **D6** | B scoped to **Worker own task** |

---

## 4. Audience A — sovereign

### 4.1 Pass criteria

- During the captured window: **no** connections to **public internet** addresses / public DNS that indicate WAN use.  
- **Allowed:** loopback / Admin on-prem allowlisted runtime (shown as **green local hop**).  
- Evidence files/screenshots from **OS connection view** and/or **firewall log** retained for jury.  
- Optional `monitor_capture_id` in WP-17.

### 4.2 Fail / block claim

- Host tools unavailable or refuse to capture → **A panel not green**; cannot state “Audience A passed.”  
- Public remote address or public DNS seen → **A fail**.  
- App widget without host artifact → **Never** as sole proof.

### 4.3 Runbook (must)

1. Apply air-gap / no-WAN policy **before** start snapshot.  
2. Start snapshot → run Expected Solution script (include inference + export moments).  
3. Stop snapshot **before** re-enabling any WAN.  
4. Label local runtime row green; confirm no public peers.

---

## 5. Audience B — operator (Monitors page)

| Tile | Required |
|---|---|
| Active task / job_id | Yes |
| model_id + selection reason (+ failover if any) | Yes |
| Device / VRAM (or CPU) | Yes (WP-10) |
| Grant status | Yes |
| Citations / file evidence labels | Yes when applicable |
| HITL queue / stale | Yes |
| Gate short denies | Yes |
| Sandbox status | Yes when code path |
| MCP allow/deny | Yes when used |
| lineage_degraded | Yes when set |

Redact secret bodies. Not a SIEM. Does not replace WP-17.

**Demo script:** open Monitors page during active task.

---

## 6. Demo vs org

| | Demo | Org |
|---|---|---|
| A | Snapshot pair + OS/firewall | Continuous / SOC ambition |
| B | Monitors page own task | Multi-task / **Admin** views ambition |
| Proof | Host **evidence pack** + B tiles + logs — **not CERT** | Same contract |

---

## 7. Must / ambition / deferred / never

### Must-work

1. A host-backed snapshot proof path (OS and/or firewall).  
2. Green local hop labelling.  
3. Hard block A claim without host evidence.  
4. B Monitors page with §5 tiles for own task.  
5. Runbook for snapshot timing.  
6. On-prem runtime ≠ “external cloud call.”

### Org-ambition

- Live A; continuous egress sensor; Admin multi-task B; wall display.

### Deferred

- Full packet forensics product; certified SOC.

### Never

- Fake secure badge.  
- Secrets on B.  
- Monitor decides plant safety.  
- Treating allowlisted local GPU hop as PS failure.

---

## 8. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Host connection/firewall evidence | Expected Solution |
| **Add** | A/B split; local hop; snapshot runbook; claim block | DM / red-team |
| **Refuse** | App-only theatre |

---

## 9. Demo acceptance

1. Start/stop snapshots show no public peers; green local runtime row present.  
2. Without host capture → A not claimable.  
3. Monitors page shows model+why, grant, device during inspect/code.  
4. Worker cannot see other users’ B data.  
5. Script includes opening Monitors page.

---

## 10. Next

GATE_90 A5 closed. Demo build uses start/stop artefact (G5).

---

## 11. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial snapshot/local-hop/claim-block pass |
| **1.1** | **FROZEN** 2026-09-19 GATE_90 A5: evidence pack language; not CERT; drop Approver-on-B ambition wording |

**Confidence:** **0.90**
