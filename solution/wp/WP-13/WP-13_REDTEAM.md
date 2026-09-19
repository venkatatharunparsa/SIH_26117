# WP-13 monitors — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-13_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** Official Expected Solution (logs **or** visible network monitor; no external calls at any point); WP-00 Audience A+B; WP-10 device display; WP-16/09 on-prem LAN allowed; WP-17 own-task scope.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Audience A uses **OS connection view** and **firewall log** (both in must-work toolbox) |
| **2** | **Start/stop snapshot pair** (not continuous live A) |
| **3** | Audience B = dedicated **Monitors page** |
| **4** | Show explicit **green local hop** (on-prem runtime) separate from WAN=0 |
| **5** | If host evidence unavailable → **block sovereign claim** (no fake badge; log-only alone ≠ A pass) |
| **6** | B visibility = **Worker own task** only |

---

## Verdict

| | |
|---|---|
| Missing | M1–M12 (snapshot gap mid-run; LAN mislabelled WAN; dual-tool burden; Monitors page missed; Approver blind; firewall empty≠safe; localhost exfil) |
| Overhyped | Snapshot pair = continuous proof; green local = audited ACL; OS view = complete DLP |
| Confidence | **~0.87** → GO WP-15 |

---

## Attack A — Start/stop snapshots (Q2) vs “at any point”

| Attack | Fix |
|---|---|
| **A1** Egress only mid-demo between snapshots | Require snapshots cover **script window**; optional mid-script spot check; document “capture during active inference/export” |
| **A2** Stop snapshot after disconnecting WAN for photo | Procedure: NIC policy **before start**; stop while workload still running or immediately after last step without re-enabling WAN |
| **A3** Live would catch more | Org-ambition continuous; demo = pair + procedure honesty |

**Decision:** D2 + mandatory **runbook** for capture timing.

---

## Attack B — OS view + firewall log (Q1)

| Attack | Fix |
|---|---|
| **B1** Two tools → demo chaos | Must-work: **either** produces A evidence; **prefer both** when available; acceptance = at least **one host-backed** artifact + checklist |
| **B2** Empty firewall log ≠ no egress | Correlate with OS connection list; “no public remote addresses” criterion |
| **C3** Miss DNS/DoH | Criterion includes DNS to public resolvers as fail |

---

## Attack C — Green local hop (Q4)

| Attack | Fix |
|---|---|
| **C1** Jury thinks any LAN is “external call” | Explicit **LOCAL RUNTIME** row (loopback/on-prem allowlist IP) marked **allowed on-prem** |
| **C2** Green-wash cloud IP as local | Only WP-09 allowlisted endpoints may be green |
| **C3** Local hop to malicious intranet | Out of A scope; grant/Admin allowlist separate |

---

## Attack D — Block sovereign claim (Q5)

| Attack | Fix |
|---|---|
| **D1** Fall back to “logs say so” only | Expected Solution allows logs **or** monitor — freeze: **A UI claim** requires host evidence; without it **cannot assert Audience A pass**. May still show WP-17 logs but **no WAN=0 badge** |
| **D2** Soft block ignored | Demo script hard gate: no A panel green without evidence files/snapshots |

---

## Attack E — Monitors page + own task (Q3/Q6)

| Attack | Fix |
|---|---|
| **E1** Page buried; jury never opens | Demo script step: open Monitors page during run |
| **E2** Approver cannot see worker task on B | Approver uses HITL UI; B = worker own-task; Admin may see more (ambition) |
| **E3** Side panel would be stickier | DM chose page — OK if scripted |

---

## Attack F — App theatre

| Attack | Fix |
|---|---|
| **F1** In-app “SECURE” without host files | Never — D5 |
| **F2** B shows secrets | Redact like WP-17 |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | Snapshot timing runbook |
| **M2** | Public vs local classification rules |
| **M3** | Green local hop only for allowlisted runtime |
| **M4** | A hard-fail without host evidence |
| **M5** | B Monitors page tile set |
| **M6** | Own-task scope |
| **M7** | DNS/public IP fail criteria |
| **M8** | Dual-tool: ≥1 host artifact must |
| **M9** | On-prem LAN ≠ PS violation |
| **M10** | A pointer optional in WP-17 |
| **M11** | Device/VRAM on B (WP-10) |
| **M12** | No continuous A required for demo |

---

## 2. Overhyped

| Claim | Reality |
|---|---|
| Snapshot = forever continuous | Windowed proof + procedure |
| Firewall log alone | Correlate connections |
| Green local = security complete | Routing honesty only |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Host OS + firewall evidence | App-only sovereign badge |
| Explicit local hop label | Calling on-prem GPU “external” |
| Hard block A without evidence | Fake secure UI |

---

## 4. Disposition

**Applied.** → `WP-13_FREEZE.md` + `WP-13_FREEZE_VERIFY.md`. Confidence **0.87**. **GO** → **WP-15**.
