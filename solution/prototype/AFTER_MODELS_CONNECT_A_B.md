# After models installed on A — set up A + connect B (phone hotspot)

**Laptop-B** = this SIH26 workbench PC  
**Laptop-A** = Ollama + GPU (models already installed)

**Target tags on A (sequential, 8 GB VRAM):**
| Tag | Job |
|-----|-----|
| `llama3.2:3b` | Inspection / Word polish |
| `qwen2.5-coder:7b` | Coding |
| `moondream` | Multimodal (image/scan) |

Confirm on A: `ollama list` shows all three.

---

## Part 1 — Laptop-A (every session)

1. Connect A to the **phone hotspot**.  
2. PowerShell:
   ```powershell
   setx OLLAMA_HOST "0.0.0.0"
   ```
   Quit Ollama (tray) → start again *(only needed once if already set)*.  
3. Get IP:
   ```powershell
   ipconfig
   ```
   Copy **IPv4** of the hotspot Wi‑Fi → `<A-IP>` (e.g. `192.168.43.10`).  
4. Check:
   ```powershell
   ollama list
   curl http://127.0.0.1:11434/api/tags
   ```
5. Leave Ollama running. Tell B the `<A-IP>`.

Optional helper on A: `scripts/hotspot_prepare_server.ps1`

---

## Part 2 — Laptop-B (this PC)

1. Connect B to the **same** phone hotspot.  
2. Test reachability:
   ```powershell
   ping <A-IP>
   curl http://<A-IP>:11434/api/tags
   ```
   You must see all three model names in the JSON.  
3. Link Workbench to A (**same PowerShell window** for API):
   ```powershell
   cd "C:\Users\THARUN PARSA\Documents\SIH26"
   .\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
   python backend/scripts/restart_api.py
   python backend/scripts/validate_station_link.py
   ```
   Expect **PASS** (cards’ `model_id`s must appear on A).  
4. Start desk:
   ```powershell
   cd apps\kwb-app
   npm run electron:dev
   ```

---

## Part 3 — What B’s config expects

`config/models.yaml` maps:

- `inspect-draft` → `llama3.2:3b`  
- `code-assist` → `qwen2.5-coder:7b`  
- `vision-scan` → `moondream`  

`validate_station_link.py` fails until those tags exist on A.

Default single-laptop (no hotspot): keep `llm_base_url: http://127.0.0.1:11434` and run API in a **new** shell without the hotspot env vars.

---

## Quick flow

```
Phone hotspot
    ├── A: Ollama 0.0.0.0:11434  + 3 models  →  note <A-IP>
    └── B: hotspot_link_workbench.ps1 -ServerIp <A-IP>
           → restart_api → validate_station_link PASS
           → electron:dev
```

---

## If something fails

| Problem | Fix |
|---------|-----|
| tags curl fails | A not on hotspot / firewall / `OLLAMA_HOST` |
| validate missing model | Tag name mismatch — `ollama list` exact string into `models.yaml` |
| gateway_deny | Re-run `hotspot_link_workbench.ps1` with correct IP |
| OOM on A | Use one model at a time; close other GPU apps |
