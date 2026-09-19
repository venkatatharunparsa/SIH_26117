# Excerpt — Continue OpenAI-compatible config (public docs)

Source: https://docs.continue.dev/customize/model-providers/top-level/openai  
License: Apache-2.0 (Continue Dev, Inc.)  
Fetched: 2026-09-19 — documentation snippets only.

## Local / OpenAI-API-compatible server

```yaml
name: My Config
version: 0.0.1
schema: v1

models:
  - name: <OPENAI_API_COMPATIBLE_PROVIDER_MODEL>
    provider: openai
    model: <MODEL_NAME>
    apiBase: http://localhost:8000/v1
    apiKey: <YOUR_CUSTOM_API_KEY>
```

## Force legacy completions endpoint (optional)

```yaml
models:
  - name: <OPENAI_API_COMPATIBLE_PROVIDER_MODEL>
    provider: openai
    model: <MODEL_NAME>
    apiBase: http://localhost:8000/v1
    useLegacyCompletionsEndpoint: true
```

## Force chat completions over Responses API (optional)

```yaml
models:
  - name: gpt-5
    provider: openai
    model: gpt-5
    useResponsesApi: false
```

## KWB takeaway

Our gateway needs injectable `base_url` (Continue: `apiBase`) + `model` + local credential — not Continue’s product config file.
