# SOURCE — from_langgraph_web

**Upstream:** LangGraph (LangChain) — interrupt / HITL pattern  
**Fetched:** 2026-09-19 (web docs only)  
**License:** LangGraph is typically MIT (confirm at package pin time); this folder is **notes-only** (no code copy).  
**Why here:** Allowlisted in `REPO_PULL_MAP.md` as “LangGraph interrupt *pattern*” for HITL — not a Wave 2 vendor merge, but named study source not yet in KWB.

## URLs used

| What | URL |
|---|---|
| Interrupts | https://docs.langchain.com/oss/python/langgraph/interrupts |
| Checkpointers | https://docs.langchain.com/oss/python/langgraph/checkpointers |

## What KWB will use later

- Metaphor only: pause at hard gate → persist decision context → resume after human ack (H1–H3/H9).
- Our gates own policy; optional LangGraph dep later is **not** required.

## Refuse list

- LangGraph-as-product / as owner of grants or HITL identity.
- Cloud LangSmith as audit truth (we use JSONL).
- Full graph framework lock-in (WP-05 refuse).

## Files

| File | Kind |
|---|---|
| `SOURCE.md` | this |
| `NOTES.md` | pattern notes only |
