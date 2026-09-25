"""Back-compat shim — prefer mcp_host."""

from __future__ import annotations

from .mcp_host import (  # noqa: F401
    MCP_MOCK_ENABLED,
    call_tool,
    echo_tool,
    enabled,
    list_tools,
    status,
)
