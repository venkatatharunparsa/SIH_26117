# Laptop-A (model server) - one-time / per-session helpers for phone hotspot demo
#
# Run ON LAPTOP-A:
#   .\scripts\hotspot_prepare_server.ps1

$ErrorActionPreference = "Continue"

Write-Host "=== Laptop-A hotspot prepare ==="
Write-Host ""
Write-Host "1) Connect this PC to the PHONE HOTSPOT first."
Write-Host "2) Your hotspot IPv4 addresses:"
Write-Host ""

Get-NetIPAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue |
    Where-Object { $_.IPAddress -notlike "127.*" } |
    ForEach-Object {
        Write-Host ("   {0,-16}  (ifIndex {1})" -f $_.IPAddress, $_.InterfaceIndex)
    }

Write-Host ""
Write-Host "Copy the address for the hotspot adapter (often 192.168.43.x or 192.168.137.x)."
Write-Host "Tell Laptop-B that IP."
Write-Host ""

$current = [Environment]::GetEnvironmentVariable("OLLAMA_HOST", "User")
Write-Host "OLLAMA_HOST (user) = '$current'"
if ($current -ne "0.0.0.0") {
    Write-Host "Setting OLLAMA_HOST=0.0.0.0 (user). Restart Ollama app after this."
    setx OLLAMA_HOST "0.0.0.0" | Out-Null
} else {
    Write-Host "OLLAMA_HOST already 0.0.0.0 - still restart Ollama if it was running before setx."
}

Write-Host ""
Write-Host "Check models:"
Write-Host "  ollama list"
Write-Host "From Laptop-B after hotspot join:"
Write-Host "  curl http://<THIS-IP>:11434/api/tags"
