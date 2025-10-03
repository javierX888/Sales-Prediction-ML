"""
Models Module
=============
Módulo para entrenar y evaluar modelos de Machine Learning.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib


class SalesPredictor:
    """Clase para entrenar modelos de predicción de ventas."""
    
    def __init__(self):
        """Inicializa el predictor."""
        self.models = {}
        self.results = {}
        self.best_model = None
    
    def prepare_data(self, df, target_column, test_size=0.2, random_state=42):
        """
        Prepara los datos para entrenamiento.
        
        Args:
            df (pd.DataFrame): Dataset completo
            target_column (str): Nombre de la columna objetivo
            test_size (float): Proporción del conjunto de prueba
            random_state (int): Semilla aleatoria
            
        Returns:
            tuple: X_train, X_test, y_train, y_test
        """
        print("\n Preparando datos para entrenamiento...")
        
        # Separar features y target
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Split train/test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        print(f" Datos preparados:")
        print(f"  - Train: {X_train.shape[0]} muestras")
        print(f"  - Test: {X_test.shape[0]} muestras")
        print(f"  - Features: {X_train.shape[1]}")
        
        return X_train, X_test, y_train, y_test
    
    def train_linear_regression(self, X_train, y_train, name='Linear Regression'):
        """
        Entrena un modelo de Regresión Lineal.
        
        Args:
            X_train: Features de entrenamiento
            y_train: Target de entrenamiento
            name (str): Nombre del modelo
            
        Returns:
            model: Modelo entrenado
        """
        print(f"\n Entrenando {name}...")
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        self.models[name] = model
        print(f" {name} entrenado")
        
        return model
    
    def train_random_forest(self, X_train, y_train, n_estimators=100, 
                           max_depth=None, name='Random Forest'):
        """
        Entrena un modelo de Random Forest.
        
        Args:
            X_train: Features de entrenamiento
            y_train: Target de entrenamiento
            n_estimators (int): Número de árboles
            max_depth (int): Profundidad máxima
            name (str): Nombre del modelo
            
        Returns:
            model: Modelo entrenado
        """
        print(f"\n Entrenando {name}...")
        print(f"  - Árboles: {n_estimators}")
        print(f"  - Profundidad: {max_depth if max_depth else 'Sin límite'}")
        
        model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42,
            n_jobs=-1
        )
        model.fit(X_train, y_train)
        
        self.models[name] = model
        print(f" {name} entrenado")
        
        return model
    
    def train_xgboost(self, X_train, y_train, n_estimators=100, 
                     learning_rate=0.1, max_depth=6, name='XGBoost'):
        """
        Entrena un modelo XGBoost.
        
        Args:
            X_train: Features de entrenamiento
            y_train: Target de entrenamiento
            n_estimators (int): Número de estimadores
            learning_rate (float): Tasa de aprendizaje
            max_depth (int): Profundidad máxima
            name (str): Nombre del modelo
            
        Returns:
            model: Modelo entrenado
        """
        try:
            import xgboost as xgb
            
            print(f"\n Entrenando {name}...")
            print(f"  - Estimadores: {n_estimators}")
            print(f"  - Learning rate: {learning_rate}")
            print(f"  - Profundidad: {max_depth}")
            
            model = xgb.XGBRegressor(
                n_estimators=n_estimators,
                learning_rate=learning_rate,
                max_depth=max_depth,
                random_state=42,
                n_jobs=-1
            )
            model.fit(X_train, y_train)
            
            self.models[name] = model
            print(f" {name} entrenado")
            
            return model
            
        except ImportError:
            print(" XGBoost no está instalado. Instálalo con: pip install xgboost")
            return None
    
    def evaluate_model(self, model, X_test, y_test, model_name):
        """
        Evalúa un modelo con métricas estándar.
        
        Args:
            model: Modelo a evaluar
            X_test: Features de prueba
            y_test: Target de prueba
            model_name (str): Nombre del modelo
            
        Returns:
            dict: Diccionario con métricas
        """
        print(f"\n Evaluando {model_name}...")
        
        # Predicciones
        y_pred = model.predict(X_test)
        
        # Métricas
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        
        metrics = {
            'RMSE': rmse,
            'MAE': mae,
            'R2': r2,
            'MAPE': mape
        }
        
        self.results[model_name] = metrics
        
        print(f"  - RMSE: {rmse:.2f}")
        print(f"  - MAE: {mae:.2f}")
        print(f"  - R²: {r2:.4f}")
        print(f"  - MAPE: {mape:.2f}%")
        
        return metrics
    
    def compare_models(self):
        """
        Compara todos los modelos entrenados.
        
        Returns:
            pd.DataFrame: Tabla comparativa
        """
        if not self.results:
            print(" No hay modelos evaluados")
            return None
        
        print("\n" + "="*70)
        print(" COMPARACIÓN DE MODELOS")
        print("="*70)
        
        df_results = pd.DataFrame(self.results).T
        df_results = df_results.sort_values('R2', ascending=False)
        
        print(df_results.to_string())
        print("="*70)
        
        # Identificar mejor modelo
        best_model_name = df_results.index[0]
        self.best_model = self.models[best_model_name]
        print(f"\n Mejor modelo: {best_model_name} (R² = {df_results.loc[best_model_name, 'R2']:.4f})")
        
        return df_results
    
    def get_feature_importance(self, model_name, feature_names, top_n=10):
        """
        Obtiene la importancia de características.
        
        Args:
            model_name (str): Nombre del modelo
            feature_names (list): Nombres de las características
            top_n (int): Top N características a mostrar
            
        Returns:
            pd.DataFrame: Importancia de características
        """
        model = self.models.get(model_name)
        
        if model is None:
            print(f" Modelo {model_name} no encontrado")
            return None
        
        if not hasattr(model, 'feature_importances_'):
            print(f" {model_name} no tiene feature_importances_")
            return None
        
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False).head(top_n)
        
        print(f"\n Top {top_n} características más importantes ({model_name}):")
        print(importance_df.to_string(index=False))
        
        return importance_df
    
    def save_model(self, model_name, filepath):
        """
        Guarda un modelo entrenado.
        
        Args:
            model_name (str): Nombre del modelo
            filepath (str): Ruta donde guardar
        """
        model = self.models.get(model_name)
        
        if model is None:
            print(f" Modelo {model_name} no encontrado")
            return
        
        joblib.dump(model, filepath)
        print(f" Modelo guardado en: {filepath}")
    
    def load_model(self, filepath, model_name):
        """
        Carga un modelo guardado.
        
        Args:
            filepath (str): Ruta del modelo
            model_name (str): Nombre para el modelo
            
        Returns:
            model: Modelo cargado
        """
        try:
            model = joblib.load(filepath)
            self.models[model_name] = model
            print(f" Modelo cargado desde: {filepath}")
            return model
        except Exception as e:
            print(f" Error al cargar modelo: {str(e)}")
            return None


# Ejemplo de uso
if __name__ == "__main__":
    print(" Módulo models.py listo para usar")
