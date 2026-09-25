# Slide 2 — LOCK + rebuild plan (updated)

**Canvas:** 960 × 420  

---

## LOCKED

### Proposed Solution (6 bullets)

1. Knowledge Work Bench (KWB) is a self-hosted industrial knowledge workbench that assists confidential desk work entirely on company premises.  
2. It keeps sensitive plant and business knowledge inside the organisation so staff need not paste into public AI tools.  
3. It helps workers verify material against local SOPs and manuals, then drafts clear insight for the next step in their workflow.  
4. It raises productivity by turning slow manual assemble-and-type work into assisted soft-copy DRAFT Word leave packs.  
5. **NEW:** It supports multiple open-weight models on the organisation GPU and routes inspection vs coding tasks to the right model without data leaving premises.  
6. Humans remain the decision makers; the app never writes plant control or ERP systems; Approver stays outside.

### Detailed explanation — organisation lanes (unchanged)

People · Workbench · Inference · Safety boundary + demo→org caption.

---

## LAYOUT (current)

| Row | Content |
|---|---|
| 1 | Proposed (6 bullets) + Detailed (org lanes) |
| 2 | **Addresses ‖ Innovation side by side** — titles **one line each** · PS-mapped addresses |
| — | **No bottom diagram** (architecture → Slide 3 Technical Approach) |

## Architecture diagram

Keep for **Technical Approach** only. Removed from Slide 2 because Detailed already shows organisation design.

## How it addresses (PS-mapped)

1. Cloud AI blocked for confidential work → self-hosted on-prem KWB  
2. Manual slow / shadow paste → on-prem assist + SOP verify + DRAFT Word leave  
3. Nothing Claude/Codex-like on open-weight for industry → agentic multimodal deliverable desk  
4. Expected Solution (≥2 tasks, sandbox, zero external calls) → route models · sandbox · Gateway-only · public net blocked  

## Prompt file

`S02_PROPOSED.md` — **FIXED**. Do not change unless reopened.

## Next slide

`S03_TECHNICAL.md` — Technical Approach @ **960×420** (architecture diagram lives here).
