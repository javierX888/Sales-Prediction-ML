# 🐳 Guía de Docker para Predicción de Ventas

## 📋 Prerequisitos

- **Docker Desktop** instalado y ejecutándose
- Git (opcional, para clonar el repositorio)

## 🚀 Inicio Rápido

### 1️⃣ Construir e Iniciar los Contenedores

```powershell
# Construir las imágenes Docker
docker-compose build

# Iniciar todos los servicios
docker-compose up -d
```

### 2️⃣ Acceder a los Servicios

Una vez iniciados los contenedores, puedes acceder a:

- **Jupyter Lab**: http://localhost:8888
- **Streamlit Dashboard**: http://localhost:8501

## 🎯 Comandos Principales

### Gestión de Contenedores

```powershell
# Iniciar servicios
docker-compose up -d

# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f jupyter
docker-compose logs -f streamlit

# Detener servicios
docker-compose stop

# Detener y eliminar contenedores
docker-compose down

# Detener y eliminar contenedores + volúmenes
docker-compose down -v
```

### Ejecutar Comandos en los Contenedores

```powershell
# Acceder a la terminal de Jupyter
docker-compose exec jupyter bash

# Ejecutar un script Python
docker-compose exec jupyter python src/data_loader.py

# Acceder a Python interactivo
docker-compose exec jupyter python

# Instalar paquete adicional
docker-compose exec jupyter pip install nombre-paquete
```

### Trabajar con Notebooks

```powershell
# Listar notebooks
docker-compose exec jupyter ls notebooks/

# Ejecutar notebook desde terminal (nbconvert)
docker-compose exec jupyter jupyter nbconvert --to notebook --execute notebooks/01_EDA.ipynb
```

## 📦 Servicios Disponibles

### 🔬 Jupyter Lab (`jupyter`)
- **Puerto**: 8888
- **Uso**: Desarrollo de notebooks, análisis exploratorio
- **Comando**: `docker-compose up jupyter`

### 📊 Streamlit Dashboard (`streamlit`)
- **Puerto**: 8501
- **Uso**: Dashboard interactivo de predicciones
- **Comando**: `docker-compose up streamlit`

### 🐍 Python Scripts (`python-scripts`)
- **Uso**: Ejecutar scripts Python en background
- **Comando**: `docker-compose exec python-scripts python tu_script.py`

## 🔧 Configuración

### Variables de Entorno

Copia `.env.example` a `.env` y configura tus variables:

```powershell
Copy-Item .env.example .env
```

### Volúmenes Montados

Los siguientes directorios están sincronizados con el contenedor:
- `./data` → `/app/data`
- `./notebooks` → `/app/notebooks`
- `./src` → `/app/src`
- `./models` → `/app/models`
- `./app` → `/app/app`

## 🔄 Actualizar Dependencias

Si agregas nuevas dependencias a `requirements.txt`:

```powershell
# Reconstruir imagen
docker-compose build --no-cache

# Reiniciar servicios
docker-compose up -d
```

## 🐛 Solución de Problemas

### Puerto ya en uso

```powershell
# Ver qué está usando el puerto 8888
netstat -ano | findstr :8888

# Cambiar puerto en docker-compose.yml
# Cambiar "8888:8888" a "8889:8888"
```

### Contenedor no inicia

```powershell
# Ver logs detallados
docker-compose logs jupyter

# Reiniciar desde cero
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Permisos de archivos

```powershell
# Acceder como root
docker-compose exec -u root jupyter bash
```

## 📊 Uso del Proyecto

### 1. Análisis Exploratorio (EDA)

```powershell
# Iniciar Jupyter
docker-compose up -d jupyter

# Abrir: http://localhost:8888
# Navegar a: notebooks/01_EDA.ipynb
```

### 2. Feature Engineering

```powershell
# Ejecutar notebook
# Abrir: notebooks/02_Feature_Engineering.ipynb
```

### 3. Modelado

```powershell
# Entrenar modelos
# Abrir: notebooks/03_Modeling.ipynb
```

### 4. Dashboard

```powershell
# Iniciar dashboard
docker-compose up -d streamlit

# Abrir: http://localhost:8501
```

## 🎯 Workflows Comunes

### Desarrollo Completo

```powershell
# 1. Iniciar todo
docker-compose up -d

# 2. Trabajar en Jupyter (http://localhost:8888)
# - Ejecutar notebooks en orden: 01, 02, 03

# 3. Ver resultados en Dashboard (http://localhost:8501)

# 4. Al terminar
docker-compose stop
```

### Solo Dashboard

```powershell
# Si ya tienes modelos entrenados
docker-compose up -d streamlit

# Abrir: http://localhost:8501
```

### Ejecutar Scripts

```powershell
# Script de entrenamiento
docker-compose exec python-scripts python -c "from src.models import SalesPredictor; print('Model ready!')"

# Script personalizado
docker-compose exec python-scripts python tu_script.py
```

## 🔒 Seguridad

### Agregar Contraseña a Jupyter

```powershell
# Generar hash de contraseña
docker-compose exec jupyter python -c "from notebook.auth import passwd; print(passwd())"

# Copiar hash y agregar a docker-compose.yml:
# --NotebookApp.password='tu_hash_aqui'
```

## 📚 Recursos Adicionales

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/)

## 🆘 Ayuda

Si encuentras problemas:

1. Revisa los logs: `docker-compose logs -f`
2. Verifica que Docker Desktop esté ejecutándose
3. Asegúrate de tener permisos de administrador
4. Revisa que los puertos 8888 y 8501 estén libres

---

**¡Listo para empezar! 🚀**

```powershell
docker-compose up -d
```
