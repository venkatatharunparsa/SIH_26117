"""In-process smoke: /orch/turn file-read packs README body into Gateway messages.

Gateway is stubbed — no live Ollama required.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from app import orchestrator as orch  # noqa: E402

_LAST_PACKED: list[dict[str, str]] = []


def _fake_gw(messages: list[dict[str, str]], **_kwargs: Any) -> dict[str, Any]:
    global _LAST_PACKED
    _LAST_PACKED = list(messages)
    sys_txt = next((m["content"] for m in messages if m.get("role") == "system"), "")
    # Prove model saw real README body
    grounded = "Knowledge Work Bench" in sys_txt or "SIH_26117" in sys_txt
    reply = (
        "Summary grounded in README: Knowledge Work Bench / SIH26117 offline desk."
        if grounded
        else "I only see task type/card/phase — no file."
    )
    return {
        "ok": True,
        "status": 200,
        "model": "stub",
        "body": {"choices": [{"message": {"role": "assistant", "content": reply}}]},
    }


def main() -> int:
    with mock.patch.object(orch.gateway, "chat_completions", side_effect=_fake_gw):
        r = orch.turn(
            task_type="inspection",
            user_id="smoke-file-read",
            intent="message",
            message="summarize README.md",
        )
        assert r.get("ok"), r
        fr = r.get("file_read") or {}
        assert fr.get("path") == "README.md", fr
        assert (fr.get("chars") or 0) > 100, fr
        tools = {t["name"]: t for t in (r.get("tools") or [])}
        assert tools.get("read_workspace_file", {}).get("ok") is True, tools
        assert tools.get("pack_gateway_chat", {}).get("file_in_pack") is True, tools

        sys_txt = next(
            (m["content"] for m in _LAST_PACKED if m.get("role") == "system"), ""
        )
        assert "trust:file" in sys_txt, sys_txt[:400]
        assert "Knowledge Work Bench" in sys_txt or "SIH_26117" in sys_txt
        assert "Do not claim you only have task type" in sys_txt
        asst = (r.get("assistant") or {}).get("text") or ""
        assert "grounded" in asst.lower() or "Knowledge Work Bench" in asst, asst
        assert "only see task type" not in asst.lower()

        # Miss path — clear orch message, no hallucinated "wasn't given"
        miss = orch.turn(
            grant_id=r["grant_id"],
            intent="message",
            message="read totally_missing_xyz.md",
        )
        assert miss.get("ok") is True, miss
        miss_tools = {t["name"]: t for t in (miss.get("tools") or [])}
        assert miss_tools.get("read_workspace_file", {}).get("ok") is False
        miss_txt = (miss.get("assistant") or {}).get("text") or ""
        assert "Could not resolve" in miss_txt or "attach" in miss_txt.lower(), miss_txt

        print(
            "SMOKE_ORCH_FILE_READ OK",
            {
                "path": fr.get("path"),
                "chars": fr.get("chars"),
                "sys_chars": len(sys_txt),
                "reply_preview": asst[:120],
            },
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
