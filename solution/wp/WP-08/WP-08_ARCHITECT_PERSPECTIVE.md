# WP-08 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-04 / WP-05 / WP-07 / WP-16 / WP-23  
**Status:** **SUPERSEDED by `WP-08_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-08_REDTEAM.md`.  
**Job of WP-08:** KWB is an **MCP/plugin host**: Admin can **add** local servers/skill packs **offline**, **allowlist** them, enforce **default-deny egress**, gate **use** by task grant, treat tool text as **T3**, and prove the host works with **≥1 local demo server** — without public MCP directory or WAN connectors.

**Sources:** Official Background (Claude/Codex-class); Expected Solution (no external calls); WP-00 local MCP; WP-05 H5; WP-07 MCP slot; MCP transports Spec; Agent Skills Spec; repo map Goose/Cursor host UX, FastMCP, Pipelock *idea*.

---

## One sentence (proposed)

KWB hosts **local, allowlisted MCP/plugin packs** brought in on **offline media**: install is **Admin + H5**, runtime use needs **grant ∩ allowlist**, every plugin defaults to **no egress**, and tool names/results stay **untrusted data** — never a cloud plugin store.

---

## 1. Host vs built-in tools

| | Built-in (WP-07) | MCP / plugin (this WP) |
|---|---|---|
| Must-work demo | Required | **Host capability** required; **one local demo server** enough |
| Install | N/A | Offline pack + Admin allowlist |
| Egress | N/A (tools local) | **Default deny** per server |
| SoR write | Forbidden | Forbidden (deny-list capabilities) |

Being a **host** ≠ shipping dozens of adapters on day one (same pattern as models/connectors).

---

## 2. Install path (air-gap)

```
Approved offline media (outside KWB download)
  → stage pack on disk (plugin.json / skills / mcp config)
  → Admin H5 allowlist + capability review
  → register local transport (stdio / localhost only)
  → available to grants that include that plugin id
```

**Never:** in-app install from public MCP Registry / HTTPS remote servers / Anthropic public MCP connector pattern.

---

## 3. Transport & runtime rules (proposed)

| Rule | Must |
|---|---|
| Transports | **stdio** and/or **localhost** only for must-work |
| Remote Streamable HTTP to internet | **Never** |
| Egress from plugin process | **Default deny**; Admin explicit allow only for on-prem LAN targets (ambition) |
| Tool descriptions / results | **T3** (WP-23) |
| Use | `grant.tool_plugin_allowlist` ∩ Admin allowlist |
| Standing secrets in config | Install-time Admin; **use** still grant-gated (WP-04) |
| Isolation | Prefer separate process; may reuse WP-16-class jail for untrusted servers (ambition/org) |

---

## 4. Capability deny-list (proposed never in allowlist)

- Write EAM/ERP/DCS/DMS SoR  
- OT / PLC control  
- Arbitrary host shell without sandbox  
- WAN/http client to public internet  
- Self-modify Admin allowlist  

Read-only plant connectors stay **WP-02** adapters preferred; MCP read tools only if Admin-approved and read-only.

---

## 5. Skill packs in plugins

- Plugin may ship `skills/` (Agent Skills layout) → plugin shelf (WP-07).  
- Still progressive load + T3 + H6 if promoting to org.  
- `SKILL.md` ≠ security boundary (WP-23).

---

## 6. Demo vs org

| | Demo | Org |
|---|---|---|
| Servers | **One** local demo MCP (e.g. read workspace helper / echo / MOCK) | Many allowlisted |
| Install UX | May pre-allowlist labelled MOCK | Full H5 Admin UX ambition |
| Egress proof | Show deny / WAN=0 with plugin present | Per-plugin egress policy |

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Host architecture: add/register local MCP.  
2. Offline-only intake principle.  
3. Admin allowlist; grant-gated use.  
4. Default-deny egress.  
5. ≥1 local demo server callable under grant.  
6. Tool text T3; no SoR-write capabilities.  
7. Fail closed if not allowlisted.

### Org-ambition

- Full H5 install wizard; pin/sign packs; per-plugin LAN allow; process jail for MCP; Pipelock-class egress intercept.

### Deferred

- Plugin marketplace UI; federation gateways; signed SBOM enterprise program.

### Never

- Public MCP registry at runtime.  
- Internet MCP / cloud connectors.  
- WAN self-install.  
- SoR/OT write via MCP.  
- Empty allowlist = all plugins.

---

## 8. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | MCP Spec + SDK (stdio/localhost); FastMCP for *our* demo server; Goose/Cursor *add server* UX; Agent Plugins pack layout; Pipelock *egress idea*; Docker MCP allowlist/pin *guidance* |
| **Add** | Offline H5; grant∩allowlist; default-deny egress; deny-list capabilities; one demo server |
| **Refuse** | Official remote servers (Drive/Slack/GitHub); MCP Registry; federation gateways; Anthropic public HTTPS MCP connector |

---

## 9. Open questions for decision maker

1. **Demo MCP purpose:** MOCK **read-only** helper (recommended) vs “echo/tools list only” — pick?  
2. **Must-work H5 UX:** full Admin wizard, or **pre-allowlisted** demo server + labelled host proof enough?  
3. **Localhost MCP:** allow `127.0.0.1` only (recommended) or also org LAN hostnames in must-work?  
4. **MCP inside WP-16 jail:** must for demo, ambition, or not required if process-isolated + egress deny?  
5. **Remove plugin:** Admin can disable/remove without workbench redesign — confirm **yes** (symmetry with models)?  
6. **Worker request plugin:** request-only (Admin installs) — confirm **yes**?

---

## 10. Next after your decisions

**Done.** Frozen as `WP-08_FREEZE.md` rev 1.0. Next: **WP-24**.
