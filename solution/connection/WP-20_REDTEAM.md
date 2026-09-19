# WP-20 KWB solution — full-system adversarial red-team + critique

**Date:** 2026-09-18  
**Target:** `WP-20_ORG_CONNECTION.md` + **entire frozen WP set** as one product  
**Mode:** Attack the **integrated** solution — seams, overclaims, PS gaps, demo failure, org fantasy.  
**Against:** Official Title/Description/Expected Solution; all `WP-*_FREEZE.md`.

---

## Verdict (executive)

| Question | Answer |
|---|---|
| Is the connected design **coherent**? | **Mostly yes** — planes, loop, plugs, Never align |
| Is it **overbuilt** vs Expected Solution? | **Yes risk** — org catalog ≫ SIH demo; must ruthlessly MOCK/LATER |
| Does it **honestly** match Official Description? | **Partial** — PPT/Excel/calc/spreadsheet **deferred** but listed in Description |
| Biggest integration dangers | Seam ordering; HITL fatigue; Audience A snapshot gap; freestyle privilege; eval rubber-stamp |
| Ready to freeze WP-20? | **Yes after applying §Fills** below |
| Ready to code? | **Not until** REAL/MOCK/LATER overlay |
| **System confidence** | **0.82** (design) / **0.00** (implementation) |

---

## Attack 1 — Complexity vs SIH reality

| Attack | Why it hurts | Critique / fix |
|---|---|---|
| **C1** 24 WPs of policy before one binary | Jury cares about G1–G5 working | Prototype overlay must mark most boxes **MOCK/LATER**; build spine = G1–G10 only |
| **C2** Every gate on every path | Demo dies in HITL clicks | Demo script: minimum H1→H2→H3; dual-role labelled; no org-ambition gates live |
| **C3** “Same architecture” hides 10× scope | Team builds org forever | Freeze: **demo_ready** (WP-18) is the only ship gate for SIH |

**Finding:** Design is strong; **delivery risk is the main enemy**. Overlay is mandatory, not optional.

---

## Attack 2 — Official Description vs deferred ambition

| PS Description item | In freezes | Honesty |
|---|---|---|
| Spreadsheet work | Ambition / deferred (WP-00/01/07) | **Must say MOCK/LATER** — do not imply must-work |
| PPT / Excel deliverables | Deferred | Same |
| Calculations with steps | Sandbox calc must; “engineering calc product” thin | Show calc-in-jail; don’t claim full calc suite |
| Past correspondence KB | Ambition corpus (WP-11) | Demo MOCK SOP/policy OK; don’t claim live mail |
| “Multiple models at once” | Catalog yes; VRAM sequential | Caption already honest — keep it |

**Finding:** WP-20 §8 Expected Solution test **passes**; Description **overhang** must be labelled in WP-20 so PPT later doesn’t lie.

---

## Attack 3 — Diagram / loop seams (integration bugs)

| Seam | Attack | Fix for WP-20 |
|---|---|---|
| **S1** Pack → Gates → HITL order | Model streams secrets to UI before G-secret | Loop must say: **gates before unmasked view** (WP-12); hold stream |
| **S2** Claims vs Pack | Claims after retrieve but model may invent before H7 | Claims/H7 bind **record-facing H2**, not every token; packer carries H7 state |
| **S3** Orch “brain” bypasses gateway | Specialist talks CUDA | Explicit **Never**: only gateway opens runtime socket |
| **S4** Tools write store then skip gates | Export raw workspace file | All **off-box** paths through H3+G-* |
| **S5** MCP egress while A shows green | Plugin WAN | WP-08 default deny + A capture during MCP demo |
| **S6** Audit fail-closed vs lineage_degraded | Operators confuse | WP-20 callout: audit hard; lineage soft |
| **S7** Classifier (WP-00) missing from diagram | Sensitivity magic | Add **classifier stub** box → ambition/MOCK; not silent |
| **S8** Templates missing from diagram | Word path unclear | Add **templates** on path to DRAFT (WP-01) |

**Finding:** Connection doc under-drew templates, classifier, stream-hold. **Fill required.**

---

## Attack 4 — Security theatre vs real residue

