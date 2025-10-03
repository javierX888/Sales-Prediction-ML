"""
Visualization Module
====================
Módulo para crear visualizaciones profesionales.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


class SalesVisualizer:
    """Clase para visualizaciones del proyecto."""
    
    def __init__(self, figsize=(12, 6)):
        """
        Inicializa el visualizador.
        
        Args:
            figsize (tuple): Tamaño por defecto de las figuras
        """
        self.figsize = figsize
        self.colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
    
    def plot_distribution(self, df, column, title=None):
        """
        Grafica la distribución de una variable.
        
        Args:
            df (pd.DataFrame): Dataset
            column (str): Columna a graficar
            title (str): Título del gráfico
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Histograma
        axes[0].hist(df[column], bins=50, color=self.colors[0], edgecolor='black', alpha=0.7)
        axes[0].set_xlabel(column)
        axes[0].set_ylabel('Frecuencia')
        axes[0].set_title(f'Histograma de {column}' if not title else title)
        axes[0].grid(True, alpha=0.3)
        
        # Boxplot
        axes[1].boxplot(df[column], vert=True)
        axes[1].set_ylabel(column)
        axes[1].set_title(f'Boxplot de {column}')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def plot_correlation_matrix(self, df, figsize=(12, 10)):
        """
        Grafica matriz de correlación.
        
        Args:
            df (pd.DataFrame): Dataset
            figsize (tuple): Tamaño de la figura
        """
        # Calcular correlación
        corr = df.select_dtypes(include=[np.number]).corr()
        
        # Crear figura
        plt.figure(figsize=figsize)
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1)
        plt.title('Matriz de Correlación', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def plot_time_series(self, df, date_column, value_column, title='Serie Temporal'):
        """
        Grafica una serie temporal.
        
        Args:
            df (pd.DataFrame): Dataset
            date_column (str): Columna de fecha
            value_column (str): Columna de valores
            title (str): Título del gráfico
        """
        plt.figure(figsize=(15, 6))
        plt.plot(df[date_column], df[value_column], color=self.colors[0], linewidth=2)
        plt.xlabel('Fecha', fontsize=12)
        plt.ylabel(value_column, fontsize=12)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_predictions_vs_actual(self, y_true, y_pred, title='Predicciones vs Valores Reales'):
        """
        Compara predicciones con valores reales.
        
        Args:
            y_true: Valores reales
            y_pred: Predicciones
            title (str): Título del gráfico
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Scatter plot
        axes[0].scatter(y_true, y_pred, alpha=0.5, color=self.colors[0])
        axes[0].plot([y_true.min(), y_true.max()], 
                     [y_true.min(), y_true.max()], 
                     'r--', lw=2, label='Línea perfecta')
        axes[0].set_xlabel('Valores Reales', fontsize=12)
        axes[0].set_ylabel('Predicciones', fontsize=12)
        axes[0].set_title('Predicciones vs Reales', fontsize=14)
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Residuos
        residuals = y_true - y_pred
        axes[1].scatter(y_pred, residuals, alpha=0.5, color=self.colors[1])
        axes[1].axhline(y=0, color='r', linestyle='--', lw=2)
        axes[1].set_xlabel('Predicciones', fontsize=12)
        axes[1].set_ylabel('Residuos', fontsize=12)
        axes[1].set_title('Gráfico de Residuos', fontsize=14)
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle(title, fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.show()
    
    def plot_feature_importance(self, importance_df, top_n=15):
        """
        Grafica importancia de características.
        
        Args:
            importance_df (pd.DataFrame): DataFrame con feature e importance
            top_n (int): Top N características a mostrar
        """
        top_features = importance_df.head(top_n)
        
        plt.figure(figsize=(10, 8))
        plt.barh(range(len(top_features)), top_features['importance'], color=self.colors[2])
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Importancia', fontsize=12)
        plt.title(f'Top {top_n} Características Más Importantes', 
                 fontsize=16, fontweight='bold')
        plt.gca().invert_yaxis()
        plt.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        plt.show()
    
    def plot_model_comparison(self, results_df):
        """
        Compara métricas de múltiples modelos.
        
        Args:
            results_df (pd.DataFrame): DataFrame con resultados de modelos
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        metrics = ['RMSE', 'MAE', 'R2', 'MAPE']
        
        for idx, metric in enumerate(metrics):
            ax = axes[idx // 2, idx % 2]
            results_df[metric].plot(kind='bar', ax=ax, color=self.colors[idx])
            ax.set_title(f'Comparación: {metric}', fontsize=14, fontweight='bold')
            ax.set_xlabel('Modelo', fontsize=12)
            ax.set_ylabel(metric, fontsize=12)
            ax.grid(True, alpha=0.3, axis='y')
            ax.tick_params(axis='x', rotation=45)
        
        plt.suptitle('Comparación de Modelos', fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()
        plt.show()
    
    def plot_missing_values(self, df):
        """
        Visualiza valores faltantes.
        
        Args:
            df (pd.DataFrame): Dataset
        """
        missing = df.isnull().sum()
        missing = missing[missing > 0].sort_values(ascending=False)
        
        if len(missing) == 0:
            print(" No hay valores faltantes para visualizar")
            return
        
        plt.figure(figsize=(10, 6))
        missing.plot(kind='bar', color=self.colors[1])
        plt.title('Valores Faltantes por Columna', fontsize=16, fontweight='bold')
        plt.xlabel('Columna', fontsize=12)
        plt.ylabel('Cantidad de Valores Faltantes', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
    
    def plot_sales_by_category(self, df, category_column, sales_column, top_n=10):
        """
        Grafica ventas por categoría.
        
        Args:
            df (pd.DataFrame): Dataset
            category_column (str): Columna de categoría
            sales_column (str): Columna de ventas
            top_n (int): Top N categorías
        """
        # Agrupar y ordenar
        category_sales = df.groupby(category_column)[sales_column].sum().sort_values(ascending=False).head(top_n)
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gráfico de barras
        category_sales.plot(kind='bar', ax=axes[0], color=self.colors[0])
        axes[0].set_title(f'Top {top_n} Categorías por Ventas', fontsize=14, fontweight='bold')
        axes[0].set_xlabel(category_column, fontsize=12)
        axes[0].set_ylabel(sales_column, fontsize=12)
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].grid(True, alpha=0.3, axis='y')
        
        # Gráfico circular
        axes[1].pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', 
                   colors=self.colors, startangle=90)
        axes[1].set_title('Distribución de Ventas', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
    
    def create_dashboard_summary(self, df, target_column):
        """
        Crea un resumen visual tipo dashboard.
        
        Args:
            df (pd.DataFrame): Dataset
            target_column (str): Columna objetivo
        """
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # Distribución del target
        ax1 = fig.add_subplot(gs[0, :2])
        df[target_column].hist(bins=50, ax=ax1, color=self.colors[0], edgecolor='black')
        ax1.set_title(f'Distribución de {target_column}', fontsize=14, fontweight='bold')
        ax1.set_xlabel(target_column)
        ax1.set_ylabel('Frecuencia')
        
        # Estadísticas
        ax2 = fig.add_subplot(gs[0, 2])
        ax2.axis('off')
        stats_text = f"""
        ESTADÍSTICAS
        
        Media: {df[target_column].mean():.2f}
        Mediana: {df[target_column].median():.2f}
        Std: {df[target_column].std():.2f}
        Min: {df[target_column].min():.2f}
        Max: {df[target_column].max():.2f}
        """
        ax2.text(0.1, 0.5, stats_text, fontsize=12, verticalalignment='center',
                fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Top correlaciones
        ax3 = fig.add_subplot(gs[1:, :])
        corr = df.select_dtypes(include=[np.number]).corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, ax=ax3, cbar_kws={'shrink': 0.8})
        ax3.set_title('Matriz de Correlación', fontsize=14, fontweight='bold')
        
        plt.suptitle('Dashboard de Análisis', fontsize=18, fontweight='bold', y=0.98)
        plt.show()


# Ejemplo de uso
if __name__ == "__main__":
    print(" Módulo visualization.py listo para usar")
