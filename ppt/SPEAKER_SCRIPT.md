# Speaker script — ~5 minutes

**Product:** Knowledge Work Bench · **PS:** SIH26117  
**Rule:** Prefer workbench / DRAFT Word language. Never “chatbot” / “chat app”.

---

## Opening (Slide 1 → 2) — 0:20

“Team **[TEAM_NAME]**, problem **SIH26117** for MRPL — Smart Automation, Software.  
Confidential industrial work — inspection packs, drawings, notes — cannot leave the premises. Today people either assemble packs by hand or risk pasting into public tools.”

---

## Solution (Slide 2) — 1:10

“Our product is **Knowledge Work Bench**.  
It opens a **task grant**, selects a **model card** by task type, runs retrieve and draft under **human gates**, and produces a **DRAFT Word** soft copy. Coding tasks go through a **network-none sandbox**.  
**Monitor A** records an **evidence pack** — that is proof of the sovereign claim, and it is **not** a CERT-In certificate.  
Three differences: we stay on open-weight on-prem paths versus cloud assistants; we add routing, human checkpoints, Word, and evidence versus a bare local model UI; we centre inspection artefacts versus a pure coding-agent product.”

*[Gesture to Context diagram — O1]*  
“Two people: the **engineer** works in the desk and exports the DRAFT. **Admin** brings offline packs through quarantine, then **enables Model Cards** so the GPU runtime may load only allowed weights. Inference goes only through the **gateway**. Monitor A is evidence — not a certificate.”

---

## Technical (Slide 3) — 1:00

*[Gesture to Component diagram — O2/O3]*  
“Inside: workbench plane does grants, confirm extract, retrieve, packer, Word, audit. Packed prompts leave **only** through the gateway to the runtime — cards enable weights. Sandbox is separate for calc and code. Ends at export leave; Monitor A is evidence, not CERT.”

---

## Feasibility (Slide 4) — 0:50

“The PS itself allows smaller models when 120B hardware is missing.  
Our REAL spine is already demonstrable: routing, human checkpoints, DRAFT, sandbox, evidence pack, fail-closed denies.  
Excel, SSO, live OCR engines are Later. Writing to DCS or EAM is **never**.”

---

## Impact (Slide 5) — 0:40

“Primary user: inspection engineer — they leave with a DRAFT they still own.  
Social context: Cisco’s benchmark — 48% of organisations admit pasting non-public data into GenAI.  
Time claim — labelled estimate: pack assembly from days toward **hours to a DRAFT**. Not an MRPL SLA; not FFS authority.”

---

## Close (Slide 6) — 0:30

“References: Expected Solution, MRPL scale, IndiaAI ecosystem, NIST AI RMF companion, ReAct/RAG literature.  
Difference line: artefacts, citations, and sovereign evidence on the hardware class the problem describes.  
Happy to show the live workbench and take questions.”

---

## If demo follows

Operator runs `pwsh -File scripts/start_demo.ps1` or Electron desk.  
Show: Start → Confirm extract → Retrieve → Review citations → Draft → Self-check → Export · then More → Inject secret (deny).  
Say: “DRAFT soft copy — export leave ends our solution path.”
