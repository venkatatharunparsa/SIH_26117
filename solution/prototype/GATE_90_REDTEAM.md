# GATE_90 adversarial red-team — before verify-accept

**Date:** 2026-09-19  
**Scope:** A2 WP-20 · A4 export leave · A5 Monitor A · B1–B7 design locks · claimed scores ≥0.91  
**Method:** Dual-story hunt · caption vs Expected Solution · design-thinness · REAL code vs “LOCKED” · adversarial research (evidence ≠ CERT; maker≠checker; self-HITL ≠ plant SoD)  
**Verdict (rev 1.1):** Criticals **fixed**. Re-score: arch **≥0.90** · design **≥0.90** · execute **~0.52**. Kickoff **GO** for desk UI. DM may **verify-accept** arch+design freezes.

---

## Research anchors (used as attack lenses)

| Lens | Implication for KWB |
|---|---|
| Evidence pack ≠ certification | Monitor A artefact is posture proof; never CERT / accreditation |
| Maker must not grade checker | Self-HITL H2/H3 valid for **own-work export leave**; **invalid** as plant dual-control |
| Deny-before-effect | Export leave must enforce H2 fresh + H9/sandbox-red + secrets — policy alone ≠ gate |
| Air-gap residual | USB, host kernel, phone-home runtimes — snapshot cannot claim absolute WAN=0 |

---

## Verdict scores (honest vs claimed)

| Axis | GATE_90 claimed | **Honest after RT** | Why |
|---|---|---|---|
| Architecture freeze | ≥0.91 | **~0.84** | A1–A5 freezes OK; residual dual-story docs + WP-20 thin vs figures |
| Design info (build) | ≥0.91 | **~0.76** | DESK_IA thin; B3/B4 policy≠wire; B5 template; B7 catalogue stale labels |
| Kickoff contract | GO | **GO-WITH-FIXES** | Start desk build OK after scrub Criticals |
| Execute-ready | 0.38 | **~0.38** | Honest — no change |

**Verify-accept ≥0.91?** **NO** until Critical fixes below land (or scores rewritten to honest).

---

## Attack matrix

| ID | Attack | Sev | Evidence | Fix |
|---|---|---|---|---|
| **RT-01** | READY_CHECK still sells arch 0.68 / WP-05 Approver dual / WP-20 unfrozen | **C** | `READY_CHECK_ADVERSARIAL.md` | SUPERSEDED banner + point to GATE_90_REDTEAM |
| **RT-02** | ORG_DESIGN verify still FAIL WP-05 / “H3 soft-copy in-box” | **C** | `ORG_DESIGN_SHOW_VERIFY_ADVERSARIAL.md` | Align A6 to export leave; archive or PASS note |
| **RT-03** | WP-01/15 perspective+redteam still teach in-app Approver | **C** | `wp/WP-01/*_ARCHITECT*`, `WP-15_*` | Non-binding banner → freezes rev 2.0 |
| **RT-04** | PPT pack “WAN=0 proof” kills A5 if filled | **C** | `ppt-paused/`, `PROMPT_S2/S4` | Evidence pack language only; ban bare WAN=0 |
| **RT-05** | ORG residual M5/G7 “H3 in-box / inside provide” fights A4 | **H** | `ORG_ARCHITECTURE_DIAGRAMS.md` | Patch to export leave off-box |
| **RT-06** | Monitor A REAL = loopback snapshot ≠ WP-13 OS/firewall pack | **H** | `backend/app/monitor_a.py` vs WP-13 D1 | Jury honesty label or host capture runbook |
| **RT-07** | DESK_IA = screen names only — not ≥0.91 design | **H** | `DESK_IA.md` | Add deny codes + state machine H1→H2→stale→H3 |
| **RT-08** | B5 “LOCKED” while checklist unsigned | **H** | `eval/CHECKLIST.md` | Label **TEMPLATE lock**; design ≤0.80 until signed |
| **RT-09** | B7 says create-on-build for files that exist; FX-CODE missing | **H** | `FIXTURE_CATALOGUE.md` | Fix catalogue honesty |
| **RT-10** | B3/B4 locked but export has no H9 / no artefact_version / no sandbox-red | **C** | `backend/app/main.py` export | Implement on build; demote “REAL” claims until then |
| **RT-11** | DEMO_TECH_STACK marks H9 REAL; code has no H9 | **H** | `DEMO_TECH_STACK.md` | Mark PLANNED / PARTIAL |
| **RT-12** | WP-20 §10 says do B-rows next; GATE says B DONE | **M** | `WP-20_FREEZE.md` §10 | Point next = implement desk |
| **RT-13** | APPLICATION_FLOW title “discussion draft” vs LOCKED | **M** | header | Drop draft wording |
| **RT-14** | Org continuous J vs demo start/stop — slide slip risk | **M** | O6 vs DEMO MonA | Caption org vs demo slice |
| **RT-15** | WP-05 verify still “next A2–A5” | **M** | `WP-05_FREEZE_VERIFY.md` | Mark GATE closed |
| **RT-16** | Spine deny ≠ Audience A host proof | **H** | gateway + monitor_a | Separate in runbook |
| **RT-17** | PPT may claim ≥2 model_ids without floor label | **H** | models.yaml vs ppt | Force single-tag adopt on G1 slides |
| **RT-18** | Superseded WP-20 draft still readable without banner discipline | **L** | connection draft | Cite freeze only |

---

## Locked-claim results

| Claim | Result |
|---|---|
| A2 WP-20 FROZEN | **PASS** as freeze file; residual High |
| A4 export leave | **PASS** in freezes; **FAIL** residual ORG/PPT language |
| A5 evidence ≠ CERT | **PASS** in freezes; **FAIL** residual PPT/READY |
| B1–B7 as “enough to build” | **PASS-WITH-FIXES** (thin but directional) |
| B1–B7 as “design ≥0.91” | **FAIL** — overclaim |
| Kickoff start desk | **PASS-WITH-FIXES** after Critical scrub |
| Verify-accept GATE ≥0.91 | **NO-GO** |

---

## Must-fix before verify-accept (Critical)

1. Honesty-rewrite GATE_90 scores to ~0.84 / ~0.76 (or fix all Criticals then re-score).  
2. SUPERSEDE READY_CHECK + ban PPT fill from stale WAN=0 / Approver text.  
3. Fix FIXTURE_CATALOGUE create-on-build lies.  
4. Explicitly separate: **policy lock (B3/B4)** ≠ **implemented REAL**.  
5. Patch ORG residual H3 in-box language.

## May start desk build now if

- Scores honesty-fixed  
- Builder uses only freezes + DESK_IA + FIXTURE + WP-18 (not READY_CHECK / ppt-paused / old WP perspectives)  
- First code sprint = H1 fixture path · H9/G10 on export · artefact_version/stale  

---

## Changelog

| Rev | Note |
|---|---|
| **1.0** | Pre-verify adversarial RT — GO-WITH-FIXES; verify ≥0.91 NO-GO |
| **1.1** | Criticals fixed 2026-09-19: dual-story scrub · DESK_IA wires · H1/H2/H9/G10 REAL · PPT WAN=0→evidence pack · smoke PASS. Honest arch/design **≥0.90**; execute ~0.52. **DM may verify-accept arch+design.** |
