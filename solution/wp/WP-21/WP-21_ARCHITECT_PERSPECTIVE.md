# WP-21 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-04 / WP-06 / WP-07 / WP-11 / WP-22 / WP-23 / WP-24 (card hints)  
**Status:** **SUPERSEDED by `WP-21_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-21_REDTEAM.md`.  
**Job of WP-21:** **Context assembly / data-to-pass** — build each model request from **only** what the **active grant**, **step**, and **rails** allow; delimit **T0–T4**; attach **citations** bound to retrieved chunks; truncate tool/MCP/skill blobs; **never** dump the plant corpus or bypass packer because the conductor “knows” everything.

**Sources:** Official (confidential on-prem — same logic: do not over-send locally); WP-00 Intelligent layer “what data to pass”; User AC-6 / minimize-to-grant; WP-04 grant allowlists; WP-06 conductor requests / packer enforces; WP-11 authz-first + k=5; WP-23 delimit + trust labels; WP-22 three-source labels in packed claims; NIST AC-6 *shaped* (no certification claim).

---

## One sentence (proposed)

Every `/v1` call’s messages are **assembled by the packer**: grant-scoped, step-minimal, **trust-delimited**, citation-bound, size-capped — the **orchestrator names the need**; the packer **enforces** what actually enters the model.

---

## 1. Ownership (locked by prior freezes)

| Actor | Role |
|---|---|
| **Orchestrator (WP-06)** | Declares step need: job, specialist, skill ids, retrieve intent, tools just called, `model_id` |
| **Packer (WP-21)** | Builds message list + attachments; applies ceilings, delimiters, truncations, deny |
| **Retrieve (WP-11)** | Returns **already authz-filtered** chunks (packer does not re-widen) |
| **Gateway (WP-09)** | Wire schema / size / timeout — may reject oversize packs |
| **Human** | Ultimate verifier; packer does not decide plant truth |

**Forbidden:** Orchestrator concatenating raw files into prompts; specialists pasting sibling-task context; client-supplied “include these SOP ids” without grant.

---

## 2. What may enter a pack (classes)

| Class | When | Trust | Notes |
|---|---|---|---|
| **T0 rails** | Always (system) | T0 | Never list, grant summary (ids not secrets), HITL state — **not** model-editable |
| **Job / skill body** | Progressive load for this step | T3 | Metadata first; body only if matched (WP-07) |
| **User chat / corrections** | This turn | T1 claim | Not plant fact (WP-22/23) |
| **User-attached bytes** | If in grant / attach-only | T2/T4 per H1 state | Prefer excerpts over whole binder |
| **OCR `human_verified`** | After H1 | T2 | Data, not instructions |
| **RAG chunks** | KB grant + live check | T3 | ≤ top-k from WP-11; cite metadata required when KB used |
| **Policy chunks** | Same | T3 | Distinct corpus id (WP-11) |
| **Tool / MCP stdout** | This step results | T3 | Truncate; names/descriptions T3 |
| **Prior turn summary** | Multi-turn | Re-delimit | No trust promotion across turns |
| **Images / scans** | Vision/OCR step | — | **`data:` / local bytes only** — no remote URL |

**Never in pack:** Other tasks’ grants; revoked-grant retrieve; unauthenticated ACL filters; full skill library; full MCP catalog bodies; plant SoR write APIs; WAN URLs.

---

## 3. Minimize-to-grant pipeline (proposed)

```
orchestrator step intent
  → resolve active grant_id (fail if none/revoked)
  → allowlist ∩ ceiling ∩ segregation already on grant
  → collect candidates only from allowed classes
  → for retrieve: call WP-11 (authz-first) — do not pack unauthorized docs “for helpfulness”
  → assign trust_label + delimiters (WP-23)
  → bind citations to chunk_ids actually included
  → apply size budget (card context_window_hint ∩ Admin/demo caps)
  → truncate tool/MCP/history by policy (head/tail + “truncated” marker)
  → emit PackManifest {sources, chunk_ids, trust mix, token_est, grant_id}
  → gateway sends messages
```

Empty authorized set → honest empty / `NOT FOUND` path (WP-22) — **not** invent filler context.

---

## 4. Delimiters & labels (WP-23 → here)

Packer owns **exact delimiter strings** and placement:

