# DALL·E prompt — Slide 2 Context diagram (bottom band)

**Generate canvas:** **960×420**  
**Composition:** empty white top · diagram in lower band · **no headers in the image**  
**Mirrored in:** `S02_PROPOSED.md`

Copy everything below the line into the image model.

---

```
Create a flat technical architecture CONTEXT DIAGRAM for a Smart India Hackathon idea slide.

CANVAS (mandatory):
- Exact size: 960 × 420 pixels
- White background (#FFFFFF) everywhere
- CRITICAL COMPOSITION: Leave the TOP ~220 pixels EMPTY (plain white, no boxes, no title, no logos, no “Context Diagram” header, no decoration).
- Draw ALL diagram content ONLY in the BOTTOM ~200 pixels as a single shallow horizontal band.

STYLE:
- Industrial systems engineering diagram (not marketing poster)
- Flat 2D boxes only — no shadows, no 3D, no neon, no purple gradients
- No robots, no brains, no cloud vendor logos, no stock “AI” clichés
- Navy borders #1F497D · light steel fills #E8EEF5 · blue arrows #0070C0
- Dashed red #C0504D for blocked public internet
- Sans-serif labels, short, readable when shrunk

LAYOUT — four equal-height lanes left → right INSIDE THE BOTTOM BAND ONLY (across 960 width):

LANE 1 — PEOPLE:
- Box "Worker" — assists desk · exports DRAFT
- Box "Admin (IT)" — stages USB · enables Model Cards

LANE 2 — KWB (premises):
- Box "Desk" → Box "Core / Orch"
- Box "Model Cards"
- Box "DRAFT Word export" (visually emphasized)
- Small badge "Monitor A ≠ CERT"

LANE 3 — INFERENCE:
- Box "Gateway" (label: only inference path)
- Box "Runtime /v1" (open-weight models)

LANE 4 — BOUNDARY:
- Box "Plant systems" with note "read-only"
- Box "Public internet" with red dashed style and label "BLOCKED"

ARROWS (bottom band only):
- Worker ↔ Desk
- Worker → DRAFT Word export
- Admin → Model Cards (enable)
- USB pack → Stage/quarantine → Admin
- Core → Gateway → Runtime
- Model Cards → Runtime (allowed weights)
- Core dotted to Plant read-only
- No arrows from KWB / Gateway / Runtime to Public internet

CAPTION STRIP (bottom of canvas, small grey text, exact wording):
"Worker exports DRAFT · Admin stages offline packs · Gateway only · Monitor A ≠ CERT · Plant read-only · Public net blocked"

No watermark. No title bar. No header text anywhere in the image.
```

---

## Designer check

- [ ] **960×420**  
- [ ] Empty white top · no headers  
- [ ] Boxes only in lower band  
- [ ] “Monitor A ≠ CERT” readable  
- [ ] Public net **BLOCKED**  
