"""Grant-first lexical retrieve over fixture packs (G6) — MOCK data, REAL logic.

ACL-before-retrieve (KWB/from_onyx_web): grant scopes filter the corpus *before*
search results surface — authz at retrieve, not “login then all shelves.”
No Onyx fork; we own grants. Fail closed: empty / out-of-grant → NOT FOUND.

Cite-or-abstain pipeline shape (study only — no Haystack/LlamaIndex dependency):
  KWB/from_haystack_web   — DocumentStore → Retriever → PromptBuilder → cite indices
  KWB/from_llamaindex_web — CitationQueryEngine Source N / refuse unhelpful
WP-11 will wire numbered cites; this module only returns grant-filtered hits.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .audit import log_event
from .config import DATA_DIR, KB_DIR, KNOWLEDGE_DIR, ROOT, SOP_DIR, ensure_dirs

FIXTURES = DATA_DIR / "fixtures"


def _rel_label(path: Path) -> str:
    """Stable cite path relative to repo root when possible."""
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        try:
            return str(path.relative_to(DATA_DIR)).replace("\\", "/")
        except ValueError:
            return path.name


def _iter_docs(shelves: list[str]) -> list[tuple[str, str]]:
    ensure_dirs()
    roots: list[Path] = []
    if "fixtures" in shelves:
        roots.append(FIXTURES)
    if "sop" in shelves:
        roots.append(SOP_DIR)
    if "kb" in shelves:
        roots.append(KB_DIR)
    if "knowledge" in shelves:
        roots.append(KNOWLEDGE_DIR)
    docs: list[tuple[str, str]] = []
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.suffix.lower() in {".txt", ".md"} and p.is_file():
                try:
                    docs.append(
                        (
                            _rel_label(p),
                            p.read_text(encoding="utf-8", errors="ignore"),
                        )
                    )
                except OSError:
                    continue
    return docs


def retrieve(query: str, *, shelves: list[str], k: int = 5) -> dict[str, Any]:
    """Grant-scoped term overlap. Cite-or-abstain if empty (no ACL leak)."""
    terms = [t.lower() for t in re.findall(r"[a-zA-Z0-9]{3,}", query or "")]
    scored: list[tuple[int, str, str]] = []
    for path, text in _iter_docs(shelves):
        low = text.lower()
        score = sum(1 for t in terms if t in low)
        if score:
            snippet = text.strip().splitlines()[0][:240] if text.strip() else path
            scored.append((score, path, snippet))
    scored.sort(key=lambda x: (-x[0], x[1]))
    hits = [
        {"path": p, "score": s, "snippet": sn, "label": "Confidential synthetic"}
        for s, p, sn in scored[:k]
    ]
    if not hits:
        log_event("retrieve_not_found", query=query[:200], shelves=shelves)
        return {"ok": True, "cites": [], "verdict": "NOT FOUND", "k": k}
    log_event("retrieve_hits", n=len(hits), shelves=shelves)
    return {"ok": True, "cites": hits, "verdict": "cites", "k": k}