| Attack | Reality | Fix |
|---|---|---|
| **T1** Grants + HITL + gates = “secure” | Residue, screenshots, USB malware, eyeball weights | Keep Limits language; never CERT-In/DPDP badge |
| **T2** Snapshot A | Mid-window egress | Runbook + G5; optional mid-check in eval |
| **T3** Light secret scan | Misses novel secrets | Honesty; block on hit only |
| **T4** Authz-first RAG | Mis-tagged MOCK corpus | Demo curation; org discovery worksheet |

**Finding:** Design is **defence-in-depth assistive**, not plant accreditation. WP-20 must say so in one line.

---

## Attack 5 — Demo path contradictions

| Tension | Risk | Resolve |
|---|---|---|
| Freestyle NL (WP-06) vs privilege | Invent tools | Constrained map; freeze already — **restate in WP-20** |
| One capable LLM vs G1 two ids | Skip auto-select | Proof script **forces** two task types / two cards |
| Dual-role HITL | Self-approve | Labelled role clicks only |
| Jury-day audit wipe vs eval/ | Lose evidence | eval/ pack retained separately through jury |
| CPU+GPU demo vs “GPU server” story | Jury confusion | Monitors show honest device string |
| Import UI + pre-staged weights | Fake offline | Script: import from USB/MOCK path with A on |

---

## Attack 6 — “Software brain” governance

| Attack | Fix |
|---|---|
| Orch becomes shadow Approver | Never list + HITL hard gates unchanged |
| Orch dumps capability index into prompt | Index ≠ context (WP-06/21) |
| Rules+LLM plan strips H1 | Rails verify cannot remove mandatory gates |

**Finding:** Brain framing is OK **if** WP-20 repeats the ceiling next to the diagram.

---

## Attack 7 — Missing / thin product pieces

| Gap | Severity | Disposition |
|---|---|---|
| PPT/Excel/spreadsheet | PS Description | **LATER** — explicit |
| Live plant connectors | Org | **LATER/MOCK** |
| Continuous Audience A | Org | Ambition |
| SHA-256 offline | Org | Ambition |
| Personal SKILL.md | Ambition | OK |
| Formal IdP/SSO | Org | MOCK users demo |
| Templates library detail | Medium | Add to diagram; REAL for docx templates in overlay |
| Policy-as-corpus vs T0 policy | Confused in slides | T0 = Never/HITL engine; S3 = retrieved policy chunks |

---

## Attack 8 — Eval / “done” gaming

| Attack | Fix |
|---|---|
| Sign checklist without running | eval/ paths mandatory (WP-18) |
| Pass G1–G5 skip G9–G10 | No waivers |
| Happy-path video | demo_ready boolean |

---

## Attack 9 — What would make the solution **fail** at finale

1. No two model_ids in log.  
2. Word path broken / chat-only.  
3. Sandbox missing or networked.  
4. Any public fetch during demo.  
5. “Secure” badge without host snapshot.  
6. Claiming PPT/Excel/live DMS as done when MOCK.

**Finding:** WP-18 already encodes (1–5). WP-20 must encode (6) in overlay rules.

---

## Fills — apply to WP-20 before freeze

| ID | Fill |
|---|---|
| **F1** | Add **templates** + **classifier (MOCK/ambition)** to diagram/loop |
| **F2** | Loop step: **unmasked view only after G-secret/G-class** |
| **F3** | Explicit: **only gateway** talks to runtime |
| **F4** | Description overhang table: PPT/Excel/spreadsheet/correspondence = not must-work |
| **F5** | One-line: controls **help**; not plant certification |
| **F6** | Prototype rule: build order = **G1–G10 spine** first |
| **F7** | Restate orch brain ceiling beside diagram |
| **F8** | eval/ retained even if jury-day audit wipe |

---

## Adopt / refuse (system level)

| Adopt | Refuse |
|---|---|
| Connected loop + plugs + Never | Coding before REAL/MOCK/LATER |
| Demo slice of org architecture | Shipping Description-complete PPT/Excel as must |
| Defence-in-depth honesty | “Fully secure / CERT-In certified” claims |
| G1–G10 as done bar | Architecture astronomy without eval/ |

---

## Disposition

1. Patch `WP-20_ORG_CONNECTION.md` with F1–F8.  
2. You review → **verify OK**.  
3. Freeze `WP-20_FREEZE.md`.  
4. Open **prototype overlay** (REAL/MOCK/LATER).  

**System design confidence after fills: ~0.84.** Implementation still **0.00**.
