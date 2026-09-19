# Sovereign AI Workbench — Knowledge Base

## What this is

This repository contains the complete research base for designing an **air-gapped, on-premise agentic AI workbench** for confidential industrial knowledge work in India.

The workbench is being designed for organisations that generate routine but sensitive knowledge work — approval notes, board presentations, engineering calculations, code for internal tools, review of scanned drawings, inspection reports — and cannot use cloud AI because the underlying data is confidential.

## Why this exists

Indian refineries, PSUs, defence-linked manufacturing units, government offices, regulators, banks, heavy industry, and legal institutions all perform high-volume knowledge work over documents and operational data that is often too sensitive for consumer cloud AI.

Existing tools like Claude, ChatGPT, and Codex are powerful but cloud-only. They cannot be used with P&IDs, inspection reports, vendor negotiations, incident reports, or board notes. People either do the work manually or quietly paste confidential material into public tools anyway.

This knowledge base documents the problem, the users, the workflows, the sensitive data, the document templates, the cross-sector applicability, the policy context, the competitive landscape, and the feasibility of building a sovereign alternative.

## Structure

| Folder | What it contains |
|---|---|
| `01-problem-context/` | The problem statement, the combined problem statement, and why this matters |
| `02-mrpl/` | Deep dive on Mangalore Refinery and Petrochemicals Limited — the beachhead customer |
| `03-personas/` | The 8 user personas who will use the workbench |
| `04-workflows/` | Step-by-step workflows for each persona, plus the coding sandbox required by SIH |
| `05-sensitive-data/` | Data classification framework, sensitive data inventory, what is not confidential |
| `06-document-templates/` | The 11 document templates the AI must generate, including PowerPoint board packs |
| `07-cross-sector/` | Deep dive on 20+ sectors beyond MRPL |
| `08-policy/` | Indian data sovereignty and AI policy context |
| `09-competitive-analysis/` | Open-source, commercial, and Indian AI ecosystem comparison |
| `10-feasibility/` | 36-hour hackathon feasibility, GPU choices, team allocation |
| `11-reference/` | Glossaries, organisation coverage, sources |
| `12-user-perspective/` | The lived experience of the users who wrote the problem statement |

## How to use

Each file is self-contained. Start with `00-INDEX.md` for a guided reading order.

## Sources

Primary research compiled from: MRPL annual reports, ONGC reports, MoPNG documents, OISD standards, API standards, RBI guidelines, MeitY documents, CERT-In directions, DRDO publications, PSU annual reports, defence procurement manuals, government policy documents, and industry publications. Full source list in `11-reference/05-sources.md`.

## Status

Research phase complete. Solution design pending.
