# KWB adversarial red-team report

**When:** 2026-09-20T20:12:01.341456+00:00
**Target:** `http://127.0.0.1:8080` (localhost workbench API)
**Open HIGH:** 0 · **Open MED:** 0

| ID | Attack | Result | Sev | Detail |
|----|--------|--------|-----|--------|
| A1 | public model gpt-4o | BLOCKED | info | {'detail': {'ok': False, 'error': 'gateway_deny', 'reason': 'model_not_on_card', |
| A2 | public model claude | BLOCKED | info | {'detail': {'ok': False, 'error': 'gateway_deny', 'reason': 'model_not_on_card', |
| A3 | base_url override to openai ignored | BLOCKED | info | st=200 base=http://127.0.0.1:11434 |
| B1 | fake grant retrieve | BLOCKED | info | {'detail': {'ok': False, 'error': 'grant_not_found', 'grant_id': 'deadbeef'}} |
| B2 | fake grant sandbox | BLOCKED | info | {'detail': {'ok': False, 'error': 'grant_not_found', 'grant_id': '000000000000'} |
| B3 | revoked grant retrieve | BLOCKED | info | {'detail': {'ok': False, 'error': 'grant_revoked', 'grant_id': '2e350b508fc04584 |
| B4 | revoked grant orch | BLOCKED | info | {'detail': {'ok': False, 'error': 'grant_inactive'}} |
| C1-..%2F..%2F.. | path traversal ..%2F..%2F..%2Fwindows%2Fwin.ini | BLOCKED | info | {'detail': 'Not Found'} |
| C1-../../../etc | path traversal ../../../etc/passwd | BLOCKED | info | {'detail': 'Not Found'} |
| C1-..\..\..\win | path traversal ..\..\..\windows\win.ini | BLOCKED | info | {'detail': {'error': 'unsupported_type', 'allowed': ['.docx', '.json', '.pptx'], |
| C1-....//....// | path traversal ....//....//....//windows/win.ini | BLOCKED | info | {'detail': 'Not Found'} |
| C2 | artifact download without grant_id | BLOCKED | info | file=draft-00ab78a660.docx st=403 |
| C3 | artifact wrong grant_id | BLOCKED | info | {'detail': {'error': 'grant_mismatch', 'filename': 'draft-00ab78a660.docx', 'gra |
| D1 | secret export-check | BLOCKED | info | {'detail': {'ok': False, 'error': 'secret_in_draft', 'hits': ['password_like', ' |
| D2 | openai-like key export-check | BLOCKED | info | {'detail': {'ok': False, 'error': 'secret_in_draft', 'hits': ['provider_sk_like' |
| E1 | sandbox network to example.com denied | BLOCKED | info | stdout=NET_DENY OSError
 network=host-process + socket/urlopen deny guard (not d |
| E2 | sandbox read win.ini blocked or empty | BLOCKED | info | {'ok': True, 'mode': 'process', 'exit_code': 0, 'stdout': '', 'stderr': '', 'dur |
| E3 | export after sandbox-red | BLOCKED | info | {'detail': {'error': 'draft_not_found', 'filename': 'nope.docx'}} |
| F1 | invalid attach_b64 | BLOCKED | info | {'detail': {'ok': False, 'grant_id': '86998db7aec94ebf', 'task_id': 'be061613e9d |
| F2 | empty attach | BLOCKED | info | {'detail': {'ok': False, 'grant_id': '40339cec39b741f6', 'task_id': '57326f6d974 |
| G1 | export without H2 | BLOCKED | info | {'detail': {'error': 'h2_required', 'message': 'Own-work H2 ack required before  |
| H1 | unknown MCP tool | BLOCKED | info | {'detail': {'error': 'grant_required', 'message': 'mcp/call requires grant_id'}} |
| H2 | MCP call without grant_id | BLOCKED | info | {'detail': {'error': 'grant_required', 'message': 'mcp/call requires grant_id'}} |
| I1 | audit chain verifies | BLOCKED | info | {'ok': True, 'entries': 2250, 'skipped_legacy': 0, 'tip': 'a0ce39f1ee2cb9cf87992 |

## Open issues to fix

- None at HIGH/MED from this pass.

## Scope note
API binds 127.0.0.1 — attacks assume local process access (same as desk).
True network isolation / WAN=0 not proven here.

JSON: `C:/Users/THARUN PARSA/Documents/SIH26/eval/evidence/REDTEAM_ADV.json`
