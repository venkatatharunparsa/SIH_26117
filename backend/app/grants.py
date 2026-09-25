"""Task grants — time-bounded shelf / tool ceiling; revoke-before-tool (G7)."""

from __future__ import annotations

import sqlite3
import threading
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .audit import log_event
from .config import WORKSPACE_DIR, ensure_dirs

_lock = threading.Lock()
_DB = WORKSPACE_DIR / "grants.sqlite3"


def _conn() -> sqlite3.Connection:
    ensure_dirs()
    c = sqlite3.connect(str(_DB), check_same_thread=False)
    c.row_factory = sqlite3.Row
    return c


def init_db() -> None:
    with _lock:
        c = _conn()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS grants (
              id TEXT PRIMARY KEY,
              task_id TEXT NOT NULL,
              user_id TEXT NOT NULL,
              shelves TEXT NOT NULL,
              tools TEXT NOT NULL,
              model_card TEXT,
              status TEXT NOT NULL,
              created_at TEXT NOT NULL,
              revoked_at TEXT
            )
            """
        )
        c.commit()
        c.close()


@dataclass
class Grant:
    id: str
    task_id: str
    user_id: str
    shelves: list[str]
    tools: list[str]
    model_card: str | None
    status: str

    @property
    def active(self) -> bool:
        return self.status == "open"


def open_grant(
    *,
    task_id: str,
    user_id: str = "demo-operator",
    shelves: list[str] | None = None,
    tools: list[str] | None = None,
    model_card: str | None = None,
) -> Grant:
    init_db()
    gid = uuid.uuid4().hex[:16]
    shelves = shelves or ["fixtures", "sop", "knowledge", "kb"]
    tools = tools or ["retrieve", "gateway", "sandbox", "word"]
    now = datetime.now(timezone.utc).isoformat()
    with _lock:
        c = _conn()
        c.execute(
            "INSERT INTO grants VALUES (?,?,?,?,?,?,?,?,?)",
            (
                gid,
                task_id,
                user_id,
                ",".join(shelves),
                ",".join(tools),
                model_card,
                "open",
                now,
                None,
            ),
        )
        c.commit()
        c.close()
    g = Grant(gid, task_id, user_id, shelves, tools, model_card, "open")
    log_event("grant_open", grant_id=gid, task_id=task_id, shelves=shelves, tools=tools)
    return g


def revoke(grant_id: str) -> bool:
    init_db()
    now = datetime.now(timezone.utc).isoformat()
    with _lock:
        c = _conn()
        cur = c.execute(
            "UPDATE grants SET status='revoked', revoked_at=? WHERE id=? AND status='open'",
            (now, grant_id),
        )
        c.commit()
        n = cur.rowcount
        c.close()
    if n:
        log_event("grant_revoke", grant_id=grant_id)
    return n > 0


def get(grant_id: str) -> Grant | None:
    init_db()
    with _lock:
        c = _conn()
        row = c.execute("SELECT * FROM grants WHERE id=?", (grant_id,)).fetchone()
        c.close()
    if not row:
        return None
    return Grant(
        id=row["id"],
        task_id=row["task_id"],
        user_id=row["user_id"],
        shelves=row["shelves"].split(",") if row["shelves"] else [],
        tools=row["tools"].split(",") if row["tools"] else [],
        model_card=row["model_card"],
        status=row["status"],
    )


def require_active(grant_id: str, tool: str) -> dict[str, Any] | None:
    """Return error dict if grant missing, revoked, or tool not allowed."""
    g = get(grant_id)
    if g is None:
        return {"ok": False, "error": "grant_not_found", "grant_id": grant_id}
    if not g.active:
        log_event("grant_deny", grant_id=grant_id, tool=tool, reason="revoked")
        return {"ok": False, "error": "grant_revoked", "grant_id": grant_id}
    if tool not in g.tools:
        log_event("grant_deny", grant_id=grant_id, tool=tool, reason="tool_ceiling")
        return {"ok": False, "error": "tool_not_allowed", "tool": tool, "grant_id": grant_id}
    return None
