"""
Script para generar datos de ventas sintéticos
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generar datos de ventas sintéticos
np.random.seed(42)
start_date = datetime(2020, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(1095)]  # 3 años

df = pd.DataFrame({
    'Date': dates,
    'Product': np.random.choice(['Producto A', 'Producto B', 'Producto C', 'Producto D'], 1095),
    'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 1095),
    'Sales': np.random.uniform(100, 1000, 1095) + np.random.normal(0, 50, 1095),
    'Quantity': np.random.randint(1, 50, 1095),
    'Price': np.random.uniform(10, 100, 1095)
})

# Agregar tendencia y estacionalidad
df['Sales'] = df['Sales'] + df.index * 0.5 + 200 * np.sin(df.index * 2 * np.pi / 365)
df['Sales'] = df['Sales'].clip(lower=0)

# Guardar el dataset
df.to_csv('data/raw/sales_data.csv', index=False)

print(f' Dataset generado exitosamente!')
print(f' Filas: {len(df):,}')
print(f' Columnas: {len(df.columns)}')
print(f' Fecha inicial: {df["Date"].min()}')
print(f' Fecha final: {df["Date"].max()}')
print(f' Ventas promedio: ${df["Sales"].mean():.2f}')
print(f' Ventas totales: ${df["Sales"].sum():,.2f}')
print(f'\n Archivo guardado en: data/raw/sales_data.csv')
