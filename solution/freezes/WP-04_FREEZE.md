# WP-04 Identity, session, task grants, revoke — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-01 / WP-02 rev 1.1. Reopen only if the decision maker explicitly says so.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-04_ARCHITECT_PERSPECTIVE.md`, `WP-04_REDTEAM.md` (**all M1–M12 fills + A1–A9 language fixes + Q1–Q6 defaults accepted**).  
**Verification / findings SoT:** `WP-04_REDTEAM.md`  
**Product:** **KWB**

**Stack / IdP vendor:** not locked. No NIST certification claim. Prototype shape = local users + grant records (JSON/table OK).

---

## 1. One-sentence contract

A **logged-in person** may start a **task**; only that **task grant** (source allowlist, tool/plugin allowlist, classification ceiling, optional segregation key, TTL) opens org/KB and privileged tool access — **default-deny** otherwise. Task end / abort / TTL / logout (this session) / Approver·Admin revoke → grant **revoked**: **no further privileged I/O**. Standing **role ≠ plant access**. Grants **help** safety; they are **not complete security**.

---

## 2. Limits (read first — anti overclaim)

| True | False / refuse |
|---|---|
| Grants implement **AC-6-shaped / JIT-inspired** least privilege for the assigned task | “We are NIST AC-6 compliant” |
| Revoke **stops new** org retrieve, MCP use under that grant, and in-flight privileged work for that `grant_id` | Revoke **erases** chat, human memory, or DRAFT bytes already written |
| Grant-scoped **capability tickets** are invalidated | Standing MCP **install** secrets are wiped by revoke (those are WP-08 Admin config; **use** stays grant-gated) |
| Classification ceiling filters labelled objects | Ceiling alone secures unlabelled corpora |
| MOCK identity + grant is valid for Expected Solution | MOCK grant **badge** without deny-after-revoke = security proof |
| Still required beside grants: **air-gap, HITL (WP-05), sandbox, audit (WP-17), no SoR write** | Grants replace any of those |

**RBAC ≠ grant:** role class only limits **who may request** which grant shapes. Enforcement is allowlists + ceiling + segregation + TTL.

---

## 3. Three layers (do not collapse)

| Layer | Answers | Lifetime |
|---|---|---|
| **Identity** | Who is this human? Role class: Knowledge worker / Approver / Admin (+ Auditor ambition) | Account / IdP subject |
| **Session** | Is this client login still valid? | Login → logout / idle timeout |
| **Task grant** | What may *this job* read and call, up to which class? | Task open → end / abort / TTL / revoke |

**Session without an active grant:** UI + personal workspace only — **no** org retrieve, **no** grant-gated MCP.

**Collapse forbidden:** “logged in for the shift ⇒ whole-plant RAG/MCP.”

---

## 4. Closed decisions (Q1–Q6)

| ID | Decision |
|---|---|
| **Q1 Demo** | Bare `inspect-to-note` may be **attach-only**. Must-work **also** includes one **labelled** proof: grant → allowed privileged action → **revoke** → **same action denied** (MOCK KB/source OK). Citations still only if KB grant active (WP-01). |
| **Q2 TTL** | **Admin max** + short default (task-length or fixed N minutes — exact N later). User may **shorten**, not exceed max. |
| **Q3 Approver deny expand** | Full dual-user deny UX = **org-ambition**. Must-work may **simulate** deny in MOCK/log. |
| **Q4 Unknown classification** | Org retrieve on unlabelled / unknown class → **fail-closed** (align WP-02). |
| **Q5 After revoke** | Task transcript / UI = **read-only classified residue**; **no** new org retrieve / grant-gated MCP. Local edit of existing DRAFT under **inherited** classification may continue; **export** still HITL (WP-05). |
| **Q6 Logout** | **Yes** — cascade-revoke **this session’s** active grants and **cancel in-flight** work bound to those `grant_id`s. Other sessions keep their own grants until they revoke/expire. |

**Resume / re-open after revoke (M11):** always a **new grant** (never resurrect a revoked grant id).

**Idle session vs grant TTL (M12):** **whichever fires first** wins — session idle logout cascades grants; grant TTL revokes that grant even if session remains.

---

## 5. What a grant must name (brand-free schema)

