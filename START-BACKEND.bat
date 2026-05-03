@echo off
title AK Tool - YouTube Downloader Backend
color 0C

echo.
echo  ==========================================
echo    AK TOOL - YouTube Downloader Backend
echo  ==========================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python install nahi hai!
    echo  Python download karo: https://www.python.org/downloads/
    echo.
    pause
    exit /b
)

echo  [OK] Python mila!
echo.

:: Install dependencies
echo  Dependencies install ho rahi hain...
pip install -r requirements.txt --quiet
echo  [OK] Dependencies ready!
echo.

:: Run server
echo  Backend start ho raha hai...
echo  Browser mein AK-YouTube-Downloader.html open karo
echo.
echo  ==========================================
echo   Server chal raha hai: http://localhost:5000
echo   Band karne ke liye: Ctrl+C dabao
echo  ==========================================
echo.

python app.py
pause
