# 📁 Datos Crudos (Raw Data)

Esta carpeta contiene el dataset original de ventas.

## 📊 Dataset Incluido

✅ **El dataset YA está incluido en este repositorio**

**Nombre**: Sales Forecasting Dataset  
**Fuente**: Kaggle  
**URL**: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting  
**Archivo**: `train.csv` (2 MB)  
**Licencia**: Open Database License (ODbL)

## 🚀 Uso Inmediato

No necesitas descargar nada. El dataset ya está aquí:

```
data/raw/train.csv
```

Simplemente:
1. Clona el repositorio
2. Inicia Docker con `docker-compose up -d`
3. Abre Jupyter Lab en http://localhost:8888
4. Ejecuta los notebooks

## 📋 Información del Dataset

- **Filas**: ~8,523
- **Columnas**: 12
- **Tamaño**: 2 MB
- **Variables**: 
  - Item features (peso, tipo, precio, etc.)
  - Outlet features (ubicación, tamaño, tipo)
  - Target: Item_Outlet_Sales

## 🔄 Actualizar Dataset (Opcional)

Si quieres la versión más reciente de Kaggle:

### Opción 1: Descargar manualmente
1. Ve a: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting
2. Haz clic en "Download"
3. Descarga `train.csv`
4. Reemplaza `data/raw/train.csv`

### Opción 2: Usar script automático

Desde Jupyter Notebook:
```python
from src.data_loader import quick_load
df = quick_load(force_download=True)
```

**Requisitos**:
- Cuenta de Kaggle
- Token API configurado (kaggle.json)

## 📁 Estructura Actual

```
data/raw/
├── train.csv          # Dataset (✅ incluido en repo)
└── README.md          # Este archivo
```

## ℹ️ Columnas del Dataset

```
1. Item_Identifier          - ID único del producto
2. Item_Weight              - Peso del producto
3. Item_Fat_Content         - Contenido graso (Low Fat/Regular)
4. Item_Visibility          - % de visibilidad en tienda
5. Item_Type                - Categoría del producto
6. Item_MRP                 - Precio máximo de venta
7. Outlet_Identifier        - ID único de la tienda
8. Outlet_Establishment_Year - Año de establecimiento
9. Outlet_Size              - Tamaño de la tienda
10. Outlet_Location_Type    - Tipo de ubicación
11. Outlet_Type             - Tipo de tienda
12. Item_Outlet_Sales       - ⭐ Target (ventas)
```

---

**🎯 Proyecto listo para usar** - Solo clona y ejecuta! 🚀
