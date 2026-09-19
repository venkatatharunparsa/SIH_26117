# WP-11 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-01 / WP-02 / WP-03 / WP-04 / WP-23 (WP-05 where citations meet HITL)  
**Status:** **SUPERSEDED by `WP-11_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-11_REDTEAM.md` · verify: `WP-11_FREEZE_VERIFY.md`.  
**Job of WP-11:** How KWB **retrieves** org knowledge (manuals, SOPs, correspondence, policy, optional EAM/DMS reads) under **task grant + ACL/classification/segregation**, **revision-aware**, returning **citable chunks** as **T3 untrusted data** — vectors/index beside SoR, never the plant DMS. Slow OK. Three-source *resolution* = WP-22.

**Sources:** Official Description (KB connector; ground in manuals/SOPs/correspondence); WP-00 three-level citation + slow OK; WP-02 connector/index; WP-03 verified extracts only into KB; WP-04 grant filter; WP-23 T3; Lewis et al. RAG 2020 (Spec); repo map Haystack/LlamaIndex *shape*, Onyx ACL *intent*.

---

## One sentence (proposed)

KWB **retrieves** only what the **active grant** allows, filters **before** the model sees text, cites **source + revision (or uncertainty)**, and treats every chunk as **T3 data** — the index is a **search aid**, not the system of record.

---

## 1. What WP-11 owns vs not

| Owns | Does not own |
|---|---|
| Retrieve API: query → candidate objects → **grant/ACL/ceiling/segregation filter** → rank → citable chunks | Connector attach modes (**WP-02**) |
| Index beside SoR (shape, not brand) | Binary OCR path (**WP-03**) |
| Citation fields for file/evidence level | File vs user vs policy **conflict policy** (**WP-22**) |
| Empty / NOT FOUND at retrieve layer (honest miss) | Full claim verification assembly (**WP-22**) |
| Chunks labelled T3 + delimiters contract | Exact prompt packing strings (**WP-21**) |

---

## 2. Corpora (retrieve targets)

| Corpus | Role | Must-work demo? |
|---|---|---|
| **User-attached / verified extract** | Task-local evidence (may skip org index) | **Yes** — bare inspect-to-note |
| **MOCK org KB** (manuals/SOP-like + optional policy) | Prove grant-scoped retrieve + cite + revoke-deny | **Yes** — labelled MOCK (WP-04) |
| **Policy corpus** | Company policy for three-level citation | Ambition strong; MOCK policy pack OK for demo if citations shown |
| **Correspondence** | Past mail/letters (Official) | Ambition; MOCK optional |
| **Live DMS/EAM read** | Ambition via WP-02 adapters | Not required for Expected Solution |
| **Verified OCR extracts promoted to KB** | Only after H1 (WP-03/05) | Ambition path |

**Correspondence ≠ SOP:** different corpus id + citation class; do not merge labels.

---

## 3. Retrieve pipeline (proposed)

```
Query (task-scoped)
  → Candidate search over allowlisted source_ids in grant
  → Filter BEFORE model: grant allowlist, classification ≤ ceiling,
       segregation_key match, unknown class fail-closed (WP-04),
       revoked grant → deny
  → Rank / select top-k (slow OK; accuracy > speed)
  → Emit chunks: text + citation metadata + trust_label=T3
  → Delimit for agent (WP-23 / WP-21)
```

**Never:** retrieve all corpora then filter in the prompt.  
**Never:** role dump (“engineer sees everything”).

---

## 4. Citation metadata (minimum)

| Field | Required |
|---|---|
| `source_id` / corpus class | Yes |
| `object_id` / path | Yes |
| `revision` **or** `revision_unknown=true` | Yes |
| `content_hash` when available | Preferred |
| `page` / unit id when applicable | Preferred |
| `retrieved_at` | Yes |
| `grant_id` | Yes |
| Uncertainty flag if stale/unknown revision | Yes when applicable |

Grounded file-level claims in drafts should carry these (assembly polish WP-22/21). Bare Expected Solution may omit full three-source if no KB grant (WP-01) — retrieve still must be correct when grant active.

---

## 5. Index vs SoR (frozen principle)

- Index/embeddings = **derived**, rebuildable, not plant truth.  
- Canonical bytes stay in SoR / immutable originals / MOCK packs.  
- Conversation memory (chat) ≠ plant KB.  
- Personal `.md` ≠ org retrieve corpus.

---

## 6. Fail-closed / empty

| Condition | Behaviour |
|---|---|
| No grant / revoked | Deny retrieve |
| Source not in allowlist | Deny |
| Class > ceiling / unknown | Deny (WP-04) |
| Segregation mismatch | Deny |
| Zero hits after filter | Return **empty** / NOT FOUND at retrieve — do not invent chunks |
| Connector/index down | Fail-closed or explicit degraded (WP-02) — no silent empty-as-success without flag |

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Grant-scoped retrieve; filter before model.  
2. MOCK org KB (or local folder pack) + cite metadata when KB grant used.  
3. Deny-after-revoke on retrieve (align WP-04 demo).  
4. Chunks = T3; no prompt-only ACL.  
5. Revision or explicit unknown.  
6. Empty retrieve ≠ hallucinated manuals.  
7. Slow OK; offline only.  
8. Index ≠ SoR stated.

### Org-ambition

- Live DMS/EAM; correspondence corpus; hybrid search; refresh/re-index policy; bidder segregation end-to-end; policy corpus depth.

### Deferred

- GraphRAG required; multi-vector mega-stacks; real-time CDC index.

### Never

- Vectors as SoR / replace DMS.  
- Cloud RAG / external search.  
- Retrieve without grant.  
- Filter-only-in-prompt.  
- Merge correspondence into SOP citations silently.  
- Index unverified OCR as org truth.  
- Chat memory as plant KB.

---

## 8. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Haystack/LlamaIndex *pipeline shape*; Onyx ACL-before-retrieve *intent*; GBrain provenance fields |
| **Add** | Grant+segregation filter; revision/uncertainty; T3 chunks; MOCK KB; empty honesty |
| **Refuse** | AnythingLLM/Open WebUI as KWB; Chroma-as-DMS; Graphiti required; Mem0 as plant truth |

---

## 9. Open questions for decision maker

1. **Must-work cite demo:** MOCK KB with **≥1 visible citation** (source+revision/unknown) required whenever KB grant used — confirm **yes**?  
2. **Hybrid search:** keyword+vector ambition, or **keyword/MOCK lexical enough** for must-work? (Recommend: lexical/MOCK enough; hybrid ambition.)  
3. **Top-k default:** freeze a small demo k (e.g. 3–5) or leave unset?  
4. **Stale index:** if `retrieved_at` older than Admin threshold, **warn in citation** (must) or only ambition?  
5. **Policy corpus in must-work MOCK:** include a tiny policy pack for three-level demo, or defer pack to WP-22?  
6. **Verified extract → org index:** auto after H1 (ambition) or **never auto** — only Admin promote? (Recommend: **never auto**; Admin/HITL promote.)

---

## 10. Next after your decisions

**Done.** Frozen as `WP-11_FREEZE.md` rev 1.0 (verify 0.89). Next: **WP-22**.
