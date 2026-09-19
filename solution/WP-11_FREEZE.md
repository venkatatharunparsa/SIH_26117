# WP-11 Retrieve / RAG / plant storage — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00–04, WP-03, WP-23. Reopen only if the decision maker explicitly says so.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-11_ARCHITECT_PERSPECTIVE.md`, `WP-11_REDTEAM.md` (deep), **DM 2026-09-18** (cite yes; lexical MOCK; k=5; stale warn ambition; policy MOCK three-level; never auto-promote extracts).  
**Verification:** `WP-11_FREEZE_VERIFY.md`  
**Product:** **KWB**

**Stack / vector DB:** not locked. Must-work retrieve may be **lexical over MOCK/local packs**.

---

## 1. One-sentence contract

KWB **retrieves** org knowledge only under an **active task grant**, with **authorization-first** filtering (allowlist, classification ceiling, segregation) **before** ranking, returning at most **top-k=5** (demo default) **citable T3 chunks** with **source + revision or revision_unknown** — the **index is not the SoR**; empty means miss, not invention; **never auto**-index unverified or even H1 extracts without Admin/HITL promote.

---

## 2. Limits (anti overclaim)

| True | False / refuse |
|---|---|
| Authz-first retrieve reduces cross-grant leak | Post-filter-only after global top-k is safe |
| MOCK/lexical enough for SIH must-work | We already “search the whole plant” |
| Citation proves retrieve path | Citation = claim verified (that is **WP-22**) |
| Index is derived / rebuildable | Vectors replace DMS/EAM |
| top-k=5 demo default | Quality SLA / completeness guarantee |
| Lots of org data needs careful promote/filter | Auto-ingest everything after OCR |
| Stale **warn** | Required in must-work (DM: **ambition only**) |

**Data-volume honesty:** Treating large corpora properly means **promote gates, corpus isolation, authz-first, revision metadata** — not claiming live perfect sync in the SIH demo.

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **Q1** | When KB grant used → **≥1 visible citation** (source + revision **or** `revision_unknown`) |
| **Q2** | Must-work search = **lexical / MOCK**; **hybrid** = ambition |
| **Q3** | Demo **top-k = 5** |
| **Q4** | Stale-index citation **warn** = **ambition only** |
| **Q5** | Must-work MOCK includes **policy corpus** for **three-level** demo (file + policy + user claim) |
| **Q6** | Extract → org index = **never auto**; **Admin / HITL promote** only |

---

## 4. Owns / boundary

| WP-11 owns | Later / other |
|---|---|
| Authz-first retrieve; rank inside allowed set; cite metadata; corpus ids; promote-to-index gate | Connectors **WP-02**; OCR **WP-03**; grants **WP-04**; T3 delimit **WP-23**; claim conflict **WP-22**; pack strings **WP-21** |

---

## 5. Corpora (must isolate)

| Corpus id (logical) | Must-work | Notes |
|---|---|---|
| `task_attach` / verified extract (task-local) | **Yes** | May skip org index |
| `mock_sop_manual` | **Yes** | Labelled MOCK |
| `mock_policy` | **Yes** | Three-level demo (Q5) |
| `correspondence` | Ambition | ≠ SOP citation class |
| Live DMS/EAM | Ambition | WP-02 adapters |
| Promoted verified extracts | Ambition path | **Never auto** (Q6) |

**Never** merge policy or correspondence into SOP labels.  
**Never** index chat or personal `.md` as org corpora.

---

## 6. Authorization-first retrieve pipeline (critical)

```
grant_id (server) → resolve allowlist, ceiling, segregation_key, status=active
    → candidate set := ONLY objects/chunks satisfying predicates
    → lexical search (must) / hybrid (ambition) INSIDE candidate set
    → rank → top-k (demo default 5)
    → emit chunks + citation metadata + trust_label=T3
    → deny if grant revoked / inactive at call time
```

### Hard rules

1. **Pre-filter / predicated search** — not “global ANN then drop.” Post-trim = last-resort net only; if used, must not expose unauthorized text to the model.  
2. **Scope from server grant** — never trust client-supplied ACL filters.  
3. **Live grant check** each retrieve (indexed tags alone insufficient after revoke).  
4. Chunks inherit **parent** `source_id`, classification, segregation_key; **no cross-object** chunks.  
5. Rank **only** inside authorized candidates.  
6. Query string is **data** (cannot widen grant); chunks delimited per WP-23.  
7. Citations **bound** to returned `chunk_id`s only — no citing outside the set.  
8. Zero hits → empty / miss structure — **do not invent** file evidence.

