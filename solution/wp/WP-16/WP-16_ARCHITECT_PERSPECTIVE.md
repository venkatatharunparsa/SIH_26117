# WP-16 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-05 / WP-07 / WP-23  
**Status:** **SUPERSEDED by `WP-16_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-16_REDTEAM.md`.  
**Job of WP-16:** Isolated **run and verify** of generated code/tests — **jail ≠ GPU/inference**; **network none** at org intent; resource limits; produce sandbox report. HITL before exec (agent/T2–T4) and **H9** after remain WP-05/23.

**Sources:** Official Description + Expected Solution; WP-00 sandbox plane; WP-07 `sandbox_exec`; Batch3 coding sandbox workflow (Observed prior); repo map OpenHands jail≠inference, container `--network=none`, gVisor/nsjail menu.

---

## One sentence (proposed)

KWB verifies code by running it in an **isolated sandbox** (no WAN, capped CPU/mem/time, limited FS) that is **never** the GPU inference process — pass/fail is **evidence**, not a plant decision (**H9** still required).

---

## 1. Why this WP

| Without WP-16 | Failure |
|---|---|
| “Verified” = printed code | Expected Solution lie |
| Jail wraps Ollama/vLLM | Inference dies or model weights exposed |
| Network on | Breaks sovereign / exfil |
| No limits | Host DoS |

---

## 2. Planes (do not collapse)

| Plane | Runs | Must not |
|---|---|---|
| **Runtime (GPU)** | Open-weight inference `/v1` | Execute untrusted user/agent code |
| **Sandbox** | Generated tests/scripts/calc checks | Host GPU server; plant SoR; WAN |
| **Workbench** | Orchestrates HITL + grant + report | Trust sandbox green as Approver |

---

## 3. Sandbox contract (proposed must)

| Control | Rule |
|---|---|
| **Network** | **None** (org intent + demo) — `--network=none` or equivalent |
| **FS** | Whitelist read of task workspace inputs; temp write only inside jail workdir; no host home / no model weight paths |
| **Process** | No privilege escalation; no Docker-in-Docker required for demo |
| **Resources** | CPU / memory / wall-time caps (exact numbers later; must exist) |
| **Language** | At least one demo language path (e.g. Python) — brand not locked |
| **Output** | stdout/stderr truncated + **pass/fail** + command list → sandbox report artefact |
| **Egress** | Fail if sandbox process attempts network (monitor/deny) |

**Verify** = execute tests or check script **and** record result — not LLM saying “looks correct.”

---

## 4. Lifecycle (with prior freezes)

1. Code specialist proposes code under grant (WP-07).  
2. If T2–T4-influenced → **HITL before exec** (WP-23).  
3. Run in sandbox → machine pass/fail report.  
4. **H9** human accept/reject as **decision** (WP-05).  
5. Export package → **H3** + light secret scan.  
6. Material edit → stale → re-HITL / re-H9 as applicable.

---

## 5. Org vs demo

| | Demo | Org |
|---|---|---|
| Isolation | Container `--network=none` (or equal) enough | May harden: gVisor / nsjail / bubblewrap / Firecracker (*menu*, not locked) |
| Languages | One path showable | Admin allowlist of runtimes |
| Calc | Optional; if shown, compute in sandbox not LLM | Same |

---

## 6. Must / ambition / deferred / never (proposed)

### Must-work

1. Jail ≠ GPU/inference process.  
2. Network none.  
3. Run + verify with pass/fail report artefact.  
4. Resource caps exist.  
5. FS whitelist / temp workdir.  
6. Integrates HITL pre-exec + H9.  
7. Offline; no E2B/cloud sandbox SaaS.

### Org-ambition

- Hardened isolation menu; multi-language allowlist; Semgrep optional pre-check; longer job queues.

### Deferred

- K8s Agent Sandbox as product; full Firecracker fleet.

### Never

- Wrap GPU/Ollama in code jail.  
- Cloud remote sandbox (E2B etc.).  
- Network-enabled “convenient” demo.  
- Sandbox pass = safety/FFS/statutory decision.  
- OpenSandbox / DeerFlow K8s as KWB identity.

---

## 7. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | OpenHands/Cursor *jail ≠ inference*; container `--network=none`; org isolation menu (gVisor/nsjail/…) |
| **Add** | Caps; FS rules; report artefact; HITL wiring |
| **Refuse** | E2B cloud; K8s-as-prototype-must; OpenSandbox-as-product |

---

## 8. Open questions for decision maker

1. **Demo isolation:** Docker/Podman `--network=none` as must-work default — **yes**?  
2. **Wall-time default (demo):** e.g. **30s** / **60s** / unset?  
3. **Pre-exec static check (Semgrep-like):** must-work light, ambition, or skip?  
4. **Internet in sandbox “for pip”:** **Never** (recommended) — confirm?  
5. **Calc demo in sandbox:** required for SIH, or optional if code tests alone prove verify?  
6. **Sandbox host OS:** Linux container on Windows demo via Docker Desktop OK, or require native Linux host for org paper?

---

## 9. Next after your decisions

**Done.** Frozen as `WP-16_FREEZE.md` rev 1.0. Next: **WP-08**.
