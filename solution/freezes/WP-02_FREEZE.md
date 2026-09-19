# WP-02 Surrounding systems + KB connector + KWB store — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.1** after adversarial verify). Binding with WP-00 rev 1.1 and WP-01 rev 1.1.  
**Depends on:** those freezes (must not contradict).  
**User intent (2026-09-18):** Org-level design so KWB can **connect company data sources read-only**, classify what we **build vs keep in org systems**, and verify **what is actually possible**; store KWB outputs in a **designated area with versioning** when required; list **all practical connection modes** to existing knowledge systems.  
**Verification:** `WP-02_FREEZE_REDTEAM.md`  
**Product:** **KWB**

**Stack / vendor brands:** not locked. Do not claim “MRPL runs SAP/Maximo/…” without evidence.

---

## 1. One-sentence contract

KWB sits **beside** company systems of record: at **organisation level** it is designed to **attach read-only** to **any Admin-allowlisted company knowledge/data source that passes the discovery worksheet (Possible)**, through a **pluggable connector interface**, so the org can classify what KWB **builds** vs what stays in those systems; KWB **never writes** those systems. KWB **outputs** land only in a **designated KWB store** (with **versioning** when required). “Connect all” = **architecture can onboard every feasible source** — **not** that every adapter is shipped on day one.

---

## 2. Build vs keep vs never (classification)

Use this to answer “is it possible?” and “do we build it?”

| Class | Meaning | Examples |
|---|---|---|
| **Keep in org systems (SoR)** | System of record stays where it is. KWB only **reads**. | EAM work orders, ERP postings, DMS controlled documents, mail servers, IdP |
| **Build in KWB** | Artefacts KWB creates | DRAFT docx/PDF, sandbox reports, routing/egress logs, personal `.md`, citation packs, lineage records |
| **Bridge (read connector)** | Adapter KWB **builds** to pull/index **read** views | DMS API reader, file-share crawler, DB replica query, export ingest, local MCP read tool |
| **Never** | Out of product | Write/update SoR; DCS/SIS/PLC control; cloud SaaS pull; replace EAM/ERP/DMS |

**Feasibility rule (org paper):** For each source class, mark **Possible / Hard / Not possible offline** during discovery. “Connect all” means **architecture can accept any source that fits a read adapter** — **not** that every adapter ships on day one.

---

## 3. “Connect all sources” — what is actually possible

### 3.1 What we commit (org-ambition)

- **One connector contract** (interface): source id, doc/object id, **revision/version**, hash, path/URI, timestamps, **ACL/classification labels**, payload or pointer, read-only.  
- **Any** company source that can expose data through one of the **connection modes in §4** can be onboarded **without redesigning KWB jobs** (same plug pattern as models).  
- Admin **allowlists** which sources/adapters are enabled.  
- Retrieve respects **task grant** + ACL **before** the model sees chunks (WP-00).  
- Fully **offline** — no public-internet connectors.

### 3.2 What we do **not** commit

- Shipping dozens of vendor connectors in the SIH demo.  
- Real-time sync to every system on day one.  
- Live ACL fidelity equal to production IdP without discovery (MOCK / export ACLs OK until WP-04).  
- That every OT or proprietary protocol is feasible without plant IT — mark **Hard / Not possible** honestly.

### 3.3 Must-work (demo)

| Need | Freeze |
|---|---|
| Inspection→Word | **User-attached** scan sufficient; live DMS **not** required |
| Connector shape | **Interface + MOCK pack** (or local folder) labelled **MOCK**, same schema as future adapters |
| Prove read-only | MOCK/adapters expose **read** only; no write methods |

---

## 4. All practical ways to connect existing knowledge systems (read-only)

All modes: **on-prem / offline media**, grant-scoped, no SoR write. Brands are **patterns**, not locks.

| # | Connection mode | How it works | Typical sources | Offline feasible? | Build effort |
|---|---|---|---|---|---|
| 1 | **User attach** | User uploads/selects file into the task | Scans, photos, drawings, exports | Yes | Low — **must-work** |
| 2 | **Local folder / file share crawl** | Read mounts UNC/NFS/local paths Admin allowlisted | Manuals, SOP shares, project folders | Yes | Low–med |
| 3 | **Offline media pack** | USB/approved media → stage into KWB index | Curated SOP/manual packs | Yes | Low — aligns WP-00 media |
| 4 | **Scheduled export / drop-zone** | Org IT drops ZIP/CSV/PDF to a watched folder | DMS/ERP/EAM exports | Yes | Low–med |
| 5 | **DMS / ECM read API** | On-prem API list/get document + metadata + ACL | Controlled docs, drawings | Yes if API on LAN | Med–high |
| 6 | **Database read replica / views** | SQL **SELECT**-only account on replica/view | Structured refs, tag lists, history tables | Yes on LAN | Med |
| 7 | **Application read API** (EAM/ERP) | GET-only integration account | WO metadata, equipment master | Yes on LAN | Med–high |
| 8 | **Email / correspondence archive** | Read PST/EML export or on-prem archive API | Past correspondence | Yes via export; live mail Hard | Med |
| 9 | **Local MCP read server** | Allowlisted MCP already on machine exposes **read** tools | Custom internal tools, local DBs | Yes | Med — WP-08 |
| 10 | **CDC / message bus consume** | Subscribe to on-prem events for incremental ingest | Large estates | Possible on LAN; ops Hard | High — later |
| 11 | **Object store / NAS snapshot** | Read object keys under prefix | Bulk document lakes | Yes | Med |
| 12 | **Wiki / intranet export** | Static HTML/markdown export ingest | Procedures, how-tos | Yes via export | Low–med |

