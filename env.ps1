$nodeDir   = "C:\Program Files\Lenovo\AIAgent\mcp\node-v22.16.0-win-x64"
$gitDir    = "D:\Program Files\Git\bin"
$env:Path  = "$nodeDir;$gitDir;$env:Path"
Write-Host "Node: $(node --version)" -ForegroundColor Green
Write-Host "Git:  $(git --version)" -ForegroundColor Green
