# Laptop-A only — model server (phone hotspot)

**This PC (where you read SIH26 normally) = Laptop-B.**  
**Other PC with GPU = Laptop-A.** A does **not** need the full KWB desk — only **Ollama + models**.

---

## What Laptop-A is for

| Runs on A | Does **not** need on A |
|-----------|-------------------------|
| Ollama | Electron desk / `kwb-app` |
| Your chat model(s), e.g. `llama3.2:3b` | FastAPI `:8080` |
| LAN bind so B can call `:11434` | SIH26 repo (optional) |

---

## One-time install on Laptop-A

1. Install **Ollama for Windows**: https://ollama.com/download  
2. Open PowerShell and confirm:

```powershell
ollama --version
ollama list
```

3. Models must already be on A (USB / earlier download). **Do not rely on venue pull.**  
   Example if already present:

```powershell
ollama list
# expect something like: llama3.2:3b
```

4. Bind Ollama to the network (so B can reach it on hotspot):

```powershell
setx OLLAMA_HOST "0.0.0.0"
```

5. **Fully quit Ollama** (tray icon → Quit) and start Ollama again.

6. Windows Firewall: allow **Ollama** / inbound **TCP 11434** on **Private** networks.

---

## Every demo session on Laptop-A

### 1) Join phone hotspot
Connect A to the **same** phone hotspot as B.

### 2) Read A’s IP
PowerShell:

```powershell
ipconfig
```

Find **IPv4** under the Wi‑Fi adapter for the hotspot  
(often `192.168.43.x` or `192.168.137.x`).

**Send that IP to Laptop-B** — B will use it in:

```powershell
.\scripts\hotspot_link_workbench.ps1 -ServerIp <THAT-IP>
```

### 3) Confirm Ollama is up

```powershell
ollama list
curl http://127.0.0.1:11434/api/tags
```

Leave A on, lid open/power plugged in, Ollama running. No desk on A.

---

## Optional: copy one helper script to A

If you want the helper without the whole repo, copy only:

`scripts/hotspot_prepare_server.ps1`

onto A, then:

```powershell
.\hotspot_prepare_server.ps1
```

It prints hotspot IPv4s and reminds you to set `OLLAMA_HOST`.

---

## What B (this laptop) does after A is ready

You already have the repo here. After A gives you `<A-IP>`:

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
python backend/scripts/restart_api.py
python backend/scripts/validate_station_link.py
cd apps\kwb-app
npm run electron:dev
```

---

## Quick A checklist

- [ ] Ollama installed  
- [ ] `llama3.2:3b` (or your tags) in `ollama list`  
- [ ] `OLLAMA_HOST=0.0.0.0` + Ollama restarted  
- [ ] Firewall allows 11434  
- [ ] On phone hotspot  
- [ ] IPv4 noted and given to B  
- [ ] A stays online while B runs the desk  

Full note after all models installed: `AFTER_MODELS_CONNECT_A_B.md`

