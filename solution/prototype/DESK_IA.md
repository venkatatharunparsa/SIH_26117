# Desk IA — minimal build SoT (GATE_90 B1)

**Date:** 2026-09-19  
**Status:** **LOCKED** — design-info B1 (wires thickened post RT-07)  
**Flow SoT:** `APPLICATION_FLOW_COMMON.md` A→J  
**HITL SoT:** WP-05 rev 2.0  
**API SoT:** `backend/app/main.py` v0.4  

---

## Screens

| Screen | Purpose | Shows | Does not |
|---|---|---|---|
| **1. Intent** | Start task | Task type · session user | Org chart · Approver picker |
| **2. Files** | Attach inputs | Upload / fixture pick · template | Live plant browse day-1 |
| **3. Extract + H1** | Confirm OCR/fixture | Extract · **H1** | Skip H1 on scan path |
| **4. Knowledge** | Grant + retrieve | Grant · cites / NOT FOUND · **H7** | Fake cites |
| **5. DRAFT** | Artefact | Word DRAFT · `artefact_version` | Plant “approved” |
| **6. Gates** | Own-work HITL | H2 · H9 if code · stale banner | Approver queue |
| **7. Export leave** | Soft copy off box | H3 · pack · deny reasons | Forward-accept |
| **8. Monitor B (thin)** | Own task | card · model · grant · denies | CERT · other users |

Fail-closed overlays: revoke · secret · bad URL · sandbox-red · h2_stale · h9_required.

---

## State machine (must)

```text
intent → files → [extract → H1] → [retrieve → H7?] → DRAFT(v)
    → H2(ack v) → export leave
         ↘ edit findings → v' · h2_stale → re-H2
coding: … → sandbox(report) → H9 accept → export leave
            sandbox-red or H9 reject → export DENY (G10)
```

---

## API contracts (deny codes)

| Action | Endpoint | Success needs | Deny `error` |
|---|---|---|---|
| Start | `POST /task/start` | task_type | route fail |
| H1 | `POST /task/h1-confirm` | `h1_acked=true` | `h1_not_confirmed` |
| Draft | `POST /task/inspect-draft` | grant; H7 if cites | `h7_required`, `secret_in_draft` |
| H2 | `POST /task/h2-ack` | `artefact_version` match | `h2_stale` |
| Edit | `POST /task/draft-edit` | grant | clears H2; new version |
| Sandbox | `POST /sandbox/*` | grant sandbox tool | records report |
| H9 | `POST /task/h9-ack` | prior sandbox | `sandbox_red`, `sandbox_report_missing` |
| Export leave | `POST /task/export` | fresh H2; body secrets OK; H9 if sandbox used | `h2_stale`, `h2_required`, `h9_required`, `sandbox_red_export_denied`, `secret_in_draft` |
| Monitor A | `POST /monitor-a/start\|stop` | — | evidence pack; **not CERT** |

---

## Primary walks

1. **Inspection:** 1→2→3→4→5→6(H2)→7  
2. **Stale:** edit after H2 → export deny → re-H2 → export  
3. **Fail-closed:** revoke / secret / bad model  
4. **Coding:** sandbox → H9 → export; red sandbox → export deny  

---

## Out of day-1 wire

SSO · Admin full console · continuous Monitor A UI · Excel/PPT.
