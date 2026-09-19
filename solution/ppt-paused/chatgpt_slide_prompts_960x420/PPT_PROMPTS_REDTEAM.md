# PPT image-prompt pack — adversarial red-team (Rev 2.0)

**Date:** 2026-09-18  
**Target:** `chatgpt_slide_prompts_960x420/PROMPT_S1…S6.txt` + layouts  
**Against:** Official Expected Solution · playbook · `WP-20_ORG_CONNECTION` · freezes · web-checked cites  
**Product:** Knowledge Work Bench  

---

## Verdict

| Question | Answer |
|---|---|
| Do prompts match **solution design** (not old fill pack)? | **Mostly yes** — planes, grant, gateway-only, Word must, Excel LATER, G1–G10, WAN=0 |
| Cover **Expected Solution** musts? | **Yes** on S2 addresses table |
| Cover **full org connection** (all WPs)? | **No** — several binding boxes missing or jargon-buried (see §Gaps) |
| Playbook craft? | **Strong** structure; **weak** on density vs 960×420 and screener clarity |
| Cite honesty (web-checked)? | IndiaAI / MRPL 15.0 / Cisco 48% / staff 2530 **OK with wording fixes** |
| Ready for final PNG generation? | **After Fills F1–F10 + Team ID/Name** |
| **Confidence** | Design coverage **0.78** · Image-gen success at 960×420 **0.55** · Cite honesty **0.90** |

---

## Attack 1 — Expected Solution coverage

| Expected Solution clause | In prompts? | Where | Grade |
|---|---|---|---|
| Local mid-GPU / smaller model OK | Y | S2 row1, S3 callout, S4 footer | Pass |
| Auto-select ≥2 task types | Y | S2 loop + addresses; S3; S4 REAL | Pass |
| Scan → findings → Word | Y | S2 Proposed + addresses + loop | Pass |
| Coding + sandbox verify | Y | S2 addresses row4; S4 REAL | Pass (loop itself is inspection-only — see G2) |
| Multimodal | Y | S2 Ingest; S4 REAL | Pass |
| Logs / network monitor WAN=0 | Y | S2 Proposed; S4 REAL; matrix | Pass |
| Air-gap / nothing leaves | Y | Uniqueness + NEVER cloud | Pass |

**Finding:** Expected Solution **caption-pass**. Gap: **coding path not drawn as a second spine** on the Idea loop (only in table). Screener redrawing only the boxes may miss G3.

---

## Attack 2 — Solution design (WP-20) coverage matrix

| Binding box | In prompts? | Severity if missing on PDF |
|---|---|---|
| Workbench ≠ Runtime ≠ Sandbox | Y (S3 planes) | — |
| Session ≠ grant | Y (S2 loop) | — |
| Orchestrator = software brain ceiling | Y (S2 Proposed) | — |
| Gateway-only runtime | Y | — |
| Model Cards / pluggable | Y | — |
| Ingest → H1 before KB | Y | — |
| Authz-first RAG k=5 | Y (S3) | — |
| Packer | Y (loop) | — |
| Output gates before unmasked view | Partial (“Gates→Word”) | Med — add “gates before view” |
| HITL H1/H2/H3/H9 | Y (compressed) | — |
| Word DRAFT + templates | Y | — |
| KWB store; never write plant SoR | Weak (NEVER DCS only) | **High** — add explicit store line |
| Audit fail-closed | Missing | Med |
| Lineage (WP-14) | Missing | Low for idea PDF |
| Three-source claims / H7 (WP-22) | Weak (“cited”) | **High** for PSU edge |
| T0–T4 untrusted (WP-23) | Missing | Med — one chip enough |
| Specialists + skills (WP-07) | Missing | Med |
| MCP local (WP-08) | MOCK only | OK for idea PDF |
| USB offline (WP-19) | Present as “WP-19” jargon | **High** — drop internal WP ids |
| Monitors A/B | A yes; B missing | Low |
| G1–G10 / demo_ready | Y (S4) | — |
| Description overhang Excel/PPT LATER | Y | — |
| Personal .md (WP-15) | Absent | OK (not PS-mandated) |
| Classifier | Absent | OK (MOCK/ambition) |

**Finding:** Core spine is present. **Must add:** three-source / NOT FOUND, KWB-store Never-write, skills one-liner, fail-closed, de-jargon WP-19. Coding as visible second task.

---

## Attack 3 — Playbook craft failures

| Attack | Issue | Fix |
|---|---|---|
| **P1 Density** | Official: points not paragraphs — OK. But **960×420 cannot hold** S3 8-row table + S2 5-row table without OCR errors in ChatGPT | Cut tables to **≤5 rows**; move detail to Q&A |
| **P2 Jargon** | `Session≠Grant`, `Authz RAG`, `H9`, `G1–G10`, `WP-19` confuse remote PSU screener | Plain labels + tiny glossary line |
| **P3 Risk column** | Playbook likes Challenge \| Risk \| Mitigation — have it; optional High/Med/Low missing | Add Risk level column **or** keep 3-col (OK) |
| **P4 Pointer chrome** | Content uses short headers; official template already has full pointers — OK if PNG is **content panel only** | Keep; do not redraw official titles |
| **P5 Team ID** | `⟦TEAM_ID⟧` still blank → known corpus fail | **Block export** until filled |
| **P6 Second flowchart** | S2 and S3 both have loops — playbook OK if same loop; risk of divergence | Force **identical** box labels on S2/S3 |

---

## Attack 4 — Cite / metric honesty (web-checked 2026-09-18)

