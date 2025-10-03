# 📁 Datos Procesados (Processed Data)

Esta carpeta contiene los datos después de limpieza, transformación y feature engineering.

## 📊 Archivos Generados Automáticamente

Los notebooks generarán estos archivos:

```
data/processed/
├── sales_clean.csv              # Datos limpios
├── sales_engineered.csv         # Con features nuevas
├── X_train.pkl                  # Features de entrenamiento
├── X_test.pkl                   # Features de prueba
├── y_train.pkl                  # Target de entrenamiento
├── y_test.pkl                   # Target de prueba
└── README.md                    # Este archivo
```

## ⚠️ Importante

- Estos archivos **NO se suben a GitHub** (están en `.gitignore`)
- Se generan automáticamente al ejecutar los notebooks
- Son archivos temporales que se recrean cuando sea necesario

## 🔄 Cómo Generar los Archivos

Si esta carpeta está vacía, no te preocupes. Ejecuta los notebooks en orden:

### 1️⃣ **01_EDA.ipynb** (Análisis Exploratorio)
- Carga `data/raw/train.csv`
- Explora los datos
- Identifica problemas

### 2️⃣ **02_Feature_Engineering.ipynb** (Ingeniería de Features)
- Limpia los datos
- Crea nuevas variables
- Guarda: `sales_clean.csv`, `sales_engineered.csv`

### 3️⃣ **03_Modeling.ipynb** (Modelado)
- Divide train/test
- Entrena modelos
- Guarda: archivos `.pkl`

## 📋 Descripción de Archivos

| Archivo | Descripción | Generado por |
|---------|-------------|--------------|
| `sales_clean.csv` | Datos sin valores nulos ni outliers | 02_Feature_Engineering.ipynb |
| `sales_engineered.csv` | Con features nuevas (lag, rolling, etc.) | 02_Feature_Engineering.ipynb |
| `X_train.pkl` | Features para entrenar modelos | 03_Modeling.ipynb |
| `X_test.pkl` | Features para evaluar modelos | 03_Modeling.ipynb |
| `y_train.pkl` | Target para entrenar | 03_Modeling.ipynb |
| `y_test.pkl` | Target para evaluar | 03_Modeling.ipynb |

## 🔍 Ver Archivos Generados

```python
import pandas as pd

# Ver datos limpios
df_clean = pd.read_csv('data/processed/sales_clean.csv')
print(df_clean.shape)

# Ver datos con features
df_eng = pd.read_csv('data/processed/sales_engineered.csv')
print(df_eng.columns)

# Ver splits de train/test
import pickle
with open('data/processed/X_train.pkl', 'rb') as f:
    X_train = pickle.load(f)
print(f"Train shape: {X_train.shape}")
```

## 🧹 Limpiar Archivos

Si quieres regenerar todo desde cero:

```powershell
# PowerShell
Remove-Item data\processed\*.csv, data\processed\*.pkl
```

```bash
# Linux/Mac
rm data/processed/*.csv data/processed/*.pkl
```

Luego ejecuta los notebooks nuevamente.

## 📚 Más Información

- Ver [`notebooks/01_EDA.ipynb`](../../notebooks/01_EDA.ipynb) para análisis inicial
- Ver [`notebooks/02_Feature_Engineering.ipynb`](../../notebooks/02_Feature_Engineering.ipynb) para feature engineering
- Ver [`notebooks/03_Modeling.ipynb`](../../notebooks/03_Modeling.ipynb) para modelado

---

**💡 Tip**: Esta carpeta se llena automáticamente al ejecutar los notebooks. No necesitas crear archivos manualmente.
