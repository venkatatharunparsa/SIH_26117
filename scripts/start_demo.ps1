# One-command demo start for SIH26117 Knowledge Work Bench (single laptop).
# Usage:  pwsh -File scripts/start_demo.ps1
# Requires: Python, Node, Ollama with tag llama3.2:3b already present (no pull).

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $Root "backend\app\main.py"))) {
  $Root = $PSScriptRoot
  if (-not (Test-Path (Join-Path $Root "backend\app\main.py"))) {
    Write-Error "Run from repo root: pwsh -File scripts/start_demo.ps1"
  }
}

Write-Host "KWB demo start - root: $Root" -ForegroundColor Cyan
Write-Host "Policy: Ollama inference-only · no pull · desk = apps/kwb-app" -ForegroundColor DarkGray

# Preflight Ollama (optional soft check)
try {
  $tags = Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -TimeoutSec 2
  $names = @($tags.models | ForEach-Object { $_.name })
  if ($names -notcontains "llama3.2:3b") {
    Write-Warning "Ollama up but llama3.2:3b not listed. Adopt offline before draft/retrieve."
  } else {
    Write-Host "Ollama OK · llama3.2:3b present" -ForegroundColor Green
  }
} catch {
  Write-Warning "Ollama not reachable at 127.0.0.1:11434 - start it before drafting."
}

$apiDir = Join-Path $Root "backend"
$deskDir = Join-Path $Root "apps\kwb-app"

Write-Host "Starting API on 127.0.0.1:8080 ..." -ForegroundColor Cyan
Start-Process -FilePath "python" -ArgumentList @(
  "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8080"
) -WorkingDirectory $apiDir -WindowStyle Normal

# Wait for health
$ok = $false
for ($i = 0; $i -lt 40; $i++) {
  Start-Sleep -Milliseconds 500
  try {
    $h = Invoke-RestMethod -Uri "http://127.0.0.1:8080/health" -TimeoutSec 1
    if ($h.ok) { $ok = $true; break }
  } catch { }
}
if (-not $ok) {
  Write-Error "API did not become healthy at http://127.0.0.1:8080/health"
}
Write-Host "API healthy · desk=$($h.desk)" -ForegroundColor Green

Write-Host "Starting Electron desk (apps/kwb-app) ..." -ForegroundColor Cyan
Set-Location $deskDir
if (-not (Test-Path "node_modules")) {
  Write-Host "npm install (first run) ..." -ForegroundColor Yellow
  npm install
}
npm run electron:dev
