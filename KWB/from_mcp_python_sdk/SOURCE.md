# SOURCE — from_mcp_python_sdk

**Upstream:** `vendor/python-sdk/` (official Model Context Protocol Python SDK)  
**License:** MIT (`LICENSE` copied here; upstream `vendor/python-sdk/LICENSE`)  
**Role:** Protocol study for a later offline MCP MOCK host — not a runnable install.

## What was copied (kept small, 17 modules + LICENSE)

| KWB path | Upstream path |
|---|---|
| `mcp/__init__.py` | `src/mcp/__init__.py` |
| `mcp/client/{__init__,client,session,stdio}.py` | `src/mcp/client/...` |
| `mcp/server/{__init__,session,stdio,fastmcp}.py` | `src/mcp/server/...` |
| `mcp/server/lowlevel/{__init__,server}.py` | `src/mcp/server/lowlevel/...` |
| `mcp/types/{__init__,methods,jsonrpc,version}.py` | `src/mcp/types/...` |
| `mcp/shared/{exceptions,message}.py` | `src/mcp/shared/...` |
| `LICENSE` | `LICENSE` |

**File count target:** &lt;30 — satisfied.

## Path pointers (not copied — stay in vendor)

- `src/mcp/server/mcpserver/` — high-level server helpers  
- `src/mcp/server/auth/` — OAuth / bearer (not for air-gap MOCK day-1)  
- `src/mcp/client/auth/` — client auth  
- `src/mcp-types/` — generated wire types (`mcp_types`) — runtime dep of `__init__.py`  
- `tests/`, `examples/` — full suites  

## What KWB will use later

- Client/session/stdio entry shapes for a **local MOCK** plant connector (read-only tools).
- Types / JSON-RPC method names when documenting MCP allowlist + Monitor A.

## What NOT to import as product

- Full SDK as production dependency without pin + offline wheel story.
- Auth / cloud OAuth paths; streamable HTTP to public origins.
- Do not treat this folder as `pip install -e` — imports need `mcp_types` and remaining shared modules from vendor or a proper package.

## MISSING

None for the planned entry modules above.
