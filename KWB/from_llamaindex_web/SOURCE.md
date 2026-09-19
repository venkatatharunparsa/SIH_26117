# SOURCE — from_llamaindex_web

**Upstream:** [run-llama/llama_index](https://github.com/run-llama/llama_index)  
**Fetched:** 2026-09-19 (web + raw GitHub)  
**License:** MIT  
**Role:** Alternate retrieve→cite shape via `CitationQueryEngine` (WP-11). One short module max.

## URLs used

| What | URL |
|---|---|
| CitationQueryEngine tutorial | https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/ |
| Module (raw) | https://raw.githubusercontent.com/run-llama/llama_index/main/llama-index-core/llama_index/core/query_engine/citation_query_engine.py |
| LICENSE | https://raw.githubusercontent.com/run-llama/llama_index/main/LICENSE |

## What KWB will use later

- Number sources in context (`Source N:`) and require `[n]` in the answer.
- Granular citation chunks (`citation_chunk_size`) vs coarse retrieve nodes.
- Prefer reimplement thin cite binder; optional later `pip` if needed.

## Refuse list

- LlamaIndex as product UI / agent frameworks / cloud OpenAI defaults.
- Full multimodal citation engine / workflow packages.
- Embedding-to-OpenAI as required path.

## Files

| File | Kind |
|---|---|
| `SOURCE.md` | this |
| `NOTES.md` | study |
| `excerpt_citation_query_engine.py` | templates + class header (trimmed) |
| `LICENSE.MIT.txt` | notice |
