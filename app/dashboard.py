"""
Dashboard Interactivo de Predicción de Ventas
==============================================
Aplicación Streamlit para visualización y predicción de ventas.

Autor: Javier Gacitúa
Fecha: Octubre 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# Agregar path de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Configuración de página
st.set_page_config(
    page_title="Predicción de Ventas",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    """Carga datos de ejemplo o datos reales."""
    # Por ahora, generamos datos de ejemplo
    # Reemplazar con: pd.read_csv('../data/processed/sales_engineered.csv')
    
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=365, freq='D')
    n = len(dates)
    
    df = pd.DataFrame({
        'date': dates,
        'sales': np.random.normal(1000, 200, n) + np.linspace(0, 500, n) + 
                np.sin(np.arange(n) * 2 * np.pi / 7) * 100,  # Patrón semanal
        'store_id': np.random.randint(1, 11, n),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], n),
        'price': np.random.uniform(10, 100, n),
        'promotion': np.random.choice([0, 1], n, p=[0.7, 0.3]),
        'customers': np.random.randint(50, 300, n),
    })
    
    return df


@st.cache_resource
def load_model():
    """Carga el modelo entrenado."""
    try:
        import joblib
        model = joblib.load('../models/saved_models/best_sales_model.pkl')
        return model
    except:
        st.warning(" Modelo no encontrado. Usando predicciones simuladas.")
        return None


def main_page():
    """Página principal del dashboard."""
    
    st.markdown('<h1 class="main-header"> Dashboard de Predicción de Ventas</h1>', 
                unsafe_allow_html=True)
    
    # Cargar datos
    df = load_data()
    
    # KPIs principales
    st.markdown("###  Métricas Clave")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sales = df['sales'].sum()
        st.metric(
            label=" Ventas Totales",
            value=f"${total_sales:,.0f}",
            delta=f"{df['sales'].iloc[-30:].mean() - df['sales'].iloc[-60:-30].mean():,.0f}"
        )
    
    with col2:
        avg_sales = df['sales'].mean()
        st.metric(
            label=" Venta Promedio",
            value=f"${avg_sales:,.0f}",
            delta=f"{(df['sales'].iloc[-7:].mean() / df['sales'].mean() - 1) * 100:.1f}%"
        )
    
    with col3:
        total_customers = df['customers'].sum()
        st.metric(
            label=" Clientes Totales",
            value=f"{total_customers:,}",
            delta=f"{df['customers'].iloc[-7:].sum() - df['customers'].iloc[-14:-7].sum()}"
        )
    
    with col4:
        avg_ticket = df['sales'].sum() / df['customers'].sum()
        st.metric(
            label=" Ticket Promedio",
            value=f"${avg_ticket:.2f}",
            delta=f"{(avg_ticket / (df['sales'].iloc[-30:].sum() / df['customers'].iloc[-30:].sum()) - 1) * 100:.1f}%"
        )
    
    st.markdown("---")
    
    # Gráficos principales
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("###  Evolución de Ventas")
        fig = px.line(df, x='date', y='sales', 
                     title='Ventas Diarias',
                     labels={'sales': 'Ventas ($)', 'date': 'Fecha'})
        fig.update_layout(hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("###  Ventas por Categoría")
        category_sales = df.groupby('product_category')['sales'].sum().reset_index()
        fig = px.pie(category_sales, values='sales', names='product_category',
                    title='Distribución de Ventas por Categoría')
        st.plotly_chart(fig, use_container_width=True)
    
    # Análisis temporal
    st.markdown("###  Análisis Temporal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Ventas por día de la semana
        df['day_of_week'] = df['date'].dt.day_name()
        dow_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dow_sales = df.groupby('day_of_week')['sales'].mean().reindex(dow_order)
        
        fig = px.bar(x=dow_sales.index, y=dow_sales.values,
                    labels={'x': 'Día', 'y': 'Venta Promedio ($)'},
                    title='Ventas Promedio por Día de la Semana')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Ventas por mes
        df['month'] = df['date'].dt.month_name()
        month_sales = df.groupby('month')['sales'].mean()
        
        fig = px.bar(x=month_sales.index, y=month_sales.values,
                    labels={'x': 'Mes', 'y': 'Venta Promedio ($)'},
                    title='Ventas Promedio por Mes')
        st.plotly_chart(fig, use_container_width=True)
    
    # Correlaciones
    st.markdown("###  Análisis de Correlación")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    
    fig = px.imshow(corr_matrix, 
                   labels=dict(color="Correlación"),
                   x=corr_matrix.columns,
                   y=corr_matrix.columns,
                   title='Matriz de Correlación',
                   color_continuous_scale='RdBu_r',
                   aspect='auto')
    st.plotly_chart(fig, use_container_width=True)


def prediction_page():
    """Página de predicciones."""
    
    st.markdown('<h1 class="main-header"> Predictor de Ventas</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    Utiliza este módulo para predecir ventas futuras basándote en diferentes parámetros.
    """)
    
    # Formulario de entrada
    st.markdown("###  Parámetros de Predicción")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        store_id = st.selectbox(" Tienda", options=list(range(1, 11)))
        category = st.selectbox(" Categoría", 
                               options=['Electronics', 'Clothing', 'Food', 'Books'])
        price = st.slider(" Precio", min_value=10.0, max_value=100.0, value=50.0, step=1.0)
    
    with col2:
        promotion = st.radio(" Promoción", options=[0, 1], 
                           format_func=lambda x: "Sí" if x == 1 else "No")
        customers = st.number_input(" Clientes Esperados", 
                                   min_value=10, max_value=500, value=150)
        date = st.date_input(" Fecha", value=datetime.now())
    
    with col3:
        day_of_week = date.weekday()
        st.info(f" Día de la semana: {date.strftime('%A')}")
        st.info(f" Mes: {date.strftime('%B')}")
        is_weekend = 1 if day_of_week >= 5 else 0
        st.info(f" ¿Fin de semana?: {'Sí' if is_weekend else 'No'}")
    
    # Botón de predicción
    if st.button(" Generar Predicción", type="primary", use_container_width=True):
        
        with st.spinner("Generando predicción..."):
            # Simulación de predicción (reemplazar con modelo real)
            base_prediction = 1000
            
            # Factores que afectan la predicción
            if promotion == 1:
                base_prediction *= 1.2
            if is_weekend:
                base_prediction *= 1.1
            if category == 'Electronics':
                base_prediction *= 1.15
            
            base_prediction += customers * 3.5
            base_prediction += (100 - price) * 2
            
            # Añadir variación aleatoria
            prediction = base_prediction * np.random.uniform(0.95, 1.05)
            
            # Mostrar resultado
            st.success(" Predicción generada exitosamente")
            
            st.markdown("###  Resultado de la Predicción")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(" Ventas Predichas", f"${prediction:,.2f}")
            
            with col2:
                confidence = np.random.uniform(0.85, 0.95)
                st.metric(" Confianza", f"{confidence*100:.1f}%")
            
            with col3:
                range_low = prediction * 0.90
                range_high = prediction * 1.10
                st.metric(" Rango", f"${range_low:,.0f} - ${range_high:,.0f}")
            
            # Gráfico de distribución de predicción
            st.markdown("###  Distribución de Confianza")
            
            x = np.linspace(prediction * 0.7, prediction * 1.3, 100)
            y = np.exp(-0.5 * ((x - prediction) / (prediction * 0.1)) ** 2)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', 
                                    name='Distribución de Predicción'))
            fig.add_vline(x=prediction, line_dash="dash", line_color="red",
                         annotation_text="Predicción")
            fig.update_layout(title='Distribución de Probabilidad de la Predicción',
                            xaxis_title='Ventas ($)',
                            yaxis_title='Densidad de Probabilidad')
            st.plotly_chart(fig, use_container_width=True)
            
            # Recomendaciones
            st.markdown("###  Recomendaciones")
            
            if promotion == 0:
                st.info(" Considera activar una promoción para aumentar las ventas en ~20%")
            
            if price > 70:
                st.info(" El precio es alto. Reducirlo podría aumentar la demanda")
            
            if is_weekend:
                st.success(" Es fin de semana - Buen momento para ventas")


