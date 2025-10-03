@echo off
REM Batch script para Windows - Inicio rápido de Docker
REM ====================================================

echo.
echo ========================================
echo   PREDICCION DE VENTAS - DOCKER
echo ========================================
echo.

REM Verificar si Docker está corriendo
docker ps >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Docker Desktop no esta ejecutandose
    echo.
    echo Por favor:
    echo 1. Abre Docker Desktop
    echo 2. Espera a que este listo ^(icono verde^)
    echo 3. Ejecuta este script nuevamente
    echo.
    pause
    exit /b 1
)

echo [OK] Docker Desktop esta ejecutandose
echo.

:menu
cls
echo ========================================
echo   PREDICCION DE VENTAS - MENU
echo ========================================
echo.
echo 1. Iniciar todos los servicios
echo 2. Iniciar solo Jupyter Lab
echo 3. Iniciar solo Dashboard
echo 4. Ver estado de servicios
echo 5. Ver logs
echo 6. Detener servicios
echo 7. Abrir URLs
echo 0. Salir
echo.
set /p choice="Selecciona una opcion: "

if "%choice%"=="1" goto start_all
if "%choice%"=="2" goto start_jupyter
if "%choice%"=="3" goto start_streamlit
if "%choice%"=="4" goto status
if "%choice%"=="5" goto logs
if "%choice%"=="6" goto stop
if "%choice%"=="7" goto open_urls
if "%choice%"=="0" goto end
goto menu

:start_all
echo.
echo Iniciando todos los servicios...
docker-compose up -d
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Servicios iniciados correctamente
    echo.
    echo Accede a:
    echo   Jupyter Lab: http://localhost:8888
    echo   Dashboard:   http://localhost:8501
) else (
    echo.
    echo [ERROR] Hubo un problema al iniciar los servicios
)
echo.
pause
goto menu

:start_jupyter
echo.
echo Iniciando Jupyter Lab...
docker-compose up -d jupyter
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Jupyter Lab iniciado
    echo.
    echo Accede a: http://localhost:8888
    timeout /t 3 >nul
    start http://localhost:8888
) else (
    echo.
    echo [ERROR] Hubo un problema al iniciar Jupyter
)
echo.
pause
goto menu

:start_streamlit
echo.
echo Iniciando Dashboard...
docker-compose up -d streamlit
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Dashboard iniciado
    echo.
    echo Accede a: http://localhost:8501
    timeout /t 3 >nul
    start http://localhost:8501
) else (
    echo.
    echo [ERROR] Hubo un problema al iniciar el Dashboard
)
echo.
pause
goto menu

:status
echo.
echo Estado de los servicios:
echo ========================
docker-compose ps
echo.
pause
goto menu

:logs
echo.
echo Logs de servicios ^(Ctrl+C para salir^):
echo ========================================
docker-compose logs -f
goto menu

:stop
echo.
echo Deteniendo servicios...
docker-compose stop
echo.
echo [OK] Servicios detenidos
echo.
pause
goto menu

:open_urls
echo.
echo Abriendo URLs en navegador...
start http://localhost:8888
timeout /t 1 >nul
start http://localhost:8501
echo.
echo [OK] URLs abiertas
echo.
pause
goto menu

:end
echo.
echo Hasta luego!
echo.
exit /b 0
