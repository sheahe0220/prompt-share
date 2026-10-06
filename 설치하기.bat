@echo off
rem Installs this folder's rules for Claude Code (desktop Code tab and CLI) on this PC.
rem Nothing is sent anywhere. Existing rules and skills are backed up first.
rem ASCII only on purpose: install.ps1 is found by wildcard, not by its Korean folder name.
setlocal
set PS1=
for /d %%D in ("%~dp0_*") do if exist "%%D\recipient\install.ps1" set "PS1=%%D\recipient\install.ps1"
if not defined PS1 (echo install.ps1 not found next to this file & pause & exit /b 1)
powershell -NoProfile -ExecutionPolicy Bypass -File "%PS1%" %*
echo.
pause