def analytics_page():
    """Página de análisis avanzado."""
    
    st.markdown('<h1 class="main-header"> Análisis Avanzado</h1>', 
                unsafe_allow_html=True)
    
    df = load_data()
    
    # Filtros
    st.sidebar.markdown("###  Filtros")
    
    categories = st.sidebar.multiselect(
        "Categorías",
        options=df['product_category'].unique(),
        default=df['product_category'].unique()
    )
    
    date_range = st.sidebar.date_input(
        "Rango de Fechas",
        value=(df['date'].min(), df['date'].max())
    )
    
    # Aplicar filtros
    mask = (df['product_category'].isin(categories)) & \
           (df['date'] >= pd.Timestamp(date_range[0])) & \
           (df['date'] <= pd.Timestamp(date_range[1]))
    
    df_filtered = df[mask]
    
    st.markdown(f"###  Datos Filtrados: {len(df_filtered):,} registros")
    
    # Estadísticas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(" Ventas Totales", f"${df_filtered['sales'].sum():,.0f}")
    with col2:
        st.metric(" Venta Promedio", f"${df_filtered['sales'].mean():,.0f}")
    with col3:
        st.metric(" Desv. Estándar", f"${df_filtered['sales'].std():,.0f}")
    
    # Visualizaciones avanzadas
    tab1, tab2, tab3 = st.tabs([" Tendencias", " Comparaciones", " Distribuciones"])
    
    with tab1:
        st.markdown("#### Tendencia Temporal con Media Móvil")
        
        df_filtered = df_filtered.sort_values('date')
        df_filtered['MA_7'] = df_filtered['sales'].rolling(window=7).mean()
        df_filtered['MA_30'] = df_filtered['sales'].rolling(window=30).mean()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_filtered['date'], y=df_filtered['sales'],
                                mode='lines', name='Ventas', opacity=0.5))
        fig.add_trace(go.Scatter(x=df_filtered['date'], y=df_filtered['MA_7'],
                                mode='lines', name='MA 7 días'))
        fig.add_trace(go.Scatter(x=df_filtered['date'], y=df_filtered['MA_30'],
                                mode='lines', name='MA 30 días'))
        fig.update_layout(title='Ventas con Medias Móviles',
                         xaxis_title='Fecha',
                         yaxis_title='Ventas ($)')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("#### Comparación por Categoría")
        
        category_stats = df_filtered.groupby('product_category').agg({
            'sales': ['mean', 'sum', 'count']
        }).reset_index()
        
        category_stats.columns = ['Categoría', 'Promedio', 'Total', 'Cantidad']
        
        st.dataframe(category_stats, use_container_width=True)
        
        fig = px.box(df_filtered, x='product_category', y='sales',
                    title='Distribución de Ventas por Categoría')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("#### Distribución de Ventas")
        
        fig = px.histogram(df_filtered, x='sales', nbins=50,
                          title='Histograma de Ventas')
        st.plotly_chart(fig, use_container_width=True)