| Claim in prompts | Web check | Grade | Action |
|---|---|---|---|
| IndiaAI ₹10,371.92 cr; 10,000+ GPUs; PIB PRID 2012355; 07 Mar 2024 | **Confirmed** PIB | Official | Keep |
| MRPL 15.0 MMTPA | **Confirmed** mrpl.co.in/Content/Profile | Official org | Keep |
| Staff ~2,530 | **Confirmed** Directors’ report as of **31 Mar 2025** (1,162+1,368). Newer public pages may show 2,450 @ 31 Mar 2026 — caption with date | Observed | Print **2,530 (31 Mar 2025)** |
| Cisco “48% of orgs admit…” | **Wording wrong.** Study: **48% of respondents** entered non-public company info into GenAI; **27%** orgs banned GenAI for a time | Observed | **Rewrite** (F3) |
| KPI 1–5 days → 2–3 h DRAFT | Still **Unverified** workflow study — not MRPL SLA | Unverified | Keep label; need your **YES** |
| NASSCOM USD 8→32 bn | Not re-fetched this pass | Observed (prior pack) | Keep as ecosystem **or** drop if space |
| OISD-STD-128 name only | OK | Official name | Keep |

---

## Attack 5 — Image-generation failure modes

| Mode | Why it kills “winning” | Mitigation |
|---|---|---|
| ChatGPT misspells `/v1`, `docx`, `SIH26117` | Screening ridicule | Post-edit cell-by-cell; QA list |
| Draws visible grid lines | Looks amateur | Prompt: “no visible grid in final” (already) |
| Compresses uniqueness into unread 6pt | Uniqueness fails eye path | Max **3 chips**, fewer words (F5) |
| Invents Excel tick / green matrix | MiTra theatre | Forbidden lines already; reinforce |
| Aspect not 960×420 | Layout break | Reject + regenerate |
| Internal “WP-19” on PDF | Screener confusion | Replace with “USB offline stage” |

---

## Attack 6 — Overclaim / underclaim

| Item | Risk | Disposition |
|---|---|---|
| Matrix all-Y for KWB | True only if demo delivers — idea PDF is a **promise** | Caption matrix as **design intent / demo spine** OR keep Y as product claim with S4 REAL backing |
| “Fully offline” | USB stage + venue Wi-Fi story | Keep; proof = Monitor A |
| Skills / MCP underplayed | Looks like thin router | Add one skills line |
| Lineage / audit soft | OK omit lineage; **add fail-closed** | F6 |

---

## Gaps → Fills (apply before next PNG run)

| ID | Fill | Where |
|---|---|---|
| **F1** | Replace `WP-19` → `USB offline stage (weights/packs)` | S3 |
| **F2** | Add under Proposed or Addresses: artefacts only in **KWB store**; **never write** plant SoR | S2 |
| **F3** | Cisco line → “48% of **respondents** entered non-public company info into GenAI (Cisco Privacy Benchmark 2024); 27% of orgs banned GenAI for a time — survey, not MRPL” | S5 |
| **F4** | Staff → `2,530 staff (31 Mar 2025 Directors’ report)` | S5 |
| **F5** | S2 loop footer: add `Specialists + on-disk skills · fail-closed on audit/gateway deny` | S2 |
| **F6** | S2 uniqueness chip 2: add `cite or NOT FOUND (file/user/policy)` | S2 |
| **F7** | S2 Detailed: tiny parallel note `+ code path: specialist → sandbox → H9` | S2 |
| **F8** | S3 table: cut to **6 rows** (merge Workbench+policy or drop USB footer row clutter); remove jargon | S3 |
| **F9** | S2/S3 loop labels **identical** plain English set | S2+S3 |
| **F10** | Add prompt QA block: reject if Excel must / CERT badge / blank Team ID | All README |

**Optional (ask you):** drop NASSCOM line if S6 overflows; confirm KPI YES.

---

## Coverage scorecard (after fills intended)

| Layer | Before | After fills |
|---|---|---|
| Expected Solution | 0.95 | 0.97 |
| WP-20 connection | 0.72 | **0.88** |
| Playbook craft | 0.80 | 0.85 |
| Cite honesty | 0.82 | **0.95** |
| Image-gen fitness @960×420 | 0.55 | **0.70** (still tight) |

---

## Information still required from you

| # | Ask | Blocks |
|---|---|---|
| 1 | **Team ID** | S1 / portal |
| 2 | **Registered Team Name** | S1 / oval |
| 3 | KPI **YES** to print 1–5d → 2–3h estimate? | S5 |
| 4 | Prefer keep or drop NASSCOM ecosystem line on S6? | S6 space |
| 5 | Any **measured** demo numbers (VRAM, tok/s)? If none → stay silent | Honesty |

---

## Disposition

1. Apply F1–F10 into prompts — **done in Rev 2.1**; **Rev 2.2** hardens SHARED_RULES, plain-English loop, drops NASSCOM, Session≠grant.  
2. You supply Team ID / Name / KPI YES.  
3. Regenerate PNGs; cell-edit typos.  
4. Paste into official template → PDF.

**Generation source:** `PROMPT_S1…S6.txt` + `SHARED_RULES.txt` (**Rev 2.2**).

---

## Changelog

| Rev | Change |
|---|---|
| 1.0 | Full adversarial pass + web cite check + fills list |
| 1.1 | Note F1–F10 applied into prompt files |
| 1.2 | Rev 2.2 prompt pack: SHARED_RULES, Authz retrieve, NASSCOM drop, Session≠grant |
