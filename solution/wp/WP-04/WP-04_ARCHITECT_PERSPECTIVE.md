# WP-04 — Architect perspective (superseded)

**Date:** 2026-09-18  
**Depends on:** `WP-00_FREEZE.md` rev 1.1, `WP-01_FREEZE.md` rev 1.1, `WP-02_FREEZE.md` rev 1.1  
**Status:** **SUPERSEDED by `WP-04_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-04_REDTEAM.md`.  
**Job of WP-04:** Separate **person identity / session** from **task-scoped grants**; define what a grant may open; how revoke works (including copies); what demo must prove vs MOCK; what stays Never / deferred to IdP discovery.

**Sources:** Official PS Background (confidential classes); WP-00 §7.2 / §11; WP-01 roles + jobs; WP-02 ACL-before-retrieve + bidder segregation; User (least privilege, revoke-after-task, not complete security); Spec NIST SP 800-53 Rev. 5 **AC-6** (pattern, not certification); `DESIGN_REPO_MAP_v1.md` WP-04 (Add: session ≠ grant).

---

## One sentence (proposed)

A **logged-in person** may start a **task**; only that **task grant** (sources, tools/plugins, classification ceiling, TTL) opens plant/KB access — and when the task ends, aborts, or times out, the grant is **revoked**. Standing role alone never equals whole-plant RAG or MCP.

---

## 1. Three layers (do not collapse)

| Layer | Answers | Lifetime |
|---|---|---|
| **Identity** | Who is this human? (role class: Knowledge worker / Approver / Admin) | Account / IdP subject |
| **Session** | Is this browser/workstation login still valid? | Login → logout / idle timeout |
| **Task grant** | What may *this job* read, call, and classify up to? | Task open → end / abort / TTL |

**Standing role** = who may *request* which grant classes.  
**Grant** = what is actually open *now*.  
**Session without grant** = UI only (or personal workspace with no org retrieve).

Collapse identity into “full plant access for the shift” = the leak WP-00 already forbids.

---

## 2. What a grant must name (proposed schema — brand-free)

Every active grant carries at least:

| Field | Meaning |
|---|---|
| `task_id` | Job instance (ties to WP-01 job type) |
| `person_id` + `role_class` | Who holds it |
| `source_allowlist` | Which WP-02 connector ids / corpora (or “user-attached only”) |
| `tool_plugin_allowlist` | Which local MCP/tools/skills may load |
| `classification_ceiling` | Highest class this task may touch |
| `ttl` / `expires_at` | Hard time bound |
| `status` | `active` \| `revoked` \| `expired` \| `denied` |
| `reason` / `requested_vs_approved` | Audit (Approver may deny expand) |

Optional later (ambition): purpose string, export flag (still HITL in WP-05), contractor flag.

**Prototype shape (repo map):** local user + grant JSON / table — not a full SSO product in the SIH demo.

---

## 3. Friction ladder (from WP-00 — make concrete)

| Moment | Friction | Who decides | Demo must? |
|---|---|---|---|
| **User-attached** files for this task | Low — implied grant to those attachments only | Knowledge worker starts task | **Yes** |
| **Org retrieve** (KB / connector / policy corpus) | Explicit grant (or expand) | Worker requests; Approver may deny sensitive expand | **Yes** for at least one KB-grant path *or* labelled MOCK grant UI; bare `inspect-to-note` may stay attach-only (WP-01) |
| **Write / export** out of KWB | HITL (WP-05) — not “just a grant” | Approver / policy | Gate named here; detail WP-05 |
| **MCP / skill expand** | Allowlist **and** task gate | Admin allowlist + grant must include tool | Principle **yes**; full host = WP-08 |
| **Cross-ceiling / bidder corpus** | Hard deny or Approver + segregation rules | Approver / Admin policy | Ambition path; demo can MOCK deny |

Inside an **already-active** grant: low friction for actions already allowed (WP-00 “easy inside grant”).

---

## 4. Classification ceiling (seed from Official Background — not a full taxonomy freeze)

