# Hackathon Pitch Draft — Knowledge Work Bench (SIH26117)

**Product:** Knowledge Work Bench (KWB) · **PS:** SIH26117 · **Org:** MRPL  
**Status:** Draft for rehearsal — not the official portal PPTX until team lock.  
**Tone:** Industrial evidence desk. Not “ChatGPT on-prem.”

---

## 30-second pitch

Refineries and PSUs cannot paste P&IDs, inspection scans, or board drafts into Claude or Codex.  
**Knowledge Work Bench** is an on-prem agent desk: it reads a scan, pulls SOP cites from a **local** knowledge base, stops for human gates, and leaves a **Word DRAFT** — while the gateway **refuses public models**. Judgement stays with the engineer; the app never pretends to be CERT or the Approver.

---

## 2-minute story (demo path)

1. **Open folder** of inspection fixtures (scans / field PDF).  
2. **Attach** → agent plan advances: ingest → H1 Confirm extract.  
3. Operator confirms facts → retrieve **SOP-THK-001** → H7 cite review.  
4. **Word DRAFT** appears with model/card footer — soft copy only.  
5. Flip to **coding** agent mode → second model tag → sandbox calc.  
6. Open **Monitor**: inference target = local or private LAN peer · **not air-gap theatre as CERT**.

---

## Uniqueness (3 ticks only)

1. **On-prem / no public LLM on the gateway path** (deny unregistered models).  
2. **Cite or abstain** — numbers from local SOP, else NOT FOUND.  
3. **HITL before anything looks like a record** — export is leave pack; Approver outside.

---

## What we are *not*

- Not an autonomous refinery operator  
- Not a Cursor/Claude Code clone (we borrow desk UX, not the product)  
- Not writing DCS / EAM / ERP  
- Not claiming true air-gap until NIC evidence exists  

---

## Closing line

“Same shape of agent people want from Claude — **plan, tools, iterate** — but the **policy spine** is industrial: grant, cite, draft, leave.”
