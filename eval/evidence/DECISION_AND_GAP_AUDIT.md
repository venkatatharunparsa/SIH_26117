# Decision and gap audit — SIH26117 KWB

**Date:** 2026-09-20  
**Purpose:** Lock what we keep / revise / delete before further build. Honesty over pitch.

---

## Pitch lines (operators may say)

| Say | Never say |
|-----|-----------|
| On-prem / **private LAN** Gateway path to open-weight models | Fully **air-gapped** (hotspot demo) |
| Laptop-A = model station; Laptop-B = workbench | Nothing can leave because of the phone hotspot |
| **DRAFT** soft copy; paper Approver outside the app | Certified plant record / in-app Approver |
| Monitor A = **evidence pack** · desk badge **NOT CERT** | CERT-In certified / WAN=0 proven forever |
| Auto-select: `inspect-draft→llama3.2:3b`, `code-assist→qwen2.5-coder:7b` | “Many models” without naming tags |
| OCR **framework** (+ fixture); vision model staged separately | Full multimodal vision LLM on every attach |
| Sandbox = **host-process** with H9 / export gates | Docker deny-all / no-net jail (until built) |

**Air-gap as product posture:** strongest *future* deployment (NIC evidence / offline venue). Demo today = controlled private LAN peer.

---

## Major decisions

| Decision | Status | Keep / revise / delete | Notes |
|----------|--------|------------------------|-------|
| Desk = `apps/kwb-app` Electron; refuse `kwb-desk` as primary | Locked | **Keep** | No LLM side-door from legacy desk |
| Path Desk → `/orch/turn` → Pack → Gateway → local `/v1` only | Locked | **Keep** | Core sovereignty architecture |
| Word DRAFT primary (not PPTX-only) for Expected Solution | Locked | **Keep** | PPTX may remain secondary |
| HITL H1/H7/H2; export leave; no in-app Approver | Locked | **Keep** | Matches industrial judgement outside app |
| G1: two cards; full two-tag when A has coder + chat | Revised 2026-09-20 | **Keep (revised)** | Was floor; now `llama3.2:3b` + `qwen2.5-coder:7b` |
| Coding card must not adopt vision tag (`moondream`) | Fixed | **Keep** | `cards.py` skip vision for code-assist |
| OCR day-1 = framework (Tesseract/pypdf/stub); org SoT = OCR/vision model | Locked | **Keep**; vision path **revise** in Phase 4 | Demo honesty |
| Two-laptop = phone hotspot LAN peer | Ops | **Keep** as demo ops; **never** equate to air-gap | Scripts + allowlist |
| `SOVEREIGN_INFERENCE_ALLOW_HOSTS` plain IP | Fixed | **Keep** | NoDecode parse |
| MCP = in-process allowlist host | Partial | **Keep floor**; full stdio lifecycle later | Not plant MCP registry |
| Skills + roles progressive into orch pack | Demo-wired | **Keep** | |
| Sandbox = host-process under workspace | Floor | **Revise honesty in UI**; isolation upgrade later | No fake deny-all badge |
| Turn-based `/orch/turn` (no token stream) | Current | **Revise** — Phase 2 mid-turn events/SSE | Not Cursor clone |
| OpenHands Canvas study only | Locked | **Keep** — do not fork as product | Mem0 |
| Monitor A ≠ CERT | Locked | **Keep** | Integrity chrome |

---

## Gaps vs Expected Solution (summary)

| Bullet | Coverage | Gap action |
|--------|----------|------------|
| Local deploy | Strong | Rehearse cold-boot |
| ≥2 task auto-select | API full two-tag; desk rehearse | Phase 1 desk prove |
| Inspection → Word | Strong (API + desk Workflow B) | Keep |
| Sandbox coding | API + UI path; host-process | Honesty copy Phase 4 |
| Multimodal vision | Framework / stub | Phase 4 moondream |
| Zero external calls proof | Logs + Monitor; not WAN=0 | Honest language + optional NIC rehearsal |

---

## Removable later (after workout)

Candidates to prune from Mem0 / docs noise once product is stable: duplicate Batch5 air-gap honesty rows; obsolete “G1 floor only” memories; PPTX-as-primary demo notes.

---

## Evidence pointers

- `PS_CONFIDENCE_SCORECARD.md` (~68%)
- `ROBUST_E2E_REPORT.md` (LAN peer PASS)
- `OPERATOR_COLD_BOOT_TWO_LAPTOP.md`
- Workflow B grant `dfa68ff2d9114e8c`