PS names confidential work classes. WP-04 freezes a **ceiling mechanism**, not the customer’s final label dictionary (customer-defined mappings = ambition / Observed).

**Seed classes (must be representable):**

| Seed | Typical risk if dumped into wrong task |
|---|---|
| P&ID / engineering drawings | Safety / process leak |
| Financials | Commercial leak |
| Vendor / bidder negotiations | Segregation breach (WP-02) |
| Unreleased designs | IP leak |
| Correspondence / mail | Context + PII / commercial |
| Strategy | Board / competitive |

**Mechanism (proposed):**

- Every indexed object / attachment carries `classification` (or “unknown → treat as high / fail-closed for org retrieve”).  
- Grant has `classification_ceiling`.  
- Retrieve / tool result **denied** if object class > ceiling (or segregation key mismatch).  
- **Bidder / commercial / legal** corpora: grant must include an explicit **segregation key** (e.g. bid_id / matter_id); no key → no access. Detail retrieve in WP-11; contract here.

Do **not** invent MRPL’s exact taxonomy text in this freeze.

---

## 5. Revoke — what “end” means (anti revoke-theatre)

**Triggers (proposed must):** task complete · user abort · TTL expiry · Approver revoke · Admin emergency revoke · session logout (cascades active grants for that session).

**On revoke, must-work design intent:**

| Target | Action |
|---|---|
| Active grant record | `status=revoked`; no further retrieve/tool under that id |
| Working memory / agent context for that task | Drop retrieved chunks / tool results from live context |
| New RAG / MCP calls | Fail closed |
| Tokens / API keys issued for the grant | Invalidate |

**Hard problem (must name, not pretend solved by TTL alone):**

| Residue | Risk | Proposed contract direction |
|---|---|---|
| Chat transcript already showed P&IDs | Revoke does not un-see | Mark transcript **classification-bound**; session UI may restrict re-open / copy after revoke; not “secure delete of human memory” |
| DRAFT docx / sandbox report already written | Artefact retains content | Generated artefacts **inherit** max classification seen under the grant; export still HITL (WP-05) |
| Personal `.md` updated mid-task | Standing store of secrets | Personal `.md` **must not** silently keep live grant entitlements; if task wrote sensitive excerpts into `.md`, treat as **classified residue** + promotion/HITL rules (WP-15/23) — WP-04 states the ban on “`.md` as standing plant grant” |
| Operator monitor still shows old grant as “active” | Theatre | Audience B must show **revoked/expired** truthfully (WP-13 consumes this) |

**User line (binding intent):** grants + revoke **help** safety; they are **not complete security**. Freeze must say that explicitly.

---

## 6. Identity for demo vs org

| Mode | Identity | Grant store | Must-work? |
|---|---|---|---|
| **Demo / Expected Solution** | Local MOCK users (e.g. worker + Approver) | Local grant records | **Yes** |
| **Org ambition** | Plant IdP / SSO | Same grant model; IdP maps role class | Ambition; discovery deferred |
| **Never** | KWB becomes the plant IdP | — | Never |

Contractors vs employees: **stricter grant class** (WP-01) — mechanism = ceiling + source allowlist + segregation; exact IdP groups = not invented here.

---

## 7. Mapping to WP-01 jobs (proposed defaults)

| Job | Default grant shape |
|---|---|
| `inspect-to-note` | User-attached only; optional KB expand if citations wanted |
| Multimodal / OCR path | Attachments for that task |
| Code sandbox | Workspace + sandbox tools; **no** plant SoR write; KB only if separately granted |
| `sensitive-corpus-work` | Explicit ceiling + segregation; Approver for open |
| Freestyle template work | Same as job type; freestyle ≠ elevated grant |

Specialist agents inherit **the task’s grant**, not a shared super-context (red-team agenda).

---

## 8. Must / ambition / deferred / never (proposed for freeze)

### Must-work (demo + contract)

