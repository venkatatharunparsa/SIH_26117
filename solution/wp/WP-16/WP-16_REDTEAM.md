# WP-16 sandbox — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-16_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** see §0  
**Against:** Official Expected Solution (run+verify); WP-00 jail≠GPU; WP-05 H9; WP-07 sandbox_exec; WP-23 pre-exec HITL; Batch3 sandbox workflow; repo map WP-16.

---

## 0. DM answers (binding)

| Q | Decision |
|---|---|
| **1** | Isolation with **network none** — Docker/Podman `--network=none` **valid** pattern |
| **2** | Wall-time default **60s** |
| **3** | Semgrep-like static check = **ambition** |
| **4** | Internet / pip-in-sandbox = **Never** |
| **5** | **Calc-in-sandbox required** for SIH (compute in jail, not LLM) |
| **6** | **De-Docker:** must-work **must not lock** to Docker Desktop / Docker-as-brand; same controls via Podman **or** equivalent non-Docker process jail (WSL2/Linux host OK) |

---

## Verdict

| | |
|---|---|
| Direction | **Yes** |
| Missing | M1–M10 (de-docker clarity, calc artefact, egress proof, stdout caps, mount denylist, HITL wiring) |
| Overhyped | Container = secure; 60s = enough; calc = FFS; network=none without FS denylist |
| Confidence after freeze | **~0.88** → GO WP-08 |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Q1 vs Q6 tension | **Controls** frozen; **implementation menu**: Docker/Podman `--network=none` **or** non-Docker jail meeting same policy |
| **M2** | Calc required | Demo must run ≥1 **numeric check in sandbox** (e.g. simple formula/test); not LLM arithmetic as verify |
| **M3** | Admin max time | User/org may set ≤ Admin max; default 60s |
| **M4** | Mount denylist | No model weights, no host secrets, no Docker socket |
| **M5** | Stdout/stderr bound | Truncate; store in sandbox report |
| **M6** | Network attempt | Deny + log (align Audience A) |
| **M7** | Pre-populated deps | Only **offline** staged packages in image/jail — no runtime pip |
| **M8** | Pass ≠ decision | Restate H9 |
| **M9** | Concurrent sandboxes | Org may limit; demo one at a time |
| **M10** | Non-zero exit | Fail report; still H9 |

---

## 2. Overhyped

| Attack | Fix |
|---|---|
| **A1** Docker = security | Controls matter; de-Docker avoids Desktop lock-in |
| **A2** network=none enough | Need FS/time/CPU + denylist |
| **A3** Calc in sandbox = statutory calc | Still not FFS/safety decision |
| **A4** 60s always | Default only |
| **A5** Verify = green check | H9 human decision |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Jail ≠ inference (OpenHands/Cursor pattern) | E2B cloud |
| `--network=none` *or equal* | Docker-as-product identity |
| gVisor/nsjail/bubblewrap/Firecracker *org menu* | K8s Agent Sandbox as must |
| Offline deps staged | Runtime pip/WAN |

---

## 4. Disposition

**Applied.** → `WP-16_FREEZE.md` rev 1.0. Confidence **0.88**. **GO** → **WP-08**.

*Note: DM “dedocker” interpreted as no Docker Desktop lock-in; container `--network=none` remains a valid option beside non-Docker jails.*
