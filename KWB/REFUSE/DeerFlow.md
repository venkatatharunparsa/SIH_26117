# REFUSE — DeerFlow

**Do not extract** DeerFlow into `KWB/`.

## Reasons

1. **Out of extract plan** — SIH26117 KWB pulls from OpenHands / `software-agent-sdk`, MCP Python SDK, and FastMCP only for this phase (`OPENHANDS_EXTRACT.md` + MCP MOCK later).
2. **Wrong product shape** — DeerFlow is a multi-skill content/generation agent pack (image, video, podcast, newsletter, PPT, etc.). KWB is an offline **inspection / knowledge workbench** (grants, Word DRAFT, self-HITL, sandbox ≠ GPU).
3. **Skills noise** — Public DeerFlow skills assume cloud APIs, marketplace patterns, and generative media pipelines that conflict with air-gap / WAN=0 / Monitor A.
4. **License & scope creep** — Cloning or slicing DeerFlow would dilute the intentional MIT/Apache reference set already mapped and would tempt UI/agent forks we explicitly refuse (same class as forking Agent Canvas).
5. **User / process rule** — Explicit: prefer mapped repos; **Do NOT use DeerFlow**.

## If someone asks later

Point them at `KWB/PULL_INDEX.md` and `solution/prototype/OPENHANDS_EXTRACT.md`. Skills layout reference is already covered by `from_software_agent_sdk/08_skills_example/` (OpenHands AgentSkills example), not DeerFlow.
