"""Local MCP-shaped tool host — in-process allowlist (demo).

Org target: full MCP stdio/SSE lifecycle + Admin allowlist.
Demo: grant ∩ tool allowlist; default ON; set SOVEREIGN_MCP_HOST=0 to disable.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any

from .audit import log_event
from . import skills

_raw = os.environ.get("SOVEREIGN_MCP_HOST", "1").strip().lower()
_ENABLED = _raw not in {"0", "false", "no", "off"}

DEFAULT_ALLOWLIST = frozenset(
    {"echo_tool", "list_skills", "workspace_clock", "ping_knowledge"}
)


def enabled() -> bool:
    return _ENABLED


def status() -> dict[str, Any]:
    if not _ENABLED:
        return {
            "ok": False,
            "enabled": False,
            "host": "in_process_mcp_host",
            "message": "MCP host not enabled",
            "hint": "Set SOVEREIGN_MCP_HOST=1 for in-process tools (default ON)",
            "note": "Not a stdio/SSE MCP server — demo host only",
        }
    return {
        "ok": True,
        "enabled": True,
        "host": "in_process_mcp_host",
        "server": "KWB Demo Tool Host",
        "tools": sorted(DEFAULT_ALLOWLIST),
        "note": "In-process allowlist host — not full MCP lifecycle / public registry",
    }


def list_tools() -> list[dict[str, str]]:
    return [
        {"name": "echo_tool", "description": "Echo text (connectivity)"},
        {"name": "list_skills", "description": "List skill pack ids on disk"},
        {"name": "workspace_clock", "description": "UTC clock for audit stamps"},
        {"name": "ping_knowledge", "description": "Confirm knowledge shelf reachable"},
    ]


def call_tool(
    name: str,
    arguments: dict[str, Any] | None = None,
    *,
    allowlist: set[str] | frozenset[str] | None = None,
    grant_id: str | None = None,
) -> dict[str, Any]:
    allowed = allowlist if allowlist is not None else DEFAULT_ALLOWLIST
    if not _ENABLED:
        return {"ok": False, "error": "mcp_host_not_enabled", "enabled": False}
    if name not in allowed:
        log_event("mcp_deny", tool=name, grant_id=grant_id, reason="not_on_allowlist")
        return {"ok": False, "error": "tool_not_allowlisted", "tool": name}

    args = arguments or {}
    if name == "echo_tool":
        out = {"ok": True, "tool": name, "echo": str(args.get("text") or "")}
    elif name == "list_skills":
        out = {"ok": True, "tool": name, "skills": skills.list_skills()}
    elif name == "workspace_clock":
        out = {
            "ok": True,
            "tool": name,
            "utc": datetime.now(timezone.utc).isoformat(),
        }
    elif name == "ping_knowledge":
        from .config import ROOT

        shelf = ROOT / "workspace" / "knowledge"
        out = {
            "ok": True,
            "tool": name,
            "knowledge_dir": str(shelf),
            "exists": shelf.is_dir(),
            "files": len(list(shelf.glob("*.md"))) if shelf.is_dir() else 0,
        }
    else:
        out = {"ok": False, "error": "unknown_tool", "tool": name}

    log_event("mcp_call", tool=name, grant_id=grant_id, ok=out.get("ok"))
    return out


MCP_MOCK_ENABLED = _ENABLED


def echo_tool(text: str) -> dict[str, Any]:
    return call_tool("echo_tool", {"text": text})
