# WP-07 tools/agents — deep adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-07_ARCHITECT_PERSPECTIVE.md` + DM expansion (org role×task skill/tool matrix; full org specialist catalog)  
**DM answers:** see §0  
**Against:** Official Description tools+iterate; WP-00 specialists/skills; WP-01 jobs/roles; WP-04 grants; WP-05 HITL; WP-23 T3 skills; `SKILL_LIBRARY_INTENT.md`; `DESIGN_REPO_MAP_v1.md` WP-07.

---

## 0. DM answers (binding)

| Q | Decision |
|---|---|
| **1** | Must specialists = **inspect + code** (multimodal under inspect) |
| **2** | Spreadsheet tool/specialist = **ambition** |
| **3** | Max iterations **default = 5**; **user-editable** (demo + org) |
| **4** | **Org:** prefer **distinct** model ids in log when possible; **Demo:** **single model** OK |
| **5** | Must-work tools = **built-in**; MCP = **WP-08** |
| **6** | **Org:** parallel specialists **allowed** (same grant, no super-context merge); **Demo:** **one task → one specialist** focus |
| **R0** | Org paper must define **role-based + task-based** skill library and **all org specialists/tools**; demo is a narrow slice |

---

## Verdict

| | |
|---|---|
| Architect OK but thin for org? | **Yes** — need role×task matrix + full org specialist catalog |
| Missing? | **M1–M14** |
| Overhyped? | “All specialists” = always loaded; parallel = shared brain; editable N = unbounded; skills = security |
| Confidence after freeze | **~0.87** → GO WP-16 |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Role skill packs vs task skills | **Role shelf** (worker/approver/admin capabilities) ∩ **task skill** (job how-to) ∩ grant |
| **M2** | Full org specialist catalog | Name all org-ambition specialists from WP-01 families; mark must vs ambition |
| **M3** | Tool catalog org-complete | Built-in matrix + MCP slot; spreadsheet ambition |
| **M4** | Bind formula | `visible_tools = skill.allowed-tools ∩ role_pack.tools ∩ grant.tool_allowlist ∩ Admin_allowlist` |
| **M5** | Parallel specialists | Allowed org; **separate contexts**; same `grant_id`; **no** merge of tool results into one super-prompt without orchestrator mediation |
| **M6** | Iteration default 5 | Hard default; user may raise only ≤ **Admin max** (must freeze Admin max exists; exact number later or e.g. 20) |
| **M7** | Demo vs org routing log | Demo single model OK; org prefer ≥2 ids when ≥2 cards (align Expected Solution when proving auto-select) |
| **M8** | “Any user-specified task” | Must map to **known job type** or **Admin-approved freestyle template + skill**; unknown → fail-closed / ask human — not invent specialist |
| **M9** | Approver/Admin agents | Not autonomous bots; **role skills** for UI/actions; agents still under Never |
| **M10** | Orchestrator tools | Narrow: plan, dispatch, stop, HITL handoff — no sandbox by default |
| **M11** | Skill progressive disclosure | Index metadata first; body on match (intent) |
| **M12** | Spreadsheet | Ambition specialist + tool when Excel promoted |
| **M13** | Drawing-review specialist | Ambition (WP-01) |
| **M14** | Sensitive-corpus specialist | Ambition; stricter grant (WP-01/04) |

---

## 2. Overhyped → fix

| Attack | Fix |
|---|---|
| **A1** Org catalog = all loaded every session | Catalog on disk; **runtime load narrow** |
| **A2** Parallel specialists = swarm product | Mediated by orchestrator; no CrewAI identity |
| **A3** Editable iterations = infinite | Cap by Admin max; fail-closed |
| **A4** Role skill = security boundary | Still grant + HITL + WP-23 |
| **A5** Distinct ids always | Prefer when cards exist; demo single OK |
| **A6** Freestyle task = any agent | Must bind approved skill/job or deny |

---

## 3. Source-of-truth map

| Claim | Grade |
|---|---|
| Tools: file R/W, sandbox, spreadsheet, internal search; iterate | **Official** Description |
| ≥2 task types / coding+inspect demo | **Official** Expected Solution |
| One orchestrator; separate agents; no super-context | **WP-00** / **User** |
| Skill library task/role scoped | **WP-00** + **SKILL_LIBRARY_INTENT** + **User** |
| Grants bind tools | **WP-04** |
| HITL on write/export/sandbox | **WP-05** / **WP-23** |
| Skills T3 | **WP-23** |
| Job families | **WP-01** |
| Agent Skills progressive disclosure | **Spec** agentskills.io |
| Goose/OpenHands/Continue patterns | **Repo map** Observed — not forks |

---

## 4. Adopt from which repos (patterns only)

| Repo / pattern | Adopt what | Do **not** take |
|---|---|---|
| **Agent Skills** (agentskills.io) | `SKILL.md`, progressive disclosure, allowed-tools | Skills Hub / WAN install |
| **Goose / mcp-agent** | MCP-first tool host *ideas* | Cloud MCP directory |
| **OpenHands** | Tool host + event stream + HITL for **code specialist only** | Browser use; as whole KWB |
| **Continue** | Thin client `base_url`+model | Cloud models |
| **PydanticAI** | Typed tools *style* candidate | Lock runtime |
| **Hermes** | Skill files; approve sensitive ops *behaviour* | Self-modifying agent as product |
| **CrewAI / AutoGen** | — | Swarm product identity |
| **Smolagents** | — | Code-everything default |
| **LangGraph** | Interrupt pattern already WP-05 | Lock-in as KWB |

---

## 5. Disposition

**Applied.** → `WP-07_FREEZE.md` rev 1.0. Confidence **0.87**. **GO** → **WP-16**.
