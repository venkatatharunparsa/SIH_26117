# WP-04 architect note — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-04_ARCHITECT_PERSPECTIVE.md` (not yet frozen)  
**Against:** Official PS Background (confidential classes); WP-00 §7.2 / §9 / §11; WP-01 roles/jobs; WP-02 ACL + segregation; `DESIGN_AGENDA_REDTEAM_v1.md` WP-04; `DESIGN_REPO_MAP_v1.md` WP-04; Spec NIST SP 800-53 Rev. 5 **AC-6** (least privilege for users **and processes**); Observed JIT / PAM practice.

**Stack:** not locked. No claim of NIST certification.

---

## Verdict

| Question | Answer |
|---|---|
| Directionally correct? | **Yes** — session ≠ grant; ceiling; revoke; residue honesty; MOCK IdP |
| Within KWB / WP-00–02 bounds? | **Yes** — no SoR write; not plant IdP; offline demo |
| Overhyped / fake-security risk? | **Yes — several** (see §2). Main: “drop working memory” + “invalidate tokens” sound complete; they are not |
| Missing for a freeze-grade contract? | **Yes — M1–M12** (see §1) |
| Adopt anything as product? | **Patterns only** — not Onyx/PAM/SSO apps |
| Confidence architect note as-is | **0.72** |
| Confidence after proposed fills + Q defaults | **~0.85** |

**Bottom line:** Keep the three-layer model. Strip theatre language. Add process-binding, default-deny, concurrent-task isolation, grant lifecycle audit, workspace residue, and honest demo proof. Do not claim AC-6 compliance — claim **AC-6-shaped** task privilege.

---

## 1. Missing (must fill before or in freeze)

| ID | Gap | Why it matters | Overreach? |
|---|---|---|---|
| **M1** | **Default-deny** if grant incomplete / expired / unknown source | WP-00 fail-closed; empty allowlist must not mean “all connectors” | No |
| **M2** | **Process binding:** orchestrator, specialist agents, tools, MCP calls act **on behalf of** `person_id` under `grant_id` | AC-6 applies to *processes*, not only humans. Shared super-context is named but not enforced as a field | No |
| **M3** | **Concurrent tasks:** two open tasks for one person → **two grants**, no shared retrieve pool | Same user, inspection + coding: coding must not inherit P&ID grant | No |
| **M4** | **Grant lifecycle / immutability:** request → active → expand → revoke/expire as **append-only events** (ids for WP-17) | CERT-In-shaped audit needs grant history, not only current status bit | No — logging shape, not full WP-17 |
| **M5** | **Mid-task expand** = new grant version or child grant, not silent widen of the same opaque blob | Deny-theatre: UI says “expanded” but old token still wide | No |
| **M6** | **KWB workspace residue:** drafts/exports under task path remain after revoke; inherit classification; **no** new org retrieve | Architect covers chat/docx/`.md`; under-specifies workspace files already on disk | No |
| **M7** | **Policy corpus** as an explicit allowlist source type (align WP-02 rev 1.1) | Three-level citation needs policy; “org retrieve” alone is vague | No |
| **M8** | **Demo acceptance test** (what jury sees): create grant → allowed action → revoke → **same action fails** + log lines | “MOCK grant UI” without fail-after-revoke is theatre | No |
| **M9** | **Self-approval / separation of duties** for sensitive expand | Approver denying expand is listed; worker self-approving own sensitive ceiling is not forbidden | Ambition OK to soft-require; principle should be Never for high classes |
| **M10** | **Break-glass / Admin emergency grant** | Emergency revoke exists; emergency *open* without audit is a hole if added later ad hoc | Name as ambition + mandatory audit, or Never silent break-glass |
| **M11** | **Re-open / resume task** after revoke | Is it new grant (recommended) or resurrect revoked grant? | No — pick one |
| **M12** | **Idle session vs task TTL** interaction | Session idle timeout vs grant TTL both named; which wins? | No |

