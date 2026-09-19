"""Word DRAFT generator — docx with explicit DRAFT badge (G2)."""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor

from .audit import log_event
from .config import ARTIFACTS_DIR, ensure_dirs


def write_inspection_draft(
    *,
    title: str,
    findings: str,
    cites: list[str] | None = None,
    model_id: str | None = None,
    task_id: str | None = None,
    artefact_version: str | None = None,
) -> dict:
    ensure_dirs()
    doc = Document()
    banner = doc.add_paragraph()
    run = banner.add_run("DRAFT — NOT A PLANT RECORD — FOR EXPORT / REVIEW ONLY")
    run.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0xB0, 0x00, 0x20)

    doc.add_heading(title or "Inspection note", level=1)
    meta = doc.add_paragraph()
    meta.add_run(
        f"Generated: {datetime.now(timezone.utc).isoformat()}  |  "
        f"model_id: {model_id or 'n/a'}  |  task: {task_id or 'n/a'}"
    )
    if artefact_version:
        meta.add_run(f"  |  artefact_version: {artefact_version}")

    doc.add_heading("Findings", level=2)
    doc.add_paragraph(findings or "(empty)")

    doc.add_heading("Citations", level=2)
    if cites:
        for c in cites:
            doc.add_paragraph(c, style="List Bullet")
    else:
        doc.add_paragraph("NOT FOUND — no grounded citations")

    doc.add_paragraph()
    foot = doc.add_paragraph()
    foot.add_run(
        "Status: DRAFT. KWB assists in the workbench; export leave ends the solution path. "
        "No in-app accept-for-forward. Not a plant record."
    ).italic = True

    name = f"draft-{uuid.uuid4().hex[:10]}.docx"
    path = ARTIFACTS_DIR / name
    doc.save(str(path))
    log_event(
        "word_draft",
        path=str(path),
        model_id=model_id,
        task_id=task_id,
        artefact_version=artefact_version,
    )
    return {
        "ok": True,
        "path": str(path),
        "filename": name,
        "status": "DRAFT",
        "artefact_version": artefact_version,
    }


def extract_docx_text(path: Path) -> str:
    """Best-effort plain text from docx for secrets scan on export leave."""
    doc = Document(str(path))
    parts: list[str] = []
    for p in doc.paragraphs:
        if p.text:
            parts.append(p.text)
    return "\n".join(parts)
