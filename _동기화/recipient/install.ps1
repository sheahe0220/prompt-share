# Install this Prompt collection as GLOBAL rules for Claude Code on another PC.
#
# Why: a friend uses the Claude desktop app (Code tab), not VS Code, and has no
# Python. Claude Code (CLI and desktop alike) reads %USERPROFILE%\.claude\CLAUDE.md
# and %USERPROFILE%\.claude\skills\ at the start of every conversation, so copying
# them there applies the rules to every NEW session. Open sessions need restarting.
#
# What it does (nothing else is touched):
#   1. backs up existing .claude\CLAUDE.md, writes _전역\CLAUDE.md there with the
#      author's machine paths replaced by this PC's paths
#      (recipient_preface.md is put first: apply flexibly, keep a per-PC memo)
#   2. copies dist\skills\* into .claude\skills\ (same-name skills are moved to
#      .claude\_backup_skills\<time>\ first) and fixes paths inside them
#   No hooks, no Python needed. Re-run after updating the folder.
#
# Run (or double-click 설치하기.bat in the folder root):
#   powershell -NoProfile -ExecutionPolicy Bypass -File _동기화\recipient\install.ps1
#   ... -Check        show what would change, write nothing
#   ... -HomeDir X    install into X\.claude instead of the real profile (testing)
#
# Saved as UTF-8 WITH BOM: Windows PowerShell 5.1 misreads UTF-8 without BOM.
# Keep the .bat ASCII only (cmd codepage differs between PCs).

param(
    [switch]$Check,
    [string]$HomeDir = $env:USERPROFILE,
    [switch]$Force
)
$ErrorActionPreference = 'Stop'

# this file lives in <root>\_동기화\recipient\ ; the rules folder is two levels up
$Here   = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root   = Split-Path -Parent (Split-Path -Parent $Here)
$Claude = Join-Path $HomeDir '.claude'
$Skills = Join-Path $Claude 'skills'
$Stamp  = Get-Date -Format 'yyyyMMdd_HHmmss'
$Utf8   = New-Object System.Text.UTF8Encoding($false)

# Source files (folder names are Korean; build them from code points so this file stays ASCII)
$GlobalDir = -join [char[]](0x5F, 0xC804, 0xC5ED)          # _전역
$SrcRules  = Join-Path (Join-Path $Root $GlobalDir) 'CLAUDE.md'
$SrcSkills = Join-Path (Join-Path $Root 'dist') 'skills'
if (-not (Test-Path $SrcRules))  { throw "missing rules file: $SrcRules" }
if (-not (Test-Path $SrcSkills)) { throw "missing skills folder: $SrcSkills" }

