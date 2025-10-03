# ✅ CHECKLIST DE CONFIGURACIÓN DOCKER

## 📋 Pre-requisitos

### Antes de Empezar

- [ ] **Docker Desktop instalado**
  - Descargar de: https://www.docker.com/products/docker-desktop
  - Versión mínima: 20.10+
  
- [ ] **Docker Desktop ejecutándose**
  - Verificar que el ícono esté verde
  - Esperar a que inicie completamente
  
- [ ] **Windows con WSL2 habilitado** (si usas Windows)
  - Docker Desktop lo configura automáticamente
  - Reiniciar PC si es necesario

- [ ] **Recursos suficientes asignados a Docker**
  - Mínimo 2 CPUs
  - Mínimo 4 GB RAM
  - Mínimo 20 GB espacio en disco

## 🔧 Configuración Inicial

### 1. Verificar Instalación

- [ ] Abrir PowerShell/Terminal
- [ ] Ejecutar: `docker --version`
  - ¿Sale la versión? ✅
  - ¿Error? ❌ Reinstalar Docker Desktop
  
- [ ] Ejecutar: `docker-compose --version`
  - ¿Sale la versión? ✅
  - ¿Error? ❌ Actualizar Docker Desktop
  
- [ ] Ejecutar: `docker ps`
  - ¿Muestra tabla vacía? ✅
  - ¿Error "daemon not running"? ❌ Iniciar Docker Desktop

### 2. Verificar Proyecto

- [ ] Clonar o descargar el repositorio
- [ ] Navegar a la carpeta del proyecto en terminal
- [ ] Ejecutar: `.\verify-docker.ps1`
  - ¿Todo en verde? ✅ Continuar
  - ¿Errores en rojo? ❌ Resolver problemas

### 3. Archivos Docker Presentes

Verificar que existen estos archivos:

- [ ] `Dockerfile`
- [ ] `docker-compose.yml`
- [ ] `.dockerignore`
- [ ] `requirements.txt`
- [ ] `docker-manager.ps1`
- [ ] `verify-docker.ps1`

### 4. Estructura de Carpetas

- [ ] `data/raw/` existe
- [ ] `data/processed/` existe
- [ ] `notebooks/` existe
- [ ] `src/` existe
- [ ] `models/saved_models/` existe
- [ ] `app/` existe

## 🚀 Primera Ejecución

### Construcción de Imágenes

- [ ] Ejecutar: `docker-compose build`
  - Tiempo estimado: 5-10 minutos
  - ¿Completa sin errores? ✅
  - ¿Errores? ❌ Ver logs y resolver

- [ ] Verificar imágenes creadas: `docker images`
  - ¿Aparece `sales-prediction-ml-jupyter`? ✅
  - ¿Aparece `sales-prediction-ml-streamlit`? ✅

### Inicio de Servicios

- [ ] Ejecutar: `docker-compose up -d`
  - ¿Inicia sin errores? ✅
  
- [ ] Verificar contenedores: `docker-compose ps`
  - ¿3 contenedores corriendo? ✅
  - ¿Estado "Up"? ✅

### Verificación de Acceso

- [ ] **Jupyter Lab**
  - Abrir: http://localhost:8888
  - ¿Carga la interfaz? ✅
  - ¿Puedes ver carpetas? ✅
  - ¿Puedes abrir notebook? ✅

- [ ] **Streamlit Dashboard**
  - Abrir: http://localhost:8501
  - ¿Carga el dashboard? ✅
  - ¿Se ven gráficos? ✅
  - ¿Funciona la navegación? ✅

## 🧪 Pruebas Funcionales

### Test 1: Jupyter Notebook

- [ ] Abrir: http://localhost:8888
- [ ] Navegar a `notebooks/`
- [ ] Abrir `01_EDA.ipynb`
- [ ] Ejecutar primera celda (Shift+Enter)
- [ ] ¿Se ejecuta sin errores? ✅
- [ ] ¿Se importan las librerías? ✅

### Test 2: Python en Terminal

- [ ] Ejecutar: `docker-compose exec jupyter python --version`
- [ ] ¿Muestra Python 3.9+? ✅

- [ ] Ejecutar: `docker-compose exec jupyter python -c "import pandas; print(pandas.__version__)"`
- [ ] ¿Muestra versión de pandas? ✅

### Test 3: Archivos Compartidos

