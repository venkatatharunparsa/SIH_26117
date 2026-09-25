# Operator cold boot — phone hotspot · two laptops

**Audience:** Human operator turning both machines on from shutdown through a linked workbench session.  
**Topology:** Phone hotspot LAN peer demo — **not** an air-gap claim. Laptop-A runs Ollama; Laptop-B runs this SIH26 workbench (FastAPI + Electron desk). Models stay on A; B dials A over the hotspot.

| Machine | Role | Typical hardware |
|---------|------|------------------|
| **Phone** | Personal hotspot (same SSID for both laptops) | — |
| **Laptop-A** | Model station — Ollama on TCP **11434** | HP-class GPU box |
| **Laptop-B** | Workbench — this repo (`SIH26`) | Desk + API on `:8080` |

**Expected models on A:** `llama3.2:3b` · `qwen2.5-coder:7b` · `moondream`  
**Rule:** One model in VRAM at a time. B does not pull models for the demo.

Related (shorter / role-specific): `HOTSPOT_DETAILED_WORKFLOW.md`, `LAPTOP_A_SERVER_SETUP.md`, `LAPTOP_B_WORKBENCH_SETUP.md`.

---

## Shared — before either laptop does useful work

### Phone hotspot

1. On the phone: turn on **Personal / Mobile Hotspot**.
2. Note **SSID + password**. Prefer a normal hotspot profile — **not** guest / client-isolation Wi‑Fi if the phone offers that (isolation blocks A↔B even when both “look connected”).
3. Both laptops must join **that same SSID**. Write down the SSID you used.

### What success looks like (shared)

| Phase | Pass signal |
|-------|-------------|
| Hotspot | Both laptops show connected to the **same** SSID |
| Network | A and B Wi‑Fi IPv4 are in the **same /24** (e.g. both `192.168.43.x` or both `192.168.137.x`) |
| Ollama on A | Local tags OK; B can reach `http://<A-IP>:11434/api/tags` |
| Link on B | `/inference/status` → `mode: lan_peer_laptop_a`, `is_local: false`, label `LAPTOP-A peer (<A-IP>)` |
| Desk | Monitor banner **LAPTOP-A** (not LOCAL Laptop-B) |

**Stop** if either laptop is still on campus Ethernet-only, a different SSID, or a guest network that isolates clients.

---

## Part A — Laptop-A (model station / Ollama)

Do this on the **HP-class** machine. Do **not** start the SIH desk or FastAPI on A.

### A1 — Power on, login

1. Power on Laptop-A from shutdown.
2. Sign in to Windows as the usual demo user.
3. Plug in AC power if the demo will run more than a few minutes (GPU load).

**Success:** Desktop available; you can open PowerShell.

### A2 — Join phone hotspot; note `<A-IP>`

1. Connect Wi‑Fi to the **same** phone hotspot SSID as B will use.
2. Open PowerShell and run:

```powershell
ipconfig
```

3. Under the **Wireless LAN** adapter for the phone hotspot, copy **IPv4 Address**. Call it `<A-IP>`.  
   Examples: `192.168.43.10`, `192.168.137.25`.

**Success:** You have a non-loopback IPv4 on the hotspot adapter. Send `<A-IP>` to the operator on B (chat / sticky note).

### A3 — PATH fix for Ollama

