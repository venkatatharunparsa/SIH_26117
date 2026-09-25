# Narrative arc — how the six slides tell one story

**Audience:** remote screeners (tired, ~2 min heuristic) then live jury.  
**Spine:** Problem → Workbench → How it runs → Honest 36h → Who wins → Proof we studied.

---

## Story in one paragraph (memorise)

Industrial sites cannot send P&IDs and inspection packs to cloud assistants. Engineers either assemble notes by hand or risk shadow paste. **Knowledge Work Bench** keeps work on premises: it opens a **task grant**, routes an open-weight model by **card**, runs retrieve/sandbox/draft under **human checkpoints**, and leaves a **DRAFT Word** soft copy with audit — while **Monitor A** records an evidence pack that no plant write and no CERT claim are made. Same architecture from demo laptop to org GPU socket.

---

## Slide-to-slide baton pass

| Slide | Narrative job | Baton to next |
|---|---|---|
| **1 Title** | Name the PS and the team; zero product pitch yet | “Here is what we propose…” |
| **2 Idea** | Name **KWB** + **Context diagram** + pains → mechanisms + 3 ticks | “Here is what’s inside…” |
| **3 Technical** | **Component diagram** (3 planes) + Layer/Tech/Purpose | “Can this survive 36h and mid-GPU?” |
| **4 Feasibility** | REAL/MOCK/LATER + risks/mitigations | “Who benefits, with one honest KPI…” |
| **5 Impact** | Engineer-first audience + one time estimate + social Cisco context | “We studied standards, papers, and alternatives…” |
| **6 Research** | Refs + competitor matrix + difference line | End / Q&A |

### Diagram baton

| Order | Diagram | Slide | Answers |
|---|---|---|---|
| 1st | **Context** (`prompt/DALLE_S02_CONTEXT.md` gen **920×420** → crop · topology `D01`) | 2 | Who is around the system? What never connects? |
| 2nd | **Component** (`D02_COMPONENT_DIAGRAM.md`) | 3 | What is inside? Where are the planes? |

---

## Timing (idea PDF stand-alone; live pitch ~5 min)

| Block | Time | Slide |
|---|---|---|
| Hook — confidential work cannot go to cloud | 0:20 | 1→2 |
| Product + **context diagram** | 1:10 | 2 |
| **Component diagram** + stack | 1:00 | 3 |
| Honest scope + risks | 0:50 | 4 |
| Impact + one KPI | 0:40 | 5 |
| Difference + refs tease | 0:30 | 6 |
| Buffer / close | 0:30 | — |

**Live demo is outside the PDF** — run Electron desk while pointing at slide 2 loop. Backup: `MANUAL_TEST_REPORT` walk recorded.

---

## Words we prefer (positive product language)

| Prefer | Avoid on slides |
|---|---|
| Knowledge Work Bench / industrial workbench | “chatbot”, “chat app”, “chat UI”, “not a chatbot” |
| DRAFT Word deliverable · soft copy · export leave | “final approval”, “CERTIFIED”, “CERT-In certified” |
| Task grant · Model Card · human checkpoints | “autonomous plant decisions” |
| Monitor A evidence pack | “CERT monitor”, “compliance badge” |
| Open-weight models · local `/v1` | “we trained a foundation model” |
| Two task types · one model tag (when honest) | “multi-model dual 70B” |

---

## Screener eye path (playbook)

1. Which PS? → Slide 1 filled  
2. What product? → Named **Knowledge Work Bench** on slide 2  
3. Can I redraw the flow? → Context diagram (S2) then Component diagram (S3)  
4. 36h honest? → REAL/MOCK/LATER  
5. Who benefits? → Inspection engineer + MRPL-class context  
6. Why this vs cloud / local UIs / coding agents? → Matrix + 3 ticks  
