# SOURCE — from_onyx_web

**Upstream:** [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) (formerly Danswer)  
**Fetched:** 2026-09-19 (web only — no fork)  
**License:** MIT Expat for content **outside** `ee/` directories; Enterprise License under `ee/` — see upstream LICENSE.  
**Role:** Connector + **authz-before-retrieve** intent for G6 MOCK (grant filter → NOT FOUND). Pattern only.

## URLs used

| What | URL |
|---|---|
| Connectors / Document Access Controls docs | https://docs.onyx.app/admins/connectors/overview |
| GitHub connector + permission sync | https://docs.onyx.app/admins/connectors/official/github |
| Retrieval-time ACL filter (MIT path) | https://raw.githubusercontent.com/onyx-dot-app/onyx/main/backend/onyx/db/document_access.py |
| LICENSE | https://raw.githubusercontent.com/onyx-dot-app/onyx/main/LICENSE |

## What KWB will use later

- Intent: documents visible only if connector/doc ACL allows the principal (email / group / public / cc-pair access).
- MOCK schema idea: grant scopes docs before retrieve; denied docs behave as **NOT FOUND** (no leak).
- Separate **auth** (who you are) from **retrieval ACL** (what you may see).

## Refuse list

- Onyx as product / UI / full RAG app.
- Enterprise Edition `ee/` code (permission-sync EE features) — do not copy.
- Cloud Onyx / SSO-as-must-work for air-gap demo.
- Full connector zoo (Confluence, Slack, …) as day-1.

## Files in this folder

| File | Kind |
|---|---|
| `SOURCE.md` | this |
| `NOTES.md` | study notes |
| `excerpt_document_access_filter.py` | trimmed MIT-path ACL filter |
| `mock_acl_schema.example.json` | our MOCK shape (inspired by intent) |
| `LICENSE.MIT-note.txt` | license note |
