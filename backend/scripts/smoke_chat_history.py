"""In-process smoke: workbench chat history window=10 + attach does not wipe.

Does not require a live Ollama — gateway is stubbed.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from app import orchestrator as orch  # noqa: E402


def _fake_gw(messages: list[dict[str, str]], **_kwargs: Any) -> dict[str, Any]:
    # Echo last user content so we can assert packing included prior turns
    user_bits = [m["content"] for m in messages if m.get("role") == "user"]
    prior = " | ".join(user_bits[:-1]) if len(user_bits) > 1 else ""
    reply = f"ack:{user_bits[-1][:40]}" + (f" (saw:{prior[:80]})" if prior else "")
    return {
        "ok": True,
        "status": 200,
        "model": "stub",
        "body": {"choices": [{"message": {"role": "assistant", "content": reply}}]},
    }


def main() -> int:
    assert orch.CHAT_HISTORY_WINDOW == 10, orch.CHAT_HISTORY_WINDOW
    assert orch.DEFAULT_ORG_ID == "kwb-workbench"

    with mock.patch.object(orch.gateway, "chat_completions", side_effect=_fake_gw):
        r1 = orch.turn(
            task_type="inspection",
            user_id="smoke-hist",
            intent="message",
            message="hi",
            messages=[{"role": "user", "content": "hi"}],
        )
        assert r1.get("ok"), r1
        gid = r1["grant_id"]
        assert r1.get("context_key") == f"{orch.DEFAULT_ORG_ID}/{gid}"
        assert r1.get("history_window") == 10
        assert r1.get("history_len") == 2, r1.get("history_len")
        packed = r1.get("packed_preview") or []
        assert packed and packed[0]["role"] == "system"
        assert any(p["role"] == "user" for p in packed)

        r2 = orch.turn(
            grant_id=gid,
            intent="message",
            message="What did I just say?",
            messages=[
                {"role": "user", "content": "hi"},
                {"role": "assistant", "content": "hello"},
                {"role": "user", "content": "What did I just say?"},
            ],
        )
        assert r2.get("ok"), r2
        asst = (r2.get("assistant") or {}).get("text") or ""
        assert "saw:" in asst and "hi" in asst, asst
        assert r2["history_len"] == 4

        # Fill past window — store must cap at 10
        for i in range(8):
            orch.turn(
                grant_id=gid,
                intent="message",
                message=f"ping-{i}",
            )
        st = orch._get_state(gid)
        assert st is not None
        assert len(st.chat_history) == 10, len(st.chat_history)
        assert st.org_id == orch.DEFAULT_ORG_ID

        # Attach must append, not wipe
        before = list(st.chat_history)
        att = orch.turn(
            grant_id=gid,
            intent="attach",
            attach_text="Asset V-101 thickness 7.6 mm below 8.0 mm SOP.",
            attach_filename="note.md",
        )
        assert att.get("ok") is not False, att
        st2 = orch._get_state(gid)
        assert st2 is not None
        assert len(st2.chat_history) == 10
        # Prior chat content still present somewhere in window OR replaced by rolling —
        # critical: history_len stays ≤10 and attach user line is present
        roles = [m["role"] for m in st2.chat_history]
        assert "user" in roles and "assistant" in roles
        assert any("[attach]" in m["content"] for m in st2.chat_history)
        assert before  # had prior context; attach did not clear to empty
        print("SMOKE_CHAT_HISTORY OK", {
            "context_key": st2.context_key,
            "window": orch.CHAT_HISTORY_WINDOW,
            "history_len": len(st2.chat_history),
            "attach_history_len": att.get("history_len"),
        })
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
