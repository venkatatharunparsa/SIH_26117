"""Thin MCP MOCK stub — FastMCP echo shape without hosting a real MCP server.

Inspired by:
  - KWB/from_fastmcp/examples/echo.py  (@mcp.tool echo)
  - KWB/from_mcp_python_sdk/           (protocol study)

Feature flag OFF by default. When disabled, routes report "not enabled".
Do not pip-install mcp/fastmcp into production for this stub.
Full MCP host / progressive skill tools = deferred.
"""

from __future__ import annotations

import os
from typing import Any

# SOVEREIGN_MCP_MOCK=1 to enable the in-process echo; default OFF.
MCP_MOCK_ENABLED = os.environ.get("SOVEREIGN_MCP_MOCK", "").strip() in {
    "1",
    "true",
    "TRUE",
    "yes",
    "YES",
}


def status() -> dict[str, Any]:
    if not MCP_MOCK_ENABLED:
        return {
            "ok": False,
            "enabled": False,
            "message": "MCP MOCK not enabled",
            "hint": "Set SOVEREIGN_MCP_MOCK=1 for in-process echo only (no MCP host)",
        }
    return {
        "ok": True,
        "enabled": True,
        "server": "Echo Server (MOCK)",
        "tools": ["echo_tool"],
        "note": "In-process stub — not a stdio/SSE MCP host",
    }


def echo_tool(text: str) -> dict[str, Any]:
    """FastMCP-inspired echo — only when flag is on."""
    if not MCP_MOCK_ENABLED:
        return {
            "ok": False,
            "enabled": False,
            "error": "mcp_mock_not_enabled",
            "message": "MCP MOCK not enabled",
        }
    return {"ok": True, "enabled": True, "tool": "echo_tool", "text": text}
