# NOTES — Haystack (retrieve → cite)

**Intent:** Pipeline shape only (REPO_PULL_MAP Wave 2).

## Shape

```text
DocumentStore
    → Retriever (query → documents)
    → PromptBuilder (inject numbered docs + question)
    → Generator / LLM
    → AnswerBuilder (optional: parse [n] cites → referenced documents)
```

## Citation binding

From AnswerBuilder docs (https://docs.haystack.deepset.ai/docs/answerbuilder):

- Prompt should instruct the model to cite by **1-based index** into the retrieved list.
- Optional `reference_pattern` (e.g. `r"\[(\d+)\]"`) keeps only docs actually referenced in the reply.
- Without `reference_pattern`, all retrieved docs attach to the answer object.

## KWB mapping

| Haystack idea | Ours |
|---|---|
| Retriever docs | Grant-filtered corpus hits (G6) |
| Numbered context | Citation panel / Word DRAFT footnotes |
| AnswerBuilder references | Provenance fields; refuse unverified invent |
| Pipeline.connect | Thin orchestrator steps — not Haystack runtime |

## Prefer over LlamaIndex when…

Explicit DAG of named components is easier to explain to jurors as “retrieve then cite.”
Both are study-only; pick one outline for WP-11 notes.
