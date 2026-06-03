@echo off
REM Quick Start Script for Employee Management System

echo.
echo ========================================
echo Employee Management System - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Checking Python installation...
python --version

echo.
echo Installing dependencies...
cd backend
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully!
echo.
echo Starting Flask server...
echo.
echo ========================================
echo Server running on http://localhost:5000
echo Open this URL in your web browser
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py
pause
