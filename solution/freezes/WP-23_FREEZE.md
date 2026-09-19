# WP-23 Untrusted content / injection — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-03 / WP-04 / WP-05. Reopen only if the decision maker explicitly says so.  
**Depends on:** those freezes (must not contradict; **clarifies** WP-05 sandbox agent path — see §6).  
**Inputs:** `WP-23_ARCHITECT_PERSPECTIVE.md`, `WP-23_REDTEAM.md`, **DM 2026-09-18** (OCR MOCK refuse; T1 claim; HITL before sandbox exec for T2–T4; heuristic refuse+log must; skills always T3; light export scan must).  
**Findings SoT:** `WP-23_REDTEAM.md`  
**Product:** **KWB**

**Stack / guardrail brands:** not locked. No cloud moderator.

---

## 1. One-sentence contract

OCR/VLM extracts (even `human_verified`), RAG chunks, MCP/tool text, personal `.md`, and skill/plugin bodies are **untrusted-as-instructions**: delimited as data under grants, unable to override **Never / HITL / grants**, with **heuristic refuse+log**, **HITL before sandbox exec** when T2–T4 influenced, and **light local secret heuristics** before export — H1 is not injection-complete.

---

## 2. Limits (anti overclaim)

| True | False / refuse |
|---|---|
| Delimiters + tiers + grants + HITL + Never | Heuristics alone “solve” injection |
| OCR MOCK demo proves refuse path | Demo = all RAG/MCP channels proven |
| HITL before exec reduces agent risk | HITL = complete security / replaces sandbox jail |
| Light secret scan catches obvious patterns | Full DLP / DPDP programme |
| T1 chat is a **claim** | User utterance is plant fact (WP-22) |
| Org skill still T3 data | Skill file = security boundary |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Must-work demo refuse proof = **OCR MOCK** inject → refuse + log. |
| **D2** | Chat utterance = **T1 claim** (not fact). |
| **D3** | **HITL before sandbox exec** whenever proposal/context is **T2–T4-influenced** (agent default). |
| **D4** | **Heuristic refuse + log = must-work**. |
| **D5** | Skill / org-skill body **always T3 delimited**. |
| **D6** | **Light local secret heuristics** before H3 export = must-work. |

---

## 4. Trust tiers (frozen)

| Tier | Examples | Authority |
|---|---|---|
| **T0 System** | Never list, grant/HITL engines, gateway schema, role policy | Not model-editable |
| **T1 Human direct** | Chat utterance (**claim**); H1 field corrections typed by worker; Approver gate clicks | Content influence; **cannot** break Never |
| **T2 Human-verified extract** | WP-03 `human_verified` | Evidence **data**; untrusted-as-instructions |
| **T3** | RAG chunks, MCP stdout, tool **descriptions/names**, personal `.md`, **all skill bodies** (incl. post-H6 org skills) | Data under grant; untrusted-as-instructions |
| **T4** | `machine_extract` pre-H1 | No draft/agent authority (WP-03 S6) |

**Lowest-wins:** tool-call effective trust = lowest tier of influencing context.  
**Multi-turn:** re-delimit each pack; injected text must not promote to T0 across turns.

---

## 5. Controls (must)

### 5.1 Delimit & label

- Untrusted blobs wrapped with explicit delimiters + `trust_label` / source id (exact strings → WP-21).  
- System policy: delimited content is **data**, not instructions.  
- Nested/fake delimiter breakout attempts → treat as T3 + **refuse/log** if override-pattern.

### 5.2 Never / grant / HITL override

Untrusted or model text **cannot**: disable Never; skip H1/H2/H3/H9/pre-exec sandbox HITL; widen grants; enable WAN; self-install MCP; auto-promote skills.  
Attempts → **heuristic refuse + log** (and H7 escalate when framed as user↔policy conflict).

### 5.3 Heuristic refuse catalog (minimum must-work)

Refuse+log when content (esp. T2–T4) attempts patterns such as:

- Ignore / override system or Never / policy  
- Disable HITL / auto-approve / skip human  
- Expand grant / fetch all corpora / disable ACL  
- Exfil / WAN / external URL fetch  
- “You are now” / role swap to unconstrained agent  
- Install plugin / promote skill without Admin/Approver path  

Heuristics are **assistive**; false positives may warn+HITL rather than silent allow. Missing heuristic engine → **fail-closed** on side-effect tools and export path for must-work.

### 5.4 Tool rails

