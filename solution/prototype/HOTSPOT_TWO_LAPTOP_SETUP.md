# Phone hotspot — two-laptop setup (what YOU do)

**Chosen link:** Phone hotspot  
**Laptop-A** = Ollama / model server (GPU)  
**Laptop-B** = Knowledge Workbench (this repo: FastAPI + Electron)  
**Link mode for hotspot:** **direct LAN + allowlist** (hotspot IPs are private `192.168.x.x`)

Hotspot IPs **change** each session — always re-check A’s IP and re-apply B’s config (script below).

---

## 0. Before you start

| Machine | Need |
|--------|------|
| Phone | Hotspot able to connect **both** laptops (data optional; can leave data off for “offline” story if both already have apps/models) |
| Laptop-A | Ollama installed; `llama3.2:3b` (and later 2nd model) already on disk — **no pull on stage** |
| Laptop-B | This SIH26 repo; Python + Node; API + desk |

---

## 1. Phone

1. Open **Personal Hotspot** / **Mobile Hotspot**.  
2. Note **SSID + password**.  
3. Prefer “Maximize compatibility” if available.  
4. Connect **Laptop-A** and **Laptop-B** to this hotspot (not different Wi‑Fi).

---

## 2. Laptop-A (model server) — do this first

### 2.1 Confirm hotspot IP

PowerShell:

```powershell
ipconfig
```

Under the adapter connected to the phone (often “Wireless LAN”), copy **IPv4 Address**.  
Example: `192.168.43.10` → this is `<A-IP>`.

### 2.2 Bind Ollama to LAN

PowerShell **as Admin** (once):

```powershell
setx OLLAMA_HOST "0.0.0.0"
```

Then **quit Ollama completely** from tray and start it again.

Check models:

```powershell
ollama list
```

### 2.3 Firewall (Windows)

Allow inbound **TCP 11434** on **Private** networks (Windows Defender Firewall → Inbound rule), or when Windows asks “allow Ollama”, choose **Private**.

### 2.4 Leave A alone

Do **not** need desk/API on A for this demo. Only Ollama.

---

## 3. Laptop-B (workbench)

### 3.1 Confirm you can reach A

```powershell
ping <A-IP>
curl http://<A-IP>:11434/api/tags
```

You must see JSON with models. If not: hotspot isolation / firewall / Ollama not bound.

### 3.2 Point Workbench Gateway at A (allowlist)

**Easiest — use the helper script** (from repo root on B):

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
.\scripts\hotspot_link_workbench.ps1 -ServerIp "<A-IP>"
```

This sets for the **current PowerShell session**:

- `SOVEREIGN_LLM_BASE_URL=http://<A-IP>:11434`
- `SOVEREIGN_INFERENCE_ALLOW_HOSTS=<A-IP>`

Then **in that same window** start the API (so it inherits env):

```powershell
python backend/scripts/restart_api.py
python backend/scripts/validate_station_link.py
```

Expect **PASS**.

### 3.3 Start desk

```powershell
cd apps\kwb-app
npm run electron:dev
```

Chat / attach / Word flow on B; inference runs on A.

---

## 4. Manual config (if you prefer YAML)

On B, temporarily in `config/models.yaml`:

```yaml
llm_base_url: "http://192.168.43.10:11434"   # your real <A-IP>
inference_allow_hosts:
  - "192.168.43.10"
```

Restart API. After demo, set back to `http://127.0.0.1:11434` and comment allowlist for single-laptop.

---

## 5. Verify checklist

| # | Check | Pass looks like |
|---|--------|-----------------|
| 1 | Both on phone hotspot | Same SSID |
| 2 | `ping <A-IP>` from B | Replies |
| 3 | `curl http://<A-IP>:11434/api/tags` | Model list |
| 4 | `validate_station_link.py` on B | PASS |
| 5 | Desk on B: type `hi` | Assistant reply (model on A) |

---

## 6. After hotspot session

1. Stop desk + API on B.  
2. Clear env or reopen a **new** PowerShell (so you don’t keep pointing at a dead IP).  
3. For single-laptop again: `llm_base_url: http://127.0.0.1:11434` and empty allowlist.

---

## 7. Later (not now)

- Stage **2nd chat model** on **A** offline → then G1 full.  
- Same hotspot steps; only A’s `ollama list` grows.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Ping fails | Both not on hotspot; phone “isolate clients”; try forget network & reconnect |
| Ping OK, tags fail | `OLLAMA_HOST=0.0.0.0` + restart Ollama; firewall 11434 |
| `gateway_deny` / non_local_host | Allowlist missing or IP typo; re-run `hotspot_link_workbench.ps1` |
| Works then dies | Phone slept / IP changed → new `ipconfig` on A + re-run script on B |
