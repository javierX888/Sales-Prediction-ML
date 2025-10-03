# 🚀 INICIO RÁPIDO CON DOCKER

## ⚡ En 3 pasos:

### 1️⃣ Verifica que Docker Desktop esté ejecutándose
- Abre Docker Desktop
- Espera a que el ícono se ponga verde

### 2️⃣ Construye e inicia los contenedores

Opción A - Usar el script de gestión (más fácil):
```powershell
.\docker-manager.ps1
```
Luego selecciona opción **1** (Iniciar todos los servicios)

Opción B - Comandos manuales:
```powershell
# Construir imágenes (primera vez o después de cambios)
docker-compose build

# Iniciar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f
```

### 3️⃣ Accede a los servicios

| Servicio | URL | Uso |
|----------|-----|-----|
| **Jupyter Lab** | http://localhost:8888 | Notebooks de análisis |
| **Streamlit Dashboard** | http://localhost:8501 | Dashboard interactivo |

## 🎯 Flujo de Trabajo Típico

### Primera vez:
```powershell
# 1. Construir
docker-compose build

# 2. Iniciar
docker-compose up -d

# 3. Esperar ~30 segundos

# 4. Abrir en navegador
# - Jupyter: http://localhost:8888
# - Dashboard: http://localhost:8501
```

### Días siguientes:
```powershell
# Solo iniciar (si ya construiste)
docker-compose up -d

# Al terminar
docker-compose stop
```

## 🔍 Verificar que todo funciona

```powershell
# Ver estado de contenedores
docker-compose ps

# Deberías ver 3 contenedores:
# - sales-prediction-jupyter (puerto 8888)
# - sales-prediction-dashboard (puerto 8501)
# - sales-prediction-scripts
```

## 📊 Uso de Jupyter

1. Abre: http://localhost:8888
2. Navega a la carpeta `notebooks/`
3. Abre los notebooks en orden:
   - `01_EDA.ipynb`
   - `02_Feature_Engineering.ipynb`
   - `03_Modeling.ipynb`
4. Ejecuta las celdas con `Shift + Enter`

## 📈 Uso del Dashboard

1. Abre: http://localhost:8501
2. Explora las diferentes secciones:
   - Dashboard Principal
   - Predictor
   - Análisis Avanzado
   - Acerca de

## ⚠️ Solución de Problemas Comunes

### Puerto ya en uso (8888 o 8501)
```powershell
# Ver qué proceso usa el puerto
netstat -ano | findstr :8888

# Detener servicios Docker
docker-compose down

# Reiniciar
docker-compose up -d
```

### Error al construir imagen
```powershell
# Limpiar y reconstruir desde cero
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Contenedor se detiene inmediatamente
```powershell
# Ver logs del error
docker-compose logs jupyter
# o
docker-compose logs streamlit
```

### Cambios en código no se reflejan
```powershell
# Los cambios en archivos montados son automáticos
# Si no funcionan, reinicia:
docker-compose restart

# Si agregaste paquetes a requirements.txt:
docker-compose build
docker-compose up -d
```

## 🛑 Detener y Limpiar

```powershell
# Detener servicios (mantiene contenedores)
docker-compose stop

# Detener y eliminar contenedores
docker-compose down

# Eliminar todo (contenedores + volúmenes + datos)
docker-compose down -v
```

## 💡 Comandos Útiles

```powershell
# Ver logs en tiempo real
docker-compose logs -f

# Logs de un solo servicio
docker-compose logs -f jupyter

# Acceder a terminal del contenedor
docker-compose exec jupyter bash

# Ejecutar comando Python
docker-compose exec jupyter python -c "print('Hola desde Docker!')"

# Instalar paquete adicional temporalmente
docker-compose exec jupyter pip install nombre-paquete

# Ver uso de recursos
docker stats
```

## 📚 Más Información

- **Guía completa de Docker**: [DOCKER.md](DOCKER.md)
- **README principal**: [README.md](README.md)

## ✅ Checklist de Inicio

- [ ] Docker Desktop instalado y ejecutándose
- [ ] Repositorio clonado
- [ ] Ejecutado `docker-compose build`
- [ ] Ejecutado `docker-compose up -d`
- [ ] Accedido a http://localhost:8888 (Jupyter)
- [ ] Accedido a http://localhost:8501 (Dashboard)

---

**¡Listo para empezar! 🎉**

Si tienes problemas, revisa la guía completa en [DOCKER.md](DOCKER.md)
