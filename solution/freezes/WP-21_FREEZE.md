# WP-21 Context assembly / data-to-pass — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-04 / WP-06 / WP-07 / WP-11 / WP-22 / WP-23 / WP-24.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-21_ARCHITECT_PERSPECTIVE.md`, `WP-21_REDTEAM.md`, **DM 2026-09-18** (token-vs-window; history N=4; full file when small; head+tail+marker; PackManifest log-only demo; XML-ish delimiters).  
**Findings SoT:** `WP-21_REDTEAM.md`  
**Product:** **KWB**

**Stack / tokenizer brand:** not locked. No NIST certification claim. AC-6-**shaped** least privilege for **what the model sees**.

---

## 1. One-sentence contract

Every model request is **assembled by the packer**: **grant-scoped**, step-minimal, **XML-ish trust-delimited**, citation-bound, and capped by **token-vs-window** (card hint − reserve) — the **orchestrator names the need**; the packer **enforces** what enters the model; **PackManifest** is always logged (demo UI optional).

---

## 2. Limits

| True | False / refuse |
|---|---|
| Packer enforces data-to-pass | Orchestrator pastes raw corpus |
| Token **estimate** + reserve | Exact tokenizer guarantee |
| Full file when **small** | Any attach = full binder |
| Delimiters + tiers help injection | Delimiters alone solve injection |
| Manifest always in **log** | Demo must show PackManifest UI |
| Minimize-to-grant | Dump outside grant “to be helpful” |

---

## 3. Closed decisions (DM + red-team)

| ID | Decision |
|---|---|
| **D1** | Budget = **token-vs-window**: fit `context_window_hint − reserve` (and Admin max) |
| **D2** | History = last **4** **raw** turns from **server transcript**; drop oldest first if over budget |
| **D3** | **Full file** allowed when **small** (byte ∧ page ∧ residual-token gates); else excerpt; **total attach cap** per pack |
| **D4** | Tool/MCP overflow = **head + tail + truncation marker**; each side capped |
| **D5** | **PackManifest** emitted every pack; demo Audience B = **log/inspect only** (UI = org-ambition) |
| **D6** | Delimiters = **XML-ish** `<kwb_…>` tagged blocks with `trust` (and source) attrs |
| **D7** | Orchestrator **cannot bypass** packer; retrieve only via WP-11 authz-first outputs |
| **D8** | Demo retrieve into pack **k ≤ 5** (WP-11) |

---

## 4. Ownership

| Actor | Does | Does not |
|---|---|---|
| **Orchestrator (WP-06)** | Declares step need, `model_id`, retrieve intent | Concatenate unauthorized files into messages |
| **Packer (this WP)** | Build messages; delimit; truncate; budget; manifest | Decide plant truth; widen grants |
| **WP-11** | Authz-first chunks | Packer re-query global index |
| **WP-09** | Wire reject oversize/invalid | Replace packer policy |
| **Human** | Ultimate verifier | — |

---

## 5. Pipeline (frozen)

```
step intent + grant_id
  → live grant check (fail if revoked/missing)
  → collect allowed classes only
  → retrieve via WP-11 if needed (k≤5 demo)
  → wrap T1–T4 in XML-ish delimiters + trust_label + source id
  → bind citations only to packed chunk_ids
  → apply token-vs-window budget (shrink order below)
  → tool results: head+tail+marker if over per-tool / total tool budget
  → history: last 4 raw; drop oldest if needed
  → emit PackManifest → gateway
```

Empty authorized retrieve → honest miss / `NOT FOUND` path — **no invented filler chunks**.

---

## 6. Token-vs-window budget (D1)

| Rule | Must |
|---|---|
| Window source | Card `context_window_hint` if present; else Admin/demo default |
| Reserve | **max(10% of window, 512 tokens)** reserved for completion / tool schemas |
| Usable pack | `window − reserve`, also ≤ Admin max |
| Estimate | Recorded as `token_est` (may be approximate); label honesty in manifest |
| Over budget | Shrink (§8) or **fail-closed** — never send known-overfull pack silently |
| Gateway | May still reject (WP-09) |

---

## 7. Small full-file gate (D3)

An attachment may be packed **in full** only if **all** hold:

| Gate | Demo default (must-work numbers) |
|---|---|
| Bytes | ≤ **1 MiB** per file (Admin may lower) |
| Pages | ≤ **5** pages (PDF/scan); non-paginated ≤ byte gate |
| Residual tokens | Fits in remaining budget after T0 + skills + retrieve + history reservation |
| Total attaches | Sum of attach budgets ≤ **2 MiB** / pack (demo) |

Otherwise: **excerpt** (selected/first pages within budget). Many small files still hit total cap.

Pre-H1 extracts remain **T4** (no draft/agent authority). Post-H1 = **T2** data.

