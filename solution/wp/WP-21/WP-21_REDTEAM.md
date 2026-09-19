# WP-21 context packing — adversarial red-team + DM decisions

**Date:** 2026-09-18  
**Target:** `WP-21_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Against:** Official confidentiality / on-prem; WP-00 Intelligent layer + Never dump corpus; WP-04 grants/revoke; WP-06 conductor≠packer; WP-11 authz-first k=5; WP-22 NOT FOUND / cites; WP-23 delimit + injection; NIST AC-6 *shaped* (no cert claim).

**Mode:** Attack first — packing is where grants die if “helpful.”

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Pack budget = **token-vs-window** cap (card `context_window_hint` − reserve) |
| **2** | History = last **4** raw turns |
| **3** | **Full file OK when small**; otherwise excerpt |
| **4** | Tool overflow = **head + tail + truncation marker** |
| **5** | PackManifest = **log-only for demo** (not Audience B must UI) |
| **6** | Delimiters = **yes** → freeze **XML-ish tagged blocks** (first option; see Attack F) |

---

## Verdict

| | |
|---|---|
| Missing | M1–M12 (small threshold, token estimator honesty, window reserve, history vs budget, delimiter breakout, head/tail leak, log-only ≠ no manifest, conductor bypass) |
| Overhyped | Token estimate = exact tokenizer; full-small file = always safe; log-only = operators never need pack view; delimiters = injection-proof |
| Confidence after freeze | **~0.87** → GO WP-09 |

---

## Attack A — Token-vs-window (Q1)

| Attack | Why | Fix (freeze) |
|---|---|---|
| **A1** Fake “tokens” via chars/4 | Overfill → gateway/runtime fail or silent drop | Estimate may be approximate; **must** leave **reserve**; hard fail or shrink if estimate > window−reserve; WP-09 may still reject |
| **A2** Ignore card hint / use infinite | OOM / truncate mid-instruction | Budget = `min(Admin max, card.context_window_hint − reserve)`; missing hint → Admin/demo default |
| **A3** Reserve = 0 | No room for reply / tool schema | Freeze **reserve ≥ 10%** of window or fixed demo floor (e.g. 512 tok) — pick floor in freeze |
| **A4** Packer shrinks by deleting citations first | Breaks WP-11/22 honesty | Shrink order: history older→newer (within N), then tool middles (already head+tail), then attach excerpts; **never drop citation metadata for chunks still packed**; drop chunk entirely rather than cite-less |

**Decision:** Token-vs-window **yes**, with reserve + fail-closed/shrink policy + honest estimate label in PackManifest.

---

## Attack B — History N=4 (Q2)

| Attack | Why | Fix |
|---|---|---|
| **B1** 4 full turns still blow window | Mid-range GPU | History included **only within budget**; drop oldest of the 4 first |
| **B2** Raw turns promote T3→T0 across turns | WP-23 | **Re-delimit** every pack; no promotion |
| **B3** Summarize secretly while claiming “raw” | Honesty | Must-work = **raw last 4**; summarize = ambition only |
| **B4** Injected “assistant” history forged client-side | Spoof | History from **server transcript** only |

**Decision:** Last **4** raw server turns; budget may drop oldest; re-delimit always.

---

## Attack C — Full file when small (Q3)

| Attack | Why | Fix |
|---|---|---|
| **C1** “Small” undefined → 200-page PDF as “small” | Corpus dump | Freeze **small** = under **all** of: Admin/demo **byte max**, **page max**, and remaining **token budget** after rails+skills+retrieve |
| **C2** Many “small” files sum to huge | Death by a thousand cuts | Cap **total attach budget** per pack |
| **C3** Small unscanned binary / secret-rich | Leak to model | Still trust-label; secret heuristics before **export** (WP-23); pack may include under grant — do not claim DLP |
| **C4** Pre-H1 machine extract full file → agent authority | WP-03/23 | T4 has **no draft/agent authority**; H1 still required for verified path |

**Decision:** Full file when small **yes**, with **byte + page + residual-token** gates and **total attach cap**. Demo defaults in freeze.

---

## Attack D — Head+tail truncation (Q4)

| Attack | Why | Fix |
|---|---|---|
| **D1** Tail hides “IGNORE PREVIOUS” in middle… still in head | Injection | Delimit whole blob T3; heuristics on **full pre-truncation text** when feasible; if only truncated form sent, mark `truncated=true` |
| **D2** Tail contains secrets; head looks clean | Export ≠ pack | Pack honesty: marker shows omission; export scan still WP-23 |
| **D3** No marker → model invents missing middle | Lie | Mandatory marker string + omitted char/token count in PackManifest |
| **D4** Head+tail doubles budget vs head-only | | Cap head and tail **each** (e.g. 50/50 of tool budget) |

**Decision:** Head+tail+marker **yes**, with per-side caps + `truncated` in manifest.

---

## Attack E — PackManifest log-only (Q5)

| Attack | Why | Fix |
|---|---|---|
| **E1** Log-only ⇒ skip writing manifest | Cannot audit | Manifest **must be written** every pack; demo UI may omit |
| **E2** Jury asks “what entered the model?” | Expected Solution / Audience B ambition | Demo: show via **log/inspect**; org-ambition: Audience B UI |
| **E3** Manifest logs raw secrets | Secondary leak | Manifest stores **ids, hashes, sizes, trust mix, chunk_ids** — not full secret bodies |

**Decision:** **Log-only UI for demo**; manifest **always emitted** (must-work).

---

## Attack F — Delimiter “yes” (Q6)

DM answered **yes** without naming XML vs markdown.

| Option | Attack | Upside |
|---|---|---|
| XML-ish `<kwb_data trust="T3" …>` | Model may emit fake tags | Machine-parseable; clear breakout target for heuristics |
| Markdown fences | Ambiguous with user markdown / code | Familiar |

**Adversarial pick:** **XML-ish tagged blocks** (aligns with “yes” to the architect’s primary example; better structural parse for refuse/log).

| Attack | Fix |
|---|---|
| **F1** Fake closing tags / nested system | Treat inner as data; refuse/log override patterns (WP-23) |
| **F2** Brand-lock on exact tag names | Freeze **pattern** (`kwb_*` + trust attr); exact strings in freeze appendix |
| **F3** Delimiters = solved injection | Still grants + HITL + Never — delimiters **help**, not complete |

---

## Attack G — Conductor / retrieve / parallel

| Attack | Fix |
|---|---|
| **G1** Orchestrator bypasses packer | Forbidden (WP-06); freeze restates |
| **G2** Packer re-ranks global corpus | Only WP-11 authz-first outputs |
| **G3** Parallel join merges prompts | Artefact refs only |
| **G4** Revoke mid-pack | Live grant check before emit; fail-closed |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Window reserve | ≥10% or ≥512 tok demo floor |
| **M2** | Token estimate honesty | Label `estimate`; gateway may reject |
| **M3** | Small file thresholds | Bytes + pages + residual tokens |
| **M4** | Total attach cap | Per-pack |
| **M5** | History N=4 + budget drop oldest | |
| **M6** | Head/tail split + marker | |
| **M7** | Manifest always logged; UI optional demo | |
| **M8** | XML-ish delimiter pattern | |
| **M9** | Shrink order preserves cite integrity | |
| **M10** | Server transcript only for history | |
| **M11** | No remote URLs in vision parts | |
| **M12** | k≤5 into pack (demo) | WP-11 |

---

## 2. Overhyped

| ID | Claim | Reality |
|---|---|---|
| **O1** Exact tokens | Estimate + reserve + gateway |
| **O2** Small full file safe | Still T-labelled; not DLP |
| **O3** Delimiters stop injection | Layered with WP-23/04/05 |
| **O4** Log-only = no evidence | Manifest in logs is evidence |
| **O5** Packer decides truth | Human + WP-22 |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Minimize-to-grant packer | Full-binder helpful paste |
| Token-vs-window + reserve | Unlimited context |
| XML-ish trust delimiters | Markdown-only as must-work |
| Head+tail+marker | Silent middle drop |
| Manifest always | Manifest optional |

---

## 4. Disposition

**Applied.** → `WP-21_FREEZE.md` rev 1.0. Confidence **0.87**. **GO** → **WP-09**.
