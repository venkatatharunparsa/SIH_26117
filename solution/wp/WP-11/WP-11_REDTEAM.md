# WP-11 retrieve/RAG — deep adversarial red-team + source map

**Date:** 2026-09-18  
**Target:** `WP-11_ARCHITECT_PERSPECTIVE.md`  
**DM answers (binding):** see §0  
**Why deep:** Org knowledge volume + confidential classes make retrieve the highest-leakage surface after grants. Wrong RAG = wrong plant “truth” at scale.  
**Against:** Official Description; WP-00–04, WP-03, WP-23; Lewis et al. 2020; Observed authorization-first RAG / ACL-before-retrieve research.

---

## 0. DM answers locked

| Q | Decision |
|---|---|
| **1** | KB grant ⇒ **≥1 visible citation** (source + revision or unknown) |
| **2** | Must-work = **lexical / MOCK**; hybrid = ambition |
| **3** | Demo **top-k = 5** |
| **4** | Stale-index **warn** = **ambition only** |
| **5** | Must-work includes **policy MOCK** for **three-level** demo |
| **6** | Verified extract → org index = **never auto**; Admin/HITL promote only |

---

## Verdict

| Question | Answer |
|---|---|
| Architect direction? | **Yes** — incomplete for production-shaped volume |
| Critical missing? | **Yes — D1–D16** (authz-first, chunk ACL inheritance, citation binding, promote gate, corpus isolation, query non-authority) |
| Overhyped? | “Filter before model” without **pre-filter at search**; index as truth; top-k=5 as quality |
| Beyond KWB? | Live perfect ACL sync, GraphRAG — correctly out |
| Confidence architect alone | **0.72** |
| Confidence after freeze fills + verify | **~0.89** → **GO WP-22** |

---

## 1. Deep attacks → missing fills

| ID | Attack | Missing | Fill (must unless noted) |
|---|---|---|---|
| **D1** | Retrieve-then-filter top-k → unauthorized chunks enter rank / timing leak | Soft “filter before model” | **Authorization-first:** grant/ACL/ceiling/segregation constrain candidate set **before** rank; post-trim = safety net only, never sole control |
| **D2** | Client-supplied “ACL filter” in query | Spoof | Scope derived from **server-side grant_id** only |
| **D3** | Shared vector space; neighbor chunks bleed across bidder keys | Segregation | Index **partition / hard predicate** by source allowlist + segregation_key; no cross-key ANN without predicate |
| **D4** | Chunk spans two docs / two classes | Leak | Chunks inherit **parent object** ACL/class/segregation; no cross-object chunks |
| **D5** | Model cites doc not in retrieved set | Citation theatre | Citations **bound** to returned `chunk_id`s only |
| **D6** | Hallucinate when k empty | Invent manuals | Empty → structured miss; generation must not invent file evidence (WP-22 reinforces) |
| **D7** | Index unverified OCR / chat / `.md` | Poison plant KB | **Never auto**; promote = Admin/HITL; chat/`.md` never org index |
| **D8** | Policy text merged into SOP corpus | Wrong citation class | **Separate corpus ids**: `sop_manual`, `policy`, `correspondence`, `mock_*` |
| **D9** | Query text as instruction | Injection | Query + chunks = data; WP-23 delimit; query cannot widen grant |
| **D10** | Stale ACL tags after revoke | Leak | Live check **grant status** every retrieve; indexed ACL labels insufficient alone |
| **D11** | Oversized chunk dumps whole binder | Over-pass | Max chunk size / unit bound (demo-safe); prefer page/unit from WP-03 |
| **D12** | Duplicate near-docs confuse revision | Wrong rev cited | Prefer explicit revision; if unknown mark `revision_unknown` (WP-02) |
| **D13** | top-k=5 hides better authorized hit deeper under post-filter | Recall collapse | Pre-filter fixes; document that k=5 is **demo default** not quality SLA |
| **D14** | “Lots of data” = claim live plant search | Overclaim | Must-work = MOCK/curated pack; scale/refresh = ambition |
| **D15** | Three-level without policy pack | Incomplete demo | Must-work MOCK includes **file + policy** corpora (user claim = T1, not retrieve) |
| **D16** | Ranking uses unauthorized scores | Side channel | Rank only inside authorized candidate set |

**Ambition (not blocking):** hybrid search; stale `retrieved_at` warn (DM Q4); live DMS; correspondence depth; ACL tag refresh SLA.

---

## 2. Overhyped

| Claim | Reality |
|---|---|
| Lexical MOCK “is RAG” | Enough for SIH must-work; not enterprise search quality |
| Citation present = grounded truth | Citation proves retrieve path; claim check = WP-22 |
| Index stores knowledge | Derived aid; SoR elsewhere |
| top-k=5 | Demo knob |
| Filter in application after embed search | Unsafe as sole control (D1) |

---

## 3. Source-of-truth grades (for freeze claims)

| Theme | Grade |
|---|---|
| Ground in manuals/SOPs/correspondence via local connector | **Official** Description |
| Three-level citation file/user/policy | **WP-00** / **User** |
| Slow OK; accuracy over speed | **User** / WP-00 |
| Grant + ACL before model | **WP-00/04** + **Observed** authz-first RAG |
| Index ≠ SoR | **WP-02** |
| Revision or uncertainty | **WP-02** |
| Chunks T3 | **WP-23** |
| Never auto index OCR | **DM** + WP-03/05 |
| Policy MOCK three-level | **DM** + WP-00 Q4 |
| Vector DB brand / hybrid | **Not locked** / ambition |
| Lewis RAG 2020 | **Spec** — retrieval grounds; quality ≠ generation |

---

## 4. Adopt / refuse (deep)

| Adopt | Why | Refuse |
|---|---|---|
| Authorization-first / ACL pre-filter | Stops cross-grant leakage | Post-filter-only pipelines |
| Onyx ACL-before-retrieve *intent* | Matches grants | Onyx-as-product |
| Haystack/LlamaIndex *shape* | Pipeline clarity | Replace KWB |
| GBrain provenance fields | Citations | Graph DB required |
| Partitioned / predicated index | Bidder isolation | Single soup index |
| Curated MOCK packs for demo | Honest SIH | Fake “we indexed the plant” |

---

## 5. Disposition

**Applied.** → `WP-11_FREEZE.md` + `WP-11_FREEZE_VERIFY.md`. Confidence **0.89**. **GO** → **WP-22**.
