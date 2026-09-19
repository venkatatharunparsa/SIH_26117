# WP-16 Execution sandbox — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-05 / WP-07 / WP-23.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-16_ARCHITECT_PERSPECTIVE.md`, `WP-16_REDTEAM.md`, **DM 2026-09-18** (network none; 60s default; Semgrep ambition; no pip/WAN; calc required; de-Docker).  
**Findings SoT:** `WP-16_REDTEAM.md`  
**Product:** **KWB**

**Isolation brand:** not locked (Docker/Podman **or** equivalent non-Docker jail).

---

## 1. One-sentence contract

KWB **runs and verifies** agent/user code in an isolated **sandbox** with **no network**, default **60s** wall time, FS/CPU/mem caps, and **no runtime package fetch** — the sandbox is **never** the GPU inference process; **calc checks run in the jail**; pass/fail is **evidence** only (**H9** decides); must-work must **not** depend on Docker Desktop as the only path (**de-Docker**).

---

## 2. Limits

| True | False / refuse |
|---|---|
| Network none + caps + FS denylist | Container brand = security complete |
| Calc in sandbox | Sandbox = FFS/statutory authority |
| Pass/fail report | Replaces H9 |
| De-Docker = no Desktop lock-in | Ban all containers forever |
| 60s default | Eternal SLA |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Network **none**; Docker/Podman `--network=none` is a **valid** implementation |
| **D2** | Wall-time **default 60s** (≤ Admin max) |
| **D3** | Static Semgrep-like check = **ambition** |
| **D4** | Internet / pip / package registry in sandbox = **Never** |
| **D5** | **Calc-in-sandbox required** for SIH demo (≥1 numeric verify in jail) |
| **D6** | **De-Docker:** must-work isolation **must not require Docker Desktop**; Podman or **non-Docker** process jail OK if same controls met |

---

## 4. Planes (frozen)

| Plane | May | Must not |
|---|---|---|
| **Runtime GPU** | Inference `/v1` | Execute untrusted code |
| **Sandbox** | Run tests/scripts/calc checks | Host GPU server; WAN; SoR; read model weights |
| **Workbench** | HITL, grant, report | Treat green as Approver |

---

## 5. Controls (must)

| Control | Rule |
|---|---|
| **Network** | None — block/deny; log attempts |
| **Wall time** | Default **60s**; configurable ≤ Admin max |
| **CPU / memory** | Caps exist (exact values Admin/demo later) |
| **FS read** | Whitelist task workspace inputs only |
| **FS write** | Jail workdir / temp only |
| **Mount denylist** | No model weight dirs; no host secrets; no Docker socket; no KWB grant DB |
| **Deps** | Only **pre-staged offline** packages inside image/jail |
| **Stdout/stderr** | Captured, **truncated**, stored in sandbox report |
| **Exit code** | Non-zero → fail in report |
| **Concurrency** | Demo: one sandbox job at a time |

**Implementation menu (must pick one that meets controls):**

1. Podman/Docker `--network=none` (not Desktop-mandatory), or  
2. Non-Docker process jail (e.g. OS job object / bubblewrap / nsjail on Linux/WSL2) with network disabled equivalently.

---

## 6. Lifecycle (prior freezes)

1. Code proposed under grant.  
2. Agent/T2–T4 → **HITL before exec** (WP-23).  
3. Sandbox run → report artefact.  
4. **H9** human decision (WP-05).  
5. Export → H3 + secret scan.  
6. Edit → stale / re-run as WP-05.

---

## 7. Calc requirement (D5)

- SIH must-work includes ≥1 path where a **numeric check** executes **in the sandbox** (example shape: unit test or script asserting a formula — brand/formula not locked).  
- LLM must **not** be the verifier of that numeric result.  
- Still **not** a safety/FFS/statutory decision (WP-00 Never).

---

## 8. Artefacts

| Artefact | Content |
|---|---|
| **Sandbox report** | pass/fail, exit code, truncated logs, commands, time used, network-deny notes |
| **Code artefact** | Sources in KWB workspace (WP-01) |

---

## 9. Must / ambition / deferred / never

### Must-work

1. Jail ≠ GPU.  
2. Network none; no pip/WAN.  
3. 60s default; caps; FS whitelist/denylist.  
4. Run+verify report.  
5. Calc-in-sandbox demo.  
6. De-Docker (no Docker Desktop lock-in).  
7. HITL pre-exec + H9 wiring.  
8. Offline only.

### Org-ambition

- Semgrep-like static gate; gVisor/Firecracker/nsjail menu; multi-language allowlist; higher Admin max time.

### Deferred

- K8s Agent Sandbox product; full microVM fleet.

### Never

- Wrap GPU/Ollama in code jail.  
- Cloud sandbox (E2B etc.).  
- Runtime internet/pip.  
- Sandbox pass = plant/safety decision.  
- Docker/OpenSandbox/DeerFlow as product identity.  
- Mount Docker socket into jail.

---

## 10. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Jail ≠ inference pattern | WP-00 / OpenHands-class |
| **Adopt** | `--network=none` *or equal* | Sovereign |
| **Adopt** | Org isolation menu *names* | Hardening path |
| **Add** | 60s; calc required; de-Docker; denylist; report | DM / red-team |
| **Refuse** | E2B; Docker Desktop lock-in; K8s-as-must; pip-at-runtime |

---

## 11. Demo acceptance

1. Code test runs in jail → pass/fail report (not “LLM says OK”).  
2. Numeric/calc check runs **in sandbox**.  
3. Network attempt denied/logged.  
4. Inference still works **outside** jail (prove not wrapped).  
5. No pip/WAN during run.  
6. Works without Docker Desktop (Podman or non-Docker jail).  
7. H9 still required after green.

---

## 12. Next

**WP-08** — Plugin host (MCP + skill packs).

---

## 13. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze + DM + de-Docker + calc required |

**Confidence:** **0.88**
