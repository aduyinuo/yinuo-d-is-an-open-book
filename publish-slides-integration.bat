@echo off
setlocal
title Publish the Annotated Slides integration to GitBook
cd /d "%~dp0"

echo ===============================================================
echo  Publishing the Annotated Slides integration to GitBook
echo ===============================================================
echo.

where node >nul 2>&1
if errorlevel 1 (
  echo Node.js was not found. Install it from https://nodejs.org and run this again.
  pause
  exit /b 1
)
for /f "tokens=*" %%v in ('node --version') do echo Node %%v found.
echo.

echo [1/4] Installing the GitBook CLI (this can take a minute)...
call npm install -g @gitbook/cli
if errorlevel 1 (
  echo.
  echo npm could not install the CLI. If it is a permissions error, right-click
  echo this file and choose "Run as administrator", then try again.
  pause
  exit /b 1
)
echo.

echo [2/4] Signing in to GitBook.
echo.
echo      Open  https://app.gitbook.com/account/developer
echo      and create a personal access token, then paste it below.
echo      Nothing is stored in this repository.
echo.
call gitbook auth
if errorlevel 1 (
  echo.
  echo Sign-in did not complete. Run this file again.
  pause
  exit /b 1
)
echo.

echo [3/4] Publishing the integration...
cd integrations\slides
call npm install
call gitbook publish .
if errorlevel 1 (
  echo.
  echo Publish failed. The message above says why.
  pause
  exit /b 1
)
echo.

echo [4/4] Done.
echo.
echo  Open the integration page the CLI printed above, click Install,
echo  and choose this site's space. Then paste a deck link onto a page:
echo.
echo   https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides/asu-brown-bag.html
echo.
pause