**Not missing (correctly deferred):** live IdP APIs, full taxonomy text, OpenFGA product, watermarking DRM, WP-05 export HITL detail, WP-11 ranker.

---

## 2. Overhyped / soft claims (attack → fix)

| Attack | What’s overhyped | Reality | Fix language |
|---|---|---|---|
| **A1 Revoke-theatre** | “Drop retrieved chunks from working memory” | Chat store, DRAFT files, UI scrollback, possible KV/session cache still hold content | Say: **stop further privileged I/O**; **label residue**; do not claim wipe of human-visible history |
| **A2 Token myth** | “Invalidate tokens / API keys issued for the grant” | MCP often uses **standing** server config keys (WP-08). Grant cannot magically erase Admin-installed secrets | Say: invalidate **grant-scoped capability tickets**; standing MCP install keys ≠ grant; use of MCP still **gated by grant allowlist** |
| **A3 NIST compliance cosplay** | “NIST AC-6” as if certified | AC-6 is a control family; KWB is a design pattern inspired by it | **AC-6-shaped / JIT-inspired**; not “we are AC-6 compliant” |
| **A4 Ceiling without labels** | Classification ceiling as security | If WP-02 objects lack labels, ceiling cannot filter | Ceiling **requires** object `acl_or_classification` or fail-closed (align WP-02 unknown) |
| **A5 MOCK = security** | MOCK grant UI as must-work “proof” | Jury may see a badge, not a denial | Must-work = **observable deny-after-revoke**, not a green “grant” chip alone |
| **A6 Logout cascade complete** | Logout revokes all grants | Other device/session, or server-side agent still running, may keep work | Cascade **this session’s** grants + **cancel in-flight** task work for those grant ids; multi-session = each session’s grants |
| **A7 Role = enough** | Role class on grant feels like RBAC product | Role only gates *who may request*; enforcement is allowlists | Keep sentence: **RBAC ≠ grant** |
| **A8 Segregation done** | Segregation key on grant | Without WP-11 filter + WP-02 corpus isolation, key is a string | Contract here; **enforce** in retrieve — say so |
| **A9 “Not complete security” one-liner** | Disclaim then oversell elsewhere | Mixed message if §5 still sounds absolute | One **Limits** box: air-gap, HITL, sandbox, audit, no SoR write still required |

---

## 3. Bound check — does WP-04 go beyond the solution?

| Claim / feature | In bounds? | Notes |
|---|---|---|
| Task-scoped grants + revoke | **In** | WP-00 must / User |
| MOCK local identity | **In** | WP-00 deferred SSO |
| Classification ceiling from PS seed classes | **In** | Official Background |
| Bidder segregation key | **In** | WP-02; enforce later WP-11 |
| Becoming plant IdP / cloud SSO must-work | **Out — correctly Never** | Keep |
| Grant includes SoR write | **Out — correctly Never** | Keep |
| Full PAM product / session recording / MFA stack as must-work | **Beyond SIH demo** | Ambition/Observed only |
| Claiming residue fully erased | **Beyond honesty** | Refuse |

**Verdict:** Architect note does **not** expand product identity beyond KWB. Risk is **overclaiming control effectiveness**, not wrong product shape.

---

## 4. Adopt / add / refuse (with why)