If `ollama` is not found:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Ollama;" + $env:Path
ollama --version
```

Permanent (optional, once): add `%LOCALAPPDATA%\Programs\Ollama` to the **User** PATH via System Properties → Environment Variables, or call Ollama by full path:

```powershell
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" --version
```

**Success:** `ollama --version` prints a version (this shell or after PATH update + new shell).

### A4 — Set / confirm `OLLAMA_HOST` (User env, with port)

Ollama must listen on all interfaces so B can reach it on the hotspot.

```powershell
[Environment]::GetEnvironmentVariable("OLLAMA_HOST", "User")
setx OLLAMA_HOST "0.0.0.0:11434"
```

Confirm User value:

```powershell
[Environment]::GetEnvironmentVariable("OLLAMA_HOST", "User")
# expect: 0.0.0.0:11434
```

**Important:** `setx` does not update the *current* process. For this session also set:

```powershell
$env:OLLAMA_HOST = "0.0.0.0:11434"
```

If the Ollama **tray app** was already running under an old host bind, quit it fully (tray → Quit) before `ollama serve` below.

**Success:** User env shows `0.0.0.0:11434`; current shell has the same.

### A5 — Start `ollama serve`; verify local + LAN

1. In PowerShell (PATH + `OLLAMA_HOST` set):

```powershell
ollama serve
```

2. **Leave this window open for the whole demo.** Closing it stops the server.

3. Open a **second** PowerShell on A and verify:

```powershell
Invoke-RestMethod http://127.0.0.1:11434/api/tags
Invoke-RestMethod "http://<A-IP>:11434/api/tags"
```

**Success:** Both calls return JSON with a `models` array. LAN call using `<A-IP>` must work from A itself before you blame B.

### A6 — Models expected (pull only if missing)

Still on A (second shell; serve window stays open):

```powershell
ollama list
```

You want tags present (names must match `config/models.yaml` on B):

- `llama3.2:3b`
- `qwen2.5-coder:7b`
- `moondream`

If a tag is missing and you have network / pre-staged blobs:

```powershell
ollama pull llama3.2:3b
ollama pull qwen2.5-coder:7b
ollama pull moondream
```

Venue demo preference: **pre-stage offline**; do not rely on venue pull.

**Success:** `ollama list` shows all three tags used by the workbench cards.

### A7 — Admin firewall: inbound TCP 11434 (“Ollama LAN”)

If B can ping A but `Test-NetConnection … -Port 11434` fails, fix firewall on A.

Run **PowerShell as Administrator** on A:

```powershell
New-NetFirewallRule -DisplayName "Ollama LAN" -Direction Inbound -Protocol TCP -LocalPort 11434 -Action Allow -Profile Private
```

(If a rule already exists, confirm it Allows **TCP 11434** on **Private**.)

**Success:** From A, LAN tags still work; from B (after join), port 11434 is open (Part B3).

### A8 — Optional watch script (Desktop `Ollama_Server`)

If you copied `scripts/laptop_a_ollama_watch.py` to A (e.g. Desktop folder `Ollama_Server`):

```powershell
cd $env:USERPROFILE\Desktop\Ollama_Server
python laptop_a_ollama_watch.py
```

Leave it open. When B chats or polishes a draft, `loaded:` should show a model tag.

**Success:** Watch prints tags / IP hints and updates when B hits A.

### A9 — Keep serve open

- Do not close the `ollama serve` window.
- Do not start Electron / SIH desk on A.
- Lid open / sleep disabled for the demo window if the machine sleeps aggressively.

**A is done** until teardown. Hand `<A-IP>` to B.

---

## Part B — Laptop-B (workbench · this SIH26 repo)

Repo root (this machine):

`C:\Users\THARUN PARSA\Documents\SIH26`

### B1 — Power on, login

1. Power on Laptop-B from shutdown.
2. Sign in.
3. Open PowerShell; `cd` to the repo root above.

**Success:** Repo path exists; `.\scripts\hotspot_link_workbench.ps1` is present.

### B2 — Join SAME hotspot (Wi‑Fi /24 with A — not Ethernet-only campus)

1. Connect to the **same** phone hotspot SSID as A.
2. Confirm you are **not** relying on campus Ethernet alone while A is only on the phone hotspot.

```powershell
ipconfig
```

**Success:** B’s Wi‑Fi IPv4 is in the **same /24** as `<A-IP>`.  
**Fail:** B on Ethernet `10.x` / campus only while A is `192.168.43.x` → A is unreachable for the demo. Fix: use hotspot Wi‑Fi on B.

### B3 — Reachability to A (ping, port, tags)

```powershell
ping <A-IP>
Test-NetConnection <A-IP> -Port 11434
Invoke-RestMethod "http://<A-IP>:11434/api/tags"
```

| Result | Meaning / action |
|--------|------------------|
| Ping fails | Wrong network / isolation / wrong IP → fix hotspot join |
| Ping OK, port 11434 fails | Firewall or Ollama not bound / not serving on A → A7 / A5 |
| Tags JSON with A’s models | Continue |

**Success:** `TcpTestSucceeded : True` and tags list includes A’s models.

### B4 — ONE PowerShell: link → restart API → verify status

Use **one** PowerShell window for the next commands. Session env from the link script must be inherited by the API process.

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"

.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
```

