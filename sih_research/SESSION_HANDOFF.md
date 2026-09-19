# SIH26 Session Handoff (Mem0 mirror)

**Mem0 user_id:** `cursor-local`  
**Search first in new chat:** `SIH26 SESSION BOOTSTRAP`

## Role
Assistant = Principal Solutions Architect + Principal Harness Engineer + Principal Research Engineer.  
User = decision maker.

## Project
SIH26117 — Sovereign On-Premise Agentic AI Workbench (MRPL).  
Workspace: `C:\Users\THARUN PARSA\Documents\SIH26`

## Phase
Research complete. Logical architecture **v1 locked** (`ARCHITECTURE_LOGICAL_v1.md`).  
**Org→prototype design locked and red-team-patched** (`DESIGN_ORG_PROTOTYPE_v1.md` §10). Target = **official SIH portal PDF + portal-level prototype**. No college-round work. Stack still **not** locked. **No build** until user asks.

## Binding MVP (Expected Solution)
1. Mid-GPU / small models OK  
2. Multi-model auto-select ≥2 tasks  
3. Inspection scan → Word approval note (agentic)  
4. Sandbox coding verified  
5. Multimodal OCR/vision  
6. Visible zero-egress proof  

## Demo topology (hardware FACT)
- Runtime: RTX **4060 8 GB** (Laptop A)  
- Workbench: RTX **3050 6 GB** (Laptop B, UI; GPU unused for LLM)  
- Sequential 7B-class only; both Windows; Docker `--network=none` for **code** only.

## Key docs
- `sih_research/SYNTHESIS_v1_adversarial.md`
- `sih_research/JUDGING_CRITERIA_INTAKE.md`
- `sih_research/ADVERSARIAL_READINESS_CHECK.md`
- `sih_research/sovereign-ai-workbench-kb/`
- `sih_research/judging_sources/SIH2026_Guidelines.pdf`
- `sih_research/ARCHITECTURE_LOGICAL_v1.md`
- `sih_research/DESIGN_ORG_PROTOTYPE_v1.md`
- `sih_research/DESIGN_REDTEAM_SKILLS_JUDGING_v1.md`
- `sih_research/IDEA_AND_HARDWARE_LOCK_v1.md`

- `sih_research/PLAYBOOK_KEEP_DROP_v1.md`
- `sih_research/judging_sources/SIH_SOFTWARE_PLAYBOOK.md`

- `sih_research/judging_sources/SIH2026-IDEA-Presentation-Format.pptx`
- `sih_research/judging_sources/SIH2026_TEMPLATE_EXTRACT.md`
- `sih_research/PPT_FILL_PACK_v2.md`  ← content source
- `sih_research/chatgpt_slide_prompts/CHATGPT_6SLIDE_IMAGE_SPEC.md`  ← ChatGPT PNG grid + 6 prompts
- `sih_research/chatgpt_slide_prompts/PROMPT_S2.txt` … `PROMPT_S6.txt` + `LAYOUT_S2.png` … `LAYOUT_S6.png`
- `sih_research/PPT_FILL_KIT.md`  (v1 generic — superseded)
- `sih_research/PPT_FILL_SPEC_v1.md`

## Pending from user
Fill official PPTX from PACK v2. Decide: product name, KPI A vs B, whether IndiaAI ₹ goes on slide 6. Placeholders OK until portal strings exist. Share draft for red-team. Prototype only when asked.

## Next agenda
Review their filled slides. Collect remaining: product name, nvidia-smi, public sample scan. No app code until build is requested.
