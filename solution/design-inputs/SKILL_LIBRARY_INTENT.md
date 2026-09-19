# Skill library — tools and agents

**Date:** 2026-09-17  
**Status:** Product **intent** for WP-07 / WP-08 / WP-15. Not a freeze until those WPs. Not app code.

**User:** we can add a skill library to all the tools and agents for efficient work.

**Answer:** **Yes — as a library the workbench loads from, not as every skill glued to every tool at once.**

---

## What it is

A **skill library** is an on-disk catalog of Agent Skills (`SKILL.md` + optional `scripts/` `references/` `assets/`), same format as [agentskills.io](https://agentskills.io/specification).

| Who uses it | How |
|---|---|
| **Orchestrator** | Matches task → skill `name`/`description` (~metadata only at start) |
| **Specialist agent** | Loads **that** skill body when the task is theirs |
| **Tool / MCP plugin** | Skill may list `allowed-tools` so the agent only sees the tools that skill needs |
| **Personal `.md` (WP-15)** | Daily work can **propose** a new skill file; HITL promotes it into the **org** library |

This is the same plug pattern as models and MCP: **add/remove a skill pack without redesigning the workbench.**

---

## Why not “all skills on all tools”

Dumping the whole library into every agent/tool:

- Burns context (Agent Skills **progressive disclosure** exists for this).
- Is standing privilege (contradicts task grants, WP-04).
- Lets an inspection skill see the coding sandbox and vice versa.

**Efficient** means: library is complete; **runtime load is narrow**.

```text
Skill library (on disk, air-gap)
    → index: name + description for all skills
        → task match
            → load one (or few) SKILL.md
                → only allowed-tools for that skill
                    → specialist agent runs
```

---

## Three shelves in the same library

| Shelf | Who writes | HITL to use org-wide? |
|---|---|---|
| **Org skills** | Approved pack (offline install, WP-19) | Already approved |
| **Plugin skills** | Bundled in an MCP/plugin pack (WP-08) | Plugin install gate |
| **Personal** | User daily `.md` (WP-15) | Yes, before it becomes org |

Do not store personal files next to controlled SOPs (WP-01 artefact classes).

---

## Source of truth

| Claim | Grade |
|---|---|
| Skills as directories + `SKILL.md`, progressive load | **Spec** [agentskills.io](https://agentskills.io/specification) |
| Claude/Codex-class workbench uses skills/plugins | **Official** Background + **User** host |
| Attach every skill to every tool | **Refuse** — context + grants |
| Unsupervised training as “library” | **Refuse** — WP-15 is markdown, not weights |
| Internet skill marketplace at runtime | **Refuse** — Expected Solution, zero external calls |

Repo map: adopt Hermes/Continue **skill files**, not Hermes self-modification; not Skills Hub.

---

## Where it freezes later

- **WP-00** — one line: workbench has a **skill library** (catalog).  
- **WP-07** — how agents bind skills to tools.  
- **WP-08** — plugins may ship skills.  
- **WP-15** — personal → org promotion.  
- **WP-23** — skill body is untrusted text until gated.

No skill Markdown packs are authored in this folder until WP-07/15 say so.
