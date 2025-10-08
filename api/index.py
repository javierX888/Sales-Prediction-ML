"""
Dashboard API para Vercel - Sales Prediction ML
Autor: Javier Gacitúa | Octubre 2025
"""
from flask import Flask, request, jsonify
from pathlib import Path
import csv

app = Flask(__name__)

# Datos de respaldo en caso de que no se encuentre el CSV
FALLBACK_DATA = [
    {'Sales': 261.96, 'Category': 'Furniture', 'Region': 'South', 'Segment': 'Consumer'},
    {'Sales': 731.94, 'Category': 'Furniture', 'Region': 'South', 'Segment': 'Consumer'},
    {'Sales': 14.62, 'Category': 'Office Supplies', 'Region': 'West', 'Segment': 'Corporate'},
    {'Sales': 957.58, 'Category': 'Technology', 'Region': 'West', 'Segment': 'Consumer'},
] * 25  # 100 registros de respaldo

def load_data():
    """Carga datos reales del CSV o datos de respaldo"""
    data_path = Path(__file__).parent.parent / 'data' / 'raw' / 'train.csv'
    
    if not data_path.exists():
        print("CSV no encontrado, usando datos de respaldo")
        return FALLBACK_DATA
    
    data = []
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= 200:  # Limitar a 200 registros para Vercel
                    break
                
                try:
                    data.append({
                        'Sales': float(row.get('Sales', 0)),
                        'Category': row.get('Category', 'Unknown'),
                        'Sub-Category': row.get('Sub-Category', 'Unknown'),
                        'Region': row.get('Region', 'Unknown'),
                        'Segment': row.get('Segment', 'Unknown'),
                        'Quantity': int(row.get('Quantity', 0)) if row.get('Quantity') else 1,
                        'Discount': float(row.get('Discount', 0)) if row.get('Discount') else 0,
                        'Profit': float(row.get('Profit', 0)) if row.get('Profit') else 0
                    })
                except (ValueError, KeyError) as e:
                    print(f"Error procesando fila {i}: {e}")
                    continue
        
        print(f"Datos cargados: {len(data)} registros del CSV")
        return data if data else FALLBACK_DATA
    except Exception as e:
        print(f"Error cargando CSV: {e}")
        return FALLBACK_DATA

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
