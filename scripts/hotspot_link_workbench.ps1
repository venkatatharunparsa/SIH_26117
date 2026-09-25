# Hotspot two-laptop link - configure THIS workbench session (Laptop-B)
#
# Usage (PowerShell, repo root):
#   .\scripts\hotspot_link_workbench.ps1 -ServerIp 192.168.43.10
#   python backend/scripts/restart_api.py
#   python backend/scripts/validate_station_link.py
#
# Env applies to THIS shell only. Start API from the same window.

param(
    [Parameter(Mandatory = $true)]
    [string]$ServerIp
)

$ErrorActionPreference = "Stop"

if ($ServerIp -notmatch '^\d{1,3}(\.\d{1,3}){3}$') {
    Write-Error "ServerIp must look like 192.168.43.10 (Laptop-A IPv4 on the hotspot)."
}

$base = "http://${ServerIp}:11434"
$env:SOVEREIGN_LLM_BASE_URL = $base
$env:SOVEREIGN_INFERENCE_ALLOW_HOSTS = $ServerIp

Write-Host "SOVEREIGN_LLM_BASE_URL=$env:SOVEREIGN_LLM_BASE_URL"
Write-Host "SOVEREIGN_INFERENCE_ALLOW_HOSTS=$env:SOVEREIGN_INFERENCE_ALLOW_HOSTS"
Write-Host ""
Write-Host "Probing station..."
try {
    $r = Invoke-WebRequest -Uri "$base/api/tags" -UseBasicParsing -TimeoutSec 8
    Write-Host "OK tags HTTP $($r.StatusCode)"
} catch {
    Write-Warning "Cannot reach $base/api/tags - check hotspot, OLLAMA_HOST=0.0.0.0 on A, firewall."
    Write-Warning $_.Exception.Message
}

Write-Host ""
Write-Host "Next (same window):"
Write-Host "  python backend/scripts/restart_api.py"
Write-Host "  python backend/scripts/validate_station_link.py"
Write-Host "  cd apps\kwb-app; npm run electron:dev"