---

## 8. Shrink order (when over budget)

1. Drop oldest history turns (within the last-4 window).  
2. Tighten tool head/tail caps (keep marker).  
3. Excerpt attachments further (never claim full file if excerpted).  
4. Drop lowest-rank retrieve chunks **entirely** (do not keep cite without chunk).  
5. If still over → **fail-closed**.

**Never:** strip citation metadata while leaving chunk text; strip H1/HITL rails; promote T3→T0 to “save space.”

---

## 9. History (D2)

- Source: **server** transcript only.  
- Must-work: last **4** raw turns, each **re-delimited**.  
- Summarize-older = **ambition** only.  
- Client-forged history = ignore.

---

## 10. Tool / MCP truncation (D4)

| Rule | Must |
|---|---|
| Over per-result or total tool budget | Keep **head** + **tail** + marker |
| Split | ≤ **50%** of that result’s budget each side (head/tail) |
| Marker | Explicit; include omitted size in PackManifest |
| Trust | Entire result **T3**; heuristics prefer full text before trunc when local cost allows |
| Names/descriptions | T3 always (WP-23) |

---

## 11. Delimiters (D6)

### Pattern (frozen)

```xml
<kwb_data trust="T1|T2|T3|T4" source="…" chunk_id="…" grant_id="…">
…payload…
</kwb_data>
```

- T0 rails stay **outside** these wrappers (system / policy channel).  
- Nested/fake `kwb_*` or “system” inside payload → treat as **data**; override patterns → refuse+log (WP-23).  
- Skills / RAG / MCP / `.md` / tool stdout use this family (attrs as applicable).

Exact attr set may add fields later without redesign; **`trust` + body wrap** are must.

---

## 12. PackManifest (D5)

Emitted **every** successful or failed pack attempt (fail includes reason):

| Field | Required |
|---|---|
| `grant_id` | Yes |
| `model_id` | Yes |
| `job_id` / step | Yes |
| `chunk_ids` + corpus ids | Yes when retrieve |
| `trust_mix` counts | Yes |
| `token_est`, `window`, `reserve` | Yes |
| `truncated` flags / omitted sizes | Yes if any |
| `attach_mode` full\|excerpt per file | Yes |
| `history_turns_kept` | Yes |

Demo: **log / inspect** sufficient. Org-ambition: Audience B pack viewer. Manifest must **not** dump full secret bodies — ids/sizes/hashes preferred.

---

## 13. Allowed classes (summary)

T0 rails · progressive skill body (T3) · T1 claims · attach/OCR per H1 state · WP-11 chunks (T3) · tool/MCP (T3) · local/`data:` images only.

**Never:** other-task context; revoked-grant data; remote http(s) image URLs; client ACL spoof; full skill library; capability-index dump.

---

## 14. Must / ambition / deferred / never

### Must-work

1. Packer-only assembly; no conductor bypass.  
2. Live grant check; authz-first retrieve only; k≤5 demo.  
3. Token-vs-window + reserve; shrink order / fail-closed.  
4. History last 4 raw; re-delimit.  
5. Small full-file gates; else excerpt; total attach cap.  
6. Head+tail+marker for tools.  
7. XML-ish delimiters + trust.  
8. PackManifest always logged.  
9. Citation binding; no cross-task merge.

### Org-ambition

- Audience B PackManifest UI; adaptive page pick; history summarize; Admin pack debugger; higher caps.

### Deferred

- Learned packer; cross-session memory as corpus.

### Never

- Dump corpus outside grant.  
- Remote vision URLs.  
- Delimiters-as-complete-security claim.  
- Invent chunks when retrieve empty.  
- Untrusted elevation to T0.

---

## 15. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | AC-6-shaped minimize-to-model-view; authz-before-pack | User / Spec / WP-04/11 |
| **Add** | Token-window budget; small-file gates; XML-ish `kwb_data`; PackManifest | DM / red-team |
| **Refuse** | Helpful full-binder; markdown-only must delimiters; optional manifest |

---

## 16. Demo acceptance

1. Oversize pack shrinks or fail-closes; manifest shows `token_est` / reserve.  
2. History never exceeds 4 turns; oldest dropped first under pressure.  
3. Large PDF excerpts; small PDF ≤ gates packs full with `attach_mode=full`.  
4. Huge tool stdout → head+tail+marker; omitted size logged.  
5. Manifest present in log without requiring Audience B UI.  
6. T3 blob in `kwb_data`; forged system-inside → data/refuse path.  
7. Revoke → pack/retrieve fail-closed.  
8. No remote image URL in messages.

---

## 17. Next

**WP-09** — LLM gateway (schema-valid `/v1`; may reject oversize packs).

---

## 18. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial pass on budget / small-file / delimiters / manifest |

**Confidence:** **0.87**
