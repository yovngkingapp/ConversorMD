@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Conversor Markdown - Servidor

echo ========================================
echo   Conversor a Markdown - Iniciando...
echo ========================================
echo.

REM Verificar que Python responde
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no se encuentra en el PATH.
    echo Verifica que Python este instalado y agregado al PATH.
    echo.
    pause
    exit /b 1
)

echo [OK] Python detectado.
echo [OK] Carpeta actual: %cd%
echo.
echo [INFO] El navegador se abrira en 3 segundos.
echo [INFO] NO CIERRES esta ventana mientras uses el conversor.
echo [INFO] Para detener el servidor, cierra esta ventana.
echo.

REM Abrir navegador con retraso en paralelo
start "" cmd /c "timeout /t 3 /nobreak >nul & start http://localhost:5000"

REM Arrancar servidor en esta misma ventana
python app.py

echo.
echo [INFO] El servidor se detuvo.
pause