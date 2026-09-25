"""Build denser field-form PDF + stamped scan for multi-task tests (Confidential synthetic)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "fixtures"

FORM_PAGES = [
    [
        "Confidential synthetic — FIELD INSPECTION FORM (page 1/3)",
        "Plant / Unit: Demo Hydrocracker · Area: North bank",
        "Work order (stub): WO-2026-4417",
        "Asset tag: V-101",
        "Equipment description: Vertical pressure vessel · shell course A",
        "Inspection type: UT thickness survey (spot)",
        "Date (synthetic): 2026-09-18",
        "Inspector (synthetic): Demo Inspector / Contractor Co.",
        "Measured thickness: 7.6 mm",
        "Instrument (stub): UT gauge demo-unit",
        "Location on asset: North quadrant, 1.2 m above grade, near weld toe",
    ],
    [
        "Confidential synthetic — FIELD INSPECTION FORM (page 2/3)",
        "Governing procedure: SOP-THK-001 (local KB excerpt)",
        "SOP-THK-001 minimum allowable thickness: 8.0 mm",
        "Finding class (stub): Below minimum — engineering review required",
        "Observation: Localized pit indication adjacent to circumferential weld toe.",
        "No leakage observed at time of survey (synthetic).",
        "Photos attached: scan_vessel_V101_field.png (synthetic raster)",
        "Recommended interim action: Reduce inspection interval pending integrity review.",
        "Do not treat this PDF as a plant SoR or CERT record.",
    ],
    [
        "Confidential synthetic — FIELD INSPECTION FORM (page 3/3)",
        "Cite-or-abstain rule: only quote SOP-THK-001 values present in local KB.",
        "Next step for Knowledge Work Bench demo: Confirm extract → retrieve cites → Word DRAFT.",
        "Export leave pack is soft copy for Approver OUTSIDE the application.",
        "Gateway must not call public cloud models.",
        "End of form.",
    ],
]


def _escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _page_stream(lines: list[str]) -> bytes:
    cmds = ["BT /F1 11 Tf 50 750 Td"]
    for i, line in enumerate(lines):
        if i:
            cmds.append("0 -18 Td")
        cmds.append(f"({_escape(line[:100])}) Tj")
    cmds.append("ET")
    return " ".join(cmds).encode("latin-1", errors="replace")


def write_field_pdf() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "field_inspection_form_V101.pdf"
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(str(path), pagesize=letter)
        for page in FORM_PAGES:
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, 740, page[0][:90])
            c.setFont("Helvetica", 11)
            y = 710
            for line in page[1:]:
                c.drawString(50, y, line[:95])
                y -= 20
            c.showPage()
        c.save()
        return path
    except ImportError:
        pass

    streams = [_page_stream(p) for p in FORM_PAGES]
    objs: list[bytes] = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
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


def write_field_png() -> Path:
    from PIL import Image, ImageDraw, ImageFont

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "scan_vessel_V101_field.png"
    img = Image.new("RGB", (1200, 800), color=(242, 236, 220))
    draw = ImageDraw.Draw(img)
    draw.rectangle([30, 30, 1170, 770], outline=(40, 40, 40), width=3)
    draw.rectangle([40, 40, 1160, 760], outline=(120, 90, 60), width=1)
    try:
        font = ImageFont.truetype("arial.ttf", 28)
        font_sm = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
        font_sm = font
    lines = [
        "FIELD SCAN — Confidential synthetic",
        "Asset TAG: V-101  |  Shell course A",
        "UT: 7.6 mm   SOP-THK-001 min: 8.0 mm",
        "Loc: N quadrant · 1.2 m AG · weld toe",
        "WO-2026-4417  ·  Demo Inspector",
        "NOT a plant record · SIH26 demo raster",
    ]
    y = 80
    for i, line in enumerate(lines):
        draw.text((70, y), line, fill=(20, 20, 20), font=font if i == 0 else font_sm)
        y += 70 if i == 0 else 55
    draw.polygon([(900, 120), (1120, 160), (1100, 220), (880, 180)], outline=(160, 30, 30))
    draw.text((920, 155), "SYNTH", fill=(160, 30, 30), font=font_sm)
    img.save(path, optimize=True)
    return path


def main() -> None:
    print("WROTE", write_field_pdf())
    print("WROTE", write_field_png())


if __name__ == "__main__":
    main()
