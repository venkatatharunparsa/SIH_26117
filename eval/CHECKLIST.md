# Demo eval / G1–G10 checklist

**Status:** **TEMPLATE** until signed.  
Label fixtures: **Confidential synthetic**. Monitor A ≠ CERT.  
**G1 honesty (GATE_90 A3 / WP-18 rev 1.1):** floor = single-tag adopt OK; full = ≥2 distinct `model_id`s only when staged offline — **never pull**.

| G# | Check | How | Pass rule |
|---|---|---|---|
| G1 | ≥2 task→card→model routes logged | `/task/start` inspection + coding → audit `router_select` | ≥2 task types + ≥2 `card_id`s. Floor: same `model_id` OK → note **single-tag adopt**. Full: ≥2 distinct `model_id`s if 2nd chat tag staged offline. |
| G2 | Word DRAFT + self-HITL H1/H2 | `/task/inspect-draft` → docx banner + same-user gates | No in-app Approver |
| G3 | Sandbox coding/calc + H9 | `/sandbox/calc` or `/sandbox/python` + H9 ack | Same user |
| G4 | OCR/extract path | light / fixture + H1 confirm | Fixture OK day-1 |
| G5 | Monitor A start/stop artefact | `/monitor-a/start` then `/stop` → JSON sha256 | Evidence pack — **not CERT** |
| G6 | Cite-or-abstain | `/task/retrieve` empty → NOT FOUND | No fake cite |
| G7 | Revoke grant blocks tools | revoke then call tool → `grant_revoked` | Deny-after-revoke |
| G8 | Deny public URL + card | gateway with public `base_url` → deny | Fail-closed |
| G9 | Secret in draft blocks export leave | `/task/export-check` with api_key=… | Export leave deny |
| G10 | Sandbox-red / H9 blocks export leave | coding walk + audit | Export leave deny |

Mandatory stage walks: **inspection + one fail-closed**. Coding if time.

**Signer:** _______________ **Date:** _______________  
**G1 mode used:** ☐ floor (single-tag adopt) ☐ full (≥2 model_ids)  
**demo_ready:** ☐ true ☐ false