Expect lines like:

```text
SOVEREIGN_LLM_BASE_URL=http://<A-IP>:11434
SOVEREIGN_INFERENCE_ALLOW_HOSTS=<A-IP>
OK tags HTTP 200
```

Then **in the same window**:

```powershell
python backend/scripts/restart_api.py
```

Wait until it prints `healthy`.

Verify:

```powershell
Invoke-RestMethod http://127.0.0.1:8080/inference/status
```

**Pass fields (must match):**

| Field | Expected |
|-------|----------|
| `mode` | `lan_peer_laptop_a` |
| `label` | `LAPTOP-A peer (<A-IP>)` |
| `is_local` | `False` |
| `gateway_host_ok` | `True` |
| `tags_on_target` | includes A’s models (e.g. `llama3.2:3b`, …) |

**Fail:** `mode: local_workbench_ollama` / `is_local: True` / label `LOCAL (this Laptop-B Ollama)` → API was started in another shell without link env. Stop that API and repeat B4 in **one** shell.

Optional:

```powershell
python backend/scripts/validate_station_link.py
```

Expect **PASS** (enabled card `model_id`s present on A’s tags).

#### Operator notes (B4)

- **Allow hosts:** Plain IP in `SOVEREIGN_INFERENCE_ALLOW_HOSTS` is OK after the config **NoDecode** fix — do not wrap the IP in broken JSON.
- **Port 8080:** `restart_api.py` stops the listener on 8080 then starts uvicorn. Do **not** manually start a second uvicorn if 8080 is already the linked instance. If something else owns 8080, free it or you will fight the wrong process.
- **Same shell:** Link + `restart_api` must share session env. A new PowerShell without re-running the link script points Gateway at local B again.

**Success:** `/inference/status` shows LAN peer mode and A’s tags. Keep this API shell / linked process alive for the demo.

### B5 — Start the desk (second terminal OK)

