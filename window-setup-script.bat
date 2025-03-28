@echo off
setlocal enabledelayedexpansion

:: ===== Get the directory this script is in =====
set "BASEDIR=%~dp0"
cd /d "%BASEDIR%"
echo =====================================================
echo Script started at: %BASEDIR%
echo =====================================================

:: ===== Repo URLs =====
set API_REPO=https://github.com/Talai-Next/talai-api
set BACKEND_REPO=https://github.com/Talai-Next/backend
set FRONTEND_REPO=https://github.com/Talai-Next/frontend

:: ===== Branches =====
set API_BRANCH=master
set BACKEND_BRANCH=predict_service
set FRONTEND_BRANCH=demo

:: ===== Directory Names =====
set API_DIR=talai-api
set BACKEND_DIR=backend
set FRONTEND_DIR=frontend

:: ===== Clone Repositories =====
echo.
echo Cloning repositories with their respective branches...

if not exist "%API_DIR%" (
    echo Cloning talai-api from branch %API_BRANCH%...
    git clone -b %API_BRANCH% %API_REPO% %API_DIR%
) else (
    echo talai-api already exists. Skipping clone.
)

if not exist "%BACKEND_DIR%" (
    echo Cloning backend from branch %BACKEND_BRANCH%...
    git clone -b %BACKEND_BRANCH% %BACKEND_REPO% %BACKEND_DIR%
) else (
    echo backend already exists. Skipping clone.
)

if not exist "%FRONTEND_DIR%" (
    echo Cloning frontend from branch %FRONTEND_BRANCH%...
    git clone -b %FRONTEND_BRANCH% %FRONTEND_REPO% %FRONTEND_DIR%
) else (
    echo frontend already exists. Skipping clone.
)

:: ===== Detect Python =====
echo.
echo Detecting Python version...
where py > nul 2>&1
if %errorlevel%==0 (
    set PYTHON_CMD=py
    echo Python found: py
) else (
    where python3 > nul 2>&1
    if %errorlevel%==0 (
        set PYTHON_CMD=python3
        echo Python found: python3
    ) else (
        set PYTHON_CMD=python
        echo Python fallback: python
    )
)

echo.
echo ===== talai-api Setup =====
echo.
echo Setting up talai-api (port 8080)...
cd "%BASEDIR%\%API_DIR%"

echo Creating virtual environment...
%PYTHON_CMD% -m venv venv

echo Activating environment...
call .\venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

if exist sample.env (
    echo Copying .env file...
    copy /Y sample.env .env > nul
)

echo Running database migrations...
%PYTHON_CMD% manage.py migrate

echo Starting talai-api server on port 8080...
start cmd /k "%PYTHON_CMD% manage.py runserver 8080"

cd "%BASEDIR%"

echo.
echo ===== backend Setup =====
echo Setting up backend (port 8000)...
cd "%BASEDIR%\%BACKEND_DIR%"

echo Creating virtual environment...
%PYTHON_CMD% -m venv venv

echo Activating environment...
call .\venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

if exist sample.env (
    echo Copying .env file...
    copy /Y sample.env .env > nul
)

echo Running database migrations...
%PYTHON_CMD% manage.py migrate

echo Starting backend server on port 8000...
start cmd /k "%PYTHON_CMD% manage.py runserver 8000"

cd "%BASEDIR%"

echo.
echo ===== frontend Setup =====
echo Setting up frontend...
cd "%BASEDIR%\%FRONTEND_DIR%"

echo Installing frontend dependencies...
start cmd /k "cd /d %CD% && npm install && echo Done installing. && npm run dev""

cd "%BASEDIR%"

echo.
echo =====================================================
echo All servers are now running.
echo -----------------------------------------------------
echo talai-api : http://localhost:8080
echo backend   : http://localhost:8000
echo frontend  : http://localhost:5173
echo =====================================================
pause
