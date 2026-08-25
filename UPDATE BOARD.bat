@echo off
setlocal enabledelayedexpansion
title Update the activity board
cd /d "%~dp0"

echo.
echo   Updating the activity board
echo   ---------------------------
echo.

where python >nul 2>&1
if errorlevel 1 (
  echo   Python was not found on PATH. Install Python 3 and run this again.
  echo.
  pause
  exit /b 1
)

python -m pip install --quiet matplotlib pillow >nul 2>&1

rem Drop the Clockify cache so this always pulls your latest logged time
if exist "internal\activity\clockify.json" del /q "internal\activity\clockify.json"

echo   [1/5] Looking at what changed in your project folders...
python internal\activity\capture_changes.py
if errorlevel 1 goto :fail

echo.
echo   [2/5] Pulling your time from Clockify and writing the sentences...
python internal\activity\summarize_changes.py
if errorlevel 1 goto :fail

echo.
echo   [3/5] Asking about anything Clockify has no entry for...
python internal\activity\ask_max.py

echo.
echo   [4/5] Working out where you are...
python internal\activity\collect_activity.py
if errorlevel 1 goto :fail

echo.
echo   [5/5] Drawing the heatmaps and the page...
python internal\activity\render_board.py
if errorlevel 1 goto :fail

echo.
git diff --quiet && git diff --staged --quiet
if not errorlevel 1 (
  echo   The board has not changed since last time. Nothing to publish.
  echo.
  pause
  exit /b 0
)

echo   ------------------------------------------------------------
set /p PUB=  Publish this to the site now?  [Y/N]:
if /i not "!PUB!"=="Y" (
  echo.
  echo   Left it on your machine. Run this again when you want to publish.
  echo.
  pause
  exit /b 0
)

echo.
echo   Publishing...
git add -A
git commit -q -m "Refresh the activity board"
git pull --rebase -q origin main
if errorlevel 1 (
  echo.
  echo   The pull hit a conflict. Nothing was pushed. Tell Claude.
  echo.
  pause
  exit /b 1
)
git push -q origin main
if errorlevel 1 goto :fail

echo.
echo   Published. The site will show it in a minute or two.
echo.
pause
exit /b 0

:fail
echo.
echo   Something went wrong above. Nothing was published.
echo.
pause
exit /b 1