API must keep the hotspot env. Desk can be a second terminal:

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26\apps\kwb-app"
npm run electron:dev
```

**Success:** Electron window opens; title bar health shows API up.

### B6 — Monitor banner LAPTOP-A

1. In the desk title bar, click **Monitor**.
2. Tabs: **Live log** · **Status** · **Share**.
3. On **Live log** / **Status**, the LLM banner must show **LAPTOP-A** (Status short form) / label `LAPTOP-A peer (<A-IP>)` — **not** `LOCAL Laptop-B`.
4. Optional: **Refresh target** on Live log; **Copy share text** on Share (soft evidence, not CERT).

**Success:** Banner is LAPTOP-A before you run Workflow B.

---

## Proven pitfalls (real session 2026-09-20)

| Pitfall | What you see | Fix |
|---------|--------------|-----|
| `ollama` not on PATH | Command not found on A | Prepend `%LOCALAPPDATA%\Programs\Ollama` or full path to `ollama.exe` |
| PS 5.1 em-dash in `.ps1` | Script parse errors | Scripts were fixed; use current repo scripts (no fancy dashes in source) |
| B on Ethernet only | Ping / tags fail to A | Join phone hotspot Wi‑Fi; same /24 as A |
| Ping OK, port 11434 fail | `Test-NetConnection` TcpTestSucceeded False | Admin firewall inbound TCP 11434 on A (“Ollama LAN”); confirm `ollama serve` + `OLLAMA_HOST` |
| API crash on allow_hosts JSON parse | API dies / settings error on start | Fixed (NoDecode + plain IP OK); re-run link script with plain `<A-IP>` |
| Port 8080 already in use | Wrong / double API | Use `restart_api.py` once; do not double-start uvicorn |
| Link + API in different shells | `/inference/status` stays LOCAL | Same PowerShell: link script then `restart_api.py` |
| IP changed after phone sleep | Suddenly unreachable | New `ipconfig` on A; re-run B2–B4 with new `<A-IP>` |

---

## After link — Workflow B click path (operator clicks; do not automate)

Primary inspection path on orch today: **attach → Confirm extract → cite review → Word `.docx` DRAFT → Self-check → Export leave**.  
UI labels below match `Composer` / orch asks / Monitor (2026-09).

### Suggested fixture

Prefer a real file under the repo (Document…):

| File | Role |
|------|------|
| `data/fixtures/vessel_note_text.pdf` | PDF text-layer ingest (reliable day-1) |
| `data/fixtures/scan_vessel_V101.png` | Image OCR (needs Tesseract; else fixture stub / NOT live OCR) |
| `data/fixtures/README_attach_demo.md` | Plain text / markdown attach |

Bundled picker (Composer **Load fixture**): `FX-EXT-01`, `FX-SCAN-01`, `FX-SOP-THK`, `FX-README`.

### Click steps

1. **Task type** in Composer: leave **`inspection`** selected (not `coding`).
2. Click the attach control **⌁** (title: “Add context (file / fixture)”).
3. Popover **Add context (stays in background)**:
   - **Document…** → browse to e.g.  
     `C:\Users\THARUN PARSA\Documents\SIH26\data\fixtures\vessel_note_text.pdf`  
     **or**
   - Choose a fixture id → **Load fixture**.
4. Stream should show attach / extract activity. Composer may show pill **`waiting for you`**.
5. **Confirm extract** ask (orch), e.g.  
   *Confirm extract before we treat it as input… Enter to accept…*  
   Press **Enter** (or type a corrected extract, then Enter). Send button label follows the ask (affirmative empty Enter is OK).
6. Next ask: **Review citations vs company docs… Enter to LLM-polish then write DRAFT Word…**  
   Press **Enter** (or type notes for findings).  
   This step calls Gateway → Laptop-A (polish). Watch A’s serve/watch window if open.
7. When Word DRAFT is ready: ask like  
   *Self-check Word DRAFT (`….docx`) before export leave…*  
   Press **Enter**. Monitor **Status** may show `draft` filename; H2 moves toward fresh after self-check.
8. **Export leave — soft-copy DRAFT (not CERT).** Press **Enter**.  
   Path ends at export leave — no in-app forward-accept.
9. Optional downloads in Monitor **Status**:
   - **Download DRAFT** (`.docx` when Word path succeeded)
   - **Download leave pack** (requires leave-ready + `.docx`)

**Coding path note:** Composer **··· → Sandbox calc** uses sandbox HITL; inspection attach uses the orch Word path above. Do not mix narratives for the jury.

**Deny demos (optional, More menu ···):** **Inject secret (deny demo)**, **Bad model (deny demo)**, **Revoke grant** — only if you intend to show denies.

### Smoke chat (optional before attach)

Type `hi` → Enter. On A, a chat model should load. Monitor **Live log** should show orch/gateway activity toward Laptop-A — not a desk→cloud side door.

---

## After a successful Workflow B turn — inspect Monitor & audit

### Monitor (desk)

| Tab | What to look at |
|-----|-----------------|
| **Live log** | Banner label / URL; “What just happened”; **Refresh target**; **Verify audit** |
| **Status** | Short banner **LAPTOP-A**; `url`, `tags`, `grant`, `card`, `model`, `draft`, **H2**; **Download DRAFT** / **Download leave pack**; **Last denies** |
| **Share** | **Copy share text** — soft evidence for notes; explicitly **≠ CERT** |

### Audit files (high level)

On Laptop-B, append-only audit lives under:

`workspace/audit/`

Typical day files: `audit-YYYY-MM-DD.jsonl` and chain sidecar `audit-YYYY-MM-DD.chain.json`.  
Use Monitor **Verify audit** or `GET /audit/verify` for a chain check. Do not treat this as certification.

### What to look for (demo honesty)

This is a **phone-hotspot LAN peer** demo. Do **not** claim air-gap.

| Check | Honest signal |
|-------|----------------|
| Inference host is A, not B | `/inference/status` → `lan_peer_laptop_a`, `is_local: false`, label `LAPTOP-A peer (<A-IP>)`; Monitor banner **LAPTOP-A** |
| Models | `tags_on_target` / Status `tags` match A’s `ollama list`; routed `model` on Status matches card |
| Gateway allowlist | `gateway_host_ok: true` on `/inference/status`; denies if host not allowed / not private |
| No desk→LLM side door | Desk talks to FastAPI (`127.0.0.1:8080`); model calls go Pack→**Gateway**→`SOVEREIGN_LLM_BASE_URL` (A). Free-text and polish use that path — not a hidden cloud API |
| Grants / HITL before draft | Confirm extract → cite review **before** Word DRAFT; Self-check (H2) **before** Export leave |
| Secret deny (if shown) | More → **Inject secret (deny demo)** or export-check style deny; Monitor **Last denies** / stream deny — soft-copy path must not export secrets |

Deeper org air-gap / guardrail mapping is out of scope for this cold-boot manual; use the rows above for stage honesty.

---

## Shutdown / teardown

Order matters so you do not leave a stale peer IP in a random shell.

1. **B:** Close the Electron desk.
2. **B:** Optionally stop API (Ctrl+C in the API console, or end the uvicorn started by `restart_api`).
3. **A:** Stop optional watch script (Ctrl+C).
4. **A:** Stop `ollama serve` (Ctrl+C in the serve window) and/or Quit Ollama from the tray if used.
5. Turn **off** the phone hotspot when done.

**Next day:** Hotspot DHCP may give A a **new** IP. Re-run from hotspot join (A2 + B2) with a fresh `<A-IP>`; always re-run B4 link + restart in one shell. Do not reuse yesterday’s IP blindly.

For single-laptop local work later on B, open a **new** PowerShell **without** the hotspot link env (or clear `SOVEREIGN_LLM_BASE_URL` / allow hosts) so Gateway points at local loopback again.

---

## Cheat sheet (1 page)

Replace `<A-IP>` everywhere.

### Phone

- Hotspot on · same SSID · avoid guest isolation

### Laptop-A

```powershell
ipconfig
# note Wi-Fi IPv4 → <A-IP>

