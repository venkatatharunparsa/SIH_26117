# Expected Solution E2E matrix

**Date:** 2026-09-20 (updated after PS robust suite)  
**Design:** [`PS_WORKFLOW_DESIGN.md`](PS_WORKFLOW_DESIGN.md)  
**Robust run:** [`PS_ROBUST_TEST_REPORT.md`](PS_ROBUST_TEST_REPORT.md) — **24/24 PASS** on `lan_peer_laptop_a`

| # | Expected Solution bullet | Workflow | API E2E | Desk | Status |
|---|--------------------------|----------|---------|------|--------|
| 1 | Local deploy mid-range GPU / smaller OW | WF0 | PASS | PASS | **Covered** |
| 2 | Auto-select ≥2 task types | WF1 | PASS full two-tag | Rehearse | **Covered** |
| 3 | Scanned inspection → findings → Word | WF2 | PASS orch Word leave | PASS Workflow B | **Covered** |
| 4 | Coding verified in sandbox | WF3 | PASS calc/H9/gate | MANUAL | **Covered** |
| 5 | Multimodal image/scan | WF4 | PASS (moondream/OCR honest) | Rehearse PNG | **Covered** |
| 6 | Logs/monitor no external calls | WF5 | PASS MonA + G8 + audit | Monitor UI | **Partial** — private LAN ≠ air-gap |

## Fail-closed

G7 revoke · G9 secret — **PASS** in robust suite.

## Honest claim

Private LAN peer Gateway path with open-weight models. **Not** air-gap until NIC evidence.

## Re-run

```powershell
python backend/scripts/robust_ps_workflows.py
```
