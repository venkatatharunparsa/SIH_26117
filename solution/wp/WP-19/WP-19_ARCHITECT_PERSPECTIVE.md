# WP-19 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-08 / WP-10 / WP-13 / WP-24 (WP-15 skills media; WP-17 audit)  
**Status:** **SUPERSEDED by `WP-19_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-19_REDTEAM.md`. Verify: `WP-19_FREEZE_VERIFY.md`.  
**Job of WP-19:** **Offline update** — bring **weights, MCP/plugin packs, and skill packs** into the air-gapped estate on **approved offline media**, then **stage → verify → register/allowlist** (WP-10/24/08). **No** silent Hugging Face / npm / MCP directory / Skills Hub pull during operation or “add model” demos.

**Sources:** Official Description (add models later; nothing external) + Expected Solution (no external calls at any point); WP-00 offline media outside KWB; WP-08 H5 offline packs; WP-10/24 stage+card; WP-13 A must not go green while WAN update; air-gapped MCP observed pattern.

---

## One sentence (proposed)

New models and plugins arrive as **Admin-handled offline packages**: copy from approved media → integrity check → stage on runtime/host → enable card / H5 allowlist — KWB never phones home to fetch them.

---

## 1. What travels on media

| Payload | Lands in | Then |
|---|---|---|
| Open-weight files (incl. quant) | Runtime disk (WP-10) | Card pending→enable (WP-24) |
| MCP/plugin pack | Plugin stage dir | H5 allowlist (WP-08) |
| Skill / template packs | Skill shelves | Admin/H6 as applicable (WP-07/15) |
| Optional checksums / SBOM / notes | Beside pack | Verify before enable |

**Outside KWB:** acquiring media on a connected machine is an **org ops** step — not an in-app download button.

---

## 2. Pipeline (proposed)

```
Approved offline media (USB/approved share — org policy)
  → Admin mounts/copies into quarantine/stage area
  → integrity check (checksum / size / manifest)
  → stage weights to runtime paths OR plugin/skill dirs
  → register: Model Card (pending/disabled) OR H5 review
  → enable when ready (WP-24 / H5)
  → Audience A: update procedure itself must not require WAN
  → audit events (WP-17)
```

**Fail-closed:** checksum mismatch, unknown publisher (if policy), or WAN fetch attempt → deny enable.

---

## 3. Demo vs org

| | Demo | Org |
|---|---|---|
| Media | Pre-staged on disk OK; **show** offline-add story with labelled MOCK “media drop” | Real USB/approved channel |
| Add model | Register card for already-copied weights; prove **no HF UI** | Full stage+enable |
| Add plugin | Pre-allowlisted MOCK (WP-08) + optional offline re-add | Full H5 |
| Proof | Audience A during “add” shows no public fetch | Same |

---

## 4. Must / ambition / deferred / never (proposed)

### Must-work

1. Documented offline intake path for **weights** and **plugins**.  
2. No in-app HF/npm/MCP registry/Skills Hub download.  
3. Stage then register (card / H5) — not “download = enabled.”  
4. Integrity check before enable (minimum: checksum or equivalent).  
5. Audit who staged/enabled.  
6. Demo proves add-without-WAN (even if files pre-copied).  
7. Update path compatible with Audience A (no public egress).

### Org-ambition

- Signed packs / SBOM; request queue; multi-Admin dual control; air-gap sync appliance.

### Deferred

- Automated mirror farms; continuous CVE patch product.

### Never

- In-app internet pull for models/plugins/skills.  
- Silent background updater to public registries.  
- Enable without Admin path.  
- Treat “advise download” as air-gap OK.

---

## 5. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Air-gap stage-then-register pattern |
| **Add** | Media→quarantine→checksum→stage→enable contract; demo MOCK media drop |
| **Refuse** | HF-in-UI; npm-in-sandbox; public MCP install |

---

## 6. Boundaries

| Topic | Owner |
|---|---|
| Load/unload VRAM | **WP-10** |
| Card schema | **WP-24** |
| H5 allowlist | **WP-08** |
| WAN=0 proof | **WP-13** |
| Eval “no HF during add” | **WP-18** (extend golden ambition) |

---

## 7. Open questions for decision maker

1. **Media types (must):** **USB only**, **Admin network share on-prem only**, or **either**?  
2. **Checksum:** Require **SHA-256 (or equiv) manifest** for must-work, or size+Admin eyeball enough for demo?  
3. **Who may stage files:** **Admin only**, or **operator copy + Admin enable**?  
4. **Demo story:** Must show a **visible “import from media” UI**, or **runbook + folder drop** enough?  
5. **Skill packs on media:** In must-work offline path, or **weights+plugins only** (skills later)?  
6. **Quarantine:** Mandatory **separate quarantine dir** before runtime/plugin dirs, or direct stage OK for demo?

---

## 8. Next after your decisions

**Done.** Frozen as `WP-19_FREEZE.md` rev 1.0. Next: **WP-20**.
