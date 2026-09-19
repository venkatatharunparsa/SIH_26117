# NOTES — LlamaIndex CitationQueryEngine

**Intent:** retrieve→cite pipeline shape (alongside Haystack). Prefer one short module.

## API shape (docs)

```python
from llama_index.core.query_engine import CitationQueryEngine

query_engine = CitationQueryEngine.from_args(
    index,
    similarity_top_k=3,
    citation_chunk_size=512,  # granularity of Source N chunks
)
response = query_engine.query("…")
# response includes inline [1], [2]; response.source_nodes holds sources
```

Tutorial: https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/

## Core idea from source

1. Retrieve nodes.
2. Split into numbered `Source {i}:` citation nodes (`_create_citation_nodes`).
3. Synthesize with `CITATION_QA_TEMPLATE` requiring at least one `[n]` cite; refuse unhelpful sources explicitly.

## KWB mapping

| LlamaIndex | Ours |
|---|---|
| `Source N` labels | Citation panel indices |
| `source_nodes` | Provenance list for Word DRAFT |
| “If none helpful, indicate” | NOT FOUND / refuse invent (WP-11) |
| OpenAI Settings in tutorial | Our local `/v1` gateway only |

## Vs Haystack

Both valid. Haystack = explicit component DAG; LlamaIndex = query-engine object. Study both; implement neither as product.