---

## 7. Citation metadata (minimum when KB grant used)

| Field | Rule |
|---|---|
| `chunk_id` | Yes |
| `source_id` / corpus class | Yes — visible in demo |
| `object_id` / path | Yes |
| `revision` **or** `revision_unknown=true` | Yes — visible |
| `content_hash` | Preferred |
| `page` / unit | Preferred when from paged docs |
| `retrieved_at` | Yes |
| `grant_id` | Yes |
| Stale warn vs Admin threshold | **Ambition** (Q4) |

Bare attach-only inspect-to-note may omit org citations (WP-01); **when KB grant active**, Q1 applies.

---

## 8. Index vs SoR + promote (data integrity)

- Index/embeddings = **derived**, rebuildable, offline.  
- Canonical bytes: SoR / immutable originals / curated MOCK packs.  
- **Promote to org index:** Admin and/or HITL only; **never auto** after H1 (Q6).  
- Unverified OCR / `machine_extract` → **never** org index.  
- Rebuild/reindex policy = ambition (volume ops); must-work uses curated packs.

---

## 9. Fail-closed

| Condition | Behaviour |
|---|---|
| No/revoked grant | Deny |
| Source not allowlisted | Deny |
| Class > ceiling / unknown | Deny |
| Segregation mismatch | Deny |
| Index/connector down | Fail-closed or explicit degraded (WP-02) |
| Empty authorized set | Miss — no fabricated chunks |

---

## 10. Must / ambition / deferred / never

### Must-work

1. Authz-first grant-scoped retrieve.  
2. Lexical/MOCK search; top-k=5 demo default.  
3. MOCK SOP + **MOCK policy**; ≥1 visible citation when KB grant.  
4. Deny-after-revoke on retrieve.  
5. T3 chunks; citation binding; revision or unknown.  
6. Empty ≠ invent.  
7. Never auto-promote extracts; no chat/`.md` as org index.  
8. Corpus isolation; offline; index ≠ SoR.  
9. Slow OK.

### Org-ambition

- Hybrid search; stale warn; live DMS/EAM; correspondence; refresh/ACL-sync SLA; bidder isolation at plant scale; larger k Admin-configurable.

### Deferred

- GraphRAG required; mega multi-vector stacks; real-time CDC index; timing-side-channel formal program.

### Never

- Vectors as SoR / replace DMS.  
- Cloud RAG.  
- Retrieve without grant / client-spoofed ACL.  
- Post-filter-only as primary control.  
- Auto-index OCR/chat/`.md`.  
- Merge corpus classes in citations.  
- Cite documents not in returned chunk set.  
- Silent invent on miss.

---

## 11. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Authz-first / ACL pre-filter (Observed research) | Data leak prevention |
| **Adopt** | Onyx ACL *intent*; Haystack/LlamaIndex *shape*; GBrain provenance fields | Patterns |
| **Add** | Grant live check; corpus ids; promote gate; k=5; policy MOCK; citation binding | KWB / DM |
| **Refuse** | Post-filter-only; Chroma-as-DMS; Open WebUI-as-KWB; Graphiti required; Mem0 as plant KB; “indexed the plant” theatre |

---

## 12. Demo acceptance

1. KB grant on → retrieve MOCK SOP/policy → **≥1 citation** with source + revision/unknown.  
2. Three-level path showable: **file chunk** + **policy chunk** + **user claim** (T1) labelled distinctly.  
3. Revoke grant → same retrieve **denied**.  
4. Attempt cite outside returned set → rejected by contract.  
5. Empty authorized corpus → miss, not invented SOP text.  
6. No auto promotion of OCR extract into org MOCK index.

---

## 13. Explicitly not locked

Vector engine, embedding model, exact lexical library, chunk tokenizer, Admin MB limits, UI citation chrome.

---

## 14. Next

**WP-22** — Three-source claim verification (uses WP-11 chunks + T1 claims + policy).

---

## 15. Changelog

| Rev | Note |
|---|---|
| **1.0** | Deep red-team + DM Q1–Q6 freeze |
