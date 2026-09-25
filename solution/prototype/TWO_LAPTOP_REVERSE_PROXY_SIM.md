# Two-laptop simulation — reverse proxy (after single-model PASS + 2nd model staged)

**Chosen physical link (DM):** **Phone hotspot** — see [`HOTSPOT_TWO_LAPTOP_SETUP.md`](./HOTSPOT_TWO_LAPTOP_SETUP.md).

Helpers:
- Laptop-A: `scripts/hotspot_prepare_server.ps1`
- Laptop-B: `scripts/hotspot_link_workbench.ps1 -ServerIp <A-IP>`


---

## Topology

```
LAPTOP-A  = Model / Runtime server     LAPTOP-B  = Knowledge Workbench
  Ollama (:11434) GPU                    Electron desk + FastAPI :8080
  Adopted tags only                      Grants · Orch · HITL · Word · Audit
  NO desk required                       llm_base_url → proxy → A
```

**Invariant unchanged:** Desk → Orch → Pack → **Gateway** → local-looking `/v1` only.  
Workbench must **not** open a second pipe around Gateway.

---

## Preferred link: reverse proxy on Workbench (keeps G8)

Gateway allowlists **localhost** (and optional RFC1918 peers). Safest jury story:

### Option R1 — Reverse proxy on Laptop-B (recommended)

On **Laptop-B**, run a local reverse proxy:

```text
127.0.0.1:11434  →  http://<LAPTOP-A-LAN-IP>:11434
```

Workbench config stays:

```yaml
llm_base_url: "http://127.0.0.1:11434"
```

Gateway still sees localhost → **G8 PASS**. Orch/Gateway unchanged.

**Example (Caddy on B):**

```caddy
:11434 {
  reverse_proxy <LAPTOP-A-IP>:11434
}
```

**Example (nginx on B):** listen 11434 → `proxy_pass http://<A-IP>:11434;`

**Example (SSH local forward = tunnel acting as proxy):**

```powershell
ssh -N -L 11434:127.0.0.1:11434 user@<LAPTOP-A-IP>
```

Then B’s Ollama URL remains `http://127.0.0.1:11434`.

### Option R2 — LAN peer allowlist (no proxy)

```yaml
llm_base_url: "http://<LAPTOP-A-IP>:11434"
inference_allow_hosts:
  - "<LAPTOP-A-IP>"   # RFC1918 only
```

Ollama on A: bind LAN (`OLLAMA_HOST=0.0.0.0`). **No auth** on Ollama — private LAN only; airplane / isolated AP for stage.

---

## Laptop-A (server) checklist

1. Ollama up; **no pull during demo**  
2. Tags adopted: at least `llama3.2:3b` + **2nd chat tag** (after you download offline)  
3. Optional: `config/model_station.card.example.yaml` → hand card YAML to B  
4. Firewall: allow B → A:11434 on private LAN only  

## Laptop-B (workbench) checklist

1. FastAPI `:8080` + Electron `kwb-app`  
2. Reverse proxy / SSH `-L` so `127.0.0.1:11434` hits A  
3. `python backend/scripts/validate_station_link.py` **PASS**  
4. Cards in `models.yaml` match A’s tags (inspect + code distinct `model_id`s for G1 full)  
5. Run `sim_single_model_e2e.py` adapted / Word smoke against remote via proxy  

---

## Simulation order (this machine → two boxes)

| Phase | What | Pass criteria |
|---|---|---|
| **P0** | Single laptop, one chat tag | `sim_single_model_e2e.py` PASS · G1 floor labeled |
| **P1** | Offline stage 2nd chat model on A (USB/air-gap copy — not venue pull) | `ollama list` shows 2 chat tags |
| **P2** | Same machine: point proxy/tunnel to “fake A” or second bind | station_link PASS · coding card uses 2nd tag |
| **P3** | Real two laptops + reverse proxy | Inspection Word + coding route + Monitor A · zero WAN |

---

## What we do **not** claim yet

- Two-laptop rehearsal **not** done until P3  
- G1 **full** (two `model_id`s) **not** claimed until 2nd tag exists  
- Reverse proxy ≠ physical air-gap diode / CERT  

---

## Commands (P0 now)

```powershell
cd C:\Users\THARUN PARSA\Documents\SIH26
python backend/scripts/restart_api.py
python backend/scripts/sim_single_model_e2e.py
python backend/scripts/validate_station_link.py
```

Evidence: `eval/evidence/SINGLE_MODEL_SIM.json`