| Field | Meaning | Required |
|---|---|---|
| `grant_id` | Unique id (never reused after revoke) | Yes |
| `task_id` | WP-01 job instance | Yes |
| `person_id` + `role_class` | Holder | Yes |
| `session_id` | Issuing session | Yes |
| `source_allowlist` | WP-02 connector/corpus ids and/or **`user-attached`** and/or **`policy-corpus`** | Yes (empty ≠ all) |
| `tool_plugin_allowlist` | Local MCP/tools/skills permitted | Yes (empty ≠ all) |
| `classification_ceiling` | Highest class this task may touch | Yes |
| `segregation_key` | bid_id / matter_id / … when corpus requires it | When source class demands |
| `ttl` / `expires_at` | Hard time bound ≤ Admin max | Yes |
| `status` | `active` \| `revoked` \| `expired` \| `denied` | Yes |
| `version` / parent | Expand creates **new version or child grant** (M5) | Yes on expand |
| `reason` / requested vs approved | Audit | Ambition-strong; demo may MOCK |

**Default-deny (M1):** missing/incomplete/expired/revoked/denied grant, unknown source id, or empty allowlist interpreted as wildcard → **no** org retrieve and **no** grant-gated tool/MCP call.

---

## 6. Process binding (M2) — agents are not above the grant

Every privileged action by orchestrator, specialist agent, tool, or MCP **must** carry / check `grant_id` (+ `person_id`):

- Processes act **on behalf of** the person under that grant only.  
- **One grant per task (M3):** concurrent tasks ⇒ concurrent grants; **no** shared retrieve pool or super-context merge across tasks.  
- Inspection grant must not bleed into a parallel coding task (and vice versa).

---

## 7. Friction ladder

| Moment | Friction | Who | Must-work? |
|---|---|---|---|
| **User-attached** for this task | Low — allowlist = those attachments | Knowledge worker starts task | **Yes** |
| **Org retrieve** (connectors, KB index, **policy corpus**) | Explicit grant / expand | Worker requests; Approver may deny (ambition UX) | **Yes** — at least MOCK path for Q1 proof |
| **Write / export** out of KWB | **HITL** — not “just a grant” | Approver / policy | Named here; detail **WP-05** |
| **MCP / skill use** | Admin allowlist **and** grant allowlist | Admin + grant | Principle **yes**; host detail **WP-08** |
| **Cross-ceiling / bidder corpus** | Hard deny or Approver + `segregation_key` | Approver / Admin policy | Ambition; demo may MOCK deny |
| Inside already-allowed grant | Low friction for permitted actions | — | Yes (WP-00) |

**Self-approval (M9):** Knowledge worker **must not** self-approve raising ceiling into **high** seed classes (P&ID, financials, vendor/bidder, strategy, unreleased designs) for their own task. Demo may omit dual-user UX but the **Never** principle freezes. Lower/internal attach-only needs no second person.

**Break-glass (M10):** Admin emergency **open** = **org-ambition only**, always **append-only audited**. Silent break-glass = **Never**. Emergency **revoke** = must-work capable (Admin).

---

## 8. Classification ceiling

### 8.1 Mechanism (frozen)

- Indexed objects / attachments carry `classification` (or ACL labels) per WP-02.  
- Grant carries `classification_ceiling`.  
- Retrieve / tool result **denied** if object class > ceiling, segregation mismatch, or **unknown/unlabelled** on org retrieve (**Q4 fail-closed**).  
- Ceiling **without** labels does not count as control (A4).  
- **Bidder / commercial / legal:** grant needs explicit `segregation_key`; enforcement at retrieve = **WP-11** (contract here, filter there — A8).

### 8.2 Seed classes (must be representable — not final customer dictionary)

From Official PS Background:

| Seed | Leak if wrong task |
|---|---|
| P&ID / engineering drawings | Safety / process |
| Financials | Commercial |
| Vendor / bidder negotiations | Segregation breach |
| Unreleased designs | IP |
| Correspondence / mail | PII / commercial |
| Strategy | Board / competitive |

Customer-defined full taxonomy / mappings = **org-ambition** (do not invent MRPL label text here).

---

## 9. Revoke — honest semantics

