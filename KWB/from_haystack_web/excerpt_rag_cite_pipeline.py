"""
Minimal RAG cite pipeline shape — study excerpt for KWB.
Inspired by public Haystack docs (Apache-2.0):
  https://docs.haystack.deepset.ai/docs/creating-pipelines
  https://docs.haystack.deepset.ai/docs/answerbuilder
Fetched: 2026-09-19. Not a runnable Haystack install — outline only.
"""

# Conceptual outline (pseudo / docs-shaped). Real Haystack uses:
# Pipeline, InMemoryBM25Retriever, ChatPromptBuilder, AnswerBuilder, ...

PIPELINE_STEPS = (
    "retriever",       # query → documents
    "prompt_builder",  # documents + query → messages (number docs [1]..)
    "llm",             # messages → replies
    "answer_builder",  # replies + documents → GeneratedAnswer w/ cites
)

# AnswerBuilder citation parse (from docs):
# reference_pattern=r"\[(\d+)\]"  → keep only referenced docs (1-based)


def outline_connect():
    """Document the connect order we would mirror in a thin custom loop."""
    return [
        ("retriever", "prompt_builder.documents"),
        ("prompt_builder", "llm.messages"),
        ("llm.replies", "answer_builder.replies"),
        ("retriever", "answer_builder.documents"),
    ]


PROMPT_CITE_HINT = """
Given these documents, answer the question.
Reference sources by number, e.g. [1], [2].
If nothing relevant, say so (do not invent).

{% for doc in documents %}
Document[{{ loop.index }}]:
{{ doc.content }}
{% endfor %}

Question: {{query}}
Answer:
"""
