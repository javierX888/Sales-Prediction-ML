# 📊 Modelo de Predicción de Ventas - Machine Learning

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🐳 **Proyecto 100% Dockerizado** - No necesitas instalar Python en tu PC

## 🎯 Descripción del Proyecto

Proyecto completo de Data Science para predecir ventas utilizando técnicas avanzadas de Machine Learning. Incluye análisis exploratorio de datos (EDA), feature engineering, múltiples modelos predictivos y un dashboard interactivo.

**Objetivo:** Desarrollar un modelo predictivo robusto que ayude a optimizar decisiones de negocio basadas en predicciones de ventas precisas.

## ✨ Características Principales

- � **100% Dockerizado** - No necesitas Python instalado, solo Docker Desktop
- �📈 **Análisis Exploratorio Completo (EDA)** con visualizaciones profesionales
- 🔧 **Feature Engineering Avanzado** para mejorar el rendimiento del modelo
- 🤖 **Múltiples Modelos de ML:**
  - Linear Regression (baseline)
  - Random Forest
  - XGBoost
  - Prophet (series temporales)
- 📊 **Métricas de Evaluación:** RMSE, MAE, R², MAPE
- 🎨 **Visualizaciones Interactivas** con Plotly y Seaborn
- 🖥️ **Dashboard en Streamlit** para exploración interactiva
- 💡 **Insights de Negocio** derivados del análisis
- 🚀 **Scripts de gestión** automatizados para Windows

## 📁 Estructura del Proyecto

```
Sales-Prediction-ML/
│
├── data/
│   ├── raw/                    # Datos originales
│   └── processed/              # Datos procesados
│
├── notebooks/
│   ├── 01_EDA.ipynb           # Análisis Exploratorio de Datos
│   ├── 02_Feature_Engineering.ipynb  # Creación de variables
│   └── 03_Modeling.ipynb      # Entrenamiento de modelos
│
├── src/
│   ├── data_loader.py         # Carga de datos
│   ├── preprocessing.py       # Limpieza y transformación
│   ├── feature_engineering.py # Creación de features
│   ├── models.py              # Modelos de ML
│   └── visualization.py       # Funciones de visualización
│
├── app/
│   └── dashboard.py           # Dashboard interactivo Streamlit
│
├── models/
│   └── saved_models/          # Modelos entrenados guardados
│
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación
└── .gitignore
```

## 🚀 Instalación y Configuración

### Opción A: Usando Docker (Recomendado) 🐳

**Requisitos:**
- Docker Desktop instalado

**Inicio rápido:**

```powershell
# 1. Clonar el repositorio
git clone https://github.com/javierX888/Sales-Prediction-ML.git
cd Sales-Prediction-ML

# 2. Usar el script de gestión (Windows)
.\docker-manager.ps1

# O iniciar manualmente
docker-compose up -d

# 3. Acceder a los servicios
# Jupyter Lab: http://localhost:8888
# Dashboard: http://localhost:8501
```

📖 **[Ver guía completa de Docker](DOCKER.md)**

### Opción B: Instalación Local (Python instalado)

**Requisitos:**
- Python 3.9 o superior
- pip (gestor de paquetes de Python)

**Pasos:**

1. **Clonar el repositorio:**
```bash
git clone https://github.com/javierX888/Sales-Prediction-ML.git
cd Sales-Prediction-ML
```

2. **Crear entorno virtual:**
```powershell
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Ejecutar notebooks de análisis:**
```bash
jupyter notebook
```

5. **Lanzar dashboard:**
```bash
streamlit run app/dashboard.py
```

## 📊 Uso del Proyecto

### 1. Análisis Exploratorio (EDA)
Abrir `notebooks/01_EDA.ipynb` para explorar:
- Distribución de variables
- Correlaciones
- Outliers y valores faltantes
- Patrones temporales

### 2. Feature Engineering
Ejecutar `notebooks/02_Feature_Engineering.ipynb` para:
- Crear variables derivadas
- Codificar variables categóricas
- Normalización y escalado

### 3. Modelado
Entrenar modelos con `notebooks/03_Modeling.ipynb`:
- Comparación de algoritmos
- Optimización de hiperparámetros
- Evaluación de métricas

### 4. Dashboard Interactivo
```bash
streamlit run app/dashboard.py
```

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

## 🛠️ Tecnologías Utilizadas

- **Python 3.9+**
- **Data Science:** Pandas, NumPy, SciPy
- **Machine Learning:** Scikit-learn, XGBoost, Prophet
- **Visualización:** Matplotlib, Seaborn, Plotly
- **Dashboard:** Streamlit
- **Notebooks:** Jupyter

## 📝 Roadmap del Proyecto

- [x] Configuración inicial del proyecto
- [ ] Análisis exploratorio de datos (EDA)
- [ ] Feature engineering
- [ ] Entrenamiento de modelos
- [ ] Optimización de hiperparámetros
- [ ] Dashboard interactivo
- [ ] Documentación completa
- [ ] Deployment

## 👨‍💻 Autor

**Javier Gacitúa**  
Analista de Datos | Data Scientist

## Contacto

📧 javiergaci.q@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/javier-gacitúa)
  
## Estadísticas de GitHub

![Javier's GitHub stats](https://github-readme-stats.vercel.app/api?username=javierX888&show_icons=true&theme=default)
