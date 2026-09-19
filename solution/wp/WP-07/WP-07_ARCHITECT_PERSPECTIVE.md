# WP-07 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-01 / WP-04 / WP-05 / WP-11 / WP-22 / WP-23  
**Status:** **SUPERSEDED by `WP-07_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-07_REDTEAM.md`.  
**Job of WP-07:** Freeze **local tools**, **system policy vs skills**, **one orchestrator + specialist agents** (no shared super-context), **iterate** loops, and **skill-library bind** (task-scoped `SKILL.md` + `allowed-tools`) — not a mega-agent with every plugin.

**Sources:** Official Description (plan, iterate, file R/W, sandbox, spreadsheet, internal search); Expected Solution (inspect + code + multimodal); WP-00 specialist agents + skill library; `SKILL_LIBRARY_INTENT.md`; WP-04 grants; WP-05 HITL/write; WP-23 T3 skills; repo map Goose/mcp-agent/OpenHands-*patterns*.

---

## One sentence (proposed)

KWB runs **one orchestrator** that plans and dispatches **specialist agents** for defined jobs; each specialist loads **narrow skills + allowed tools** under the **task grant**, **iterates** until HITL/stop, and never shares a standing super-context with other jobs’ tools or corpora.

---

## 1. Layers (do not collapse)

| Layer | Role |
|---|---|
| **System policy (T0)** | Never list, grant/HITL engines, tool rails — not a skill file |
| **Orchestrator** | Plan; match job → specialist + skill metadata; enforce grant; iterate/stop |
| **Specialist agent** | One job family context; loads skill body; calls allowed tools |
| **Tools** | Local capabilities (built-in + later MCP via WP-08) |
| **Skill library** | On-disk catalog; progressive load; shelves org/plugin/personal |

**Framework ≠ company:** agent loop runs *inside* policy; LangGraph/CrewAI-as-product refused.

---

## 2. Official tool families (proposed)

| Tool family | Official hook | Must-work? | Gates |
|---|---|---|---|
| **Internal search / retrieve** | Description internal search | **Yes** (WP-11) | Grant + authz-first |
| **File read** (workspace / allowed paths) | file read | **Yes** | Grant |
| **File write** (KWB workspace DRAFT/code) | file write | **Yes** | Grant; H4b edit OK; org-shelf = H4; export = H3 |
| **Sandbox exec** | code execution / verify | **Yes** | Grant; **HITL before exec** if T2–T4 (WP-23); H9 after |
| **Ingest / OCR path invoke** | multimodal | **Yes** (WP-03) | Grant; H1 |
| **Spreadsheet** | Description spreadsheet | **Ambition** (Excel deferred WP-00) | Same write/HITL rules when promoted |
| **MCP tools** | Claude/Codex-class host | Principle **yes**; host = **WP-08** | Admin allowlist + grant |

**Never tools:** SoR write, OT/DCS control, WAN fetch, cloud MCP.

---

## 3. Specialists (proposed must set)

| Specialist | Jobs (WP-01) | Default tools (illustrative) |
|---|---|---|
| **Inspect / doc** | `inspect-to-note`, multimodal feed | ingest, retrieve, file R/W workspace, cite/claim helpers |
| **Code** | `code-sandbox` | file R/W workspace, sandbox exec |
| **Orchestrator-only** | routing, stop, HITL queue handoff | no sandbox; no cross-job retrieve merge |

**Ambition:** spreadsheet specialist when Excel promoted.

**Hard rule:** specialists inherit **this task’s grant only** — no shared super-context across concurrent tasks (WP-04).

---

## 4. Skill library bind (from intent → freeze shape)

```
Library index (name + description)
  → orchestrator matches task
    → load 1..few SKILL.md (progressive)
      → intersect skill.allowed-tools ∩ grant.tool_allowlist ∩ Admin allowlist
        → specialist runs
```

- Skills = **T3** delimited (WP-23) even when org-approved.  
- Not every skill on every tool.  
- Personal → org only via H6 (WP-05).  
- Offline packs only (WP-19 later).

---

## 5. Iterate (Official)

- Plan → act → observe → continue until success criteria, HITL gate, grant revoke, or user abort.  
- **Not** one-shot chat as the product path.  
- Max-iteration / timeout fail-closed (exact N later).

---

## 6. System prompt vs skill

| | System policy | Skill |
|---|---|---|
| Authority | T0 | T3 data / how-to |
| Can change Never? | No path | No |
| Loaded | Always (workbench) | Per task match |

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Orchestrator + ≥2 specialists (inspect, code) for Expected Solution jobs.  
2. Tool families: retrieve, file R/W workspace, sandbox, ingest invoke.  
3. Skill library progressive bind; intersect allowlists.  
4. Iterate loop; no shared super-context.  
5. System policy ≠ skill.  
6. All tool calls carry `grant_id` (WP-04).  
7. Side-effect tools respect WP-05 / WP-23 HITL.

### Org-ambition

- Spreadsheet specialist; richer skill packs; more specialists; MCP tools via WP-08 UX.

### Deferred

- Multi-agent debate swarms; browser use; autonomous long-running farms.

### Never

- One mega-agent with all tools/plugins standing.  
- Shared super-context across tasks.  
- CrewAI/AutoGen swarm as product identity.  
- Skill restrictions as sole security.  
- SoR/OT/WAN tools.  
- Glue entire skill library into every prompt.

---

## 8. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Goose/mcp-agent *MCP-first host ideas*; OpenHands *tool host + HITL* for **code specialist only**; Continue thin client shape; Agent Skills progressive disclosure |
| **Add** | Specialist table; allowlist intersect; iterate; policy≠skill |
| **Refuse** | CrewAI/AutoGen swarms; Smolagents code-everything; OpenHands browser; LangGraph lock-in; cloud Continue models |

---

## 9. Boundary vs later WPs

| Topic | WP-07 | Later |
|---|---|---|
| Sandbox jail ≠ GPU | Tool contract | **WP-16** |
| MCP install host | Tool use principle | **WP-08** |
| Which model card | Specialist runs under route | **WP-06 / WP-24** |
| Context packing | Tools return data | **WP-21** |
| Personal skill UX | Bind rules | **WP-15** |

---

## 10. Open questions for decision maker

1. **Must specialists:** confirm **inspect + code** only for must-work (multimodal folds into inspect) — **yes**?  
2. **Spreadsheet tool:** keep **ambition** until Excel promoted — **yes**?  
3. **Max iterations (demo):** freeze a number (e.g. **8** or **12**) or leave unset?  
4. **Orchestrator model:** same card as specialist OK for demo, or must log **distinct** orchestrator vs specialist ids when possible?  
5. **Built-in tools vs MCP for must-work search/file/sandbox:** built-in required; MCP optional demo server — confirm **yes**?  
6. **Parallel specialists on one task:** forbid (recommended) or allow under same grant?

---

## 11. Next after your decisions

**Done.** Frozen as `WP-07_FREEZE.md` rev 1.0. Next: **WP-16**.
