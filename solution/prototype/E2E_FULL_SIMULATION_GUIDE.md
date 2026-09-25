# KWB end-to-end simulation guide

**Purpose:** From both laptops **powered off** → linked workbench → every PS workflow, with **fallbacks** when something fails.  
**Audience:** Operator running a seamless simulation (not a developer deep-dive).  
**Honesty:** This is a **private LAN / on-prem Gateway** demo (phone hotspot peer). It is **not** a true air-gap until you add NIC/WAN evidence.

**Fresh verification (2026-09-20 night, after API restart):**


| Suite                      | Result                                                 |
| -------------------------- | ------------------------------------------------------ |
| `robust_ps_workflows.py`   | **24/24 PASS** · `lan_peer_laptop_a` @ `10.45.226.121` |
| `e2e_one_model.py`         | **PASS** · dual-tag `llama3.2:3b` / `qwen2.5-coder:7b` |
| `smoke_platform.py`        | **OK**                                                 |
| `validate_endpoints.py`    | **18/18**                                              |
| `validate_station_link.py` | **OK**                                                 |
| `hitl_gates_smoke.py`      | **OK**                                                 |


Tags on A during that run: `moondream:latest`, `qwen2.5-coder:7b`, `llama3.2:3b`.

Related files: `OPERATOR_COLD_BOOT_TWO_LAPTOP.md`, `PS_WORKFLOW_DESIGN.md`, `PS_ROBUST_TEST_REPORT.md`, `DECISION_AND_GAP_AUDIT.md`.

---



## 0. What you are simulating


| Role         | Machine                     | Job                                                      |
| ------------ | --------------------------- | -------------------------------------------------------- |
| **Laptop-A** | Model station (e.g. HP)     | Ollama + GPU; serves open-weight models on LAN           |
| **Laptop-B** | Workbench (this SIH26 repo) | FastAPI + Electron desk; **never** calls public LLMs     |
| **Phone**    | Hotspot                     | Same SSID for A and B (client isolation off if possible) |


**Path of truth:** Desk → `/orch/turn` → Orchestrator → Pack → **Gateway** → Ollama on A (or local B).  
**Not CERT.** DRAFT ≠ plant record. Monitor A = evidence pack only.

---



## 1. Cold boot — Laptop-A (model station)



### 1.1 Power on → hotspot

1. Power on A · sign in.
2. Connect Wi‑Fi to the **phone hotspot**.
3. Note IPv4:

```powershell
ipconfig
```

Copy Wi‑Fi **IPv4** = `<A-IP>` (example from live run: `10.45.226.121`).


| Failure                    | Fallback                                                   |
| -------------------------- | ---------------------------------------------------------- |
| No Wi‑Fi IP                | Rejoin hotspot; disable VPN if it steals default route     |
| Ethernet only, no hotspot  | Join hotspot SSID; do not rely on campus Ethernet for A↔B  |
| IP changed since last demo | Always re-copy `<A-IP>`; B link script must use the new IP |




### 1.2 Ollama on PATH

```powershell
Test-Path "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"
$env:Path = "$env:LOCALAPPDATA\Programs\Ollama;" + $env:Path
ollama list
```


| Failure                      | Fallback                                                                                                   |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `ollama` not recognized      | Prepend Path as above, or call full path to `ollama.exe`                                                   |
| `ollama list` empty          | `ollama pull llama3.2:3b` then `qwen2.5-coder:7b` then `moondream` (**before** venue; never pull mid-demo) |
| Timed out waiting for server | Kill `Get-Process ollama* | Stop-Process -Force`; start `ollama serve` in a dedicated window               |




### 1.3 Bind for LAN + firewall

```powershell
[System.Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "User")
$env:OLLAMA_HOST = "0.0.0.0:11434"
```

**Admin PowerShell (once):**

```powershell
New-NetFirewallRule -DisplayName "Ollama LAN" -Direction Inbound -Protocol TCP -LocalPort 11434 -Action Allow -Profile Any
```

Quit tray Ollama if needed, then **leave this window open:**

```powershell
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" serve
```

Verify:

```powershell
Invoke-RestMethod http://127.0.0.1:11434/api/tags
Invoke-RestMethod http://<A-IP>:11434/api/tags
```


| Failure                        | Fallback                                                                                                               |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Local tags OK, LAN tags fail   | Firewall rule missing / not Admin; or `OLLAMA_HOST` was `0.0.0.0` without port — set `0.0.0.0:11434` and restart serve |
| `Access is denied` on firewall | Right‑click PowerShell → Run as administrator                                                                          |
| Serve window closed mid-demo   | Restart serve before B continues                                                                                       |


**Optional:** Desktop `Ollama_Server\watch_ollama_server.ps1` or repo `scripts/laptop_a_ollama_watch.py`.

---



## 2. Cold boot — Laptop-B (workbench)



### 2.1 Power on → same hotspot

1. Power on B · sign in.
2. Connect **Wi‑Fi** to the **same** hotspot (not Ethernet-only campus).

```powershell
ipconfig
```

