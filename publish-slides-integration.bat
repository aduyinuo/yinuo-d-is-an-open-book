@echo off
setlocal
title Publish the Annotated Slides integration to GitBook
cd /d "%~dp0integrations\slides"

echo.
echo  ==============================================================
echo   Annotated Slides - publish to GitBook
echo  ==============================================================
echo.
echo   You will be asked for one thing: a GitBook access token.
echo   Get it at  https://app.gitbook.com/account/developer
echo.

where node >nul 2>&1
if errorlevel 1 (
  echo   Node.js was not found. Install it from https://nodejs.org
  echo   and run this file again.
  echo.
  pause
  exit /b 1
)

call npm install --no-audit --no-fund
if errorlevel 1 (
  echo.
  echo   npm install failed. The message above says why.
  pause
  exit /b 1
)

node publish.mjs
if errorlevel 1 (
  echo.
  echo   Publish did not finish. The message above says why.
  pause
  exit /b 1
)

pause
