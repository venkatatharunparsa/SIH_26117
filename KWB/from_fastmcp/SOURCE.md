# SOURCE — from_fastmcp

**Upstream:** `vendor/fastmcp/` (PrefectHQ FastMCP; workspace package `fastmcp_slim`)  
**License:** Apache-2.0 (`LICENSE` copied here)  
**Role:** Study for **one** later MCP MOCK server — ergonomic decorator API.

## What was copied (minimal — full slim tree is 250+ files)

| KWB path | Upstream path |
|---|---|
| `core/__init__.py` | `fastmcp_slim/fastmcp/__init__.py` |
| `core/settings.py` | `fastmcp_slim/fastmcp/settings.py` |
| `core/types.py` | `fastmcp_slim/fastmcp/types.py` |
| `core/server/server.py` | `fastmcp_slim/fastmcp/server/server.py` |
| `core/tools/__init__.py` | `fastmcp_slim/fastmcp/tools/__init__.py` |
| `core/tools/base.py` | `fastmcp_slim/fastmcp/tools/base.py` |
| `examples/echo.py` | `examples/echo.py` |
| `LICENSE` | `LICENSE` |

## Path pointers (not copied)

- Full package: `vendor/fastmcp/fastmcp_slim/fastmcp/` (~251 `.py` files)
- Other demos: `vendor/fastmcp/examples/` (auth OAuth demos, smart_home, tasks, …)
- Prefer re-reading `examples/echo.py` + `server/server.py` patterns when building MOCK

## What KWB will use later

- `@mcp.tool` / resource / prompt decorator style for a **single** offline plant MOCK.
- Settings knobs awareness (logging, deprecations) — do not pull telemetry cloud defaults into product.

## What NOT to import as product

- Entire `fastmcp_slim` tree into the repo as a fork.
- OAuth example servers (`examples/auth/**`) — WAN / IdP.
- Skills marketplace / remote providers / desktop helpers.
- These copies are **not** importable alone (heavy relative imports).

## MISSING

None for the planned minimal set. Full core intentionally not duplicated (size rule).
