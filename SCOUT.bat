@echo off
setlocal enabledelayedexpansion
title Opportunity scout
cd /d "%~dp0"

echo.
echo   Looking for opportunities
echo   -------------------------
echo.

where python >nul 2>&1
if errorlevel 1 (
  echo   Python was not found on PATH. Install Python 3 and run this again.
  pause
  exit /b 1
)

python -m pip install --quiet pyyaml certifi >nul 2>&1

echo   [1/3] Reading the sources...
python internal\opportunities\fetch.py
if errorlevel 1 goto :fail

echo.
echo   [2/3] Scoring them against your profile...
python internal\opportunities\score.py
if errorlevel 1 goto :fail

echo.
echo   [3/3] Writing the pages...
python internal\opportunities\build_pages.py
if errorlevel 1 goto :fail

echo.
git diff --quiet && git diff --staged --quiet
if not errorlevel 1 (
  echo   Nothing has changed since the last run.
  echo.
  pause
  exit /b 0
)

set /p PUB=  Publish this to the site now?  [Y/N]:
if /i not "!PUB!"=="Y" (
  echo.
  echo   Left it on your machine.
  echo.
  pause
  exit /b 0
)

git add -A
git commit -q -m "Opportunity scout refresh"
git pull --rebase -q origin main
if errorlevel 1 (
  echo   The pull hit a conflict. Nothing was pushed.
  pause
  exit /b 1
)
git push -q origin main
if errorlevel 1 goto :fail
echo.
echo   Published.
echo.
pause
exit /b 0

:fail
echo.
echo   Something went wrong above. Nothing was published.
echo.
pause
exit /b 1