### 9.1 Triggers (must)

Task complete · user abort · grant TTL · Approver revoke · Admin emergency revoke · **session logout** (this session’s grants) · session idle timeout (via logout cascade).

### 9.2 On revoke — must do

| Target | Action |
|---|---|
| Grant record | `status=revoked` (or `expired`); **no reuse** of `grant_id` |
| New org retrieve / grant-gated MCP/tools | **Fail closed** |
| In-flight privileged work for that `grant_id` | **Cancel** |
| Grant-scoped capability tickets | **Invalidate** |
| Audience B / grant display | Show **revoked/expired** truthfully (WP-13 consumes) |

### 9.3 Residue (in design scope — not “wiped”)

| Residue | Contract |
|---|---|
| Chat / transcript | Classification-bound **read-only** after revoke (Q5) |
| DRAFT docx / sandbox report / **KWB workspace files** (M6) | Inherit **max classification seen** under the grant; no new org I/O; export = WP-05 |
| Personal `.md` | **Must not** store live grant entitlements or act as standing org ACL; sensitive excerpts = classified residue → WP-15 / WP-23 |
| Human memory / screen already viewed | Out of software control — why grants are **not complete security** |

---

## 10. Grant lifecycle events (M4) — minimal for audit

Append-only events (fields refined in WP-17), at least:

`grant_created` · `grant_expanded` (new version/child) · `grant_denied` · `grant_revoked` · `grant_expired` · privileged `action_allowed` / `action_denied` under `grant_id`.

Do not rely on a mutable status bit alone as history.

---

## 11. Identity modes

| Mode | Identity | Grant store | Bucket |
|---|---|---|---|
| Demo / Expected Solution | Local **MOCK** users | Local grant records | **Must-work** |
| Org ambition | Plant IdP / SSO maps → role class | Same grant model | Ambition |
| — | KWB as plant IdP | — | **Never** |
| — | Cloud IdP required for offline demo | — | **Never** |

Contractors vs employees: **stricter** allowlist / ceiling / segregation (WP-01). Exact IdP group DNs = not invented here.

---

## 12. Mapping to WP-01 jobs (defaults)

| Job | Default grant shape |
|---|---|
| `inspect-to-note` | `user-attached`; optional KB/policy expand if citations wanted |
| Multimodal / OCR | Attachments for that task |
| Code sandbox | Workspace + sandbox tools; **no** SoR write; KB only if separately granted |
| `sensitive-corpus-work` | Explicit ceiling + segregation; Approver for high open (ambition UX) |
| Freestyle templates | Same as job type — freestyle ≠ elevated grant |

---

## 13. Must / ambition / deferred / never

### 13.1 Must-work

1. Authenticate a **person** (MOCK OK).  
2. Start task → create grant with allowlists, ceiling, TTL ≤ Admin max.  
3. **Default-deny** privileged I/O without a valid active grant.  
4. Org retrieve / MCP only if grant allows; bind calls to `grant_id`.  
5. One grant per task; no cross-task merge.  
6. Revoke/expire/logout(this session) → fail-closed further privileged I/O + cancel in-flight.  
7. Observable **deny-after-revoke** demo proof (Q1).  
8. Residue honesty + Limits box (§2).  
9. Unknown class on org retrieve → fail-closed.  
10. Resume after revoke → **new** grant.

### 13.2 Org-ambition

- Live IdP/SSO → role class.  
- Full Approver expand/deny UX.  
- Customer classification dictionary + mappings.  
- End-to-end bidder/matter segregation with WP-11.  
- Admin emergency **open** (audited).  
- AC-6(7)-shaped periodic review of **who may request** which grant classes.  
- Optional ReBAC tuple shape (OpenFGA-*style*, not cloud SaaS).

### 13.3 Deferred

- Perfect live ACL sync with plant IdP (WP-02).  
- DRM / watermark every pixel.  
- Secure erase of human-viewed content.  
- Full PAM session recording / MFA product stack as SIH must-work.

### 13.4 Never

