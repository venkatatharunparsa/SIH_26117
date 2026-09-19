# WP-07 Tools, prompts, specialist agents — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-01 / WP-04 / WP-05 / WP-11 / WP-22 / WP-23.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-07_ARCHITECT_PERSPECTIVE.md`, `WP-07_REDTEAM.md`, **DM 2026-09-18** (org role×task skill/tool catalog; demo slice; iteration default 5 editable; distinct ids org / single demo; parallel org / one specialist demo).  
**Findings SoT:** `WP-07_REDTEAM.md`  
**Product:** **KWB**  
**Related intent:** `SKILL_LIBRARY_INTENT.md` (superseded where this freeze conflicts — freeze wins).

**Stack / agent framework:** not locked.

---

## 1. One-sentence contract

At **organisation level**, every user task maps to a **role pack + task skill(s) + specialist(s) + allowed tools** under a **task grant**; the **skill library** is complete on disk but **runtime load is narrow**. The **SIH demo** is a **slice**: one task → one specialist, built-in tools, iteration default **5** (editable ≤ Admin max), single model OK — while org paper keeps the **full specialist/tool catalog** and may run **parallel specialists** without shared super-context.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Org catalog lists all specialists/tools | All of them loaded into every session |
| Parallel specialists (org) | Swarm / shared super-brain |
| Editable iteration limit | Unbounded loops |
| Role + task skills | Skills alone = security |
| Demo one specialist | Org has only two agents forever |
| Distinct model ids when possible (org) | Demo must use two GPUs |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Must-work specialists: **inspect** + **code** (multimodal under inspect) |
| **D2** | Spreadsheet = **ambition** |
| **D3** | Iteration **default = 5**; user may edit; ≤ **Admin max** (fail-closed above max) |
| **D4** | **Org:** prefer **distinct** model ids in routing log when multiple cards exist; **Demo:** **single model** OK |
| **D5** | Must-work tools = **built-in**; MCP via **WP-08** |
| **D6** | **Org:** parallel specialists **allowed**; **Demo:** **one task → one specialist** |
| **D7** | Org must publish **role×task → skill → tools** matrix; unknown task → map to approved job/skill or **fail-closed** |

---

## 4. Architecture layers

| Layer | Role |
|---|---|
| **System policy (T0)** | Never, grants, HITL, tool rails — not a `SKILL.md` |
| **Orchestrator** | Plan; match role+task → skill(s)+specialist(s); dispatch; iterate/stop; HITL handoff |
| **Specialist agent** | One job-family context; loads task skill body; calls intersected tools |
| **Skill library** | On-disk catalog (org / plugin / personal shelves) |
| **Tools** | Built-in + (later) MCP |

All tool/agent calls carry **`grant_id`** (WP-04). Skills delimited **T3** (WP-23).

---

## 5. Skill library — role + task (org-critical)

### 5.1 Bind formula (frozen)

```
visible_tools =
    skill.allowed-tools
  ∩ role_pack.allowed-tools
  ∩ grant.tool_plugin_allowlist
  ∩ Admin_allowlist
```

```
loaded_skills =
    match(task_type, role_class) from library index
  → progressive load of 1..few SKILL.md bodies
  → never entire library
```

### 5.2 Role packs (org)

| Role class | Role pack intent | Typical tools (intersected later) |
|---|---|---|
| **Knowledge worker** | Run jobs; attach; verify OCR; edit workspace DRAFT; request grants | ingest, retrieve, file R/W workspace, sandbox (if code job), cite helpers |
| **Approver** | H2/H3/H7/H9 decisions; deny grant expand; skill promote | HITL actions; read monitors; **no** unbounded sandbox by default |
| **Admin** | Cards, MCP/skill allowlist, templates, offline intake, Audience A | Admin config tools; **not** silent engineering Approver |

Role packs are **skills/metadata**, not autonomous Approver/Admin bots (WP-00 Never).

### 5.3 Task skills (org catalog — must exist as named slots)

| Task / job id | Shelf | Bucket | Specialist |
|---|---|---|---|
| `inspect-to-note` | Org | **Must** | Inspect |
| `multimodal-understand` | Org | **Must** (may share inspect specialist) | Inspect |
| `code-sandbox` | Org | **Must** | Code |
| `doc-search-cite` | Org | Ambition | Retrieve/doc |
| `correspondence-ground` | Org | Ambition | Retrieve/doc |
| `drawing-review` | Org | Ambition | Drawing |
| `sensitive-corpus-work` | Org | Ambition | Sensitive (stricter grant) |
| `spreadsheet-assist` | Org | Ambition/deferred w/ Excel | Spreadsheet |
| `board-deck` | Org | Deferred (PPT) | Doc/deck |
| `rulebook-calc` | Org | Deferred (calc) | Calc/code |
| Freestyle (company-allowed) | Org/personal propose | Per policy | Mapped specialist or deny |
| Plugin-bundled skills | Plugin | Per WP-08 install | As declared |
| Personal skills | Personal | Ambition; H6 to org | Same |

**Unknown user task:** orchestrator must map to an approved job/skill **or fail-closed / ask human** — must not invent a specialist with all tools.

---

## 6. Specialist catalog (organisation level)

| Specialist id | Org bucket | Jobs served | Notes |
|---|---|---|---|
| **orchestrator** | Must | All | Dispatch only; no sandbox default; no cross-task merge |
| **inspect_doc** | **Must** | inspect-to-note, multimodal-understand | Demo primary |
| **code** | **Must** | code-sandbox | Demo primary |
| **retrieve_cite** | Ambition | doc-search-cite, correspondence-ground | Heavy WP-11/22 |
| **drawing** | Ambition | drawing-review | WP-01 ambition |
| **sensitive** | Ambition | sensitive-corpus-work | Stricter grant/segregation |
| **spreadsheet** | Ambition | spreadsheet-assist | When Excel promoted |
| **calc** | Deferred | rulebook-calc | Org-only calc |
| **deck** | Deferred | board-deck | PPT deferred |