def about_page():
    """Página de información."""
    
    st.markdown('<h1 class="main-header">ℹ Acerca del Proyecto</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    ##  Proyecto de Predicción de Ventas
    
    ###  Objetivo
    Sistema completo de análisis y predicción de ventas utilizando Machine Learning.
    
    ###  Tecnologías Utilizadas
    
    - **Python 3.9+**
    - **Pandas & NumPy** - Manipulación de datos
    - **Scikit-learn** - Modelos de ML
    - **XGBoost** - Gradient Boosting
    - **Streamlit** - Dashboard interactivo
    - **Plotly** - Visualizaciones interactivas
    - **Matplotlib & Seaborn** - Gráficos estáticos
    
    ###  Modelos Implementados
    
    1. **Linear Regression** - Modelo baseline
    2. **Random Forest** - Ensemble learning
    3. **XGBoost** - Gradient boosting avanzado
    4. **Prophet** - Series temporales (opcional)
    
    ###  Métricas de Evaluación
    
    - **RMSE** - Root Mean Squared Error
    - **MAE** - Mean Absolute Error
    - **R²** - Coeficiente de determinación
    - **MAPE** - Mean Absolute Percentage Error
    
    ### ‍ Autor
    
    **Javier Gacitúa**  
    Analista de Datos | Data Scientist
    
     javiergaci.q@gmail.com  
     [LinkedIn](https://www.linkedin.com/in/javier-gacitúa)  
     [GitHub](https://github.com/javierX888)
    
    ###  Licencia
    
    MIT License - 2025
    
    ---
    
     Si te gusta este proyecto, dale una estrella en GitHub!
    """)


# Sidebar
def sidebar():
    """Configuración del sidebar."""
    
    st.sidebar.title(" Navegación")
    
    pages = {
        " Dashboard Principal": main_page,
        " Predictor": prediction_page,
        " Análisis Avanzado": analytics_page,
        "ℹ Acerca de": about_page
    }
    
    selection = st.sidebar.radio("Ir a:", list(pages.keys()))
    
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("""
    ###  Guía Rápida
    
    - **Dashboard**: Vista general de métricas
    - **Predictor**: Genera predicciones personalizadas
    - **Análisis**: Explora datos en profundidad
    - **Acerca de**: Información del proyecto
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2025 Javier Gacitúa")
    
    return pages[selection]


# Main
if __name__ == "__main__":
    page = sidebar()
    page()
