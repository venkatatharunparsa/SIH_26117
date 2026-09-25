# Detailed workflow — Phone hotspot · Laptop-A ↔ Laptop-B

**Follow in order. Do not skip checks.**

| Machine | Role |
|---------|------|
| **Phone** | Hotspot (private LAN) |
| **Laptop-A** | Ollama + models (GPU server) |
| **Laptop-B** | This SIH26 workbench (FastAPI + Electron desk) |

**Models on A (example):** `llama3.2:3b` · `qwen2.5-coder:7b` · `moondream`  
**Rule:** One model in VRAM at a time. B never pulls models for the demo.

---

## Phase 0 — Once per machine (before demo day)

### 0A — Laptop-A (once)

1. Install [Ollama for Windows](https://ollama.com/download).  
2. Stage models offline so `ollama list` shows your three tags.  
3. Open PowerShell **as user** (once):
   ```powershell
   setx OLLAMA_HOST "0.0.0.0"
   ```
4. Quit Ollama from the system tray → start Ollama again.  
5. Windows Firewall → allow **Ollama** / inbound **TCP 11434** on **Private**.  
6. Optional: copy `scripts/laptop_a_ollama_watch.py` onto A (Desktop is fine).

### 0B — Laptop-B (once) — already done if you ran setup

1. Repo at `C:\Users\THARUN PARSA\Documents\SIH26`.  
2. Run:
   ```powershell
   cd "C:\Users\THARUN PARSA\Documents\SIH26"
   .\scripts\setup_laptop_b.ps1
   ```
3. Confirm `config\models.yaml` cards point at A’s tags.  
4. Confirm files exist: `scripts\hotspot_link_workbench.ps1`.

---

## Phase 1 — Phone hotspot

1. On the phone: turn on **Personal / Mobile Hotspot**.  
2. Note SSID + password.  
3. Connect **Laptop-A** to that hotspot.  
4. Connect **Laptop-B** to the **same** hotspot.  
5. Confirm both show connected (not guest Wi‑Fi of a hotel that isolates clients).

**Stop here if either laptop is still on a different network.**

---

## Phase 2 — Laptop-A online as server

Do this **on A**:

### Step 2.1 — Confirm hotspot IP

```powershell
ipconfig
```

Find the adapter for the phone hotspot (Wireless LAN).  
Copy **IPv4 Address** → write it down as `<A-IP>`  
Examples: `192.168.43.10` · `192.168.137.25`

### Step 2.2 — Confirm Ollama

```powershell
ollama list
curl http://127.0.0.1:11434/api/tags
```

You must see your model names in the JSON.

### Step 2.3 — Start live log (recommended)

```powershell
cd <folder-with-script>
python laptop_a_ollama_watch.py
```

Leave this window open. When B calls A, you should see a model appear under `loaded:`.

### Step 2.4 — Tell Laptop-B

Send/chat the value of `<A-IP>` to the person on B (or yourself).

**A is done for now.** Leave Ollama + watch running. Do not start the SIH desk on A.

---

## Phase 3 — Laptop-B link to A

Do this **on B**. Use **one PowerShell window** for steps 3.2–3.4.

### Step 3.1 — Can B reach A?

```powershell
ping <A-IP>
curl http://<A-IP>:11434/api/tags
```

| Result | Action |
|--------|--------|
| Ping fails | Both not on hotspot / phone isolating clients → fix network |
| Ping OK, curl fails | A firewall or `OLLAMA_HOST` / Ollama not restarted |
| curl shows models | Continue |

### Step 3.2 — Point Gateway at A

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
```

You should see:
```text
SOVEREIGN_LLM_BASE_URL=http://<A-IP>:11434
SOVEREIGN_INFERENCE_ALLOW_HOSTS=<A-IP>
OK tags HTTP 200
```

**Do not close this PowerShell.**

### Step 3.3 — Restart API in the SAME window

```powershell
python backend/scripts/restart_api.py
```

Wait until it prints healthy.

### Step 3.4 — Verify “where” LLM is

```powershell
Invoke-RestMethod http://127.0.0.1:8080/inference/status
```

**Pass looks like:**
- `label`: `LAPTOP-A peer (<A-IP>)`  
- `is_local`: `False`  
- `tags_on_target`: includes models from A  

**Fail looks like:**
- `label`: `LOCAL (this Laptop-B Ollama)`  
- `is_local`: `True`  

→ API was started in another window without hotspot env. Stop that API and repeat 3.2–3.4 in **one** shell.

Optional:
```powershell
python backend/scripts/validate_station_link.py
```
Expect **PASS**.

### Step 3.5 — Start the desk

Still fine to use a second terminal for the desk (API must stay in the hotspot shell):

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26\apps\kwb-app"
npm run electron:dev
```

---

## Phase 4 — Prove A↔B in the product

1. Open desk → click **Monitor**.  
2. Tab **Live log** / **Status**: banner must say **LAPTOP-A**, not LOCAL.  
3. Title bar should also show the Laptop-A label.  
4. New chat → type `hi` → Enter.  
5. On **Laptop-A** watch window: `loaded:` should show e.g. `llama3.2:3b`.  
6. Monitor **Live log** on B: look for `gateway_chat` with `base_url` / Laptop-A label.  
7. Tab **Share** → **Copy share text** if you want to save/send evidence (not CERT).

Optional inspection path: attach fixture → Confirm extract → cites → Word DRAFT → Self-check → Export.

---

## Phase 5 — End of session

1. Close desk on B.  
2. Stop API (Ctrl+C in API shell) or leave machine.  
3. Open a **new** PowerShell on B later for single-laptop work (so old `<A-IP>` env is gone).  
4. On A: stop watch script; you may quit Ollama.  
5. Turn off phone hotspot when done.

---

## Cheat sheet (every new hotspot session)

| # | Where | Command / action |
|---|--------|------------------|
| 1 | Phone | Hotspot on |
| 2 | A + B | Join hotspot |
| 3 | A | `ipconfig` → `<A-IP>` |
| 4 | A | Ollama up + optional `python laptop_a_ollama_watch.py` |
| 5 | B | `ping` + `curl http://<A-IP>:11434/api/tags` |
| 6 | B | `.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>` |
| 7 | B | `python backend/scripts/restart_api.py` *(same shell)* |
| 8 | B | `Invoke-RestMethod …/inference/status` → must be LAPTOP-A |
| 9 | B | `npm run electron:dev` → Monitor shows LAPTOP-A |
| 10 | Both | `hi` on B → model loads on A watch |

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Cannot ping A | Same hotspot? Try forget network & reconnect; avoid guest isolation |
| curl tags fail | `OLLAMA_HOST=0.0.0.0` + restart Ollama; firewall 11434 |
| inference_status still LOCAL | Hotspot script + restart API in **same** shell |
| gateway_deny / non_local_host | Allowlist missing — re-run hotspot script |
| IP changed after phone sleep | New `ipconfig` on A; re-run B steps 6–8 |
| validate missing model | Tag name on A must match `models.yaml` exactly |
| OOM on A | Close other GPU apps; sequential cards only |

---

## Related files

- Laptop-A Cursor prompt: `CURSOR_PROMPT_LAPTOP_A.md`  
- Laptop-A setup: `LAPTOP_A_SERVER_SETUP.md`  
- Laptop-B setup: `LAPTOP_B_WORKBENCH_SETUP.md`  
- After models: `AFTER_MODELS_CONNECT_A_B.md`
