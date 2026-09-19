# Trimmed excerpt — LlamaIndex CitationQueryEngine (MIT)

Source: https://raw.githubusercontent.com/run-llama/llama_index/main/llama-index-core/llama_index/core/query_engine/citation_query_engine.py
Copyright (c) Jerry Liu — MIT License
Fetched: 2026-09-19 — templates + class docstring only (full multimodal engine omitted).

```python
from llama_index.core.prompts import PromptTemplate

CITATION_QA_TEMPLATE = PromptTemplate(
    "Please provide an answer based solely on the provided sources. "
    "When referencing information from a source, "
    "cite the appropriate source(s) using their corresponding numbers. "
    "Every answer should include at least one source citation. "
    "Only cite a source when you are explicitly referencing it. "
    "If none of the sources are helpful, you should indicate that. "
    "For example:\n"
    "Source 1:\n"
    "The sky is red in the evening and blue in the morning.\n"
    "Source 2:\n"
    "Water is wet when the sky is red.\n"
    "Query: When is water wet?\n"
    "Answer: Water will be wet when the sky is red [2], "
    "which occurs in the evening [1].\n"
    "Now it's your turn. Below are several numbered sources of information:"
    "\n------\n"
    "{context_str}"
    "\n------\n"
    "Query: {query_str}\n"
    "Answer: "
)

DEFAULT_CITATION_CHUNK_SIZE = 512
DEFAULT_CITATION_CHUNK_OVERLAP = 20


class CitationQueryEngine:  # subclass BaseQueryEngine upstream
    """
    Citation query engine.

    Args:
        retriever: A retriever object.
        citation_chunk_size: Size of citation chunks, default=512.
        citation_chunk_overlap: Overlap of citation nodes, default=20.
    """

    @classmethod
    def from_args(cls, index, similarity_top_k: int = 3, citation_chunk_size: int = 512, **kwargs):
        """Build engine from an index (see upstream for full signature)."""
        ...

    def _create_citation_nodes(self, nodes):
        """Modify retrieved nodes to be granular numbered sources."""
        # each chunk → "Source {i}:\\n{text_chunk}\\n"
        ...

    def _query(self, query_bundle):
        """retrieve → _create_citation_nodes → synthesize with CITATION_QA_TEMPLATE"""
        ...
```

**KWB takeaway:** number sources in context; require `[n]`; fail soft when sources unhelpful.
