# Keep this PC's Claude rules in step with the author's public repo.
#
# Why: the author edits the rules often. Instead of sending a new zip each time,
# this PC keeps a git clone of github.com/sheahe0220/prompt-share (public, rules only)
# and a Claude Code SessionStart hook runs this script: git pull, and when a new
# version arrived, run install.ps1 again (it keeps the "이 PC 메모" section).
#
# Run
#   powershell -NoProfile -ExecutionPolicy Bypass -File C:\claude-prompt\update.ps1 -Install
#       first time: install the rules now and add the SessionStart hook
#   powershell -NoProfile -ExecutionPolicy Bypass -File C:\claude-prompt\update.ps1
#       what the hook runs: pull, reinstall only if something changed. Quiet otherwise.
#   ... -Uninstall   remove the hook (rules stay installed)
#   ... -HomeDir X   use X\.claude instead of the real profile (testing)
#
# A hook must never block Claude: every failure becomes a one-line message and exit 0.
# Saved as UTF-8 WITH BOM (Windows PowerShell 5.1 misreads UTF-8 without BOM).

param(
    [switch]$Install,
    [switch]$Uninstall,
    [string]$HomeDir = $env:USERPROFILE
)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)

$Root     = Split-Path -Parent $MyInvocation.MyCommand.Path
$Settings = Join-Path (Join-Path $HomeDir '.claude') 'settings.json'
$Marker   = 'prompt-share-update'
$HookCmd  = 'powershell -NoProfile -ExecutionPolicy Bypass -File ' + $MyInvocation.MyCommand.Path.Replace('\', '/')

function Say([string]$msg) {
    # SessionStart hook: a JSON systemMessage is shown to the user
    $o = @{ systemMessage = "[지침 갱신] $msg" }
    Write-Output (ConvertTo-Json -InputObject $o -Compress)
}

function Find-Installer {
    foreach ($d in Get-ChildItem $Root -Directory -Filter '_*') {
        $p = Join-Path (Join-Path $d.FullName 'recipient') 'install.ps1'
        if (Test-Path $p) { return $p }
    }
    throw "install.ps1 not found under $Root"
}

function Run-Installer {
    $out = & powershell -NoProfile -ExecutionPolicy Bypass -File (Find-Installer) -HomeDir $HomeDir 2>&1
    if ($LASTEXITCODE -ne 0) { throw ("install.ps1 failed: " + (($out | Select-Object -Last 3) -join ' / ')) }
    return $out
}

function Set-Hook([bool]$add) {
    $dir = Split-Path -Parent $Settings
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    if (Test-Path $Settings) {
        $raw = [IO.File]::ReadAllText($Settings, [Text.Encoding]::UTF8)
        Copy-Item $Settings ("$Settings.bak." + (Get-Date -Format 'yyyyMMdd_HHmmss'))
    } else { $raw = '{}' }
    if (-not $raw.Trim()) { $raw = '{}' }
    $cfg = ConvertFrom-Json $raw
    if (-not $cfg.PSObject.Properties['hooks']) { $cfg | Add-Member -NotePropertyName hooks -NotePropertyValue (New-Object PSObject) }
    $hooks = $cfg.hooks
    $list = @()
    if ($hooks.PSObject.Properties['SessionStart']) { $list = @($hooks.SessionStart) }
    # drop our old entry (path may have changed), keep everything else as is
    $list = @($list | Where-Object { -not (@($_.hooks) | Where-Object { $_.statusMessage -eq $Marker -or "$($_.command)" -like '*update.ps1*' }) })
    if ($add) {
        $entry = New-Object PSObject -Property @{ hooks = @( (New-Object PSObject -Property @{
            type = 'command'; command = $HookCmd; timeout = 60; statusMessage = $Marker }) ) }
        $list = @($entry) + $list
    }
    if ($hooks.PSObject.Properties['SessionStart']) { $hooks.PSObject.Properties.Remove('SessionStart') }
    if ($list.Count -gt 0) { $hooks | Add-Member -NotePropertyName SessionStart -NotePropertyValue $list }
    $json = ConvertTo-Json -InputObject $cfg -Depth 50
    [IO.File]::WriteAllText($Settings, $json, (New-Object System.Text.UTF8Encoding($false)))
    # read back: a broken settings.json stops Claude Code from starting
    $null = ConvertFrom-Json ([IO.File]::ReadAllText($Settings, [Text.Encoding]::UTF8))
}

try {
    if (-not (Test-Path (Join-Path $Root '.git'))) { throw "not a git clone: $Root" }
    $remote = (& git -C $Root remote get-url origin 2>$null)
    if ("$remote" -notlike '*prompt-share*') { throw "origin is not prompt-share: $remote" }

    if ($Uninstall) { Set-Hook $false; Write-Host "hook removed from $Settings"; exit 0 }

    $before = (& git -C $Root rev-parse HEAD).Trim()
    $env:GIT_TERMINAL_PROMPT = '0'
    # PS 5.1 turns native stderr into a terminating error under 'Stop'; judge by the exit code instead
    $ErrorActionPreference = 'Continue'
    $pull = & git -C $Root -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=15 pull --ff-only -q 2>&1
    $pullOk = ($LASTEXITCODE -eq 0)
    $ErrorActionPreference = 'Stop'
    $after = (& git -C $Root rev-parse HEAD).Trim()

    if ($Install) {
        Run-Installer | ForEach-Object { Write-Host $_ }
        Set-Hook $true
        Write-Host "hook added to $Settings"
        Write-Host "  $HookCmd"
        if (-not $pullOk) { Write-Host "note: git pull failed ($pull). Installed the copy already here." }
        exit 0
    }
    if (-not $pullOk) {
        $why = ("$pull" -replace '\s+', ' ').Trim()
        if ($why.Length -gt 150) { $why = $why.Substring(0, 150) }
        Say ("새 판을 받지 못했습니다(인터넷 확인). 지금 설치된 지침으로 계속합니다. " + $why)
        exit 0
    }
    if ($before -ne $after) {
        $null = Run-Installer
        $n = (& git -C $Root rev-list --count "$before..$after").Trim()
        Say "원작자가 고친 지침 ${n}건을 받아 설치했습니다. 새 대화부터 적용됩니다."
    }
} catch {
    Say ("오류: " + $_.Exception.Message)
}
exit 0
