"""Generate harder OCR/PDF fixtures for outsider E2E (noisy image + multi-page PDF)."""
from __future__ import annotations

import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "fixtures"

NOISY_LINES = [
    "Confidential synthetic — SIH26 complex OCR",
    "Job: INSP-2026-0918  Plant: Demo Unit 3",
    "Asset TAG: V-101  Shell course: A",
    "UT reading: 7.6 mm  (SOP-THK-001 min 8.0 mm)",
    "Location: N quadrant ~1.2 m above grade",
    "Finding: pit / weld toe indication",
    "Action: reduce inspection interval",
]

PDF_PAGES = [
    [
        "Confidential synthetic — vessel note page 1/2",
        "Inspection note (DRAFT source)",
        "Asset: V-101 shell course A",
        "Measured thickness: 7.6 mm",
        "SOP-THK-001 minimum allowable: 8.0 mm",
        "Location: North quadrant, 1.2 m above grade",
        "Raw notes: Pit indication near weld toe.",
    ],
    [
        "Confidential synthetic — vessel note page 2/2",
        "Compare against prior UT campaign (stub).",
        "Cite SOP-THK-001 only — do not invent limits.",
        "Recommend reduced inspection interval.",
        "Operator: demo · not a plant record until Approver.",
        "Export leave after H2 self-HITL on Word DRAFT.",
    ],
]


def write_noisy_png() -> Path:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont

    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(42)
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), color=(235, 228, 210))
    draw = ImageDraw.Draw(img)
    for _ in range(4000):
        x, y = rng.randint(0, w - 1), rng.randint(0, h - 1)
        c = 180 + rng.randint(0, 50)
        draw.point((x, y), fill=(c, c - 8, c - 20))
    try:
        font = ImageFont.truetype("arial.ttf", 26)
        font_sm = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()
        font_sm = font
    y = 50
    for i, line in enumerate(NOISY_LINES):
        x = 48 + int(6 * math.sin(i * 0.7))
        draw.text((x, y), line, fill=(28, 26, 22), font=font if i == 0 else font_sm)
        y += 70 if i == 0 else 58
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    path = OUT / "scan_vessel_V101_noisy.png"
    img.save(path, optimize=True)
    return path


def _escape_pdf_text(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _page_stream(lines: list[str]) -> bytes:
    cmds = ["BT /F1 11 Tf 50 750 Td"]
    for i, line in enumerate(lines):
        if i:
            cmds.append("0 -18 Td")
        cmds.append(f"({_escape_pdf_text(line)}) Tj")
    cmds.append("ET")
    return " ".join(cmds).encode("latin-1", errors="replace")


def write_multipage_pdf() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "vessel_note_multipage.pdf"
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(str(path), pagesize=letter)
        for page in PDF_PAGES:
            c.setFont("Helvetica", 12)
            y = 720
            for line in page:
                c.drawString(50, y, line)
                y -= 22
            c.showPage()
        c.save()
        return path
    except ImportError:
        pass

    streams = [_page_stream(p) for p in PDF_PAGES]
    objs: list[bytes] = []
    objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objs.append(b"")  # pages placeholder
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    content_ids: list[int] = []
    for st in streams:
        content_ids.append(len(objs) + 1)
        objs.append(f"<< /Length {len(st)} >>\nstream\n".encode() + st + b"\nendstream")
    page_ids: list[int] = []
    for cid in content_ids:
        page_ids.append(len(objs) + 1)
        objs.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents {cid} 0 R "
            f"/Resources << /Font << /F1 3 0 R >> >> >>".encode()
        )
    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    objs[1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode()

    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objs, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"
    xref_at = len(out)
    out += f"xref\n0 {len(objs) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for off in offsets[1:]:
        out += f"{off:010d} 00000 n \n".encode()
    out += (
        f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_at}\n%%EOF\n"
    ).encode()
    path.write_bytes(bytes(out))
    return path


def main() -> None:
    print("WROTE", write_noisy_png())
    print("WROTE", write_multipage_pdf())


if __name__ == "__main__":
    main()
