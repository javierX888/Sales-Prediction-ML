# PowerShell Script - Gestión de Contenedores Docker
# ===================================================
# Script para facilitar el uso de Docker en Windows

# Colores para output
$info = "Cyan"
$success = "Green"
$error = "Red"
$warning = "Yellow"

function Show-Menu {
    Clear-Host
    Write-Host "=" -ForegroundColor $info -NoNewline
    Write-Host "========================================" -ForegroundColor $info
    Write-Host "   PREDICCIÓN DE VENTAS - DOCKER MENU" -ForegroundColor $info
    Write-Host "========================================" -ForegroundColor $info
    Write-Host ""
    Write-Host "1.  Iniciar todos los servicios" -ForegroundColor $info
    Write-Host "2.  Iniciar solo Jupyter Lab" -ForegroundColor $info
    Write-Host "3.  Iniciar solo Dashboard Streamlit" -ForegroundColor $info
    Write-Host "4.  Ver logs de servicios" -ForegroundColor $info
    Write-Host "5.  Detener servicios" -ForegroundColor $info
    Write-Host "6.  Reiniciar servicios" -ForegroundColor $info
    Write-Host "7.   Reconstruir imágenes" -ForegroundColor $info
    Write-Host "8.   Limpiar contenedores y volúmenes" -ForegroundColor $info
    Write-Host "9.  Ver estado de contenedores" -ForegroundColor $info
    Write-Host "10.  Abrir terminal en Jupyter" -ForegroundColor $info
    Write-Host "11.  Abrir URLs en navegador" -ForegroundColor $info
    Write-Host "0.  Salir" -ForegroundColor $error
    Write-Host ""
}

function Start-AllServices {
    Write-Host "`n Iniciando todos los servicios..." -ForegroundColor $info
    docker-compose up -d
    if ($LASTEXITCODE -eq 0) {
        Write-Host " Servicios iniciados correctamente" -ForegroundColor $success
        Write-Host "`n URLs disponibles:" -ForegroundColor $info
        Write-Host "   Jupyter Lab: http://localhost:8888" -ForegroundColor $success
        Write-Host "   Streamlit:   http://localhost:8501" -ForegroundColor $success
    } else {
        Write-Host " Error al iniciar servicios" -ForegroundColor $error
    }
    Pause
}

function Start-Jupyter {
    Write-Host "`n Iniciando Jupyter Lab..." -ForegroundColor $info
    docker-compose up -d jupyter
    if ($LASTEXITCODE -eq 0) {
        Write-Host " Jupyter Lab iniciado" -ForegroundColor $success
        Write-Host "`n URL: http://localhost:8888" -ForegroundColor $success
        Start-Sleep -Seconds 2
        Start-Process "http://localhost:8888"
    } else {
        Write-Host " Error al iniciar Jupyter" -ForegroundColor $error
    }
    Pause
}

function Start-Streamlit {
    Write-Host "`n Iniciando Dashboard Streamlit..." -ForegroundColor $info
    docker-compose up -d streamlit
    if ($LASTEXITCODE -eq 0) {
        Write-Host " Dashboard iniciado" -ForegroundColor $success
        Write-Host "`n URL: http://localhost:8501" -ForegroundColor $success
        Start-Sleep -Seconds 2
        Start-Process "http://localhost:8501"
    } else {
        Write-Host " Error al iniciar Dashboard" -ForegroundColor $error
    }
    Pause
}

function Show-Logs {
    Write-Host "`n Logs de servicios (Ctrl+C para salir)..." -ForegroundColor $info
    docker-compose logs -f
}

function Stop-Services {
    Write-Host "`n Deteniendo servicios..." -ForegroundColor $warning
    docker-compose stop
    if ($LASTEXITCODE -eq 0) {
        Write-Host " Servicios detenidos" -ForegroundColor $success
    } else {
        Write-Host " Error al detener servicios" -ForegroundColor $error
    }
    Pause
}

function Restart-Services {
    Write-Host "`n Reiniciando servicios..." -ForegroundColor $info
    docker-compose restart
    if ($LASTEXITCODE -eq 0) {
        Write-Host " Servicios reiniciados" -ForegroundColor $success
    } else {
        Write-Host " Error al reiniciar servicios" -ForegroundColor $error
    }
    Pause
}

function Rebuild-Images {
    Write-Host "`n  Reconstruyendo imágenes..." -ForegroundColor $info
    Write-Host "  Esto puede tardar varios minutos" -ForegroundColor $warning
    docker-compose build --no-cache
    if ($LASTEXITCODE -eq 0) {
        Write-Host " Imágenes reconstruidas" -ForegroundColor $success
        Write-Host "`n¿Deseas iniciar los servicios? (S/N)" -ForegroundColor $info
        $response = Read-Host
        if ($response -eq "S" -or $response -eq "s") {
            Start-AllServices
        }
    } else {
        Write-Host " Error al reconstruir imágenes" -ForegroundColor $error
    }
    Pause
}

function Clean-Docker {
    Write-Host "`n  ADVERTENCIA: Esto eliminará contenedores y volúmenes" -ForegroundColor $warning
    Write-Host "¿Estás seguro? (S/N)" -ForegroundColor $warning
    $response = Read-Host
    
    if ($response -eq "S" -or $response -eq "s") {
        Write-Host "`nEliminando contenedores y volúmenes..." -ForegroundColor $info
        docker-compose down -v
        if ($LASTEXITCODE -eq 0) {
            Write-Host " Limpieza completada" -ForegroundColor $success
        } else {
            Write-Host " Error en la limpieza" -ForegroundColor $error
        }
    } else {
        Write-Host " Operación cancelada" -ForegroundColor $info
    }
    Pause
}

function Show-Status {
    Write-Host "`n Estado de contenedores:" -ForegroundColor $info
    Write-Host "================================" -ForegroundColor $info
    docker-compose ps
    Write-Host ""
    Write-Host " Uso de imágenes:" -ForegroundColor $info
    Write-Host "================================" -ForegroundColor $info
    docker images | Select-String "sales-prediction"
    Pause
}

function Open-Terminal {
    Write-Host "`n Abriendo terminal en contenedor Jupyter..." -ForegroundColor $info
    docker-compose exec jupyter bash
}

function Open-URLs {
    Write-Host "`n Abriendo URLs en navegador..." -ForegroundColor $info
    Start-Process "http://localhost:8888"
    Start-Sleep -Seconds 1
    Start-Process "http://localhost:8501"
    Write-Host " URLs abiertas" -ForegroundColor $success
    Pause
}

# Loop principal
do {
    Show-Menu
    $selection = Read-Host "Selecciona una opción"
    
    switch ($selection) {
        '1' { Start-AllServices }
        '2' { Start-Jupyter }
        '3' { Start-Streamlit }
        '4' { Show-Logs }
        '5' { Stop-Services }
        '6' { Restart-Services }
        '7' { Rebuild-Images }
        '8' { Clean-Docker }
        '9' { Show-Status }
        '10' { Open-Terminal }
        '11' { Open-URLs }
        '0' { 
            Write-Host "`n ¡Hasta luego!" -ForegroundColor $success
            exit 
        }
        default { 
            Write-Host "`n Opción inválida" -ForegroundColor $error
            Pause
        }
    }
} while ($true)
