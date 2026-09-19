# WP-13 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-04 / WP-06 / WP-08 / WP-09 / WP-10 / WP-11 / WP-12 / WP-16 / WP-17 / WP-14  
**Status:** **SUPERSEDED by `WP-13_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-13_REDTEAM.md`. Verify: `WP-13_FREEZE_VERIFY.md`.  
**Job of WP-13:** **Monitors** — **Audience A** sovereign proof (**WAN/external = 0**, prefer **host/OS** evidence) and **Audience B** operator proof (live task: **card + why**, citations, HITL, sandbox, **grant**, plugin allow/deny, device/VRAM, lineage strip). App-only green badge while the OS still egresses = **fake**.

**Sources:** Official Expected Solution (“logs **or** visible network monitor”; no external calls **at any point** = sovereign proof); WP-00 Monitors A+B; User operator needs; WP-10 GPU/VRAM display; WP-17 log feed; WP-16 network-none; follow-list WP-13.

---

## One sentence (proposed)

KWB shows **two audiences** the truth: **A** — host-backed proof that the demo/org path makes **no public-internet calls**; **B** — operators see **what the task is doing now** (model, grant, cites, HITL, sandbox, plugins) without replacing the audit log.

---

## 1. Two audiences (locked intent)

| Audience | Job | Success look |
|---|---|---|
| **A — Sovereign / jury** | Prove air-gap | Visible **network/egress** evidence: no WAN to public internet during run |
| **B — Operator / worker** | Use like Claude-class tool | Live panel: card+reason, grant, citations, HITL queue, sandbox, MCP allow/deny, device/VRAM, degraded flags |

**Both required** at org design. Demo must show **A** and a **usable B slice**.

---

## 2. Audience A — sovereign monitor (proposed)

| Principle | Must |
|---|---|
| Prefer **host/OS** evidence | e.g. OS firewall log, `netstat`/Resource Monitor snapshot, disconnected NIC proof, local packet capture summary — **brand-free** |
| App widget alone | **Insufficient** as sole proof (theatre risk) |
| What “0” means | No connections to **public internet / WAN**; on-prem LAN to local runtime **allowed** and should be **labelled** as on-prem |
| When | Continuously or on-demand capture covering the **whole demo scenario** (“at any point”) |
| Tie-in | Optional pointer/id stored in WP-17 |

**Honesty:** If host tool unavailable, **fail the A proof** — do not invent a fake “SECURE” badge.

---

## 3. Audience B — operator monitor (proposed)

| Tile | Source |
|---|---|
| Active task / job_id | WP-06 |
| Selected **model_id** + reason (+ failover) | WP-06/24 |
| Device name / VRAM (or CPU) | WP-10 |
| Active **grant** status | WP-04 |
| Citations / file labels | WP-11/12 |
| HITL queue / stale | WP-05 |
| Gate short denies | WP-12 |
| Sandbox running/pass/fail | WP-16 |
| MCP/plugin allow/deny | WP-08 |
| `lineage_degraded` | WP-14 |
| Recent audit snippets | WP-17 (own task) |

**Not:** Full admin SIEM; not raw secret bodies.

---

## 4. Demo vs org

| | Demo | Org |
|---|---|---|
| A | One clear host-backed WAN=0 capture + label on-prem runtime hop | Continuous / SOC-fed ambition |
| B | Single operator panel for active task | Multi-task dashboards ambition |
| Placement | Visible during Expected Solution script | Always-on ops |

---

## 5. Must / ambition / deferred / never (proposed)

### Must-work

1. Audience A: host/OS-backed proof path for no **public** egress during demo.  
2. Label on-prem runtime traffic as **not** “external cloud.”  
3. Audience B panel with model+why, grant, HITL, sandbox, citations/labels, device/VRAM.  
4. No sole reliance on in-app “air-gapped ✓” without host evidence.  
5. B reads from live state + WP-17; does not replace audit.  
6. Plugin allow/deny visible when MCP used.

### Org-ambition

- Continuous egress sensor; multi-user B; wall displays; SIEM hooks.

### Deferred

- Certified SOC product; full packet forensics suite.

### Never

- Fake secure badge while WAN open.  
- Claiming LAN-to-GPU is a PS violation (it is on-prem).  
- Monitor = plant safety authority.  
- Dumping secrets on B panel.

---

## 6. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Host firewall / connection list *evidence*; operator status strip *idea* |
| **Add** | A/B split; on-prem vs WAN labelling; B tile catalogue |
| **Refuse** | App-only sovereign theatre; cloud status SaaS |

---

## 7. Boundaries

| Topic | Owner |
|---|---|
| Durable events | **WP-17** |
| Lineage diagram | **WP-14** |
| Eval of WAN=0 scenario | **WP-18** |
| Runtime probe | **WP-10** |

---

## 8. Open questions for decision maker

1. **Audience A primary tool (demo):** Prefer **OS built-in** connection view (Task Manager / Resource Monitor / `netstat`), **local firewall log**, or **offline packet capture** summary — pick one must-work path?  
2. **A refresh:** **Live** updating during demo, or **start/stop snapshot** pair enough?  
3. **B layout:** **Always-visible side panel**, or **dedicated Monitors page** (must-work)?  
4. **On-prem LAN line:** Must A explicitly show a **green “local runtime”** row separate from WAN=0, or only “no public IPs”?  
5. **Failure:** If host evidence unavailable, **block “sovereign demo” claim** (hard), or allow **log-only** Expected Solution alternative without A UI?  
6. **Who sees B:** **Worker own task only** (like audit), or **Approver also sees** tasks in their queue?

---

## 9. Next after your decisions

**Done.** Frozen as `WP-13_FREEZE.md` rev 1.0. Next: **WP-15**.