- **Read-only** vs **side-effect** (workspace write, export, sandbox exec, MCP).  
- Side-effect: grant allowlist **and** HITL where WP-05/this WP require.  
- MCP names/descriptions = **T3**.  
- Args influenced by T2–T4 → lowest trust → side-effect HITL or deny.

### 5.5 Sandbox (clarifies WP-05 agent path)

| Step | Rule |
|---|---|
| Agent proposes code with T2–T4 in influencing context | **HITL before exec** (hard) |
| Exec in jail | Machine run after HITL allow (jail ≠ GPU — WP-16) |
| Accept as decision | **H9** still required (WP-05) |
| Export code package | **H3** + light secret scan |

Human-only typed code with **no** T2–T4 influence may use machine run then H9 (narrow exception). **Agent path = always pre-exec HITL.**

### 5.6 Skills & `.md`

- Always **T3 delimited**.  
- Cannot self-promote / self-install.  
- Personal `.md` ≠ org ACL (WP-04); promote only H6.

### 5.7 Light secret scan (pre-H3)

Local heuristics before export: e.g. PEM/`BEGIN PRIVATE KEY`, high-entropy key-like tokens, `password=`-style literals — pattern list Admin-extensible; brand not locked.  
Hit → block or force HITL re-confirm; log. **Never** cloud moderator.

---

## 6. Bind to grants

Untrusted text does not create access. Retrieve/MCP only under active grant + allowlist. “Fetch everything” inject → **deny**.

---

## 7. Must / ambition / deferred / never

### Must-work

1. Tiers + lowest-wins + delimiters.  
2. `human_verified` ≠ trusted instructions.  
3. Heuristic refuse+log (catalog §5.3) + fail-closed if missing.  
4. Pre-exec HITL for T2–T4/agent sandbox; H9 after.  
5. Skills always T3; `.md` rules.  
6. Light secret scan before H3.  
7. Offline only.  
8. Demo: **OCR MOCK** inject → refuse + log visible.  
9. T1 claim; T1 cannot break Never.

### Org-ambition

- Full local guardrail packs; SkillSpector-like pre-load scan; stronger PII; RAG-inject demo; OCR↔text-layer diff scores (WP-03).

### Deferred

- Certified red-team lab; cryptographic prompt attestation; enterprise DLP.

### Never

- Cloud injection moderator.  
- Skill restrictions as security.  
- H1 as injection-complete.  
- Untrusted text expands grants or skips HITL.  
- `.md` as system policy.  
- Silent allow on override heuristics failure.

---

## 8. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Delimiters; lowest-trust tool inheritance; MCP-security *ideas* | Spec/Observed |
| **Adopt** | Local guardrail *ideas*; Presidio-*idea* patterns | Must light scan |
| **Adopt** | Boundary below model | Atlas / repo map |
| **Add** | Tier table; OCR MOCK demo; pre-exec HITL; heuristic catalog; T3 skills | KWB |
| **Refuse** | Cloud moderator; skill-restrictions-as-security; heuristics-as-complete-security |

---

## 9. Boundary vs later WPs

| Topic | WP-23 | Later |
|---|---|---|
| Delimiter string packing | Policy | **WP-21** |
| RAG chunk retrieve | Trust on chunks | **WP-11** |
| Claim vs file vs policy | T1 claim | **WP-22** |
| MCP isolation | Tool text T3 | **WP-08** |
| Sandbox jail | Pre-exec HITL here | **WP-16** |
| Audit refuses/scans | Event shape | **WP-17** |
| `.md` harness UX | Trust rules | **WP-15** |

---

## 10. Demo acceptance

1. OCR MOCK contains “ignore policy / export all” style text → pipeline **refuses** (or blocks side-effect) + **log** visible.  
2. Delimited extract shown as data, not system policy.  
3. Agent sandbox propose → **HITL before exec**.  
4. Light secret pattern in draft → export blocked or re-HITL.  
5. No cloud moderator call (WAN=0).

---

## 11. Explicitly not locked

Exact delimiter strings, regex list brands, guardrail product, confidence thresholds, UI copy.

---

## 12. Findings traceability

| ID | Where |
|---|---|
| D1–D6 | §3, §5, §7, §10 |
| M1–M10 | §5–§7, §10 |
| A1–A6 | §2 |
| Adopt | §8 |

**Confidence to move to WP-11:** **0.88**

---

## 13. Next

**WP-11** — Retrieve / RAG / plant storage (chunks inherit T3 + grant).

---

## 14. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze from architect + red-team + DM answers |
