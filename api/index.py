"""
Dashboard API para Vercel - Sales Prediction ML
Autor: Javier Gacitúa | Octubre 2025
"""
from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
from pathlib import Path
import os

app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

# Cargar datos de muestra
def load_data():
    """Carga datos de muestra para el dashboard"""
    try:
        # Intentar cargar desde data/raw/train.csv
        data_path = Path(__file__).parent.parent / 'data' / 'raw' / 'train.csv'
        if data_path.exists():
            df = pd.read_csv(data_path)
            # Limitar a 100 registros para Vercel
            return df.head(100)
    except Exception as e:
        print(f"Error cargando datos: {e}")
    
    # Datos dummy si no se encuentra el archivo
    return pd.DataFrame({
        'Sales': [261.96, 731.94, 14.62, 957.58, 22.37, 48.86, 7.28, 907.15, 18.50, 114.90] * 10,
        'Category': ['Furniture', 'Furniture', 'Office Supplies', 'Technology', 'Office Supplies'] * 20,
        'Region': ['South', 'South', 'West', 'West', 'West'] * 20,
        'Segment': ['Consumer', 'Consumer', 'Corporate', 'Consumer', 'Consumer'] * 20
    })

@app.route('/')
def home():
    """Página principal del dashboard"""
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    """API: Estadísticas del dataset"""
    try:
        df = load_data()
        
        # Detectar columna de ventas (Sales o sales)
        sales_col = 'Sales' if 'Sales' in df.columns else 'sales' if 'sales' in df.columns else None
        
        if sales_col:
            stats = {
                'total_records': int(len(df)),
                'mean_sales': float(df[sales_col].mean()),
                'max_sales': float(df[sales_col].max()),
                'min_sales': float(df[sales_col].min()),
                'total_sales': float(df[sales_col].sum()),
                'median_sales': float(df[sales_col].median())
            }
        else:
            stats = {
                'error': 'Columna de ventas no encontrada',
                'columns': list(df.columns)
            }
        
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data')
def get_data():
    """API: Obtener datos para gráficos"""
    try:
        df = load_data()
        
        # Limitar a 50 registros para gráficos
        sample = df.head(50)
        
        # Convertir a formato JSON serializable
        data = sample.to_dict('records')
        
        return jsonify({
            'data': data,
            'columns': list(df.columns),
            'total_records': len(df)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/categories')
def get_categories():
    """API: Análisis por categorías"""
    try:
        df = load_data()
        
        # Detectar columnas
        sales_col = 'Sales' if 'Sales' in df.columns else 'sales'
        category_col = 'Category' if 'Category' in df.columns else 'category'
        
        if category_col in df.columns and sales_col in df.columns:
            category_stats = df.groupby(category_col)[sales_col].agg(['sum', 'mean', 'count']).to_dict('index')
            
            return jsonify({
                'categories': category_stats,
                'category_column': category_col
            })
        else:
            return jsonify({'error': 'Columnas no encontradas'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    """API: Predicción simple (simulada)"""
    try:
        data = request.json
        
        # Predicción simulada basada en precio
        # En producción, aquí cargarías un modelo .pkl
        price = float(data.get('price', 100))
        quantity = int(data.get('quantity', 1))
        
        # Fórmula simple de predicción
        base_prediction = price * quantity * 1.15  # 15% de margen
        
        return jsonify({
            'prediction': round(base_prediction, 2),
            'status': 'success',
            'note': 'Predicción simulada. En producción usaría modelo ML entrenado.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/health')
def health():
    """API: Health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'Sales Prediction ML Dashboard',
        'version': '1.0.0'
    })

# Necesario para Vercel
application = app

# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
