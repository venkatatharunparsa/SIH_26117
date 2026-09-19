# WP-02 freeze — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-02_FREEZE.md` (third walked WP: WP-00 → WP-01 → **WP-02**)  
**Note:** If you meant **WP-03 Ingest** (OCR/multimodal), say so — that WP is later in the queue (after WP-04/05). This audit is on **WP-02**.  
**Against:** Official PS, WP-00/01 freezes, `DESIGN_REPO_MAP_v1.md`, air-gap RAG practice (Observed).

---

## Verdict

| Question | Answer |
|---|---|
| Within KWB / WP-00–01 bounds? | **Yes** — read-only beside SoR; no DCS write; offline; MOCK demo |
| Goes beyond solution bound? | **No hard overreach.** Soft risk: “any source” misread as “all adapters shipped” — already mitigated in §3; tighten in rev 1.1 |
| Missing items? | **Yes — few** (policy corpus, stale/fail-closed, commercial segregation, adopt pointers) → **rev 1.1** |
| Confidence WP-02 contract for later WPs | **0.84** |

---

## 1. Bounds check (in / out)

### Inside limits (keep)

| Claim | Bound source |
|---|---|
| Read-only connectors; never write SoR | WP-00 Q3 / Never |
| Pluggable adapter ≠ every adapter built | Same pattern as WP-00 models |
| User-attach + MOCK for must-work | WP-00/01 Expected Solution path |
| Designated KWB output store + versioning | WP-01 workbench-generated; WP-00 lineage ambition |
| Offline / no cloud SaaS connectors | WP-00 fully offline |
| DMS/EAM/ERP/mail as read ambition | Official Description KB connector + WP-00 deferred live connectors |
| Index ≠ plant SoR | WP-00 / WP-01 artefact classes |

### Would be beyond bounds (correctly excluded)

| Excluded | Why beyond KWB |
|---|---|
| Replace SAP/Maximo/DMS | Wrong product |
| Write work orders / post ERP | WP-00 Never |
| Cloud Drive/Slack/GitHub MCP catalog | Offline Never |
| OT control via connector | Never |
| Claiming MRPL vendor inventory | Unverified |
| Shipping 12 production adapters in SIH demo | Ambition ≠ must-work |

### Soft overreach (watch)

| Risk | Status |
|---|---|
| Org slides say “connects to everything” without Possible/Hard/Not | Freeze already has worksheet — **require** worksheet language in one-sentence/ambition |
| CDC/bus (mode 10) sounds like always-on plant integration | Already Deferred/Hard — OK |
| Output versioning engine locked early | Path/DB not locked — OK; detail WP-14 |

---

## 2. Claim verification (sample ledger)

| Claim | Grade | OK? |
|---|---|---|
| Local KB **connector** to manuals/SOPs/correspondence | **Official** Description | Yes |
| Read-only to existing systems | **WP-00** | Yes |
| Live EAM/DMS ambition; MOCK demo | **WP-00** | Yes |
| Connect all = adapter architecture | **User** + **Derived** | Yes if not “all shipped” |
| §4 connection modes | **Observed** enterprise RAG (export, share, API, replica) + **Derived** | Yes as pattern catalog |
| Reject cloud SaaS / write MCP | **WP-00** | Yes |
| KWB designated store + versioning | **User** + WP-01 generated class | Yes |
| Never auto-file to plant DMS | **WP-00/01** | Yes |
| Feasibility Possible/Hard/Not | **Derived** honesty | Yes |

---

## 3. Missing (fill in rev 1.1)

| ID | Missing | Why required | Beyond bound if added wrong? |
|---|---|---|---|
| M1 | **Company policy corpus** as a first-class read source | WP-00 three-level citation needs **policy** as evidence source | No — still read-only |
| M2 | **Fail-closed / stale** when connector down or revision unknown | WP-00 fail-closed; avoid silent empty RAG | No |
| M3 | **Commercial / bidder segregation** note on connectors | Prior research: never leak bidder A into B eval | No — ACL/grant rule, not new system |
| M4 | **Adopt** pointers (Onyx connector layer, GBrain/AKB cite fields, Haystack pipeline later) | Repo map; avoid reinventing | Adopt **patterns only** — not fork |
| M5 | Explicit **LIMS / training LMS** as optional Hard read | Completeness of “company sources” list | Optional; not must-work |
| M6 | Boundary: WP-02 = **connect/store contract**; WP-11 = retrieve; WP-03 = OCR ingest of binaries | Prevent WP-02 swallowing OCR/RAG | Clarifies limits |

Not missing: IdP design (WP-04), vector brand, vendor APIs.

---

## 4. What to adopt (patterns only — not forks)

From `DESIGN_REPO_MAP_v1.md` + Observed air-gap RAG practice:

| Adopt | From | Why that only | Do not take |
|---|---|---|---|
| Many systems as **data-access layer**, not the app | **Onyx** connector pattern | PS “KB connector” | Onyx **actions**/writes; SaaS Slack/Google connectors |
| Schema-stable **MOCK** JSON for EAM/DMS | Repo map WP-02 | Demo without live plant | Fake “we integrated SAP” claims |
| Provenance fields: source_uri, hash, revision, review_status | **GBrain / AKB** field ideas | Citations + lineage | Graph DB as product |
| Ingest→retrieve pipeline shape later | **Haystack / LlamaIndex** | WP-11, not WP-02 core | Embed their product UI |
| ACL on chunks at index time; filter before retrieve | Air-gap RAG practice (Observed) | WP-00 grant/ACL | Cloud FGA SaaS |
| Git/Markdown as optional **canonical** for org-promoted skills — not plant SoR | GBrain/TeamBrain | Personal→org skills | Syncing plant docs only via Git |

**Required to add in KWB (not in those repos):** discovery worksheet Possible/Hard/Not; designated **KWB output store** separate from index; hard **Never write** on SoR; offline-media-only onboard; MCP write deny-list.

---

## 5. Attacks that fail / pass

| Attack | Result |
|---|---|
| Jury: “You said all sources — where is SAP?” | **Pass** if demo shows interface+MOCK and org paper shows worksheet |
| CISO: “RAG becomes SoR” | **Pass** — index ≠ SoR; plant-controlled class |
| MCP writes Maximo | **Pass** if deny-list enforced (WP-08) — principle in freeze |
| Versioning in Documentum via API | **Blocked** — Never write |
| Empty answers when DMS down, presented as truth | **Gap M2** — fail-closed needed |
| Policy never ingested → three-source broken | **Gap M1** |
| Bidder leak via shared index | **Gap M3** |

---

## 6. Confidence

| Layer | Conf | Source |
|---|---|---|
| Align WP-00/01 + Official connector | 0.90 | Freezes + PS Description |
| “All sources” honesty | 0.85 | Adapter + feasibility (user intent) |
| Connection mode catalog completeness | 0.80 | Observed patterns; not every proprietary OT protocol |
| Output store vs plant SoR | 0.90 | User + WP-01 |
| Adopt map clarity | 0.88 | DESIGN_REPO_MAP |
| **Overall WP-02** | **0.84** | After rev 1.1 fills |

---

## 7. Recommendation

Apply **rev 1.1** micro-fills (M1–M4, M6). Keep freeze. Do not expand into OCR (WP-03) or full RAG (WP-11). Next queue: **WP-04**.