**Success:** Wi‑Fi IPv4 in same `/24` as A (example: B `10.45.226.51`, A `10.45.226.121`).


| Failure                                     | Fallback                                                                            |
| ------------------------------------------- | ----------------------------------------------------------------------------------- |
| Wi‑Fi disconnected; only Ethernet `10.11.x` | Join hotspot Wi‑Fi; ping will fail until then                                       |
| Tailscale / VPN active                      | Usually OK if Wi‑Fi still has hotspot IP; if ping fails, disconnect VPN temporarily |
| Different SSID / guest network              | Rejoin main hotspot; disable AP isolation on phone if present                       |




### 2.2 Reach A

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
ping <A-IP>
Test-NetConnection <A-IP> -Port 11434Invoke-RestMethod http://<A-IP>:11434/api/
tags
```



Use `Invoke-RestMethod` (not bare `curl` on Windows PowerShell — avoids script warning prompts).


| Failure                       | Fallback                                  |
| ----------------------------- | ----------------------------------------- |
| Destination host unreachable  | B not on hotspot (see 2.1)                |
| Ping OK, port 11434 fails     | A firewall / serve not bound — fix A §1.3 |
| Tags fail after serve restart | Wait 2–3s; recheck `OLLAMA_HOST`          |




### 2.3 Link + fresh API (ONE PowerShell window)

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
python backend/scripts/restart_api.py
Invoke-RestMethod http://127.0.0.1:8080/inference/status
```

**Must see:** `mode = lan_peer_laptop_a`, `label = LAPTOP-A peer (...)`, `is_local = False`, `runtime_reachable = True`, tags include the three models.


| Failure                                | Fallback                                                                                       |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Script parse error (old em-dash)       | Repo scripts fixed; pull latest; re-run                                                        |
| API crash `inference_allow_hosts` JSON | Plain IP OK after NoDecode fix; or set `$env:SOVEREIGN_INFERENCE_ALLOW_HOSTS = '["10.x.x.x"]'` |
| Status still **LOCAL**                 | Link + `restart_api` not in **same** shell — re-run both in one window                         |
| `API did not come up` / port 8080 busy | `netstat -ano | findstr :8080` → stop old PID; do not start a second uvicorn                   |
| `g9 400` during restart                | **Expected** (secret smoke) — ignore if `healthy` printed                                      |


Manual env if script skipped:

```powershell
$env:SOVEREIGN_LLM_BASE_URL = "http://<A-IP>:11434"
$env:SOVEREIGN_INFERENCE_ALLOW_HOSTS = "<A-IP>"
python backend/scripts/restart_api.py
```



### 2.4 Start desk

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26\apps\kwb-app"
npm run electron:dev
```

Titlebar should show API `127.0.0.1:8080` and **LAPTOP-A peer**. Open **Monitor**.


| Failure                        | Fallback                         |
| ------------------------------ | -------------------------------- |
| npm errors                     | `npm install` in `apps/kwb-app`  |
| Health dot red                 | API down — §2.3                  |
| UI looks stale after code pull | Fully quit Electron and relaunch |


---



## 3. Automated fresh suite (optional but recommended)

After §2.3, in the **same** linked shell:

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
python backend/scripts/robust_ps_workflows.py
python backend/scripts/e2e_one_model.py
python backend/scripts/smoke_platform.py
python backend/scripts/validate_station_link.py
```

**Expect:** `SCORE 24/24`, E2E PASS, station OK.  
Evidence: `eval/evidence/PS_ROBUST_TEST_REPORT.md`, `E2E_ONE_MODEL.json`.


| Failure           | Fallback                                                                        |
| ----------------- | ------------------------------------------------------------------------------- |
| WF2 Word timeout  | Increase wait; check A VRAM / serve log; retry once                             |
| WF4 image fails   | Vision may unload after large coder load — wait; or accept OCR/stub source line |
| Station link FAIL | Re-ping A; re-link IP                                                           |


---



## 4. End-to-end desk workflows (PS)

Design detail: `PS_WORKFLOW_DESIGN.md`. Do these in order for a full simulation story.

### WF0 — Prove the link (30 seconds)

1. Monitor → **Status**.
2. Confirm posture: private LAN peer · not air-gap.
3. Tags list · model/card after a chat.

**Fallback:** If LOCAL, stop — fix §2.3 before any story.

---



### WF1 — Dual-model auto-select

1. `+ new` · task **inspection** · Send `hi`.
2. Status / Share: card `inspect-draft` · model `llama3.2:3b`.
3. A serve log may show load.
4. `+ new` · task **coding** · Send `hi`.
5. Expect `code-assist` · `qwen2.5-coder:7b` (8GB may unload previous model — latency is normal).


| Failure                      | Fallback                                      |
| ---------------------------- | --------------------------------------------- |
| Coding still picks moondream | Fixed in `cards.py` — restart API             |
| Same model_id both           | Station missing coder tag — pull on A offline |
| Very slow first coding reply | Cold load 7B on 8GB — wait; watch A           |


---



### WF2 — Inspection → Word DRAFT (main story)

