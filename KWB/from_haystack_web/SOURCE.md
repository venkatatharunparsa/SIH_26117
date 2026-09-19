# SOURCE — from_haystack_web

**Upstream:** [deepset-ai/haystack](https://github.com/deepset-ai/haystack)  
**Fetched:** 2026-09-19 (web docs only)  
**License:** Apache-2.0  
**Role:** Pipeline shape for retrieve → prompt → generate → cite (WP-11). Function outline, not product UI.

## URLs used

| What | URL |
|---|---|
| Creating pipelines | https://docs.haystack.deepset.ai/docs/creating-pipelines |
| AnswerBuilder (citation indices) | https://docs.haystack.deepset.ai/docs/answerbuilder |
| LICENSE | https://raw.githubusercontent.com/deepset-ai/haystack/main/LICENSE |

## What KWB will use later

- Component graph: retriever → prompt_builder → llm → (optional) answer_builder.
- Numbered sources in prompt + `reference_pattern` like `\[(\d+)\]` to bind cites to retrieved docs.
- Our panel cites verified extracts only; Haystack is shape, not dependency day-1.

## Refuse list

- Haystack UI / deepset Cloud / production Haystack app as KWB.
- OpenAIChatGenerator cloud defaults as required runtime.
- Full haystack package tree in `vendor/`.

## Files

| File | Kind |
|---|---|
| `SOURCE.md` | this |
| `NOTES.md` | study |
| `excerpt_rag_cite_pipeline.py` | minimal public-docs-shaped module |
| `LICENSE.Apache-2.0.txt` | notice |
