# WP-18 fail-closed + eval — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-18_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** Official Expected Solution; WP-00 Never/fail-closed; deny paths in WP-04/09/12/13/16/17/22/23/24; follow-list goldens.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | **Yes** → must-work goldens = **G1–G10** (full set) |
| **2** | **Manual checklist** (no required automated runner) |
| **3** | Include **deliberate fault injection** (revoke, bad model, …) |
| **4** | **Yes** → require **`eval/` evidence pack** |
| **5** | **Any teammate** may sign checklist |
| **6** | Any must golden fail → **block “demo ready”** (no waivers) |

---

## Verdict

| | |
|---|---|
| Missing | M1–M10 (manual rubber-stamp; inject coverage list; eval/ contents; demo-ready definition; degrade vs fail-closed; G5 host dependency) |
| Overhyped | Checklist alone = continuous quality; any teammate = no accountability |
| Confidence | **~0.88** → GO WP-19 |

---

## Attack A — Manual checklist (Q2) + any signer (Q5)

| Attack | Fix |
|---|---|
| **A1** Checkbox without evidence | **eval/** pack mandatory (Q4); each G# links to artifact paths |
| **A2** Teammate signs without running | Sign attests “I ran / witnessed”; false sign = process fail — freeze requires **named signer + date** on checklist |
| **A3** No automation forever | Ambition: script later; must-work stays manual |

---

## Attack B — G1–G10 + no waivers (Q1/Q6)

| Attack | Fix |
|---|---|
| **B1** Soft “almost pass” | **Demo ready** boolean = all G1–G10 pass; else blocked |
| **B2** Skip G9/G10 as “security optional” | All ten must |
| **B3** G5 blocked by missing host tools | Per WP-13: cannot claim A — then **G5 fail** → demo not ready (honest) |

---

## Attack C — Deliberate inject (Q3)

| Attack | Fix |
|---|---|
| **C1** Vague “inject somehow” | Minimum inject set: **revoke mid-task**, **unregistered/disabled model_id**, plus at least one of: secret-in-draft, sandbox-red, empty cite/`NOT FOUND` |
| **C2** Inject breaks machine permanently | Use MOCK fixtures; restore script in runbook |
| **C3** Inject not logged | Must leave WP-17 deny events |

---

## Attack D — eval/ pack (Q4)

| Attack | Fix |
|---|---|
| **D1** Empty folder | Minimum contents: checklist.md; routing log extract; docx path; sandbox report; A snapshots; deny logs for injects |
| **D2** Secrets in pack | Redact; hashes/ids only where needed |
| **D3** Pack becomes SoR | Evidence copy only |

---

## Attack E — Fail-open under demo pressure

| Attack | Fix |
|---|---|
| **E1** “Just this once” cloud | Never — G5/G8 catch |
| **E2** Silent default model | G8 + WP-09 |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | G1–G10 must; no waiver |
| **M2** | Manual checklist + named signer/date |
| **M3** | eval/ minimum manifest |
| **M4** | Inject minimum set |
| **M5** | demo_ready definition |
| **M6** | Failure matrix from architect §2 |
| **M7** | Degrade only where prior freezes allow |
| **M8** | Evidence retention = jury window (WP-17) |
| **M9** | No LLM-judge required |
| **M10** | Suite = prototype spine after WP-20 |

---

## 2. Disposition

**Applied.** → `WP-18_FREEZE.md` + `WP-18_FREEZE_VERIFY.md`. Confidence **0.88**. **GO** → **WP-19**.
