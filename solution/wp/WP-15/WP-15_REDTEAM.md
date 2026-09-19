# WP-15 personal `.md` — adversarial red-team + DM decisions

> **NON-BINDING SUPERSEDED.** Historical only. Binding = freezes WP-01/05 rev 2.0: Approver=org paper only; self-HITL; export leave; Admin=IT. (Skill promote H6 ≠ in-app Approver queue.)

**Date:** 2026-09-18  
**Target:** `WP-15_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** User self-learning intent; WP-00 Never (no weight train / no auto-promote); WP-05 H6; WP-07 personal shelf; WP-23 T3; Agent Skills Spec; **Not** Official PS mandate.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Demo must-work = **freeform `.md` note** (SKILL.md pack = ambition) |
| **2** | **User-only** authorship (no agent-proposed drafts must-work) |
| **3** | Demo shows **full H6 promote accept** |
| **4** | Load only when **pinned** and/or **tag-matched** to job |
| **5** | Secrets = **export scan only** (WP-12/23) — no extra personal-shelf scanner must |
| **6** | **Admin hold** on promote/export paths (retention) |

---

## Verdict

| | |
|---|---|
| Missing | M1–M10 (pin bypass; freeform≠skill tools; H6 demo dual-role; hold vs user delete; tag spoof; PS honesty; T3 still) |
| Overhyped | Freeform note = full Agent Skills; export scan = no residue in personal files; pinned = security |
| Confidence | **~0.88** → GO WP-18 |

---

## Attack A — Freeform `.md` only (Q1)

| Attack | Fix |
|---|---|
| **A1** Note claims `allowed-tools: *` | Freeform notes are **guidance text only** — **no** tool allowlist power; only SKILL.md on personal shelf may declare tools (ambition) intersected with grant |
| **A2** Jury thinks Skills Spec incomplete | Honesty: demo = note harness; SKILL.md = org-ambition |

---

## Attack B — User-only (Q2)

| Attack | Fix |
|---|---|
| **B1** Agent silently writes personal shelf | Must-work: **no** agent write to personal shelf; user editor only |
| **B2** “Assist” smuggled as autocomplete into file | Disallow auto-save from model to personal path |

---

## Attack C — Full H6 accept (Q3)

| Attack | Fix |
|---|---|
| **C1** Worker self-H6 | Role-correct: Approver/Admin (WP-05); dual-role demo OK if labelled |
| **C2** Promote copies secrets into org shelf | H6 review shows content; export/promote still G-secret if packaged; org shelf still T3 |

---

## Attack D — Pin / tag match (Q4)

| Attack | Fix |
|---|---|
| **D1** Default load all personal notes | **Default off**; require pin and/or tag∩job |
| **D2** Tags forged to match every job | Tags user-set; orchestrator match is advisory; still T3 + grant |
| **D3** Pin forgotten → feature invisible | Demo script: pin before task |

---

## Attack E — Export scan only (Q5)

| Attack | Fix |
|---|---|
| **E1** Secrets sit in personal `.md` on disk | Honesty Limits: scan at **H3/export** and promote package; not continuous DLP |
| **E2** Skip scan on H6 promote copy | **Promote path** runs light secret heuristic before org shelf write (same WP-23 patterns) — still “export/promote scan” family, not a second product |

**Decision:** No extra always-on scanner; **H3 and H6-promote** both invoke light secret heuristics.

---

## Attack F — Admin hold (Q6)

| Attack | Fix |
|---|---|
| **F1** User deletes during incident | **Hold** when: pending H6, or included in export package, or Admin legal hold flag |
| **F2** Hold forever blocks UX | Hold scoped; Admin release |
| **F3** Hold ≠ org SoR | Still personal/org shelf inside KWB |

---

## Attack G — PS / training

| Attack | Fix |
|---|---|
| **G1** Slide “PS requires self-learning” | **Refuse** — User feature only |
| **G2** Fine-tune marketed as harness | Never |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | Freeform = text only; no tool power |
| **M2** | User-only writes |
| **M3** | H6 full accept demo; role-correct |
| **M4** | Pin/tag load gate |
| **M5** | Secret heuristics on H3 + H6 promote |
| **M6** | Admin hold rules |
| **M7** | T3 always; separate shelf |
| **M8** | Block internet-compat skills |
| **M9** | Not weight training |
| **M10** | Not PS-mandated |

---

## 2. Overhyped / refuse

| Refuse |
|---|
| Agent auto-write personal shelf |
| Auto-promote |
| WAN skill hub |
| Personal `.md` as ACL |
| Weight training |

---

## 3. Disposition

**Applied.** → `WP-15_FREEZE.md` + `WP-15_FREEZE_VERIFY.md`. Confidence **0.88**. **GO** → **WP-18**.
