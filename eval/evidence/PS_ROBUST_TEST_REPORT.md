# PS robust workflow test report

**When:** 2026-09-20T19:27:57.208942+00:00
**API:** `http://127.0.0.1:8080`
**Inference:** {'mode': 'lan_peer_laptop_a', 'label': 'LAPTOP-A peer (10.45.226.121)', 'host': '10.45.226.121', 'runtime_reachable': True, 'tags': ['moondream:latest', 'qwen2.5-coder:7b', 'llama3.2:3b']}
**Score:** **24/24**

| WF | Check | Result | Detail |
|----|-------|--------|--------|
| WF0 | health | PASS | 200 |
| WF0 | inference_status | PASS | {'ok': True, 'llm_base_url': 'http://10.45.226.121:11434', 'host': '10.45.226.121', 'mode': 'lan_peer_laptop_a', 'label' |
| WF0 | runtime_reachable | PASS | LAPTOP-A peer (10.45.226.121) |
| WF1 | start_inspection | PASS | inspect-draft |
| WF1 | start_coding | PASS | code-assist |
| WF1 | two_distinct_cards | PASS | inspect-draft vs code-assist |
| WF1 | two_distinct_models | PASS | llama3.2:3b vs qwen2.5-coder:7b |
| WF2 | orch_attach | PASS | phase=await_confirm_extract |
| WF2 | confirm_extract | PASS | phase=await_review_cites |
| WF2 | word_draft | PASS | file=draft-5e9fe99d08.docx phase=await_self_check |
| WF2 | self_check | PASS | phase=await_export |
| WF2 | export_leave | PASS | phase=done |
| WF3 | sandbox_calc | PASS | {'ok': True, 'mode': 'process', 'exit_code': 0, 'stdout': '0.40000000000000036\n', 'stderr': '', 'du |
| WF3 | h9_ack | PASS | 200 |
| WF3 | sandbox_red_or_export_gate | PASS | red=200 export=422 |
| WF4 | image_attach | PASS | vision=True stub_or_ocr=True |
| WF4 | multimodal_engine_honest | PASS | Confirm extract before we treat it as input. Source: on-device vision model (moondream) via Gateway. Enter to accept, or paste a corrected extract. |
| WF5 | monitor_a_start | PASS | 1c6b6911e0d9 |
| WF5 | monitor_a_stop | PASS | 200 |
| WF5 | audit_verify | PASS | {'ok': True, 'entries': 1853, 'skipped_legacy': 0, 'tip': '6cb3d15970070391a669b |
| WF5 | g8_deny_public_model | PASS | 403 |
| WF5 | gateway_host_ok | PASS | None |
| FC | g9_secret_deny | PASS | 400 |
| FC | g7_revoke_blocks | PASS | 403 |

## Design
See `PS_WORKFLOW_DESIGN.md`.

## Honesty
Private LAN / on-prem Gateway path. Not true air-gap. Monitor A ≠ CERT.

JSON: `C:/Users/THARUN PARSA/Documents/SIH26/eval/evidence/PS_ROBUST_TEST.json`