**Demo slice:** only **inspect_doc** *or* **code** per run (D6) — both exist in product; jury shows one path at a time (plus routing proof across two jobs over the demo script as WP-01 requires).

**Parallel (org only):** ≥2 specialists may run under **same `grant_id`** with **separate contexts**; orchestrator mediates; **forbidden** to concatenate all tool memories into one super-context.

---

## 7. Tool catalog

### 7.1 Built-in (organisation)

| Tool id | Must / ambition | Used by | Gates |
|---|---|---|---|
| `retrieve` | **Must** | inspect, retrieve_cite, sensitive | Grant; authz-first WP-11 |
| `file_read_workspace` | **Must** | most | Grant |
| `file_write_workspace` | **Must** | inspect, code, … | Grant; H4b; org-shelf H4 |
| `ingest_ocr` | **Must** | inspect | Grant; H1 WP-03/05 |
| `sandbox_exec` | **Must** | code | Grant; pre-HITL if T2–T4 WP-23; H9 |
| `claim_label` / cite helper | **Must** when KB path | inspect, retrieve_cite | WP-22 |
| `spreadsheet_ops` | Ambition | spreadsheet | Same write/HITL |
| `export_download` | **Must** (user-facing) | via HITL H3 | Not free agent spam |
| MCP `*` | Host **WP-08** | per allowlist | Admin + grant |

### 7.2 Never tools

SoR write · OT/DCS · WAN/http fetch · cloud MCP · unrestricted shell on host.

---

## 8. Iterate

- Default **max_iterations = 5** (D3).  
- User-editable per task ≤ **Admin max** (org configures; demo Admin max ≥5).  
- Stop on: success criteria, HITL gate, grant revoke, user abort, max reached → fail-closed / hand to human.  
- Official **iterate** — not one-shot chat as product path.

---

## 9. Models in log (D4)

| Mode | Rule |
|---|---|
| **Demo** | Single model id OK for specialist+orchestrator |
| **Org** | Prefer distinct card ids when catalog has ≥2 suitable cards; Expected Solution auto-select proof still requires ≥2 task types → ≥2 ids when demonstrating routing (WP-01) — org deploy should enable that |

---

## 10. Must / ambition / deferred / never

### Must-work (demo + contract)

1. Orchestrator + inspect_doc + code specialists exist.  
2. Demo: one task → one specialist; built-in tools; iteration default 5 editable.  
3. Skill bind formula §5.1; progressive load.  
4. Role packs for worker/approver/admin.  
5. Task skills for must jobs.  
6. No shared super-context; grant on every call.  
7. System policy ≠ skill.  
8. Org paper includes full catalogs §5–§7 even if demo slices.

### Org-ambition

- Full specialist set; parallel specialists; MCP tools; spreadsheet/drawing/sensitive packs; distinct model routing day-to-day.

### Deferred

- PPT/calc specialists as active; swarm debate; browser agents.

### Never

- Mega-agent all tools standing.  
- Load entire skill library every turn.  
- Parallel without isolation / super-context merge.  
- Unbounded iterations.  
- Invent specialist for unknown task with full toolbelt.  
- CrewAI/AutoGen/Smolagents/OpenHands-browser as product identity.  
- Skill restrictions as sole security.  
- SoR/OT/WAN tools.

---

## 11. Adopt / add / refuse (repos)

| Source | Adopt | Refuse |
|---|---|---|
| **agentskills.io** | SKILL.md, progressive disclosure, allowed-tools | Skills Hub WAN |
| **Goose / mcp-agent** | MCP-first host *ideas* | Public MCP directory |
| **OpenHands** | Code specialist tool host + HITL *pattern* | Browser; whole product |
| **Continue** | Thin client shape | Cloud models |
| **PydanticAI** | Typed tools *style* | Lock |
| **Hermes** | Skill files; approve sensitive ops *behaviour* | Self-mod agent product |
| **CrewAI / AutoGen** | — | Swarm KWB |
| **Our Add** | Role×task matrix; org catalog; demo slice; bind formula; parallel isolation | — |

---

## 12. Demo acceptance

1. Inspect job → **inspect_doc** only; skills narrow; tools intersected.  
2. Code job → **code** only; sandbox under HITL rules.  
3. Iteration default 5; user can edit; cannot exceed Admin max.  
4. No second specialist context merged in demo run.  
5. Single model log OK in demo.  
6. Attempt “load all skills” → system still progressive/narrow.

---

## 13. Boundary → next

| Topic | Later |
|---|---|
| Sandbox jail ≠ GPU | **WP-16** |
| MCP install host | **WP-08** |
| Model cards / route | **WP-24 / WP-06** |
| Context packing | **WP-21** |
| Personal `.md` harness | **WP-15** |

---

## 14. Source-of-truth summary

| Theme | Grade |
|---|---|
| Tool list + iterate | **Official** Description |
| Inspect + code demo | **Official** Expected Solution |
| Orchestrator + specialists | **WP-00** |
| Jobs / role classes | **WP-01** |
| Grants on tools | **WP-04** |
| HITL | **WP-05** |
| Skills T3 | **WP-23** |
| Skill library intent | **User** + Spec Agent Skills |
| DM demo/org split | **DM** 2026-09-18 |

---

## 15. Next

**WP-16** — Execution sandbox (jail ≠ GPU).

---

## 16. Changelog

| Rev | Note |
|---|---|
| **1.0** | Org role×task catalog + demo slice + deep red-team |

**Confidence:** **0.87**
