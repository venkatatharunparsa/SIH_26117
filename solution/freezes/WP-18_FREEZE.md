# WP-18 Fail-closed + eval suite — FREEZE

**Date:** 2026-09-19  
**Status:** **FROZEN** (rev **1.1**) — G1 honesty + self-HITL / export-leave alignment.  
**Prior:** rev 1.0 (2026-09-18).  
**Depends on:** Prior freezes (behaviour owned there; this WP catalogues + tests).  
**Aligns:** WP-00 rev 2.0 · WP-01/05 rev 2.0 · GATE_90 **A3** · no-pull Ollama adopt.  
**Inputs:** `WP-18_ARCHITECT_PERSPECTIVE.md`, `WP-18_REDTEAM.md`, **DM 2026-09-18** (G1–G10; manual checklist; deliberate inject; eval/ pack; any teammate signer; no waiver).  
**Findings SoT:** `WP-18_REDTEAM.md`  
**Verify SoT:** `WP-18_FREEZE_VERIFY.md`  
**Product:** **KWB**

---

## 1. One-sentence contract

KWB **fails closed** (or degrades only where a prior freeze allows) with **logged reasons** — never to cloud/HF/unregistered models — and is **demo-ready** only when **golden G1–G10** all pass on a **manual checklist** backed by an **`eval/` evidence pack**, including **deliberate fault injections**.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Fail-closed on security boundaries | Fail-open for demo convenience |
| G1–G10 all required | Waive security goldens |
| Manual checklist + eval/ artifacts | Checkbox without evidence |
| Any teammate may sign | Unsigned / anonymous pass |
| Degrade only if prior WP allows | Silent privilege widen |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Must-work goldens = **G1–G10** |
| **D2** | Runner = **manual checklist** (automation = ambition) |
| **D3** | Suite includes **deliberate fault injection** |
| **D4** | **`eval/` evidence pack** required |
| **D5** | Signer = **any teammate** (name + date required) |
| **D6** | Any must fail → **`demo_ready = false`** (no waivers) |

---

## 4. Fail-closed / degrade

| Mode | Use |
|---|---|
| **Fail-closed** | Grant/gateway/card/HITL/gate/audit-write/WAN-A failures |
| **Degrade** | Only per prior freeze (attach-only without KB cites; `lineage_degraded`; etc.) |
| **Forbidden** | Cloud `base_url`, HF pull, skip card, skip HITL, invent citations, silent model substitute |

Failure matrix: as in architect §2 — behaviour remains owned by source WPs; WP-18 requires they are **testable**.

---

## 5. Golden suite (must)

| ID | Task | Pass evidence (min) |
|---|---|---|
| **G1** | Auto-select ≥2 task types | Routing log `task_type → card_id → model_id` with ≥2 task types and ≥2 **card_id**s. **Floor (honest):** one adopted chat tag → same `model_id` OK — checklist/PPT must label **single-tag adopt**. **Full:** ≥2 distinct `model_id`s only when ≥2 chat tags are **locally staged** (offline; **never pull** to pass G1). |
| **G2** | Scan → findings → DRAFT Word | docx + **self-HITL** H1/H2 evidence (same operating user) |
| **G3** | Code + sandbox verify | Sandbox report + **H9** (same user); calc-in-jail |
| **G4** | Multimodal understand | OCR/VLM path evidence (fixture+H1 OK day-1) |
| **G5** | Audience A evidence | Host start/stop **snapshots** + green local hop — **not CERT** |
| **G6** | Missing cite / NOT FOUND | Honest gap UI/log — no fake cite |
| **G7** | Revoke/expired grant | Deny-after-revoke log |
| **G8** | Unregistered/disabled model | Gateway deny code |
| **G9** | Secret in DRAFT | Unmasked / **export leave** deny |
| **G10** | Sandbox red | **Export leave** blocked (with H9 path) |

### Deliberate inject (minimum)

Must exercise at least: **revoke mid-task (G7)**, **bad/unregistered model (G8)**, and **≥1 of** {secret-in-draft (G9), sandbox-red (G10), NOT FOUND/missing cite (G6)}.

---

## 6. Checklist + eval/ pack

### Checklist

- One row per G1–G10: pass/fail, evidence path, notes.  
- Signer: **person name + date**.  
- `demo_ready` = all pass.

### `eval/` minimum contents

| Path / item | Purpose |
|---|---|
| `checklist.md` (or equivalent) | Signed results |
| Routing/gateway log extract | G1, G8 |
| DRAFT docx (or path ref) | G2 |
| Sandbox report | G3, G10 |
| Multimodal evidence ref | G4 |
| Audience A snapshots | G5 |
| Deny/inject audit extracts | G6–G10 as applicable |

Redact secrets. Pack is evidence — not plant SoR. Retain per WP-17 demo window.

---

## 7. Must / ambition / deferred / never

### Must-work

1. Fail-closed policy §4.  
2. G1–G10 + inject minimum.  
3. Manual checklist + eval/ pack + named signer.  
4. `demo_ready` hard gate.  
5. Suite becomes prototype acceptance spine after WP-20.

### Org-ambition

- Automated runner; expanded goldens; CI.

### Deferred

- External certification lab.

### Never

- Waive must goldens.  
- Fail-open to cloud/HF.  
- Pass without eval/ evidence.  
- LLM-as-judge as required gate.

---

## 8. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Expected Solution as oracle | Official |
| **Add** | G# ids; eval/ manifest; inject set; demo_ready | DM / red-team |
| **Refuse** | Happy-path video alone; waivers |

---

## 9. Demo acceptance (meta)

1. Complete eval/ with all G1–G10 pass.  
2. Injects present in audit.  
3. Unsigned or incomplete pack → not demo-ready.  
4. Any fail → demo_ready false.

---

## 10. Next

GATE_90 remainders: **WP-20** · A4/A5 naming · design B-rows. Eval runs use G1 floor/full as above.

---

## 11. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze G1–G10 + manual eval/ + no waiver |
| **1.1** | **FROZEN** 2026-09-19: G1 floor/full honesty (no pull); G2/G3 self-HITL; G5 ≠ CERT; G9/G10 = export leave; align WP-00 2.0 / GATE_90 A3 |

**Confidence:** **0.90** (G1 honesty closed)
