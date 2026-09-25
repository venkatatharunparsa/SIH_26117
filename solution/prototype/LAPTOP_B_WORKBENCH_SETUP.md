# Laptop-B setup (THIS machine = Knowledge Workbench)

**Role:** Desk + FastAPI + grants/HITL/Word — **not** the GPU model host.  
**Models live on Laptop-A** after hotspot link. Local Ollama on B is optional fallback only.

---

## What this script / checklist installs

| Piece | Purpose |
|-------|---------|
| Python deps (`backend/requirements.txt` + root if present) | FastAPI, docx, pptx, OCR libs |
| `apps/kwb-app` npm deps | Electron desk |
| Config | `models.yaml` cards → A’s tags; default `llm_base_url` localhost until hotspot script |
| Helpers | `hotspot_link_workbench.ps1`, validate + restart scripts |

---

## One-command setup (run on B)

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
.\scripts\setup_laptop_b.ps1
```

Then when A is on hotspot with IP `<A-IP>`:

```powershell
.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
python backend/scripts/restart_api.py
python backend/scripts/validate_station_link.py
cd apps\kwb-app; npm run electron:dev
```

---

## Manual checklist

1. Python 3.11+ and Node 18+ installed  
2. `pip install -r backend/requirements.txt` (and root `requirements.txt` if present)  
3. `cd apps/kwb-app; npm install`  
4. Confirm files: `config/models.yaml`, `scripts/hotspot_link_workbench.ps1`  
5. Single-laptop smoke (optional, local Ollama): `python backend/scripts/sim_single_model_e2e.py`  
6. Two-laptop: do **not** pull models on B — only link to A  

---

## Card map (expects these tags on A)

| Card | model_id |
|------|----------|
| inspect-draft | llama3.2:3b |
| code-assist | qwen2.5-coder:7b |
| vision-scan | moondream |
