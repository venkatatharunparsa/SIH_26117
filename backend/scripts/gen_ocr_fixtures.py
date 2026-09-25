"""Generate demo OCR fixtures: scan PNG + text-layer PDF under data/fixtures/."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "fixtures"

LINES = [
    "Confidential synthetic — SIH26 OCR fixture",
    "Asset: V-101 shell course A",
    "Location: North quadrant, 1.2 m above grade",
    "Measured thickness: 7.6 mm",
    "SOP-THK-001 minimum: 8.0 mm",
    "Notes: Pit indication near weld toe.",
    "Recommend reduced inspection interval.",
]


def write_png() -> Path:
    from PIL import Image, ImageDraw, ImageFont

    OUT.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (900, 520), color=(248, 246, 240))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 28)
        font_sm = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
        font_sm = font
    y = 40
    for i, line in enumerate(LINES):
        draw.text((40, y), line, fill=(20, 24, 32), font=font if i == 0 else font_sm)
        y += 58 if i == 0 else 52
    path = OUT / "scan_vessel_V101.png"
    img.save(path)
    return path


def write_pdf() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "vessel_note_text.pdf"
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(str(path), pagesize=letter)
        c.setFont("Helvetica", 12)
        y = 720
        for line in LINES:
            c.drawString(50, y, line)
            y -= 22
        c.save()
        return path
    except ImportError:
        pass

    # Minimal PDF 1.4 with Helvetica text operators (no reportlab)
    stream = (
        b"BT /F1 12 Tf 50 750 Td "
        b"(Confidential synthetic SIH26 vessel note) Tj "
        b"0 -20 Td (Asset: V-101 shell course A) Tj "
        b"0 -18 Td (Location: North quadrant 1.2 m above grade) Tj "
        b"0 -18 Td (Measured thickness: 7.6 mm) Tj "
        b"0 -18 Td (SOP-THK-001 minimum: 8.0 mm) Tj "
        b"0 -18 Td (Notes: Pit indication near weld toe.) Tj "
        b"ET"
    )
    parts: list[bytes] = [b"%PDF-1.4\n"]
    body = b""
    offsets = [0]

    def obj(n: int, data: bytes) -> None:
        nonlocal body
        offsets.append(len(parts[0]) + len(body))
        body += f"{n} 0 obj\n".encode() + data + b"\nendobj\n"

    obj(1, b"<< /Type /Catalog /Pages 2 0 R >>")
    obj(2, b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    obj(
        3,
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Contents 5 0 R /Resources << /Font << /F1 4 0 R >> >> >>",
    )
    obj(4, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    obj(5, f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")
    xref_pos = len(parts[0]) + len(body)
    xref = f"xref\n0 {len(offsets)}\n0000000000 65535 f \n".encode()
    for off in offsets[1:]:
        xref += f"{off:010d} 00000 n \n".encode()
    trailer = (
        f"trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\n"
        f"startxref\n{xref_pos}\n%%EOF\n"
    ).encode()
    path.write_bytes(parts[0] + body + xref + trailer)
    return path


def main() -> int:
    png = write_png()
    pdf = write_pdf()
    print("WROTE", png, png.stat().st_size)
    print("WROTE", pdf, pdf.stat().st_size)
    from pypdf import PdfReader

    text = "".join((p.extract_text() or "") for p in PdfReader(str(pdf)).pages)
    print("PDF_TEXT_CHARS", len(text.strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
