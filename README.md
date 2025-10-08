# 📊 Modelo de Predicción de Ventas - Machine Learning

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Podman](https://img.shields.io/badge/Podman-Ready-892CA0.svg)](https://podman.io/)
[![Docker](https://img.shields.io/badge/Docker-Compatible-2496ED.svg)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🐳 **Compatible con Podman y Docker** - O ejecución nativa sin contenedores

## 🎯 Descripción del Proyecto

Proyecto completo de Data Science para predecir ventas utilizando técnicas avanzadas de Machine Learning. Incluye análisis exploratorio de datos (EDA), feature engineering, múltiples modelos predictivos y un dashboard interactivo.

**Objetivo:** Desarrollar un modelo predictivo robusto que ayude a optimizar decisiones de negocio basadas en predicciones de ventas precisas.

**Dataset:** [Sales Forecasting - Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) (9,800 registros, 18 columnas)

**Demo en vivo:** [https://sales-prediction-ml.vercel.app](https://sales-prediction-ml.vercel.app)

## ✨ Características Principales

- 🐳 **Contenedorizado** - Compatible con **Podman** (recomendado) o **Docker**
- 💻 **Ejecución Nativa** - También funciona sin contenedores
- 📈 **Análisis Exploratorio Completo (EDA)** con visualizaciones profesionales
- 🔧 **Feature Engineering Avanzado** para mejorar el rendimiento del modelo
- 🤖 **Múltiples Modelos de ML:**
  - Linear Regression (baseline)
  - Random Forest
  - XGBoost
  - Prophet (series temporales)
- 📊 **Métricas de Evaluación:** RMSE, MAE, R², MAPE
- 🎨 **Visualizaciones Interactivas** con Plotly y Seaborn
- 🖥️ **Dashboard en Streamlit** para exploración interactiva
- 🌐 **Demo desplegado en Vercel**
- 💡 **Insights de Negocio** derivados del análisis
- 🚀 **Scripts de gestión** automatizados para Windows

## 📁 Estructura del Proyecto

```
Sales-Prediction-ML/
│
├── data/
│   ├── raw/                    # Datos originales (train.csv incluido)
│   └── processed/              # Datos procesados
│
├── notebooks/
│   ├── 01_EDA.ipynb           # Análisis Exploratorio de Datos
│   ├── 02_Feature_Engineering.ipynb  # Creación de variables
│   └── 03_Modeling.ipynb      # Entrenamiento de modelos
│
├── src/
│   ├── data_loader.py         # Carga de datos (Kaggle o local)
│   ├── preprocessing.py       # Limpieza y transformación
│   ├── feature_engineering.py # Creación de features
│   ├── models.py              # Modelos de ML
│   └── visualization.py       # Funciones de visualización
│
├── app/
│   └── dashboard.py           # Dashboard interactivo Streamlit
│
├── api/                       # API Flask para Vercel
│   └── index.py              # Backend del dashboard web
│
├── templates/                 # Templates HTML
│   └── index.html            # Dashboard web
│
├── models/
│   └── saved_models/          # Modelos entrenados guardados
│
├── Dockerfile / Containerfile # Configuración de contenedor
├── docker-compose.yml         # Orquestación de servicios
├── requirements.txt           # Dependencias para Vercel (Flask + pandas)
├── requirements-full.txt      # Dependencias completas (ML, notebooks, etc.)
├── vercel.json               # Configuración para Vercel
└── README.md                  # Esta documentación
```

> **Nota:** `requirements.txt` contiene solo las dependencias mínimas para el deployment en Vercel. Para desarrollo local completo, usa `requirements-full.txt`.

## 🚀 Instalación y Configuración

Tienes **3 opciones** para ejecutar este proyecto:

---

### 🌟 Opción 1: Usando Podman (Recomendado)

[Podman](https://podman.io/) es una alternativa a Docker, sin daemon, más segura y de código abierto.

**Requisitos:**
- [Podman Desktop](https://podman-desktop.io/downloads) instalado

**Ventajas sobre Docker:**
- ✅ Sin daemon (más seguro)
- ✅ Rootless por defecto
- ✅ Compatible con Docker CLI
- ✅ Código 100% abierto
- ✅ Menor consumo de recursos

**Instalación Windows:**

```powershell
# Instalar con Winget
winget install -e --id RedHat.Podman-Desktop

# O descargar desde: https://podman-desktop.io/downloads
```

**Inicio rápido:**

```powershell
# 1. Clonar el repositorio
git clone https://github.com/javierX888/Sales-Prediction-ML.git
cd Sales-Prediction-ML

# 2. Construir e iniciar con Podman Compose
podman-compose up -d

# O usar Podman directamente
podman build -t sales-prediction .
podman run -d -p 8888:8888 -p 8501:8501 \
  -v ./data:/app/data \
  -v ./notebooks:/app/notebooks \
  sales-prediction

# 3. Acceder a los servicios
# Jupyter Lab: http://localhost:8888
# Dashboard: http://localhost:8501
```

**Comandos útiles de Podman:**

```powershell
# Ver contenedores en ejecución
podman ps

# Ver logs
podman logs sales-prediction-jupyter
podman logs sales-prediction-dashboard

# Detener servicios
podman-compose down

# Limpiar todo
podman system prune -a
```

---

### 🐳 Opción 2: Usando Docker

**Requisitos:**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado

**Inicio rápido:**

```powershell
# 1. Clonar el repositorio
git clone https://github.com/javierX888/Sales-Prediction-ML.git
cd Sales-Prediction-ML

# 2. Iniciar con Docker Compose
docker-compose up -d

# O usar script de gestión (Windows)
.\docker-manager.ps1

# 3. Acceder a los servicios
# Jupyter Lab: http://localhost:8888
# Dashboard: http://localhost:8501
```

**Comandos útiles de Docker:**

```powershell
# Ver contenedores
docker ps

# Ver logs
docker logs sales-prediction-jupyter

# Detener servicios
docker-compose down

# Reconstruir imágenes
docker-compose build --no-cache
```

📖 **[Ver guía completa de Docker](DOCKER.md)**

---

### 💻 Opción 3: Instalación Nativa (Sin Contenedores)

Para ejecutar el proyecto directamente en tu sistema sin Podman o Docker.

**Requisitos:**
- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- 4GB RAM mínimo recomendado

**Instalación Python:**

**Windows:**
```powershell
# Descargar desde: https://www.python.org/downloads/
# O instalar con Winget
winget install -e --id Python.Python.3.9

# Verificar instalación
python --version
```

**Linux/Mac:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.9 python3-pip

# macOS (con Homebrew)
brew install python@3.9
```

**Pasos de instalación:**

```bash
# 1. Clonar el repositorio
git clone https://github.com/javierX888/Sales-Prediction-ML.git
cd Sales-Prediction-ML

# 2. Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual:
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias completas (incluye ML, notebooks, etc.)
pip install --upgrade pip
pip install -r requirements-full.txt

# 4. Verificar instalación
python -c "import pandas, sklearn, xgboost; print('Instalación exitosa')"
```

**Ejecutar Jupyter Lab:**

```bash
# Iniciar Jupyter Lab
jupyter lab --port=8888 --no-browser

# Abrir en navegador: http://localhost:8888
```

**Ejecutar Dashboard:**

```bash
# Iniciar Streamlit
streamlit run app/dashboard.py --server.port=8501

# Abrir en navegador: http://localhost:8501
```

**Ejecutar notebooks:**

```bash
# Opción 1: Desde Jupyter Lab (recomendado)
jupyter lab

# Opción 2: Desde línea de comandos
jupyter nbconvert --execute --to notebook --inplace notebooks/01_EDA.ipynb
```

---

## 📊 Dataset

**Fuente:** [Sales Forecasting - Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)

**Descripción:**
- **Tamaño:** 9,800 registros
- **Columnas:** 18 variables
- **Tipo:** Datos de ventas históricos
- **Ubicación:** `data/raw/train.csv` (incluido en el repositorio)

**Columnas principales:**
- `Order Date`: Fecha del pedido
- `Sales`: Monto de la venta (variable objetivo)
- `Category`: Categoría del producto
- `Region`: Región geográfica
- `Segment`: Segmento de cliente

---

## 🎯 Uso del Proyecto

### 1️⃣ Análisis Exploratorio (EDA)

```bash
# Abrir Jupyter Lab: http://localhost:8888
# Navegar a: notebooks/01_EDA.ipynb
```

El notebook incluye:
- Carga y exploración inicial del dataset
- Análisis de valores faltantes
- Distribución de la variable objetivo (ventas)
- Análisis de correlaciones
- Detección de outliers
- Visualizaciones interactivas

### 2️⃣ Feature Engineering

```bash
# Navegar a: notebooks/02_Feature_Engineering.ipynb
```

Transformaciones incluidas:
- Features temporales (día, mes, año, día de la semana)
- Lag features (ventas pasadas)
- Rolling features (promedios móviles)
- Encoding de variables categóricas
- Normalización de features numéricas

### 3️⃣ Modelado

```bash
# Navegar a: notebooks/03_Modeling.ipynb
```

Modelos entrenados:
- Regresión Lineal (baseline)
- Random Forest
- XGBoost
- Prophet (series temporales)

Evaluación con métricas:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coeficiente de Determinación)
- MAPE (Mean Absolute Percentage Error)

### 4️⃣ Dashboard Interactivo

```bash
# Local: http://localhost:8501
# Demo: https://sales-prediction-ml.vercel.app
```

Funcionalidades del dashboard:
- Visualización de estadísticas clave
- Gráficos interactivos
- Predicción en tiempo real
- Análisis por categorías

---

## 📈 Resultados y Métricas

### Comparación de Modelos

| Modelo | RMSE | MAE | R² | MAPE |
|--------|------|-----|-----|------|
| Linear Regression | TBD | TBD | TBD | TBD |
| Random Forest | TBD | TBD | TBD | TBD |
| XGBoost | TBD | TBD | TBD | TBD |
| Prophet | TBD | TBD | TBD | TBD |

*Nota: Las métricas se actualizarán después del entrenamiento*

## 💡 Insights de Negocio

🔍 **Principales Hallazgos:**
- [Pendiente: Se completará después del análisis]

📊 **Recomendaciones:**
- [Pendiente: Se completará después del análisis]

---

## 🛠️ Tecnologías Utilizadas

| Categoría | Tecnologías |
|-----------|-------------|
| **Machine Learning** | scikit-learn 1.3.0, XGBoost 1.7.6, Prophet 1.1.4 |
| **Data Science** | Pandas 2.0.3, NumPy 1.24.3, SciPy 1.11.1 |
| **Visualización** | Matplotlib 3.7.2, Seaborn 0.12.2, Plotly 5.15.0 |
| **Dashboard** | Streamlit 1.25.0, Flask 3.0.0 (Vercel) |
| **Notebooks** | Jupyter Lab |
| **Lenguaje** | Python 3.9 |
| **Contenedores** | Podman (recomendado), Docker (compatible) |
| **Deploy** | Vercel |

---

## 📝 Roadmap del Proyecto

- [x] Configuración inicial del proyecto
- [x] Análisis exploratorio de datos (EDA)
- [x] Feature engineering
- [x] Entrenamiento de modelos
- [ ] Optimización de hiperparámetros
- [x] Dashboard interactivo
- [x] Documentación completa
- [x] Deployment en Vercel

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor

**Javier Gacitúa**

- GitHub: [@javierX888](https://github.com/javierX888)
- Email: javiergaci.q@gmail.com
- LinkedIn: [Javier Gacitúa](https://www.linkedin.com/in/javier-gacitúa)
- Proyecto: [Sales-Prediction-ML](https://github.com/javierX888/Sales-Prediction-ML)
- Demo: [https://sales-prediction-ml.vercel.app](https://sales-prediction-ml.vercel.app)

---

## 🙏 Agradecimientos

- Dataset de [Kaggle - Sales Forecasting](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
- Comunidad de Podman y Docker
- Streamlit por el framework de dashboard
- Vercel por el hosting gratuito

---

## 📚 Documentación Adicional

- [QUICKSTART.md](QUICKSTART.md) - Guía de inicio rápido
- [DOCKER.md](DOCKER.md) - Guía detallada de Docker/Podman
- [DOCKER-COMMANDS.md](DOCKER-COMMANDS.md) - Referencia de comandos
- [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitectura del proyecto
- [CHECKLIST.md](CHECKLIST.md) - Lista de verificación

---

## ⭐ Si te gustó este proyecto

Dale una estrella ⭐ al repositorio y compártelo con otros.

---

**Última actualización:** Octubre 2025