- Session = whole-plant corpus access.  
- Standing org-retrieve capability past task end.  
- Grant that **writes** EAM/ERP/DCS/DMS SoR.  
- Empty allowlist = all sources/tools.  
- Resurrect revoked `grant_id`.  
- Self-approve high-class ceiling expand for own task.  
- Silent break-glass open.  
- Personal `.md` as standing org grant / ACL bypass.  
- Cloud IdP as offline demo dependency.  
- Claim grants replace HITL, air-gap, sandbox, or audit.  
- Claim residue fully erased by revoke.

---

## 14. Adopt / add / refuse (patterns only)

| | What | Why |
|---|---|---|
| **Adopt** | NIST SP 800-53 **AC-6** least privilege for users **and processes** (assigned task) | Spec hook for task grants |
| **Adopt** | JIT / PAM **time-bound then revoke** (Observed) | Matches User revoke-after-task |
| **Adopt** | Onyx **RBAC/SSO shape** (ambition) | Auth ≠ retrieval ACL |
| **Adopt** | Agent-governance *ideas* (identity/policy/audit around agents) | M2 process binding |
| **Adopt** | Air-gap RAG: ACL/grant filter **before** model sees chunks | WP-02 / WP-00 |
| **Adopt (names only)** | Nabhi-like friction tiers as optional language | Align ladder with HITL |
| **Add (ours)** | Session ≠ grant; ceiling; segregation key contract; residue honesty; MOCK grant store; **deny-after-revoke** test; append-only grant events | No OSS workbench is the SIH product |
| **Refuse** | “Login once, RAG everything”; cloud FGA/SSO as must-work; CyberArk-as-KWB; inventing MRPL IdP DNs; NIST compliance theatre; OAuth/OIDC cloud stack for offline must-work |

---

## 15. Boundary vs later WPs

| Topic | WP-04 | Later |
|---|---|---|
| Export / draft accept / write HITL | Not only a grant | **WP-05** |
| OCR → human → KB | Grant may allow ingest sources | **WP-03** |
| Retrieve rank / cite / enforce segregation filter | Contract + ceiling | **WP-11** |
| MCP install / standing secrets | Use gated by grant | **WP-08** |
| Injection via OCR/RAG/MCP/`.md` | `.md` not a grant | **WP-23 / WP-15** |
| Monitor UI | Grant truth required | **WP-13** |
| Full audit retention | Event ids required | **WP-17** |
| Context packing under grant | Ceiling + minimize | **WP-21** |

---

## 16. Demo acceptance (must be showable)

1. MOCK user starts task → grant **active** (attach and/or MOCK org source).  
2. Privileged action **succeeds** (e.g. MOCK retrieve or grant-gated tool).  
3. Revoke (or TTL).  
4. **Same** action **fails closed**; UI/log shows grant **revoked** + deny.  
5. Transcript/DRAFT remain as **residue**, not as live entitlement.

A green “grant” chip alone **fails** this acceptance test.

---

## 17. Explicitly not locked here

Exact TTL minutes, IdP product, grant DB engine, ReBAC library, MFA, session-recording PAM, full sensitivity taxonomy strings, MRPL group DNs, UI wireframes.

---

## 18. Findings incorporated (traceability)

| Red-team ID | Where frozen |
|---|---|
| M1 Default-deny | §5, §13.1 |
| M2 Process / `grant_id` | §6 |
| M3 One grant per task | §6, §13.1 |
| M4 Append-only events | §10 |
| M5 Expand = new version/child | §5 |
| M6 Workspace residue | §9.3 |
| M7 Policy corpus | §5, §7 |
| M8 Deny-after-revoke demo | §4 Q1, §16 |
| M9 Self-approve ban (high class) | §7, §13.4 |
| M10 Break-glass | §7, §13.2 / §13.4 |
| M11 Resume = new grant | §4 |
| M12 Idle vs TTL | §4 |
| A1–A9 Overclaim fixes | §2, §9 |
| Q1–Q6 defaults | §4 |
| Adopt map | §14 |
| Bounds | §13.4 Never; Limits §2 |

**Post-fill confidence (from red-team):** ~**0.85** for use by later WPs.

---

## 19. Next

**WP-05** — HITL map (critical + weak spots), under WP-00–04.

---

## 20. Changelog

| Rev | Note |
|---|---|
| **1.0** | Initial freeze: architect + full `WP-04_REDTEAM.md` findings accepted |
