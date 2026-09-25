"""PowerPoint DRAFT generator — pptx with explicit DRAFT badge (desk path)."""

from __future__ import annotations

import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

from .audit import log_event
from .config import ARTIFACTS_DIR, TEMPLATES_DIR, ensure_dirs

# Cool slate + steel teal (not purple AI-slop)
_SLATE = RGBColor(0x1E, 0x29, 0x3B)
_TEAL = RGBColor(0x0F, 0x76, 0x6E)
_INK = RGBColor(0x0F, 0x17, 0x2A)
_MUTED = RGBColor(0x47, 0x55, 0x69)
_BANNER = RGBColor(0x9F, 0x12, 0x39)


def _set_run(run, *, size: int, bold: bool = False, color: RGBColor = _INK) -> None:
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = "Calibri"


def _fill_shape(shape, color: RGBColor) -> None:
    fill = shape.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_title_slide(prs: Presentation, title: str, subtitle: str) -> None:
    blank = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(blank)
    # Full-bleed slate band
    band = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5)
    )
    _fill_shape(band, _SLATE)
    band.line.fill.background()

    box = slide.shapes.add_textbox(Inches(0.7), Inches(2.0), Inches(11.5), Inches(1.2))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = "Knowledge Work Bench"
    _set_run(run, size=18, bold=True, color=RGBColor(0x5E, 0xEA, 0xD4))

    box2 = slide.shapes.add_textbox(Inches(0.7), Inches(2.7), Inches(11.5), Inches(1.5))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    run2 = p2.add_run()
    run2.text = title or "Briefing DRAFT"
    _set_run(run2, size=36, bold=True, color=RGBColor(0xF8, 0xFA, 0xFC))

    box3 = slide.shapes.add_textbox(Inches(0.7), Inches(4.5), Inches(11.5), Inches(1.2))
    tf3 = box3.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    run3 = p3.add_run()
    run3.text = subtitle
    _set_run(run3, size=14, color=RGBColor(0xCB, 0xD5, 0xE1))

    foot = slide.shapes.add_textbox(Inches(0.7), Inches(6.8), Inches(11.5), Inches(0.4))
    pf = foot.text_frame.paragraphs[0]
    rf = pf.add_run()
    rf.text = "DRAFT — NOT A PLANT RECORD — FOR EXPORT / REVIEW ONLY"
    _set_run(rf, size=11, bold=True, color=RGBColor(0xFE, 0xCD, 0xD3))


def _add_bullets_slide(
    prs: Presentation,
    heading: str,
    bullets: list[str],
    *,
    footer: str = "DRAFT · soft copy · not CERT",
) -> None:
    blank = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank)

    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.12), Inches(7.5)
    )
    _fill_shape(accent, _TEAL)
    accent.line.fill.background()

    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12), Inches(0.7))
    tp = title_box.text_frame.paragraphs[0]
    tr = tp.add_run()
    tr.text = heading
    _set_run(tr, size=26, bold=True, color=_SLATE)

    body = slide.shapes.add_textbox(Inches(0.6), Inches(1.2), Inches(12), Inches(5.2))
    tf = body.text_frame
    tf.word_wrap = True
    items = bullets[:8] or ["(empty)"]
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = 0
        p.space_after = Pt(10)
        run = p.add_run()
        run.text = f"•  {item}"
        _set_run(run, size=16, color=_INK)

    foot = slide.shapes.add_textbox(Inches(0.6), Inches(6.9), Inches(12), Inches(0.35))
    fp = foot.text_frame.paragraphs[0]
    fr = fp.add_run()
    fr.text = footer
    _set_run(fr, size=10, color=_MUTED)


def extract_key_points(text: str, *, max_points: int = 8) -> list[str]:
    """Lightweight README/md/txt extract — headings, bullets, key lines."""
    raw = (text or "").strip()
    if not raw:
        return []
    points: list[str] = []
    seen: set[str] = set()

    def _add(line: str) -> None:
        clean = re.sub(r"^[#*\-\d\.\)\s]+", "", line).strip()
        clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", clean)
        if len(clean) < 8:
            return
        key = clean.lower()
        if key in seen:
            return
        seen.add(key)
        points.append(clean[:220])

    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#") or s.startswith(("-", "*", "•")) or re.match(r"^\d+[\.\)]\s", s):
            _add(s)
        elif ":" in s and len(s) < 160:
            _add(s)
        if len(points) >= max_points:
            break

    if len(points) < 3:
        for para in re.split(r"\n\s*\n", raw):
            one = " ".join(para.split())
            if len(one) > 40:
                _add(one[:220])
            if len(points) >= max_points:
                break
    return points[:max_points]


def build_retrieve_query(extract_text: str, bullets: list[str] | None = None) -> str:
    parts = bullets or extract_key_points(extract_text)
    blob = " ".join(parts) if parts else extract_text
    terms = re.findall(r"[A-Za-z0-9-]{3,}", blob)
    # Prefer distinctive / domain tokens
    prefer = [
        t
        for t in terms
        if t.lower()
        not in {
            "the",
            "and",
            "for",
            "with",
            "from",
            "this",
            "that",
            "confidential",
            "synthetic",
            "demo",
        }
    ]
    return " ".join(prefer[:14]) or "Knowledge Work Bench draft policy"


