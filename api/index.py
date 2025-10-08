"""
Dashboard API para Vercel - Sales Prediction ML
Autor: Javier Gacitúa | Octubre 2025
"""
from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)

# Datos de muestra estáticos (sin pandas para evitar problemas de compatibilidad)
SAMPLE_DATA = [
    {'Sales': 261.96, 'Category': 'Furniture', 'Region': 'South', 'Segment': 'Consumer'},
    {'Sales': 731.94, 'Category': 'Furniture', 'Region': 'South', 'Segment': 'Consumer'},
    {'Sales': 14.62, 'Category': 'Office Supplies', 'Region': 'West', 'Segment': 'Corporate'},
    {'Sales': 957.58, 'Category': 'Technology', 'Region': 'West', 'Segment': 'Consumer'},
    {'Sales': 22.37, 'Category': 'Office Supplies', 'Region': 'West', 'Segment': 'Consumer'},
    {'Sales': 48.86, 'Category': 'Furniture', 'Region': 'South', 'Segment': 'Consumer'},
    {'Sales': 7.28, 'Category': 'Office Supplies', 'Region': 'West', 'Segment': 'Corporate'},
    {'Sales': 907.15, 'Category': 'Technology', 'Region': 'West', 'Segment': 'Consumer'},
    {'Sales': 18.50, 'Category': 'Office Supplies', 'Region': 'West', 'Segment': 'Consumer'},
    {'Sales': 114.90, 'Category': 'Furniture', 'Region': 'South', 'Segment': 'Consumer'},
    {'Sales': 394.27, 'Category': 'Technology', 'Region': 'East', 'Segment': 'Corporate'},
    {'Sales': 2.544, 'Category': 'Office Supplies', 'Region': 'Central', 'Segment': 'Home Office'},
    {'Sales': 1685.60, 'Category': 'Technology', 'Region': 'West', 'Segment': 'Consumer'},
    {'Sales': 87.78, 'Category': 'Furniture', 'Region': 'Central', 'Segment': 'Consumer'},
    {'Sales': 45.20, 'Category': 'Office Supplies', 'Region': 'East', 'Segment': 'Consumer'},
] * 7  # 105 registros en total

def load_data():
    """Retorna datos de muestra"""
    return SAMPLE_DATA

@app.route('/')
def home():
    """Página principal del dashboard"""
    try:
        # Leer el HTML directamente
        html_path = Path(__file__).parent.parent / 'templates' / 'index.html'
        if html_path.exists():
            with open(html_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return '''
            <!DOCTYPE html>
            <html>
            <head><title>Sales Prediction ML</title></head>
            <body>
                <h1>Sales Prediction ML Dashboard</h1>
                <p>Template not found. API endpoints available:</p>
                <ul>
                    <li>/api/health</li>
                    <li>/api/stats</li>
                    <li>/api/data</li>
                    <li>/api/categories</li>
                    <li>/api/predict (POST)</li>
                </ul>
            </body>
            </html>
            '''
    except Exception as e:
        return f'<html><body><h1>Error</h1><p>{str(e)}</p></body></html>', 500

@app.route('/api/stats')
def get_stats():
    """API: Estadísticas del dataset"""
    try:
        data = load_data()
        sales = [record['Sales'] for record in data]
        
        stats = {
            'total_records': len(data),
            'mean_sales': round(sum(sales) / len(sales), 2),
            'max_sales': round(max(sales), 2),
            'min_sales': round(min(sales), 2),
            'total_sales': round(sum(sales), 2),
            'median_sales': round(sorted(sales)[len(sales) // 2], 2)
        }
        
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data')
def get_data():
    """API: Obtener datos para gráficos"""
    try:
        data = load_data()
        
        # Limitar a 50 registros para gráficos
        sample = data[:50]
        
        return jsonify({
            'data': sample,
            'columns': ['Sales', 'Category', 'Region', 'Segment'],
            'total_records': len(data)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/categories')
def get_categories():
    """API: Análisis por categorías"""
    try:
        data = load_data()
        
        # Agrupar por categoría manualmente
        categories = {}
        for record in data:
            cat = record['Category']
            if cat not in categories:
                categories[cat] = {'sales': [], 'count': 0}
            categories[cat]['sales'].append(record['Sales'])
            categories[cat]['count'] += 1
        
        # Calcular estadísticas
        category_stats = {}
        for cat, info in categories.items():
            category_stats[cat] = {
                'sum': round(sum(info['sales']), 2),
                'mean': round(sum(info['sales']) / info['count'], 2),
                'count': info['count']
            }
        
        return jsonify({
            'categories': category_stats,
            'category_column': 'Category'
        })
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
