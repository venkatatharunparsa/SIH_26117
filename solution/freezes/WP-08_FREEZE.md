# WP-08 Plugin host (MCP + skill packs) — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-04 / WP-05 / WP-07 / WP-16 / WP-23.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-08_ARCHITECT_PERSPECTIVE.md`, `WP-08_REDTEAM.md`, **DM 2026-09-18** (demo MOCK enough; org full local MCP; pre-allowlist proof; localhost/stdio must; jail ambition; remove yes; worker request / Admin install).  
**Findings SoT:** `WP-08_REDTEAM.md`  
**Product:** **KWB**

**Stack / MCP SDK brand:** not locked.

---

## 1. One-sentence contract

KWB is a **local MCP/plugin host**: packs arrive on **offline media**, **Admin allowlists** (H5), **workers request** but do not self-install, **use** requires **grant ∩ allowlist**, transports are **stdio / localhost** for must-work, **egress defaults to deny**, tool text is **T3**, Admin can **disable/remove** without redesign — demo proves the host with **one pre-allowlisted labelled MOCK** server; **organisation** supports the **full local MCP lifecycle**.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Demo one MOCK server proves host shape | Demo = plant integrations done |
| Allowlist + egress deny + grant | Allowlist alone = security |
| Localhost/stdio must-work | “Any localhost port” wild open |
| Org full local MCP catalog | Public registry / WAN MCP |
| MCP optional read tools | MCP replaces WP-02 connectors |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Demo = MOCK local server enough; **org = full local MCP lifecycle** |
| **D2** | Demo H5 = **pre-allowlisted + labelled proof** |
| **D3** | Must-work transport = **stdio and/or 127.0.0.1 only**; org LAN = ambition + explicit egress allow |
| **D4** | MCP in WP-16 jail = **ambition** |
| **D5** | Admin **disable/remove** without workbench redesign = **yes** |
| **D6** | Worker **request** only; Admin **installs** (H5) = **yes** |

---

## 4. Demo vs organisation

| Capability | Demo must-work | Organisation |
|---|---|---|
| Be a host (register local MCP) | **Yes** — one server | **Yes** — many |
| Server type | MOCK read-only / echo — **labelled** | Real internal tools (Admin-approved) |
| Install UX | Pre-allowlisted | Offline media + H5 (full UX ambition) |
| Worker request | Principle | Request queue ambition |
| Grant-gated use | **Yes** | **Yes** |
| Default-deny egress | **Yes** + WAN=0 proof | Per-server policy; LAN allow ambition |
| Disable/remove | Showable | **Yes** |
| Capability deny-list | Enforced | Enforced |
| Process jail | Not required | Ambition |
| Plugin-shipped skills | Optional | Supported (plugin shelf) |

---

## 5. Organisation local MCP lifecycle (full checklist)

Org paper requires KWB can:

1. **Stage** pack from offline media (no in-app WAN download).  
2. **Register** server (command/args or localhost endpoint **explicitly pinned**).  
3. **Record** integrity metadata (at least path + content hash).  
4. **Allowlist / enable** via Admin (H5).  
5. **Declare capabilities** (tools); **reject** deny-listed capabilities at allowlist time.  
6. **Bind to grants** (`tool_plugin_allowlist`).  
7. **Invoke** under active grant; fail-closed if missing.  
8. **Default-deny egress**; optional Admin LAN allow (ambition).  
9. **Audit** allow/deny/invoke (WP-17 shape).  
10. **Disable** (soft) and **remove** (unregister) without redesign.  
11. Attach **plugin skills** to plugin shelf; progressive load; T3.  
12. Accept **worker requests**; only Admin completes install.

---

## 6. Transport & security rules

| Rule | Freeze |
|---|---|
| Must-work transports | **stdio**, **127.0.0.1** only |
| Internet / public HTTPS MCP | **Never** |
| MCP Registry at runtime | **Never** |
| Egress | **Default deny** |
| Tool names/descriptions/results | **T3** (WP-23) |
| Secrets in config | Admin store; never dump into model context |
| Empty allowlist | ≠ all plugins |
| Pin bind | Specific command/args or host:port — not wildcard localhost |

---

## 7. Capability deny-list (never allowlist)

- SoR write (EAM/ERP/DCS/DMS)  
- OT/PLC control  
- Unrestricted host shell  
- Public WAN/http client  
- Self-modify Admin allowlist  

Prefer WP-02 read connectors for plant knowledge; MCP read tools only if Admin-approved read-only.

---

## 8. Install / request / remove

```
Worker request (optional)
  → Admin reviews pack (offline)
  → H5 allowlist + capability check
  → register pinned local transport
  → grant may include plugin id
  → use under grant
  → Admin disable/remove anytime
```

Demo may skip request UX and ship **pre-allowlisted MOCK** with label **MOCK / pre-allowlisted**.

---

## 9. Must / ambition / deferred / never

### Must-work

1. Host architecture + org lifecycle checklist on paper.  
2. One labelled pre-allowlisted local MOCK MCP demo.  
3. Grant ∩ allowlist use; fail-closed.  
4. Default-deny egress; stdio/localhost only.  
5. Deny-list capabilities.  
6. Admin disable/remove.  
7. Worker cannot self-install from WAN.  
8. Tool text T3.  
9. Offline intake principle.

### Org-ambition

- Full H5 wizard; request queue UI; LAN egress allow; WP-16 jail for MCP; sign/pin SBOM; Pipelock-class intercept.

### Deferred

- Marketplace UI; federation gateways; enterprise SBOM program.

### Never

- Public MCP registry / WAN install.  
- Cloud/remote internet MCP.  
- SoR/OT write via MCP.  
- Empty allowlist = all.  
- Claim demo MOCK = live plant MCP.  
- Anthropic public HTTPS MCP connector pattern.

---

## 10. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | MCP Spec + SDK (stdio/localhost) | Protocol |
| **Adopt** | FastMCP for *our* demo server | Build MOCK |
| **Adopt** | Goose/Cursor *add server* UX | Host metaphor |
| **Adopt** | Agent Plugins pack layout | skills + mcp.json |
| **Adopt** | Pipelock / Docker MCP *egress/allowlist ideas* | Below-model control |
| **Add** | Offline H5; org lifecycle; demo MOCK label; pin bind; remove | KWB |
| **Refuse** | Registry; Drive/Slack/GitHub servers; federation; public HTTPS connector |

---

## 11. Demo acceptance

1. Pre-allowlisted MOCK MCP appears as **allowlisted**.  
2. Call succeeds **under grant**; fails when grant lacks plugin / revoked.  
3. Label shows MOCK — not fake plant system.  
4. No WAN during plugin use (Audience A).  
5. Admin can disable → further calls fail-closed.

---

## 12. Next

**WP-24** — Model registry (pluggable models).

---

## 13. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze: demo MOCK + org full local MCP lifecycle |

**Confidence:** **0.87**
