# Script de Verificación de Docker
# =================================
# Verifica que Docker esté correctamente configurado

$ErrorActionPreference = "Continue"

function Write-Success {
    param($message)
    Write-Host " $message" -ForegroundColor Green
}

function Write-Failure {
    param($message)
    Write-Host " $message" -ForegroundColor Red
}

function Write-Info {
    param($message)
    Write-Host "ℹ  $message" -ForegroundColor Cyan
}

function Write-Warning {
    param($message)
    Write-Host "  $message" -ForegroundColor Yellow
}

Write-Host ""
Write-Host " VERIFICACIÓN DE CONFIGURACIÓN DOCKER" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. Verificar Docker Desktop
Write-Info "1. Verificando Docker Desktop..."
try {
    $dockerVersion = docker --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Docker Desktop instalado: $dockerVersion"
    } else {
        Write-Failure "Docker Desktop no está instalado o no está en el PATH"
        Write-Warning "Instala Docker Desktop desde: https://www.docker.com/products/docker-desktop"
        exit 1
    }
} catch {
    Write-Failure "Error al verificar Docker"
    exit 1
}

# 2. Verificar Docker Compose
Write-Info "`n2. Verificando Docker Compose..."
try {
    $composeVersion = docker-compose --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Docker Compose disponible: $composeVersion"
    } else {
        Write-Failure "Docker Compose no disponible"
        exit 1
    }
} catch {
    Write-Failure "Error al verificar Docker Compose"
    exit 1
}

# 3. Verificar que Docker esté corriendo
Write-Info "`n3. Verificando estado de Docker..."
try {
    docker ps > $null 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Docker está ejecutándose"
    } else {
        Write-Failure "Docker Desktop no está ejecutándose"
        Write-Warning "Inicia Docker Desktop y espera a que esté listo"
        exit 1
    }
} catch {
    Write-Failure "Docker no está respondiendo"
    exit 1
}

# 4. Verificar archivos necesarios
Write-Info "`n4. Verificando archivos del proyecto..."

$requiredFiles = @(
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    ".dockerignore"
)

$missingFiles = @()
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Success "Encontrado: $file"
    } else {
        Write-Failure "Falta: $file"
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-Failure "`nFaltan archivos críticos del proyecto"
    exit 1
}

# 5. Verificar estructura de directorios
Write-Info "`n5. Verificando estructura de directorios..."

$requiredDirs = @(
    "data\raw",
    "data\processed",
    "notebooks",
    "src",
    "models\saved_models",
    "app"
)

foreach ($dir in $requiredDirs) {
    if (Test-Path $dir) {
        Write-Success "Directorio existe: $dir"
    } else {
        Write-Warning "Directorio no existe: $dir (se creará automáticamente)"
    }
}

# 6. Verificar puertos disponibles
Write-Info "`n6. Verificando puertos disponibles..."

$ports = @(8888, 8501)
$portsInUse = @()

foreach ($port in $ports) {
    $connection = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
    if ($connection) {
        Write-Warning "Puerto $port está en uso"
        $portsInUse += $port
    } else {
        Write-Success "Puerto $port disponible"
    }
}

if ($portsInUse.Count -gt 0) {
    Write-Warning "`nAlgunos puertos están en uso. Si tienes problemas:"
    Write-Info "  - Detén otros servicios en esos puertos"
    Write-Info "  - O modifica los puertos en docker-compose.yml"
}

# 7. Verificar recursos de Docker
Write-Info "`n7. Verificando recursos de Docker..."
try {
    $dockerInfo = docker info 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Información de Docker obtenida correctamente"
        
        # Extraer información relevante
        $cpus = ($dockerInfo | Select-String "CPUs:").ToString().Split(':')[1].Trim()
        $memory = ($dockerInfo | Select-String "Total Memory:").ToString().Split(':')[1].Trim()
        
        Write-Info "  CPUs disponibles: $cpus"
        Write-Info "  Memoria total: $memory"
        
        # Advertir si recursos son bajos
        if ([int]$cpus -lt 2) {
            Write-Warning "  Se recomienda al menos 2 CPUs para Docker"
        }
    }
} catch {
    Write-Warning "No se pudo obtener información de recursos"
}

# 8. Verificar imágenes existentes
Write-Info "`n8. Verificando imágenes Docker existentes..."
$images = docker images --filter "reference=sales-prediction*" --format "{{.Repository}}:{{.Tag}}" 2>&1

if ($images -and $images.Count -gt 0) {
    Write-Info "Imágenes encontradas:"
    foreach ($image in $images) {
        Write-Info "  - $image"
    }
} else {
    Write-Info "No hay imágenes construidas. Se construirán al ejecutar docker-compose build"
}

# 9. Verificar contenedores existentes
Write-Info "`n9. Verificando contenedores existentes..."
$containers = docker ps -a --filter "name=sales-prediction" --format "{{.Names}} ({{.Status}})" 2>&1

if ($containers -and $containers.Count -gt 0) {
    Write-Info "Contenedores encontrados:"
    foreach ($container in $containers) {
        Write-Info "  - $container"
    }
} else {
    Write-Info "No hay contenedores creados"
}

# Resumen final
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " RESUMEN DE VERIFICACIÓN" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($missingFiles.Count -eq 0 -and $LASTEXITCODE -eq 0) {
    Write-Success "`n Todos los requisitos están satisfechos"
    Write-Host ""
    Write-Info " Próximos pasos:"
    Write-Host ""
    Write-Host "   1. Construir imágenes:" -ForegroundColor White
    Write-Host "      docker-compose build" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   2. Iniciar servicios:" -ForegroundColor White
    Write-Host "      docker-compose up -d" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   3. O usar el script de gestión:" -ForegroundColor White
    Write-Host "      .\docker-manager.ps1" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   4. Acceder a:" -ForegroundColor White
    Write-Host "      - Jupyter Lab: http://localhost:8888" -ForegroundColor Green
    Write-Host "      - Dashboard: http://localhost:8501" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Failure "`n Hay problemas que deben resolverse"
    Write-Warning "`nRevisa los mensajes de error anteriores"
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Pausar para que el usuario pueda leer
Read-Host "Presiona Enter para continuar"