- Wrap T1–T4 blobs with explicit markers + `trust_label` + source id.  
- T0 never inside user/tool wrappers.  
- Nested fake “system” inside T3 → treat as data; heuristic refuse/log if override pattern (WP-23).  
- Multi-turn: **re-pack**; do not promote T3→T0 because the model “remembered” it.

Exact marker syntax brand-free until freeze (open Q).

---

## 5. Size & truncation (proposed)

| Knob | Demo proposal | Org |
|---|---|---|
| Retrieve | WP-11 **k=5** hard into pack | Admin may raise k; pack still capped |
| Tool/MCP result | Cap chars/tokens per result + total | Same + per-plugin caps |
| Attachments | Excerpt pages/sections; not whole drawing set by default | Ambition: smarter page pick |
| History | Last N turns or summary-of-summary | Ambition |
| Hard fail | Over Admin max → fail-closed or mandatory shrink | Same |

Mid-range GPU context is **finite** — treat as product constraint, not excuse to skip minimize.

---

## 6. Citations in the pack

When KB grant active:

- Include citation metadata for **every** chunk packed (WP-11 fields).  
- Model-facing text may carry short cite tags; **UI/log** must show binding.  
- Packer **refuses** to include a cite for a chunk not in this pack.  
- Three-source labels (S1/S2/S3) for material claims are **WP-22** — packer carries prior labels / H7 state as T0/T1 metadata, does not invent reconciliation.

Attach-only jobs may omit org cites (WP-01/11).

---

## 7. Parallel / multi-specialist

Per WP-06/07: **no shared super-context**.

- Each specialist run → **own pack** under **own grant_id** (or same grant but still isolated message assemblies).  
- `parallel_join` merges only **allowed artefact refs** (paths/ids), not raw sibling prompts.

---

## 8. Conductor vs packer (anti-confusion)

| Orchestrator may | Packer must |
|---|---|
| Request “need SOP clauses about X” | Call retrieve under grant; drop if deny |
| Request “include tool result #3” | Truncate + T3 wrap |
| Pass `model_id` + params | Not change card; may use `context_window_hint` |
| Hold capability **index** | Not dump index into every prompt |

---

## 9. Must / ambition / deferred / never (proposed)

### Must-work

1. Pack only under active grant; live deny on revoke.  
2. Authz-first retrieve results only; k≤ demo default into pack.  
3. T0–T4 delimit + trust labels on untrusted blobs.  
4. Truncate tool/MCP/history; PackManifest logged.  
5. Local/`data:` images only.  
6. No cross-task prompt merge.  
7. Citations bound to packed chunks when KB used.  
8. Orchestrator cannot bypass packer.

### Org-ambition

- Adaptive page/section pick; compression summaries with cite preservation; Admin pack debugger UI.

### Deferred

- Learned packer models; cross-session memory stores as standing corpus.

### Never

- Dump plant corpus outside grant.  
- Remote image/http fetch into vision messages.  
- Client-spoofed ACL in pack.  
- Treat packer output as plant fact.  
- Untrusted text elevating to T0.

---

## 10. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | AC-6-shaped least privilege for **what the model sees**; progressive disclosure (skills) |
| **Adopt** | Authz-before-pack (air-gap RAG pattern) |
| **Add** | PackManifest; delimiter ownership; size budgets; conductor≠packer split |
| **Refuse** | “Helpful” full-binder paste; shared mega-context; packer as SoR |

---

## 11. Open questions for decision maker

1. **Pack budget (demo):** hard cap as **token estimate** (e.g. fit card window − reserve), or simpler **char/page caps** for must-work?  
2. **History:** keep **last N raw turns** (propose N=3 or 5), or **summarize older turns** (ambition) for must-work demo?  
3. **Attachments:** default **excerpt** (e.g. selected pages / first N pages) vs allow **full file** when user attaches a small PDF?  
4. **Tool results:** on overflow, keep **head + tail** with truncation marker, or **head only**?  
5. **Audience B:** must operators see **PackManifest** (what entered the model) as must-work, or log-only for demo?  
6. **Delimiter style:** freeze **XML-ish tagged blocks** (e.g. `<kwb_data trust="T3" …>`) vs **markdown fences with headers** — pick one for must-work?

---

## 12. Next after your decisions

**Done.** Frozen as `WP-21_FREEZE.md` rev 1.0. Next: **WP-09**.