| Source | Adopt what | Why | Do **not** take |
|---|---|---|---|
| **NIST SP 800-53 AC-6** | Least privilege for **users and processes** for the **assigned task** | Official Spec hook; matches “task grant” | Certification paperwork; every AC-6 enhancement as must-work |
| **JIT / PAM practice** (Observed) | Time-bound elevation → auto revoke at task end / TTL | Implements AC-6 in ops; matches User revoke-after-task | CyberArk/etc. as KWB; session recording as must-work |
| **AC-6(7) privilege review** | Periodic review of **who may request** which grant classes | Stops standing “Approver forever for all ceilings” drift | Full IAM recertification product in SIH demo |
| **Onyx RBAC/SSO** (repo map) | Org-ambition: identity maps to role class | Real air-gap RAG apps separate auth from retrieval ACL | Cloud SSO as must-work; “login = all connectors” |
| **Microsoft Agent Governance Toolkit** *(ideas)* | Identity + policy + audit around agents | Agents are processes under grants (M2) | Locking to that toolkit / cloud Graph |
| **Nabhi trust tiers** *(names only)* | observe → propose → act as **friction language** optional | Aligns friction ladder with HITL | Tenancy / Company Brain product |
| **OpenFGA / Zanzibar-style ReBAC** | Ambition shape: grant as tuple (user, relation, object) | Clean segregation keys | Cloud FGA SaaS; must-work dependency |
| **OAuth “scopes” metaphor** | Teach allowlists as scopes on a task ticket | Familiar mental model | OIDC/OAuth cloud stack for offline demo |
| **Air-gap RAG practice** (WP-02) | Filter ACL **before** model sees chunks | Already frozen next door | Role-dump retrieve |
| **Our Add (KWB-only)** | Session ≠ grant; ceiling; residue honesty; MOCK grant JSON; deny-after-revoke demo test | No OSS workbench does this end-to-end for SIH | Inventing MRPL IdP group DNs |

---

## 5. Recommended defaults for open questions (so freeze is not blocked)

| Q | Recommendation | Why |
|---|---|---|
| 1 Demo | **Attach-only** for bare `inspect-to-note` must-work **plus** one **labelled** grant→use→revoke→**deny** proof (MOCK KB source OK) | WP-01 citations optional; revoke must be visible |
| 2 TTL | **Admin max** + default short (task-length or fixed N min); user may shorten, not exceed max | Matches JIT; avoids infinite grant |
| 3 Approver deny expand | **Ambition** for full dual-user UX; must-work may **simulate deny** in log/MOCK | Dual-role demo already allowed in WP-01 |
| 4 Unknown classification | **Fail-closed** for org retrieve | Align WP-02 stale/unknown |
| 5 Chat after revoke | **Read-only residue**; no new org retrieve/MCP; optional continued local edit of DRAFT under inherited class | Anti theatre; usability |
| 6 Logout | **Yes** — cascade revoke **this session’s** grants + cancel in-flight work | M6/A6 refined |

---

## 6. Proposed micro-fills for architect → freeze (M/A map)

1. Add **Default-deny** + incomplete grant = no org I/O.  
2. Add **`grant_id` on every privileged process call** (agent/tool/MCP).  
3. Add **one grant per task**; no cross-task context merge.  
4. Add **append-only grant events** (minimal fields for WP-17).  
5. Soften revoke language (A1–A2).  
6. Add **workspace residue** row.  
7. Add **policy corpus** to source types.  
8. Add **demo acceptance:** deny-after-revoke observable.  
9. Add **Limits** box (not complete security + siblings).  
10. Replace “NIST AC-6” compliance tone with **AC-6-shaped**.  
11. Resume task = **new grant** (recommended).  
12. Resolve Q1–Q6 with §5 defaults unless decision maker overrides.

---

## 7. Confidence breakdown

| Theme | Score | Note |
|---|---|---|
| Session ≠ grant | 0.92 | Consistent WP-00/User/agenda |
| Within product bounds | 0.90 | No IdP/SoR overreach |
| Revoke honesty | 0.70 → ~0.88 with A1–A2 fills | Theatre risk today |
| Classification mechanism | 0.75 | Needs fail-closed + labels |
| Demo proof | 0.65 → ~0.85 with M8 | UI chip ≠ proof |
| Adopt map | 0.88 | Patterns clear |
| **Overall** | **0.72 → ~0.85** after fills |

---

## 8. Disposition

**Applied.** All §6 fills + §5 Q defaults accepted into **`WP-04_FREEZE.md` rev 1.0**. Architect note superseded. Next: **WP-05**.

No stack lock. No app code.