def write_pptx_draft(
    *,
    title: str,
    findings: str,
    bullets: list[str] | None = None,
    cites: list[str] | None = None,
    match_notes: list[str] | None = None,
    model_id: str | None = None,
    task_id: str | None = None,
    artefact_version: str | None = None,
    template: str = "kwb_brief",
) -> dict[str, Any]:
    """Write a DRAFT .pptx under workspace/artifacts (optionally seeded from template)."""
    ensure_dirs()
    points = [b for b in (bullets or []) if b.strip()]
    if not points:
        points = extract_key_points(findings) or [findings.strip()[:220] or "(empty)"]

    prs: Presentation | None = None
    tpl = TEMPLATES_DIR / f"{template}.pptx"
    if tpl.is_file():
        try:
            prs = Presentation(str(tpl))
            # Drop existing slides by building a fresh deck from template masters
            # python-pptx cannot easily clear; if template has slides, still add ours.
            # Prefer blank generation with brand rules when template is a seed shell.
            if len(prs.slides) > 0:
                prs = None
        except Exception:
            prs = None
    if prs is None:
        prs = Presentation()
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    subtitle = (
        f"DRAFT soft copy · {generated}"
        f" · model {model_id or 'n/a'} · task {task_id or 'n/a'}"
        + (f" · v{artefact_version}" if artefact_version else "")
    )
    _add_title_slide(prs, title or "Integrity briefing (DRAFT)", subtitle)

    agenda = [
        "Confirm extract (human)",
        "Match against company knowledge",
        "Key points from attachment",
        "Company-document citations",
        "Recommended next actions",
    ]
    _add_bullets_slide(prs, "Agenda", agenda)
    _add_bullets_slide(prs, "Extracted key points", points)

    cite_bullets = list(cites or [])[:8]
    if not cite_bullets:
        cite_bullets = ["NOT FOUND — no grounded citations under grant"]
    _add_bullets_slide(prs, "Company document matches", cite_bullets)

    matches = list(match_notes or [])[:6]
    if matches:
        _add_bullets_slide(prs, "Verification notes", matches)

    next_actions = [
        "Self-check this DRAFT before export leave",
        "Treat as soft copy only — not CERT / not a plant record",
        "Fold corrections into findings and regenerate if needed",
    ]
    if findings and findings.strip():
        next_actions.insert(0, findings.strip()[:200])
    _add_bullets_slide(prs, "Next actions", next_actions)

    name = f"draft-{uuid.uuid4().hex[:10]}.pptx"
    path = ARTIFACTS_DIR / name
    prs.save(str(path))
    log_event(
        "pptx_draft",
        path=str(path),
        model_id=model_id,
        task_id=task_id,
        artefact_version=artefact_version,
        template=template,
    )
    return {
        "ok": True,
        "path": str(path),
        "filename": name,
        "status": "DRAFT",
        "artefact_version": artefact_version,
        "format": "pptx",
    }


def extract_pptx_text(path: Path) -> str:
    """Best-effort plain text from pptx for secrets scan on export leave."""
    prs = Presentation(str(path))
    parts: list[str] = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if not hasattr(shape, "text"):
                continue
            t = (shape.text or "").strip()
            if t:
                parts.append(t)
    return "\n".join(parts)


def write_sample_templates() -> dict[str, str]:
    """Create 1–2 seed .pptx shells under workspace/templates/."""
    ensure_dirs()
    out: dict[str, str] = {}

    # Brief template shell (title + agenda placeholders — generator rebuilds content)
    brief = Presentation()
    brief.slide_width = Inches(13.333)
    brief.slide_height = Inches(7.5)
    # Empty shell — generator detects slides and rebuilds; keep zero slides for clean seed
    brief_path = TEMPLATES_DIR / "kwb_brief.pptx"
    brief.save(str(brief_path))
    out["kwb_brief"] = str(brief_path)

    findings = Presentation()
    findings.slide_width = Inches(13.333)
    findings.slide_height = Inches(7.5)
    findings_path = TEMPLATES_DIR / "inspection_findings.pptx"
    findings.save(str(findings_path))
    out["inspection_findings"] = str(findings_path)

    # Also write a filled sample for visual demo of brand
    sample = Presentation()
    sample.slide_width = Inches(13.333)
    sample.slide_height = Inches(7.5)
    _add_title_slide(
        sample,
        "Inspection findings (sample template)",
        "Confidential synthetic · Knowledge Work Bench brand shell",
    )
    _add_bullets_slide(
        sample,
        "Sample agenda",
        [
            "Scope and asset",
            "Measurements vs SOP",
            "Company knowledge cites",
            "Recommended follow-up",
        ],
    )
    _add_bullets_slide(
        sample,
        "Sample findings",
        [
            "V-101 shell course A measured 7.6 mm",
            "SOP-THK-001 minimum 8.0 mm",
            "Recommend reduced inspection interval",
        ],
    )
    sample_path = TEMPLATES_DIR / "inspection_findings_sample.pptx"
    sample.save(str(sample_path))
    out["inspection_findings_sample"] = str(sample_path)

    log_event("pptx_templates_written", **{k: Path(v).name for k, v in out.items()})
    return out
