# NOTES — LangGraph interrupt pattern (HITL)

**Allowlisted:** REPO_PULL_MAP — “LangGraph interrupt *pattern* only”.  
**Not Wave 2 extract bulk** — notes only; no module copied.

## Pattern (docs 2026-09-19)

1. Compile graph with a **checkpointer** (persist state while paused).
2. Pass stable `config={"configurable": {"thread_id": "…"}}`.
3. Inside a node: `approved = interrupt(payload)` → execution pauses; payload surfaces to caller.
4. Resume: same `thread_id` + `Command(resume=value)` → value becomes return of `interrupt()`.
5. **Critical:** on resume, the **node restarts from the beginning** — code before `interrupt()` re-runs (must be idempotent).

Docs: https://docs.langchain.com/oss/python/langgraph/interrupts

## KWB mapping

| LangGraph | Ours |
|---|---|
| `interrupt(payload)` | Hard gate wait (H1 OCR ack, H2 stale, H3/H9 evidence) |
| checkpointer + thread_id | Session/grant-scoped pending decision record |
| `Command(resume=…)` | Desk accept / edit / reject → continue orch |
| Graph-as-runtime | **Refuse** — thin custom loop owns grants/Word |

## Already decided

WP-05: adopt interrupt/resume *pattern*; refuse LangGraph-as-product and in-app Approver queue cosplay.

## Other named sources checked (not duplicated here)

| Source | Status |
|---|---|
| Agent Skills `SKILL.md` | Already in `from_software_agent_sdk/08_skills_example` |
| Langfuse self-host | Pattern only; we already have `audit.py` JSONL — no extract |
| GBrain provenance | Named in WP-11; no clear MIT slice fetched this pass — **skipped** |
| Goose / mcp-agent | Covered by MCP / FastMCP slices |
| NeMo / LlamaFirewall | Ideas only in freezes — not Wave 2 allowlist bulk |
