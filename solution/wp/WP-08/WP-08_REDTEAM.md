# WP-08 MCP host — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-08_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** see §0  
**Against:** Official Background + Expected Solution offline; WP-00/04/05/07/16/23; MCP Spec; MCP security draft; repo map WP-08.

---

## 0. DM answers (binding)

| Q | Decision |
|---|---|
| **1 Demo vs org** | **Demo:** MOCK read-only (or echo) local server **enough**. **Org:** full local MCP host capability (install, allowlist, grant use, egress deny, remove, multi-server). |
| **2 H5 UX** | **Pre-allowlisted** demo server + **labelled** host proof |
| **3 Network** | Must-work: **localhost / stdio only**. Org LAN MCP = **ambition** under explicit Admin egress allow |
| **4 Jail** | MCP in WP-16-class jail = **ambition** |
| **5 Remove** | **Yes** — Admin disable/remove without workbench redesign |
| **6 Request** | **Yes** — worker **requests**; Admin installs (H5) |

---

## Verdict

| | |
|---|---|
| Direction | **Yes** |
| Missing | M1–M12 (lifecycle, pin, write-deny enforce, secrets, stdio hijack, demo label, org multi-server) |
| Overhyped | One echo server = enterprise MCP; allowlist = security; localhost = safe |
| Confidence after freeze | **~0.87** → GO WP-24 |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Org “all local MCP things” checklist | Catalog: add, list, enable/disable, remove, grant bind, egress policy, audit, skill pack attach, fail-closed |
| **M2** | Capability schema on register | Declare tools read/write/network; reject SoR-write / WAN at allowlist time |
| **M3** | Pin / integrity | Ambition sign; must: path + hash recorded on allowlist |
| **M4** | Secrets in mcp.json | Admin-only; not copied into model context; use still grant-gated |
| **M5** | Stdio malware | Process isolation ambition; must: no elevating to Admin via tool |
| **M6** | Localhost port scan | Bind allowlist to **specific** command/args or port — not “any localhost” |
| **M7** | Demo labelled | UI/log: **MOCK / pre-allowlisted** — not “integrated SAP MCP” |
| **M8** | Disable vs delete | Soft-disable blocks use; remove drops registration |
| **M9** | Request queue | Worker request artefact; Admin approve/deny (ambition UX; must: principle) |
| **M10** | Plugin skills shelf | On install, skills enter plugin shelf; still T3 + progressive |
| **M11** | Egress default deny proof | Demo shows plugin present + no WAN |
| **M12** | Empty allowlist | ≠ all plugins (align WP-04) |

---

## 2. Overhyped

| Attack | Fix |
|---|---|
| **A1** Demo echo = full host done | Org checklist required on paper |
| **A2** Allowlist = secure | + egress deny + grant + T3 + deny-list |
| **A3** Localhost safe | Specific bind; no WAN; capability review |
| **A4** H5 pre-allow = no Admin role | Admin still owns allowlist changes |
| **A5** MCP replaces WP-02 connectors | Connectors first-class; MCP optional read tools |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| MCP Spec stdio/localhost; FastMCP demo server; Goose/Cursor add-server UX; plugin pack layout; Pipelock egress *idea* | Public registry; Drive/Slack/GitHub servers; federation; public HTTPS MCP connector |

---

## 4. Disposition

**Applied.** → `WP-08_FREEZE.md` rev 1.0. Confidence **0.87**. **GO** → **WP-24**.
