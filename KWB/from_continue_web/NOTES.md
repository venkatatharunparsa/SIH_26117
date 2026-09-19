# NOTES — Continue.dev (client triad)

**Intent (REPO_PULL_MAP Wave 2):** Study only. We write a thin `httpx` client; we do not fork Continue.

## Pattern to adopt

Continue configures models with an OpenAI-compatible triad:

| Field | Continue YAML | Our workbench |
|---|---|---|
| Protocol adapter | `provider: openai` | OpenAI-shape HTTP client |
| Model id | `model: <MODEL_ID>` | Model Card `model_id` |
| Endpoint root | `apiBase: http://localhost:8000/v1` | gateway `base_url` / `llm_base_url` |
| Credential | `apiKey` | local/Bearer or dummy for air-gap |

Docs (2026-09-19): https://docs.continue.dev/customize/model-providers/top-level/openai

Compatible local runtimes called out in Continue docs include llama-cpp-python, vLLM, LocalAI, text-gen-webui — same class as our deferred runtime pick.

## Extra knobs (awareness only)

- `useLegacyCompletionsEndpoint: true` → force `/completions` instead of `/chat/completions`.
- `useResponsesApi: false` → force `/chat/completions` when `/responses` is unwanted.
- We stay on `/v1/chat/completions` + `/v1/models` (LCD).

## Map to G1 / G8

- G1: catalog + enabled card + local endpoint.
- G8: deny public WAN URLs in gateway — Continue’s cloud defaults are the anti-pattern.

## Do not take

Extension UI, cloud autocomplete providers, embeddings/rerank cloud stacks, marketplace skills.
