# WP-10 freeze — verification + source-of-truth + PS check

**Date:** 2026-09-18  
**Target:** `WP-10_FREEZE.md` rev 1.0  
**Against:** Official PS; WP-00/09/24; `WP-10_REDTEAM.md`; DM answers; Observed local multi-model `/v1` servers (pattern only).

**Grades:** **Official** | **WP-*** | **DM** | **Observed** | **Derived**

---

## Verdict

| Question | Answer |
|---|---|
| All DM answers in freeze? | **Yes** |
| Every substantive claim sourced? | **Yes** (§2) |
| PS runtime/multi-model slice satisfied? | **Yes** (§3) |
| Whole PS done? | **No** — remaining WPs + prototype |
| Contradict prior freezes? | **No** (OpenRouter = local shape only) |
| **Confidence / GO WP-12** | **0.88** |

---

## 1. Completeness (DM)

| ID | In freeze? | Where |
|---|---|---|
| R0 shallow HW / connect URL | Yes | D0, §4 |
| Q1 pre-load 2 | Yes | D1, §6 |
| Q2 LRU | Yes | D2, §6 |
| Q3 org GPU / demo hybrid | Yes | D3, §7 |
| Q4 show GPU/VRAM | Yes | D4, §8 |
| Q5 one runtime + single key | Yes | D5, §5 |
| Q6 quantised | Yes | D6 |

---

## 2. Claim ledger

| Claim | Source | Hold? |
|---|---|---|
| Self-hosted on org GPU server; nothing leaves | **Official** Description | Yes |
| Multiple open-weight at once; not locked to one; addable without redesign | **Official** Description | Yes |
| Workstation or server; mid-range; smaller if no 120B | **Official** Expected Solution | Yes |
| Software category; weights on hardware plane | **Official** Category + **WP-00** | Yes |
| Enable ≠ VRAM loaded | **WP-24** | Yes |
| One load attempt then fail-closed | **WP-09** | Yes |
| Jail ≠ GPU | **WP-00/16** | Yes |
| No public base_url / HF-in-op | **WP-00/09/24** | Yes |
| Pre-load 2; LRU; org GPU-only; demo CPU+GPU; probe; single key multiplex; quant | **DM** | Yes |
| Local OpenRouter-*shape* ≠ openrouter.ai | **Derived** red-team B | Yes |
| Provided URL/capabilities → cards after Admin enable | **DM** + **WP-24** | Yes |
| Venue will supply models/GPU | **Unverified** — not relied on as sole plan | Yes |
| Exact runtime brand | **Not** claimed | Yes |

---

## 3. PS checklist (honest)

### Satisfied by WP-10 (+ planes)

- Open-weight local serve; multi-id; add without redesign; honest “at once”; workstation/server; mid-range/smaller/quant; org GPU path; air-gap runtime (no WAN pull).

### Satisfied elsewhere (not this freeze’s job)

- Task auto-select → WP-06/24  
- Agentic tools/iterate → WP-06/07  
- Sandbox → WP-16  
- OCR/multimodal path → WP-03  
- Word DRAFT → WP-01/05  
- KB/citations → WP-11/22  
- Visible WAN=0 monitor → WP-13  

### Still open on queue

- WP-12, 17, 14, 13, 15, 18, 19, 20 → then prototype overlay.

---

## 4. Residual risks

| Risk | Park |
|---|---|
| Demo CPU path accidentally org-default | Profile flag + acceptance |
| LRU vs dual warm proof | Pin warm pair during script |
| Provided URL is public | WP-09 endpoint reject |
| Quant quality overclaim | Card notes |

---

## 5. Confidence

| Theme | Score |
|---|---|
| Official multi-model / open-weight | 0.94 |
| Shallow HW + connect model | 0.90 |
| Local single-key multiplex | 0.88 |
| Org/demo compute split | 0.90 |
| PS slice honesty | 0.92 |
| **Overall** | **0.88** |
