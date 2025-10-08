# Containerfile/Dockerfile para Proyecto de Predicción de Ventas
# ================================================================
# Compatible con Docker y Podman

# Usar imagen oficial de Python 3.9
FROM python:3.9-slim

# Información del mantenedor
LABEL maintainer="javiergaci.q@gmail.com"
LABEL description="Contenedor para proyecto de Predicción de Ventas con ML"
LABEL version="1.0"
LABEL compatibility="Docker y Podman"

# Establecer directorio de trabajo
WORKDIR /app

# Variables de entorno para Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Crear directorios necesarios
RUN mkdir -p data/raw data/processed models/saved_models

# Exponer puertos
# 8888 para Jupyter
# 8501 para Streamlit
EXPOSE 8888 8501

# Comando por defecto: iniciar Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