# Never on the author's own profile: there the rules are exported by _동기화\내보내기.py and the
# skills are junctions to the originals. Overwriting them would put the recipient preface into
# the author's rules and cut the junctions (the author asked that sharing must not affect his work).
$AuthorProfile = 'C:\Users\SGJEONG99'
if (-not $Force -and ($HomeDir.TrimEnd('\') -ieq $AuthorProfile)) {
    throw "This is the author's own profile. Use apply.bat there. (Use -HomeDir <folder> to test elsewhere.)"
}

# Paths written by the author that must point at this PC instead
$AuthorRoot = 'C:\Users\SGJEONG99\Desktop\Prompt'
$AuthorPy   = 'C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe'
$AuthorHome = 'C:\Users\SGJEONG99'

# Python on this PC, if any. The rules name one interpreter; use the local one or plain "python"
$Py = $null
foreach ($name in @('python', 'py')) {
    $c = Get-Command $name -ErrorAction SilentlyContinue
    if ($c -and $c.Source -notmatch 'WindowsApps') { $Py = $c.Source; break }   # skip the Store stub
}
if (-not $Py) { $Py = 'python' }

function Convert-Paths([string]$text) {
    # Two passes through placeholders. Replacing in place chained: once the author root
    # became this PC's root, the home-folder replace hit it again (found in a test,
    # 2026-09-22), which also happens whenever the folder sits under the user profile.
    $m = [string][char]1
    $text = $text.Replace($AuthorPy, "${m}PY${m}")
    $text = $text.Replace($AuthorRoot, "${m}ROOT${m}")
    $text = $text.Replace($AuthorHome, "${m}HOME${m}")
    $text = $text.Replace("${m}PY${m}", $Py).Replace("${m}ROOT${m}", $Root).Replace("${m}HOME${m}", $HomeDir)
    return $text
}

Write-Host "source   : $Root"
Write-Host "target   : $Claude"
Write-Host "python   : $Py"
if ($Check) { Write-Host "(check only, nothing is written)" }

# 1. global rules --------------------------------------------------------------
# recipient preface first: tells Claude these rules came from someone else's field and
# must be applied flexibly, and to keep a per-PC memo at the end of the file
$Preface = Join-Path $Here 'recipient_preface.md'
if (-not (Test-Path $Preface)) { throw "missing preface: $Preface" }
$rules = [IO.File]::ReadAllText($Preface, [Text.Encoding]::UTF8) + "`r`n" +
         [IO.File]::ReadAllText($SrcRules, [Text.Encoding]::UTF8)
$rules = Convert-Paths $rules
# the author's own PC keeps its name in $Root, so only warn elsewhere
if ($rules.Contains('SGJEONG99') -and -not $Root.Contains('SGJEONG99')) { Write-Warning "rules still mention the author's home folder" }
$dstRules = Join-Path $Claude 'CLAUDE.md'

# keep the "이 PC 메모" section the recipient's Claude wrote after the last install
$MemoHead = '## ' + (-join [char[]](0xC774, 0x20, 0x50, 0x43, 0x20, 0xBA54, 0xBAA8))   # "## 이 PC 메모"
$memo = "$MemoHead`r`n`r`n" + (-join [char[]](0xC544, 0xC9C1, 0x20, 0xC5C6, 0xC74C, 0x2E)) + "`r`n"  # "아직 없음."
if (Test-Path $dstRules) {
    $old = [IO.File]::ReadAllText($dstRules, [Text.Encoding]::UTF8)
    $k = $old.LastIndexOf($MemoHead)
    if ($k -ge 0) { $memo = $old.Substring($k) }
}
$rules = $rules.TrimEnd() + "`r`n`r`n" + $memo
if ($Check) {
    Write-Host ("[1] would write CLAUDE.md ({0} chars){1}" -f $rules.Length,
        $(if (Test-Path $dstRules) { ', backing up the existing one' } else { '' }))
} else {
    New-Item -ItemType Directory -Force -Path $Claude | Out-Null
    if (Test-Path $dstRules) {
        $bak = "$dstRules.bak.$Stamp"
        Copy-Item $dstRules $bak
        Write-Host "[1] backup  : $bak"
    }
    [IO.File]::WriteAllText($dstRules, $rules, $Utf8)
    Write-Host "[1] written : $dstRules"
}

# 2. skills -------------------------------------------------------------------
$names = @(Get-ChildItem $SrcSkills -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') })
if ($names.Count -eq 0) { throw "no skills found in $SrcSkills" }
$backupDir = Join-Path (Join-Path $Claude '_backup_skills') $Stamp
$fixed = 0
foreach ($s in $names) {
    $dst = Join-Path $Skills $s.Name
    if ($Check) {
        Write-Host ("[2] would install skill {0}{1}" -f $s.Name, $(if (Test-Path $dst) { ' (existing one backed up)' } else { '' }))
        continue
    }
    New-Item -ItemType Directory -Force -Path $Skills | Out-Null
    if (Test-Path $dst) {
        New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
        Move-Item $dst (Join-Path $backupDir $s.Name)
    }
    Copy-Item $s.FullName $dst -Recurse
    Get-ChildItem $dst -Recurse -File -Include *.md, *.py, *.txt | ForEach-Object {
        $t = [IO.File]::ReadAllText($_.FullName, [Text.Encoding]::UTF8)
        $n = Convert-Paths $t
        if ($n -ne $t) { [IO.File]::WriteAllText($_.FullName, $n, $Utf8); $fixed++ }
    }
    Write-Host "[2] skill   : $($s.Name)"
}

if (-not $Check) {
    $got = @(Get-ChildItem $Skills -Directory | Where-Object { $names.Name -contains $_.Name }).Count
    if ($got -ne $names.Count) { throw "installed $got of $($names.Count) skills" }
    if (Test-Path $backupDir) { Write-Host "    replaced skills kept in $backupDir" }
    Write-Host ("done: rules 1, skills {0}, files with paths fixed {1}" -f $got, $fixed)
    Write-Host "Start a NEW conversation in Claude (desktop Code tab or CLI) to use the rules."
    if ($Py -eq 'python') {
        Write-Host ""
        Write-Host "Python was not found. The rules work without it, but the check tools"
        Write-Host "(document, slide and manuscript checkers) and scripted figures need it."
        Write-Host "Ask Claude in a new conversation: set up Python for these rules."
    }
}
