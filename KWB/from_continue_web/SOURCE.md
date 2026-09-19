# SOURCE — from_continue_web

**Upstream:** [continuedev/continue](https://github.com/continuedev/continue) · docs  
**Fetched:** 2026-09-19 (web only — no local `vendor/` clone)  
**License:** Apache-2.0 (`https://raw.githubusercontent.com/continuedev/continue/main/LICENSE`)  
**Role:** Study OpenAI-shape `apiBase`/`base_url` + `model` client triad for our thin `httpx` gateway.

## URLs used

| What | URL |
|---|---|
| OpenAI / compatible provider docs | https://docs.continue.dev/customize/model-providers/top-level/openai |
| Config YAML reference | https://docs.continue.dev/reference/ |
| LICENSE | https://raw.githubusercontent.com/continuedev/continue/main/LICENSE |

## What KWB will use later

- Local `/v1` endpoint shape: `provider: openai` + `model` + `apiBase: http://localhost:…/v1`.
- Confirm gateway triad already in `backend/app/gateway.py` matches Continue/OpenHands class clients.
- Optional: deny cloud defaults; keep Model Cards as catalog (WP-24).

## Refuse list

- Continue IDE extension / UI as product shell.
- Cloud model defaults (OpenAI/Anthropic as day-1 runtime).
- LiteLLM / BerriAI cloud proxy as product brain (listed as compatible provider — do not adopt).
- Full Continue repo clone into `vendor/` (not needed for this slice).

## Files in this folder

| File | Kind |
|---|---|
| `SOURCE.md` | this |
| `NOTES.md` | study notes |
| `excerpt_openai_compatible_config.yaml` | public docs YAML snippets |
| `LICENSE.Apache-2.0.txt` | license pointer (short notice) |