- [ ] Crear archivo de prueba en `data/raw/test.txt` (desde Windows)
- [ ] Ejecutar: `docker-compose exec jupyter ls /app/data/raw/`
- [ ] ¿Aparece `test.txt`? ✅
- [ ] Eliminar archivo de prueba

### Test 4: Dashboard Interactivo

- [ ] Abrir: http://localhost:8501
- [ ] Cambiar pestaña en sidebar
- [ ] ¿Funciona la navegación? ✅
- [ ] Usar el predictor
- [ ] ¿Genera predicción? ✅

## 📊 Verificación de Logs

### Logs sin Errores

- [ ] Ejecutar: `docker-compose logs jupyter`
  - ¿Sin errores críticos? ✅
  - ¿Jupyter Lab está listo? ✅

- [ ] Ejecutar: `docker-compose logs streamlit`
  - ¿Sin errores críticos? ✅
  - ¿Streamlit corriendo? ✅

## 🔄 Ciclo Completo de Trabajo

### Flujo de Desarrollo

- [ ] Editar archivo Python en VS Code (Windows)
- [ ] Guardar cambios
- [ ] Ejecutar en Jupyter: `import src.data_loader`
- [ ] ¿Se cargan los cambios? ✅

### Flujo de Notebooks

- [ ] Abrir notebook en Jupyter
- [ ] Ejecutar celdas
- [ ] Guardar notebook
- [ ] ¿Se guarda en carpeta local? ✅
- [ ] Verificar archivo en Windows

### Flujo de Modelos

- [ ] Entrenar modelo en notebook
- [ ] Guardar en `models/saved_models/`
- [ ] Verificar archivo en Windows
- [ ] Dashboard puede cargar modelo ✅

## 🛑 Detención Correcta

### Apagar Servicios

- [ ] Ejecutar: `docker-compose stop`
- [ ] ¿Se detienen sin errores? ✅

- [ ] Verificar: `docker-compose ps`
- [ ] ¿Todos en estado "Exit"? ✅

### Reinicio

- [ ] Ejecutar: `docker-compose start`
- [ ] ¿Se inician sin errores? ✅
- [ ] ¿URLs accesibles? ✅

## 🧹 Limpieza (Opcional)

### Limpiar Recursos

- [ ] Detener: `docker-compose down`
- [ ] ¿Contenedores eliminados? ✅

- [ ] Ver imágenes: `docker images`
- [ ] Eliminar si necesario: `docker rmi sales-prediction-ml-jupyter`

## ✅ Verificación Final

### Todo Funciona Si:

- [ ] ✅ Docker Desktop está corriendo
- [ ] ✅ Contenedores iniciados con `docker-compose up -d`
- [ ] ✅ Jupyter accesible en http://localhost:8888
- [ ] ✅ Dashboard accesible en http://localhost:8501
- [ ] ✅ Puedes ejecutar notebooks
- [ ] ✅ Cambios en archivos se reflejan en contenedores
- [ ] ✅ Puedes guardar y cargar modelos
- [ ] ✅ Sin errores en logs

## 🆘 Solución de Problemas Comunes

### Puerto en uso
```powershell
# Ver qué usa el puerto
netstat -ano | findstr :8888

# Cambiar puerto en docker-compose.yml
# O detener el otro servicio
```

### Contenedor se detiene
```powershell
# Ver por qué falló
docker-compose logs jupyter

# Reconstruir
docker-compose build --no-cache
docker-compose up -d
```

### No hay espacio en disco
```powershell
# Ver uso de Docker
docker system df

# Limpiar recursos no usados
docker system prune -a
```

### Cambios no se reflejan
```powershell
# Para código Python: son automáticos

# Para requirements.txt:
docker-compose build
docker-compose up -d
```

## 📚 Recursos de Ayuda

Si algo no funciona:

1. [ ] Leer **QUICKSTART.md**
2. [ ] Ejecutar `.\verify-docker.ps1`
3. [ ] Consultar **DOCKER.md** completo
4. [ ] Revisar **DOCKER-COMMANDS.md**
5. [ ] Ver logs: `docker-compose logs -f`

## 🎉 ¡Listo!

Si todas las casillas están marcadas ✅, tu entorno Docker está perfectamente configurado.

**Próximo paso:** Abrir Jupyter Lab y comenzar el análisis!

```powershell
# Iniciar proyecto
docker-compose up -d

# Abrir Jupyter
start http://localhost:8888

# Abrir Dashboard
start http://localhost:8501
```

---

**Fecha de verificación:** _________________

**Todo funciona:** ✅ / ❌

**Notas:**
```




```