**Explicitly rejected modes:** cloud SaaS connectors; any write/update/delete/post; remote URL fetch of documents from the public internet; MCP that can write plant SoR.

**OT/DCS:** not a knowledge connector target for control actions. If read-only process **snapshots** are ever considered, that is a separate **Hard** discovery item — default **Never** for control paths (WP-00).

---

## 5. Surrounding systems map

### 5.1 Never replace / never write

DCS, SIS, PLC, OT control · EAM/CMMS SoR · ERP SoR · Permit/isolation/MOC execution · Plant IdP as KWB product · DMS as SoR (KWB is not the DMS).

### 5.2 Read candidates (org)

| Store type | Modes (§4) often used |
|---|---|
| Manuals / SOPs / drawings | 2, 3, 4, 5, 11 |
| Past correspondence | 4, 8 |
| EAM / ERP metadata | 4, 6, 7 |
| Local curated knowledge | 3, 2 |
| **Company policy corpus** | 2, 3, 4, 5 — required for three-level citation (WP-00) |
| Custom internal tools data | 9, 6 |
| LIMS / LMS (optional) | 4, 6, 7 — mark **Hard** until discovery |

### 5.3 Feasibility worksheet (org discovery — template)

For each candidate source, Admin/IT fills:

`source_name | class | connection_mode | ACL available? | revision id? | Possible/Hard/Not | onboard phase`

This is how “connect all” stays honest.

---

## 6. KB connector contract (what we build)

The **connector interface** is what KWB builds once; adapters implement it.

**Must provide per object/chunk:**

- `source_system`, `object_id`, `revision`, `content_hash`  
- `uri_or_path`, `title`, `mime_or_type`  
- `acl_or_classification` (as available)  
- `retrieved_at`  
- text or binary pointer for indexing  

**Operations allowed:** list / get / search-within-source (optional) — **read only**.  
**Operations forbidden:** create / update / delete / approve / post.

**Index** beside the connector is **not** the plant SoR (WP-00 / WP-01 plant-controlled class).

**Fail-closed / freshness:**

- If an allowlisted connector is **down** or returns error → fail closed or explicit **degraded** state; do **not** silently invent plant facts.  
- Prefer objects with **revision** (or content_hash). If revision unknown, mark citation uncertainty; do not pretend currency.  
- Stale index vs SoR: org ambition includes refresh/re-ingest policy (schedule or event); detail with WP-11.

**Segregation:** Connectors and indexes for **commercial / bidder / legal** corpora must support **grant isolation** so one bidder’s or party’s material cannot appear in another’s task (stricter allowlist + ACL). Detail WP-04/11.

**WP boundary:** WP-02 = **connect + classify + KWB output store**. Binary OCR/vision ingest = **WP-03**. Retrieve/rank/cite assembly = **WP-11**. Lineage engine brand = **WP-14**.

**Prototype:** MOCK adapter + optional local folder adapter.  
**Org:** add adapters per discovery worksheet without changing jobs.

### 6.1 Adopt (patterns only — not forks)

| Adopt | From | Do not take |
|---|---|---|
| Multi-source **connector layer** (search/access ≠ the whole app) | Onyx *pattern* | Write **actions**; cloud SaaS connectors |
| MOCK schemas stable for EAM/DMS-shaped data | Repo map | Claiming live SAP without adapter |
| Provenance fields (uri, hash, revision) | GBrain/AKB *field ideas* | Graph DB as required product |
| ACL labels on indexed objects; filter before model sees data | Air-gap RAG practice (Observed) | Cloud-only auth services |
| Pipeline shape later | Haystack/LlamaIndex *shape* | Replacing KWB with those products |

---

## 7. Designated KWB output store + versioning

### 7.1 Where outputs live

All **workbench-generated** artefacts (WP-01) are stored only under a **designated KWB output area** (path/volume/DB chosen later — not a plant DMS).

