# Slide 2 — image generation prompt (960×420)

**Slide 2 status:** FIXED / LOCKED 2026-09-21 — stop regenerating unless user reopens.  
**Next:** Slide 3 → `S03_TECHNICAL.md`  

**Architecture diagram:** keep for **Technical Approach (Slide 3)** — not on this slide.  
**This slide:** no bottom diagram (Detailed already shows organisation design).

Copy below the line into the image model.

---

```
Create one flat presentation content panel. Exact size: 960 × 420 pixels. White #FFFFFF. No 3D, no neon, no purple, no robots, no SIH chrome, no watermarks. No architecture / context diagram anywhere on this panel.

VERTICAL LAYOUT (only two content rows — use full height):
- Row 1 (~230 px): Proposed Solution (LEFT) + Detailed explanation (RIGHT)
- Row 2 (~190 px): TWO TABLES SIDE BY SIDE
- Bottom title bars MUST be single-line text (never wrap titles onto two lines)
- NO bottom diagram band. NO gateway/runtime/plant drawing.

TITLE BARS (critical):
- All four section titles are ONE continuous line each. Do not break mid-title.
- Left-bottom title EXACT single line: How it addresses the problem
- Right-bottom title EXACT single line: Innovation and uniqueness of the solution
- If needed, use slightly smaller title font so the full phrase fits on one line inside the navy bar.

════════════════════════════════
ROW 1 LEFT — Proposed Solution
Navy title bar, white text: Proposed Solution
Six bullets EXACT:
• Knowledge Work Bench (KWB) is a self-hosted industrial knowledge workbench that assists confidential desk work entirely on company premises
• It keeps sensitive plant and business knowledge inside the organisation so staff need not paste into public AI tools
• It helps workers verify material against local SOPs and manuals, then drafts clear insight for the next step in their workflow
• It raises productivity by turning slow manual assemble-and-type work into assisted soft-copy DRAFT Word leave packs
• It supports multiple open-weight models on the organisation GPU and routes inspection vs coding tasks to the right model without data leaving premises
• Humans remain the decision makers; the app never writes plant control or ERP systems; Approver stays outside

ROW 1 RIGHT — Detailed explanation of the proposed solution
Navy title bar, white text: Detailed explanation of the proposed solution
Four organisation lanes left→right (design view, not build checklist):
People: Worker — assists and exports drafts · Admin (IT) — stages offline model packs / enables cards
Workbench (organisation): Task desk · Grants & policy · Local knowledge retrieve (SOPs / manuals) · Draft Office deliverables (Word leave pack) · Audit trail
Inference (organisation): Gateway is the only path · Open-weight models on organisation GPU runtime
Safety boundary: Plant systems read-only · Public internet blocked · Solution ends at export leave
Caption EXACT: Same logical design from a mid-range demo GPU to full organisation GPU server — scale cards and connectors, do not redesign the product.

════════════════════════════════
ROW 2 — SIDE BY SIDE TABLES (full width; fill cells, little empty space)

LEFT — navy title bar, white text EXACT on ONE LINE (never two lines): How it addresses the problem
Columns: Problem in the PS | How our solution addresses it
4 rows EXACT (map official Background / Description / Expected Solution):
Sensitive knowledge work cannot use cloud assistants (Claude / Codex class) because data must stay on premises | KWB runs self-hosted on the organisation network/GPU so confidential desk work never needs public AI
Staff today either work manually (slow) or quietly paste secrets into public tools | KWB assists on premises: verify against local SOPs/manuals and produce DRAFT Word leave packs so work is faster without leaving the fence
No deployable open-weight workbench yet that industrial users can use like Claude / Codex | KWB is that desk: agentic multi-step assist, multimodal scans/notes, real soft-copy deliverables — not chat-only
Organisation must run many confidential desk tasks (notes, calcs, code assist, scan/drawing review) under one on-prem policy | KWB is one workbench for those organisation tasks: task-routed open-weight models, company-SOP retrieve with cite/NOT FOUND, sandbox-verified calc/code, soft-copy leave packs — inference stays Gateway-only inside the organisation boundary

RIGHT — navy title bar, white text EXACT on ONE LINE (never two lines): Innovation and uniqueness of the solution
Columns: Instead of | We propose
3 rows EXACT:
Manual-only confidential desk work | On-prem assisted draft, SOP verify, and Word leave pack
Public GenAI for plant / PSU documents | Same class of help with data kept on premises
Bare local chat around one model | Full industrial workbench: task-routed models, deliverables, human gates, Approver outside

Style: #E8EEF5 fills, #1F497D borders/titles, #0070C0 accents. Dense readable text. No INSERT. No size callouts in the image. No architecture diagram.
```
