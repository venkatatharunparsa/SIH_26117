# WP-02 — Architect perspective (not frozen)

**Date:** 2026-09-17  
**Depends on:** `WP-00_FREEZE.md` rev 1.1, `WP-01_FREEZE.md` rev 1.1  
**Status:** **SUPERSEDED by `WP-02_FREEZE.md`.** Kept for history.  
**Job of WP-02:** Name surrounding **plant / org systems** — what KWB is **not**, what it may **read** (never write), how the **KB connector** attaches, what the **demo** mocks.

Official PS: local **knowledge base connector** to manuals, SOPs, **past correspondence**; nothing external.  
**WP-00:** read-only to existing systems; live EAM/DMS connectors = ambition; MOCK OK for demo; never DCS/SIS/PLC write.  
Do **not** invent MRPL product brand names (SAP/Maximo/etc.) as confirmed facts.

---

## One sentence (proposed)

KWB sits **beside** plant systems of record: it **connects read-only** (or mocks that shape) to knowledge stores so jobs can ground drafts; it **does not replace** EAM, DMS, ERP, historian, IdP, or DCS, and it **never writes** them.

---

## 1. Boundary rule (from WP-00 — restate for this WP)

| KWB | Surrounding systems |
|---|---|
| Drafts artefacts in **KWB workspace** | Remain **systems of record** |
| May **read** under **task grant** | Own create/update/delete/approve workflows |
| Offline / on-prem only | May be on same LAN; **not** public internet |

**Plant-controlled** artefacts (WP-01) live in surrounding systems (or exports from them). KWB does not become their DMS.

---

## 2. System classes (generic — not vendor locks)

### 2.1 Never our job (KWB is not this product)

| System class | Why out |
|---|---|
| **DCS / SIS / PLC / OT control** | WP-00 Never; not a knowledge workbench |
| **EAM / CMMS** as the maintenance system of record | We don’t replace work-order lifecycle |
| **ERP** as finance/procurement SoR | We don’t post invoices or POs |
| **Permit / isolation / MOC execution systems** | No autonomous permit/signature (WP-00 Never) |
| **Plant IdP / SSO** as product | Deferred; MOCK identity OK for demo |
| **Historian / LIMS as control analytics** | Process AI complementary; not our core PS spine |

### 2.2 May connect **read-only** (org-ambition)

| Store type | PS / freeze hook | What KWB reads (examples) | Writes? |
|---|---|---|---|
| **Document / DMS / file share** | Manuals, SOPs, drawings | Controlled PDFs, revisions | **Never** |
| **Correspondence store** | Past correspondence | Mail/export archives (ACL’d) | **Never** |
| **EAM / ERP read APIs or exports** | Ambition live connectors | Tag, WO history, metadata — if granted | **Never** |
| **Local curated KB pack** | Connector + demo | Staged manuals/SOP excerpts on approved media | N/A (files in KWB index, still not plant SoR write) |

### 2.3 Demo / must-work posture

| Need | Proposal |
|---|---|
| Expected Solution inspection→Word | **User-attached scan** is enough; live DMS **not** required |
| Grounding / three-source | Ambition; demo may use **MOCK plant-controlled pack** (same schema as future connector) |
| Prove connector shape | MOCK JSON/files labelled **MOCK** — same fields as future read connector |

WP-00 already: live EAM/DMS = ambition; MOCK schemas OK.

---

## 3. Knowledge base connector (what “connector” means)

Not “Chroma is the plant.” Connector = **adapter** that:

1. Declares **source system class** + **revision/id** of each chunk/doc  
2. Enforces **ACL / grant** before retrieve (WP-00)  
3. Returns citations usable as **file/evidence** level (WP-00 three-source)  
4. Speaks only **read** operations  
5. Works **offline** (no SaaS DMS in the cloud)

**Prototype:** file/folder or MOCK pack behind the same interface.  
**Org:** swap adapter to real DMS/mail export without redesigning KWB jobs (same idea as pluggable models).

---

## 4. Mapping to WP-01 jobs

| Job | Surrounding systems needed? |
|---|---|
| `inspect-to-note` (must) | Optional KB; scan is user-attached |
| `code-sandbox` (must) | None (workspace + sandbox) |
| `multimodal-understand` (must) | None beyond input image |
| `doc-search-cite` / `correspondence-ground` | **Yes** — DMS/mail read or MOCK |
| `drawing-review` | Drawing from attach or DMS read |
| `sensitive-corpus-work` | Stricter ACL on commercial/legal stores |

---

## 5. Local MCP vs plant connector

| Path | Role |
|---|---|
| **KB / plant read connector** | First-class KWB integration for SoR **reads** |
| **Local MCP** | User/org allowlisted tools already on machine — must **not** become a write path to EAM/DCS |

Admin allowlist must reject MCP servers that write plant systems (WP-00 Never). Detail in WP-08; principle freezes here.

---

## 6. What WP-02 must never do

- Name a vendor (SAP, Maximo, SharePoint, …) as “MRPL uses X” without evidence.  
- Allow write/update/delete on any SoR.  
- Require live plant integration for Expected Solution demo.  
- Put OT historian control loops in scope.  
- Treat the vector index as the system of record.  
- Use internet SaaS connectors.

---

## 7. Proposed freeze buckets

| Bucket | Content |
|---|---|
| **Must-work** | Connector **interface** + ability to run demo on **user-attached** inputs; optional **MOCK** plant pack labelled MOCK |
| **Org-ambition** | Read adapters for DMS/files, correspondence; optional EAM/ERP **read**; revision-aware citations |
| **Deferred** | Live IdP-tied ACL sync; full multi-system mesh |
| **Never** | Write any SoR; replace EAM/ERP/DCS; OT agent; cloud DMS |

---

## 8. Open questions for your perspective

1. Demo KB: **MOCK pack only**, or also a small real local folder of sample SOPs you will supply?  
2. Correspondence: in ambition as **mail export / file archive** only, or do you expect a live mail server read later?  
3. EAM/ERP read: **ambition** (WP-00) — confirm keep, or demote to deferred?  
4. Should WP-02 freeze an explicit **deny-list** of MCP capabilities (write WO, write tag, …)?  
5. Any surrounding system you want **named as out** beyond the table (e.g. LIMS, training LMS)?

---

## 9. Next after you answer

Adversarial pass → `WP-02_FREEZE.md` → WP-04 (identity, session, grants) per follow-list order.
