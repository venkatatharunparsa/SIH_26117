# Cursor prompt — paste this on **Laptop-A** (model server)

Copy everything below the line into a **new Cursor chat on Laptop-A**.

---

You are setting up **Laptop-A = KWB Model Workstation** for SIH26117 Knowledge Work Bench.

## Role of this machine
- Run **Ollama only** (GPU inference).
- Do **NOT** install or run the Electron desk / FastAPI workbench here.
- Models must already be local — **never `ollama pull` during venue/demo** unless the user explicitly allows offline staging at home.

## Required models (8 GB VRAM, load one at a time)
- `llama3.2:3b` — inspection / Word polish
- `qwen2.5-coder:7b` — coding
- `moondream` — multimodal / vision

Confirm with `ollama list`. If missing, tell the user to stage offline; do not pull unless they say so.

## Tasks (do in order)
1. Verify Ollama installed; set user env `OLLAMA_HOST=0.0.0.0`; fully quit and restart Ollama.
2. Ensure Windows Firewall allows inbound TCP **11434** on Private networks.
3. Instruct user to join **phone hotspot** (same as Laptop-B).
4. Print this machine’s hotspot **IPv4** (`ipconfig` / Get-NetIPAddress) clearly as `<A-IP>` for Laptop-B.
5. Verify locally: `curl http://127.0.0.1:11434/api/tags` shows the three tags.
6. **Show live logs** so the user can see when Laptop-B calls this machine:
   - Prefer a visible PowerShell window that tails Ollama activity, OR
   - Run a small loop that polls `/api/ps` every 2s and prints loaded model + timestamp when it changes,
   - And/or enable Ollama logging if available on Windows and open the log path.
7. Keep a **status banner** in the terminal, refreshing:
   - time · OLLAMA_HOST · IPv4 · tags present · currently loaded model (from `/api/ps`) · last change
8. Write a short `LAPTOP_A_READY.txt` on the Desktop with: `<A-IP>`, tags, and the exact line Laptop-B must run:
   `.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>`

## Success criteria
- Ollama reachable on `http://<A-IP>:11434/api/tags` from another device on the hotspot.
- User can watch the A terminal and see when a model loads / requests arrive.
- User has `<A-IP>` to paste on Laptop-B.

## Do not
- Start FastAPI :8080 or Electron on A.
- Claim air-gap CERT.
- Change Laptop-B config from this machine.

Begin by checking `ollama list` and printing the hotspot IPv4.
