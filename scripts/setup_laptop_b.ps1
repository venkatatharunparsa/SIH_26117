# Setup Laptop-B (Workbench) — run on THIS PC
#   cd SIH26 repo root
#   .\scripts\setup_laptop_b.ps1

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Host "=== Laptop-B Workbench setup ==="
Write-Host "Root: $Root"
Write-Host ""

# --- Python ---
Write-Host "[1/5] Python"
python --version
if (Test-Path "$Root\backend\requirements.txt") {
    Write-Host "pip install -r backend/requirements.txt"
    python -m pip install -r "$Root\backend\requirements.txt"
}
if (Test-Path "$Root\requirements.txt") {
    Write-Host "pip install -r requirements.txt (root extras)"
    python -m pip install -r "$Root\requirements.txt"
}

# --- Node / Electron desk ---
Write-Host ""
Write-Host "[2/5] Node / kwb-app"
node --version
npm --version
Push-Location "$Root\apps\kwb-app"
npm install
Pop-Location

# --- Paths / dirs ---
Write-Host ""
Write-Host "[3/5] Workspace dirs"
@(
    "workspace\artifacts",
    "workspace\templates",
    "workspace\knowledge",
    "workspace\audit",
    "data\skills",
    "data\fixtures"
) | ForEach-Object {
    $p = Join-Path $Root $_
    New-Item -ItemType Directory -Force -Path $p | Out-Null
    Write-Host "  ok $_"
}

# --- Config check ---
Write-Host ""
Write-Host "[4/5] Config"
$models = Join-Path $Root "config\models.yaml"
$routing = Join-Path $Root "config\routing_rules.yaml"
$hotspot = Join-Path $Root "scripts\hotspot_link_workbench.ps1"
if (-not (Test-Path $models)) { Write-Error "Missing config/models.yaml" }
if (-not (Test-Path $routing)) { Write-Error "Missing config/routing_rules.yaml" }
if (-not (Test-Path $hotspot)) { Write-Error "Missing hotspot_link_workbench.ps1" }
Write-Host "  models.yaml + routing_rules.yaml + hotspot script present"
Write-Host "  Default llm_base_url should be 127.0.0.1 until hotspot_link is run"

# --- Smoke imports ---
Write-Host ""
Write-Host "[5/5] Import check"
Push-Location "$Root\backend"
python -c "from app.config import get_settings; from app import cards, word_draft, mcp_host, skills, roles; print('imports_ok', get_settings().llm_base_url)"
Pop-Location

Write-Host ""
Write-Host "=== Laptop-B setup DONE ==="
Write-Host "Next when Laptop-A is on hotspot:"
Write-Host "  .\scripts\hotspot_link_workbench.ps1 -ServerIp <A-IP>"
Write-Host "  python backend/scripts/restart_api.py"
Write-Host "  python backend/scripts/validate_station_link.py"
Write-Host "  cd apps\kwb-app; npm run electron:dev"
Write-Host ""
Write-Host "Guide: solution\prototype\LAPTOP_B_WORKBENCH_SETUP.md"
