# 🏗️ Arquitectura del Proyecto con Docker

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCKER DESKTOP (Windows)                      │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Docker Compose Network                       │  │
│  │                                                           │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌──────────┐│  │
│  │  │   JUPYTER LAB   │  │   STREAMLIT     │  │  PYTHON  ││  │
│  │  │                 │  │   DASHBOARD     │  │  SCRIPTS ││  │
│  │  │  Port: 8888     │  │   Port: 8501    │  │          ││  │
│  │  │                 │  │                 │  │          ││  │
│  │  │  ┌───────────┐  │  │  ┌───────────┐  │  │          ││  │
│  │  │  │ Notebooks │  │  │  │  Web UI   │  │  │          ││  │
│  │  │  │ 01_EDA    │  │  │  │ Dashboard │  │  │          ││  │
│  │  │  │ 02_Feature│  │  │  │ Predictor │  │  │          ││  │
│  │  │  │ 03_Model  │  │  │  │ Analytics │  │  │          ││  │
│  │  │  └───────────┘  │  │  └───────────┘  │  │          ││  │
│  │  │                 │  │                 │  │          ││  │
│  │  └────────┬────────┘  └────────┬────────┘  └────┬─────┘│  │
│  │           │                    │                 │      │  │
│  │           └────────────────────┴─────────────────┘      │  │
│  │                              │                          │  │
│  │                    ┌─────────▼─────────┐               │  │
│  │                    │  SHARED VOLUMES   │               │  │
│  │                    │                   │               │  │
│  │                    │  • data/          │               │  │
│  │                    │  • notebooks/     │               │  │
│  │                    │  • src/           │               │  │
│  │                    │  • models/        │               │  │
│  │                    │  • app/           │               │  │
│  │                    └───────────────────┘               │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │   TU PC (Windows)   │
                 │                     │
                 │  • Archivos locales │
                 │  • Sincronizados    │
                 │  • Edición directa  │
                 └─────────────────────┘
```

## 📦 Componentes del Sistema

### 1. Contenedor Jupyter Lab
- **Propósito**: Desarrollo y análisis de datos
- **Puerto**: 8888
- **Acceso**: http://localhost:8888
- **Contenido**:
  - Notebooks de análisis
  - Entorno Python completo
  - Todas las librerías de ML

### 2. Contenedor Streamlit
- **Propósito**: Dashboard interactivo
- **Puerto**: 8501
- **Acceso**: http://localhost:8501
- **Características**:
  - Visualizaciones en tiempo real
  - Predicciones interactivas
  - Análisis avanzado

### 3. Contenedor Python Scripts
- **Propósito**: Ejecutar scripts en background
- **Uso**: Procesamiento batch, entrenamientos largos
- **Acceso**: Via terminal con `docker-compose exec`

## 🔄 Flujo de Datos

```
┌──────────────┐
│  Tu PC       │
│  (Windows)   │
└──────┬───────┘
       │
       │ Editas archivos
       │ en VS Code
       │
       ▼
┌──────────────────┐
│  Volúmenes       │
│  Compartidos     │
│  (Sincronizados) │
└──────┬───────────┘
       │
       │ Los cambios se
       │ reflejan automáticamente
       │
       ▼
┌──────────────────────────────────┐
│  Contenedores Docker             │
│                                   │
│  Jupyter ──▶ Lee/Escribe datos   │
│  Streamlit ──▶ Lee modelos       │
│  Scripts ──▶ Procesa datos       │
└──────────────────────────────────┘
```

## 📊 Arquitectura de Datos

```
data/
├── raw/                    # Datos originales
│   └── *.csv              ├─▶ Leídos por Jupyter
│
├── processed/             # Datos procesados
    └── *.csv              ├─▶ Generados por notebooks
                           └─▶ Leídos por Dashboard

models/
└── saved_models/          # Modelos entrenados
    └── *.pkl              ├─▶ Generados por notebooks
                           └─▶ Usados por Dashboard

src/
├── data_loader.py         # Módulos compartidos
├── preprocessing.py       ├─▶ Usados por todos
├── feature_engineering.py │   los contenedores
├── models.py              │
└── visualization.py       ┘
```

## 🌐 Puertos y Accesos

| Puerto | Servicio | URL Local | Descripción |
|--------|----------|-----------|-------------|
| 8888 | Jupyter Lab | http://localhost:8888 | IDE de notebooks |
| 8501 | Streamlit | http://localhost:8501 | Dashboard web |

## 🔐 Seguridad y Acceso

### Jupyter Lab (Sin contraseña por defecto)
```yaml
# Para agregar contraseña, editar docker-compose.yml:
command: jupyter lab --NotebookApp.password='tu_hash'
```

### Streamlit (Acceso público en localhost)
```yaml
# Solo accesible desde tu PC por defecto
# Para acceso externo, configurar en docker-compose.yml
```

## 💾 Persistencia de Datos

### Volúmenes Montados (Persistentes)
```yaml
volumes:
  - ./data:/app/data          # ✅ Persiste
  - ./notebooks:/app/notebooks # ✅ Persiste
  - ./src:/app/src             # ✅ Persiste
  - ./models:/app/models       # ✅ Persiste
```

### Datos en Contenedor (No persistentes)
- Paquetes instalados manualmente con `pip install`
- Archivos creados fuera de las carpetas montadas
- Configuraciones temporales

**💡 Tip**: Para persistir paquetes, agrégalos a `requirements.txt` y reconstruye.

## 🔄 Ciclo de Desarrollo

```
1. Editar código en VS Code (Windows)
   └─▶ Cambios automáticamente disponibles en contenedor

2. Ejecutar en Jupyter/Streamlit (Docker)
   └─▶ Procesar datos, entrenar modelos

3. Guardar resultados (Docker)
   └─▶ Automáticamente guardados en Windows

4. Commit a Git (Windows)
   └─▶ Todo el progreso guardado
```

## 📈 Escalabilidad

### Agregar más servicios:
```yaml
# docker-compose.yml
  new-service:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    networks:
      - sales-network
```

### Recursos del sistema:
```powershell
# Ver uso de recursos
docker stats

# Limitar recursos (docker-compose.yml):
deploy:
  resources:
    limits:
      cpus: '2.0'
      memory: 4G
```

## 🐛 Debugging

### Ver logs en tiempo real:
```powershell
docker-compose logs -f jupyter
```

### Acceder a shell del contenedor:
```powershell
docker-compose exec jupyter bash
```

### Inspeccionar red:
```powershell
docker network inspect sales-prediction-ml_sales-network
```

## 🎯 Ventajas de esta Arquitectura

✅ **Sin instalación de Python** en Windows
✅ **Entorno consistente** en cualquier máquina
✅ **Múltiples servicios** corriendo simultáneamente
✅ **Aislamiento** entre proyectos
✅ **Fácil de compartir** con equipo
✅ **Desarrollo en Windows**, ejecución en Linux (contenedores)
✅ **Edición en tiempo real** sin reiniciar contenedores

---

📚 **Más información**:
- [DOCKER.md](DOCKER.md) - Guía completa de Docker
- [QUICKSTART.md](QUICKSTART.md) - Inicio rápido
- [README.md](README.md) - Documentación general