1. Session **inspection**.
2. Attach ⌁ → Document… →
  `data\fixtures\README_attach_demo.md`  
   (or `vessel_note_text.pdf`).
3. **Confirm extract** (Enter / yes).
4. **Confirm cites** (Enter).
5. Wait — tool card shows **phase chips**; Monitor Live log moves; A GPU busy.
6. **Self-check** Word DRAFT → Enter.
7. **Export leave** → Enter.
8. Monitor → Download DRAFT `.docx` · grant revoked message.


| Failure                     | Fallback                                                              |
| --------------------------- | --------------------------------------------------------------------- |
| Stuck on running, no phases | Reload desk (SSE); API must be post–confidence-rebuild build          |
| Polish fails / gateway deny | Check `/inference/status` allow host; A serve up                      |
| Got PPTX not Word           | Should be Word on orch path — use WF2 orch, not legacy PPTX-only docs |
| Export blocked              | Self-check H2; or secret/sandbox-red (intentional deny demos)         |


---



### WF3 — Sandbox coding

1. Coding session (or More menu with grant).
2. More → **Sandbox calc**.
3. Ack H9 if prompted.
4. Optional deny demo: **Sandbox red** → export should fail (fail-closed).


| Failure            | Fallback                                                              |
| ------------------ | --------------------------------------------------------------------- |
| 403 sandbox        | Grant inactive — start coding session / orch continue first           |
| Expect Docker jail | Product is **host-process** sandbox — say that aloud (Status says so) |


---



### WF4 — Multimodal image

1. Inspection session.
2. Attach `data\fixtures\scan_vessel_V101.png`.
3. Confirm ask source line:
  - Prefer: **on-device vision model (moondream)**  
  - Fallback: Tesseract / **fixture stub — NOT live OCR** (honest).
4. Confirm extract (full Word optional).


| Failure              | Fallback                                    |
| -------------------- | ------------------------------------------- |
| Vision timeout       | OCR/stub path still reaches Confirm extract |
| Tesseract missing    | Stub is OK for demo if labeled              |
| Wrong engine claimed | Never say “full multimodal” if stub         |


---



### WF5 — Sovereign proof theatre

1. Monitor **Live log** during a turn — gateway / orch_phase lines.
2. More → **Evidence pack start** → **stop**.
3. More → **Bad model** → deny.
4. **Verify audit**.
5. Share → Copy share text (shows LAPTOP-A URL + tags).


| Failure                | Fallback                                                                       |
| ---------------------- | ------------------------------------------------------------------------------ |
| Live log empty         | Open Monitor before turn; check `kind` mapping (fixed); Status/Share still SoT |
| Someone says “air-gap” | Correct to **private LAN peer**; air-gap = later NIC rehearsal                 |
| CERT language          | Badge is **NOT CERT** — keep it                                                |


---



### Fail-closed demos (optional)


| Demo            | More / API    | Expect       |
| --------------- | ------------- | ------------ |
| Secret in draft | Inject secret | Export deny  |
| Revoke          | Revoke grant  | Tools 403    |
| Public model    | Bad model     | Gateway deny |


---



## 5. What “seamless” looks like (checklist)

- [ ] A: `ollama serve` window open, LAN tags OK  
- [ ] B: Wi‑Fi same `/24`, ping + port 11434 OK  
- [ ] Status = **LAPTOP-A peer**, not LOCAL  
- [ ] WF1 both models visible  
- [ ] WF2 Word `.docx` + export leave  
- [ ] WF3 calc runs  
- [ ] WF4 image has honest source line  
- [ ] WF5 Monitor + deny + audit  
- [ ] Pitch: private LAN · NOT CERT · DRAFT soft copy  

---



## 6. Teardown

1. Quit Electron.
2. Stop API (Ctrl+C on uvicorn / restart script stop).
3. Stop `ollama serve` on A.
4. Turn off hotspot.
5. Next day: IPs change — restart from §1–2.

---



## 7. After this guide — changes / fixes (parked)

Fresh suite above was **green**. Do **not** change product until you decide. Candidates to discuss later (not done now):

1. True air-gap rehearsal (NIC off) vs keeping honest LAN claim
2. Excel workflow (PS description; not Expected Solution bullet)
3. Stronger sandbox isolation than host-process
4. Token streaming (beyond phase chips)
5. PPT / pitch scrub for overclaims
6. Desk dual-model timing rehearsal on 8GB VRAM

---



## 8. One-page cheat sheet

**A**

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Ollama;" + $env:Path
$env:OLLAMA_HOST = "0.0.0.0:11434"
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" serve
# other window: Invoke-RestMethod http://<A-IP>:11434/api/tags
```

**B**

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"
ping <A-IP>
.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
python backend/scripts/restart_api.py
Invoke-RestMethod http://127.0.0.1:8080/inference/status
python backend/scripts/robust_ps_workflows.py
cd apps\kwb-app; npm run electron:dev
```

**Desk story:** WF1 dual model → WF2 Word leave → WF3 sandbox → WF4 PNG → WF5 Monitor/deny.