1. Session authenticates a **person** (MOCK OK).  
2. Starting a task creates a **grant** with allowlists + ceiling + TTL.  
3. Org retrieve and MCP use only succeed if grant allows.  
4. Task end / abort / TTL → grant **revoked**; further retrieve/tools fail closed.  
5. Audience-facing grant state can show active vs revoked (even if full WP-13 later).  
6. Explicit statement: **not complete security**; residue (chat/draft/`.md`) is in design scope.

### Org-ambition

- Live IdP/SSO mapping.  
- Approver workflow for grant expand / deny.  
- Full customer classification dictionary + mappings.  
- Bidder/matter segregation enforced end-to-end with WP-11.  
- Emergency Admin revoke across sessions.

### Deferred

- Perfect live ACL sync with plant IdP (WP-02 already deferred).  
- Cryptographic DRM / watermarking of every pixel.  
- Treating revoke as secure erase of human-viewed content.

### Never

- Session = whole-plant corpus access.  
- Standing tokens that survive task end for org retrieve.  
- Grant that includes write to EAM/ERP/DCS/DMS SoR.  
- Cloud IdP as runtime dependency for offline demo.  
- Personal `.md` acting as a standing org grant / second ACL bypass.  
- Claiming grants replace HITL, air-gap, or audit.

---

## 9. Adopt / add / refuse (patterns only)

| | |
|---|---|
| **Adopt (pattern)** | NIST AC-6 / PAM JIT: privilege for the assigned task, then remove |
| **Add (ours)** | Person session ≠ task grant; classification ceiling; revoke + residue honesty; MOCK grant JSON for demo |
| **Refuse** | “Login once, RAG everything”; cloud FGA SaaS as must-work; inventing MRPL IdP group names; Neo4j/SSO product as this WP |

---

## 10. Boundary vs later WPs

| Topic | This WP | Later |
|---|---|---|
| Export / draft accept HITL | Named as not-only-grant | **WP-05** |
| OCR → human → KB | Grant may allow ingest path | **WP-03** |
| Retrieve rank/cite | Uses grant + ACL filter | **WP-11** |
| MCP host install | Grant gates use | **WP-08** |
| Injection via residue | Ban `.md` as grant | **WP-23 / WP-15** |
| Monitor UI polish | Grant truth required | **WP-13** |
| Audit fields | Grant id on events | **WP-17** |

---

## 11. Open questions for decision maker

1. **Bare Expected Solution demo:** is attach-only grant enough for must-work, with one **labelled MOCK** “org grant + revoke” proof — or must live KB grant be in the must-work video?  
2. **TTL default:** short fixed demo TTL (e.g. task-length / N minutes) vs user-chosen within Admin max?  
3. **Approver deny of expand:** must-work (second MOCK user) or ambition?  
4. **Unknown classification on indexed object:** fail-closed for org retrieve (recommended) or treat as Internal?  
5. **Chat after revoke:** freeze re-open of that task transcript as read-only classified residue, or allow continued chat without retrieve?  
6. **Logout:** always cascade-revoke all active grants for that session? (recommended **yes**)

---

## 12. Red-team fills — accepted into freeze

All rows below are binding in `WP-04_FREEZE.md` rev 1.0 (see that file §18 for traceability).

| ID | Fill |
|---|---|
| M1 | **Default-deny** if grant incomplete / expired / empty allowlist ≠ all sources |
| M2 | Every privileged agent/tool/MCP call bound to `grant_id` |
| M3 | **One grant per task**; no cross-task retrieve merge |
| M4 | Append-only grant lifecycle events (for WP-17) |
| M5 | Expand = new grant version / child grant — no silent widen |
| M6 | KWB **workspace** drafts inherit classification; revoke stops new org I/O only |
| M7 | **Policy corpus** explicit in source allowlist |
| M8 | Demo must show **deny-after-revoke**, not only a grant badge |
| A1–A9 | Soften revoke language; **AC-6-shaped**; Limits box |
| Q1–Q6 | Defaults accepted (attach-only + MOCK deny proof; Admin-max TTL; etc.) |

---

## 13. Next

**Done.** See `WP-04_FREEZE.md`. Next walk: **WP-05**.