| Content | Store | Versioning |
|---|---|---|
| DRAFT docx / PDF | KWB output area | **Yes** — each regenerate/accept-edit = new version; keep lineage to task id |
| OCR extract / findings fields | KWB output area | Yes (task-scoped) |
| Code + sandbox report | KWB output area | Yes |
| Routing log / egress evidence | KWB audit/evidence area | Append-only preferred |
| Personal `.md` / skills | Personal shelf (separate from plant + from org drafts) | Yes for skill promotion history |
| Citation / NOT FOUND packs | KWB output area | Yes when produced |
| Lineage records | KWB lineage store (engine WP-14) | Yes — task ↔ input revisions ↔ output versions |

### 7.2 Rules

- **Never** auto-write outputs into EAM/ERP/DCS/DMS-of-record.  
- Human may **export/download** from KWB (HITL per WP-00/01); filing into plant DMS is a **human/org** action outside KWB write APIs.  
- Versioning **required** for Office-like DRAFTs and for any artefact tied to approval HITL; optional for ephemeral UI.  
- Retention follows **company policy** (WP-00 → WP-17).

### 7.3 Must-work vs ambition

| | |
|---|---|
| **Must-work** | Designated local output folder (or equivalent) for demo artefacts; task id on files; simple version suffix or timestamp |
| **Org-ambition** | Full version chain + lineage links to source revisions + audit |

---

## 8. Local MCP vs plant connector

| | Plant/KB connector | Local MCP |
|---|---|---|
| Purpose | First-class SoR **read** / knowledge ingest | Allowlisted tools already on machine |
| Write SoR | **Forbidden** | **Forbidden** (Admin deny-list) |
| Onboard | Adapter + discovery worksheet | Allowlist existing local server |

---

## 9. Mapping to WP-01 jobs

| Job | Sources |
|---|---|
| Must-work inspect/code/multimodal | User attach (± MOCK KB) |
| `doc-search-cite` / `correspondence-ground` | Modes 2–5, 8, 11 |
| `drawing-review` | Attach or DMS read |
| `sensitive-corpus-work` | Stricter allowlist + grants |

---

## 10. Never (WP-02)

- Write/edit/delete/approve in any company SoR.  
- Replace EAM/ERP/DMS/DCS.  
- Cloud/public internet connectors.  
- Claim every vendor adapter is already built.  
- Invent MRPL system brand inventory as Official.  
- Use the vector/index as plant SoR.  
- Store KWB DRAFTs as if they were controlled plant records without human filing.

---

## 11. Buckets summary

| Bucket | Content |
|---|---|
| **Must-work** | Connector **interface**; MOCK (and/or local folder) read adapter; user-attach; designated **output area** with basic versioning |
| **Org-ambition** | Onboard **any** feasible company source via §4 modes; discovery worksheet; full version+lineage; EAM/ERP/DMS/mail **read** adapters as Possible |
| **Deferred** | CDC/bus at scale; perfect live ACL sync with IdP |
| **Never** | §10 |

---

## 12. Closed decisions

| Topic | Decision |
|---|---|
| Connect all company sources | **Org design = pluggable read-only adapters for all feasible sources**; not “all built in demo” |
| Classify build vs keep | **§2** frozen |
| Verify possibility | **Discovery worksheet** Possible/Hard/Not |
| Connection modes | **§4** catalog frozen as the allowed pattern list |
| KWB outputs | **Designated store + versioning** (§7) |
| Demo | User-attach + MOCK/interface; no live plant required |
| EAM/ERP/DMS/mail | Read ambition when Possible |
| Write paths | Never |

---

## 13. Explicitly not locked

Exact DMS/EAM products, SQL dialects, MCP server list, output filesystem path, vector DB brand, sync schedule.

---

## 14. Next

**WP-04** — Identity, session, task grants, revoke (follow-list order), under WP-00–02.

---

## 15. Adversarial note (absorbed)

| Attack | Response in this freeze |
|---|---|
| “All sources” = fake universality | = adapter architecture + feasibility classes, not infinite connectors shipped |
| Connector becomes SoR | Index ≠ SoR; plant-controlled remains outside |
| MCP bypasses read-only | Deny write; allowlist |
| Output versioning in plant DMS | Forbidden; KWB store only |
| Demo blocked on live SAP | User-attach + MOCK sufficient |
| Silent empty RAG when DMS down | Fail-closed / degraded (§6) |
| Missing policy for three-source | Policy corpus as read candidate (§5.2) |
| Bidder/commercial leak | Segregation rule (§6) |

---

## 16. Changelog (rev 1.0 → 1.1)

| Change | Why |
|---|---|
| One-sentence: allowlisted + Possible worksheet | Kill “everything connected” slide-speak |
| Policy corpus + optional LIMS/LMS | Completeness for citation + company sources |
| Fail-closed / revision / segregation | Red-team M2/M3 |
| WP-02 vs WP-03/11/14 boundary | Keep ingest/retrieve out of this WP |
| Adopt table (Onyx/GBrain/Haystack patterns) | Repo map without fork |
