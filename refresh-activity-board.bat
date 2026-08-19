@echo off
setlocal
title Refresh the activity board
cd /d "%~dp0internal\activity"

echo Looking at what you have been working on...
echo.

where python >nul 2>&1
if errorlevel 1 (
  echo Python was not found on PATH. Install Python 3 and run this again.
  pause
  exit /b 1
)

python -m pip install --quiet matplotlib pillow >nul 2>&1

python capture_changes.py
if errorlevel 1 goto :fail

python summarize_changes.py
if errorlevel 1 goto :fail

python ask_max.py

python collect_activity.py
if errorlevel 1 goto :fail

python render_board.py
if errorlevel 1 goto :fail

echo.
echo Board and page updated. Commit and push in GitHub Desktop to publish.
echo.
pause
exit /b 0

:fail
echo.
echo Something went wrong above. Nothing was published.
pause
exit /b 1
