@echo off
setlocal
title Projects on the board
cd /d "%~dp0internal\activity"

where python >nul 2>&1
if errorlevel 1 (
  echo Python was not found on PATH. Install Python 3 and run this again.
  pause
  exit /b 1
)

python control_window.py
exit /b 0
