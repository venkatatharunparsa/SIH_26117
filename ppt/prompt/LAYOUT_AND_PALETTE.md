# LAYOUT + PALETTE — for ChatGPT text layout & DALL·E images

Use this in every image prompt and when asking ChatGPT to “layout the slide.”

---

## Official template constraints

- Exactly **6 slides** including title.  
- Pointers **must not be renamed**: Title · Proposed Solution · Technical Approach · Feasibility and Viability · Impact and Benefits · Research and References.  
- Stay inside the white content rectangle of the official SIH template.  
- Density: **bullets, tables, diagrams** — not paragraphs.  
- PDF must **stand alone** (video may never be clicked).

---

## Page geometry (all idea slides)

```
TOP ~8%: official chrome / slide title (template)
CONTENT:
  Words / tables: top 55–65%
  Primary visual: bottom 30–40% (full width band preferred)
FOOT: 1-line caption under diagram (optional)
```

Slide 1: centered title block only (no diagram).  
Slide 2: words top · **context band** bottom (`DALLE_S02_CONTEXT.md` · gen **920×420** empty-top → crop **~920×200**).  
Slide 3: Layer table or short stack top · **component strip** bottom (`DALLE_S03_COMPONENTS.md`).  
Slide 4–6: tables dominate; small icons OK, no second architecture diagram.

---

## Color system (industrial — not purple SaaS)

| Token | Hex | Use |
|---|---|---|
| Navy | `#1F497D` | Box borders · titles |
| Steel | `#E8EEF5` | Box fill |
| Accent blue | `#0070C0` | Primary arrows |
| Warn red | `#C0504D` | Blocked internet (dashed) |
| Ok green | `#2E7D4F` | Tick / REAL |
| Ink | `#1A1A1A` | Body text |
| Mute | `#5A6570` | Captions |

**Avoid:** purple gradients, neon glow, cartoon robots, stock “AI brain” clichés.

---

## Typography (when ChatGPT suggests)

- Titles: bold sans, short.  
- Body: 9–12 pt equivalent bullets.  
- Diagram labels: 9–11 pt · max 2 lines per box.  
- Prefer IBM Plex / Calibri / Segoe — industrial, not display serif.

---

## Diagram export sizes

| Diagram | Target PNG |
|---|---|
| S2 Context band | Generate **920×420** (empty top) → **crop bottom ~920×200** for slide |
| S3 Component strip | Generate **920×420** (empty top) → **crop bottom ~920×200** · see `DALLE_S03` |

Transparent or white background. No drop shadows. Flat boxes + arrows.
