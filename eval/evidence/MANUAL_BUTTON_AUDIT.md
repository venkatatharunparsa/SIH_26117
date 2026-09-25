# Manual button audit — kwb-app

**Date:** 2026-09-20  
**Method:** Code-path review + API exercise of wired actions. Desk dual-model API prove: `e2e_one_model.py` PASS on LAPTOP-A peer (`inspect→llama3.2:3b`, `code→qwen2.5-coder:7b`). UI click smoke for attach/HITL already recorded in Workflow B + MANUAL_TEST_REPORT.

| Control | Location | Expected | Result | Notes |
|---------|----------|----------|--------|-------|
| + new session | SessionList | New inspection session | PASS (wired) | `onNew` |
| Select session | SessionList | Switch active | PASS (wired) | |
| Monitor toggle | Titlebar | Open/close panel | PASS (wired) | |
| Task type inspection/coding | Composer | Switches task / conductor | PASS (wired) | Dual-tag API proven |
| Attach Document… | Composer | File picker → orch attach | PASS (Workflow B) | README fixture |
| Load fixture | Composer | Loads demo fixture | PASS (wired) | |
| Clear attach label | Composer | Clears pill | PASS (wired) | |
| Send / Confirm | Composer | `/orch/turn` | PASS | Busy shows `…` |
| Edit draft | More | draft-edit tool | PASS (API e2e) | |
| Sandbox calc | More | `/sandbox/calc` | PASS (API) | |
| Sandbox red | More | fail demo | PASS (API G10) | |
| Evidence pack start/stop | More | Monitor A | PASS (API) | ≠ CERT |
| Inject secret | More | G9 deny | PASS (API) | |
| Bad model | More | G8 deny | PASS (API) | |
| Revoke grant | More | 403 tools | PASS (API G7) | |
| Tool card expand | Transcript | Toggle body | PASS (wired) | |
| Live log / Status / Share tabs | Monitor | Switch | PASS (wired) | |
| Refresh target | Monitor | `/inference/status` | PASS | Shows LAPTOP-A |
| Verify audit | Monitor | `/audit/verify` | PASS (API) | |
| Download DRAFT | Monitor | artefact URL | PASS (Workflow B) | |
| Download leave pack | Monitor | leave pack | PASS (API) | |
| Copy share text | Monitor | Clipboard | PASS (wired) | |

## Dual-model / external GPU prove (this run)

```
inference: lan_peer_laptop_a @ 10.45.226.121
G1: inspect-draft→llama3.2:3b / code-assist→qwen2.5-coder:7b
e2e_one_model.py: PASS (all gates)
```

## Residual UI taste (Phase 3 — not button failures)

Static feel during long LLM calls (no mid-turn phases) — Phase 2. Visual hierarchy / logo — Phase 3.