$env:Path = "$env:LOCALAPPDATA\Programs\Ollama;" + $env:Path
setx OLLAMA_HOST "0.0.0.0:11434"
$env:OLLAMA_HOST = "0.0.0.0:11434"

ollama serve
# leave open

# second shell:
Invoke-RestMethod http://127.0.0.1:11434/api/tags
Invoke-RestMethod "http://<A-IP>:11434/api/tags"
ollama list
# llama3.2:3b · qwen2.5-coder:7b · moondream

# Admin once if needed:
New-NetFirewallRule -DisplayName "Ollama LAN" -Direction Inbound -Protocol TCP -LocalPort 11434 -Action Allow -Profile Private

# optional:
python laptop_a_ollama_watch.py
```

### Laptop-B

```powershell
cd "C:\Users\THARUN PARSA\Documents\SIH26"

ping <A-IP>
Test-NetConnection <A-IP> -Port 11434
Invoke-RestMethod "http://<A-IP>:11434/api/tags"

# ONE shell:
.\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>
python backend/scripts/restart_api.py
Invoke-RestMethod http://127.0.0.1:8080/inference/status
# mode=lan_peer_laptop_a · LAPTOP-A peer · is_local=False · tags_on_target

# other terminal:
cd apps\kwb-app
npm run electron:dev
# Monitor → LAPTOP-A
# ⌁ → Document… → data\fixtures\vessel_note_text.pdf
# Confirm extract → cites → Word DRAFT → Self-check → Export leave
```

### Teardown

Desk → stop API (optional) → stop `ollama serve` on A → hotspot off · next session re-note `<A-IP>`.

---

## Appendix — Air-gap honesty (do not skip)

| Demo today | Air-gap later |
|------------|---------------|
| Phone hotspot **private LAN** peer A↔B | Venue: disconnect WAN NICs / airplane + LAN-only |
| Gateway allowlist RFC1918 / loopback | Same + packet capture / firewall deny egress |
| Monitor A = **evidence pack** | Still ≠ CERT-In; optional NIC screenshots in leave pack |
| Say: “on-prem Gateway · open-weight on A” | Say: “air-gapped rehearsal with NIC evidence” only when true |

**Never** claim the hotspot demo is air-gapped.

## Appendix — Agent liveliness (2026-09-20)

While a turn runs, desk shows **phase chips** on the orch tool card and Monitor Live log picks up `orch_phase` / `gateway_chat_start` via SSE `/orch/events` + audit. This is **not** Cursor token streaming.
