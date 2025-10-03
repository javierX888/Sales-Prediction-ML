"""
Feature Engineering Module
===========================
Módulo para crear y transformar variables (features).
"""

import pandas as pd
import numpy as np
from datetime import datetime


class FeatureEngineer:
    """Clase para ingeniería de características."""
    
    def __init__(self):
        """Inicializa el ingeniero de características."""
        self.created_features = []
    
    def create_date_features(self, df, date_column):
        """
        Crea características a partir de fechas.
        
        Args:
            df (pd.DataFrame): Dataset
            date_column (str): Nombre de la columna de fecha
            
        Returns:
            pd.DataFrame: Dataset con nuevas características
        """
        df_new = df.copy()
        
        print(f"\n Creando características de fecha desde: {date_column}")
        
        # Convertir a datetime si no lo es
        df_new[date_column] = pd.to_datetime(df_new[date_column])
        
        # Extraer componentes de fecha
        df_new[f'{date_column}_year'] = df_new[date_column].dt.year
        df_new[f'{date_column}_month'] = df_new[date_column].dt.month
        df_new[f'{date_column}_day'] = df_new[date_column].dt.day
        df_new[f'{date_column}_dayofweek'] = df_new[date_column].dt.dayofweek
        df_new[f'{date_column}_quarter'] = df_new[date_column].dt.quarter
        df_new[f'{date_column}_weekofyear'] = df_new[date_column].dt.isocalendar().week
        
        # Características adicionales
        df_new[f'{date_column}_is_weekend'] = df_new[f'{date_column}_dayofweek'].isin([5, 6]).astype(int)
        df_new[f'{date_column}_is_month_start'] = df_new[date_column].dt.is_month_start.astype(int)
        df_new[f'{date_column}_is_month_end'] = df_new[date_column].dt.is_month_end.astype(int)
        
        new_features = [
            f'{date_column}_year', f'{date_column}_month', f'{date_column}_day',
            f'{date_column}_dayofweek', f'{date_column}_quarter', f'{date_column}_weekofyear',
            f'{date_column}_is_weekend', f'{date_column}_is_month_start', f'{date_column}_is_month_end'
        ]
        
        self.created_features.extend(new_features)
        print(f" Creadas {len(new_features)} características de fecha")
        
        return df_new
    
    def create_lag_features(self, df, column, lags=[1, 7, 30]):
        """
        Crea características de rezago (lag features).
        
        Args:
            df (pd.DataFrame): Dataset
            column (str): Columna a rezagar
            lags (list): Lista de períodos de rezago
            
        Returns:
            pd.DataFrame: Dataset con características de rezago
        """
        df_new = df.copy()
        
        print(f"\n⏳ Creando lag features para: {column}")
        
        for lag in lags:
            df_new[f'{column}_lag_{lag}'] = df_new[column].shift(lag)
            self.created_features.append(f'{column}_lag_{lag}')
        
        print(f" Creados {len(lags)} lag features")
        return df_new
    
    def create_rolling_features(self, df, column, windows=[7, 30]):
        """
        Crea características de ventana móvil (rolling features).
        
        Args:
            df (pd.DataFrame): Dataset
            column (str): Columna para calcular rolling
            windows (list): Tamaños de ventana
            
        Returns:
            pd.DataFrame: Dataset con rolling features
        """
        df_new = df.copy()
        
        print(f"\n Creando rolling features para: {column}")
        
        for window in windows:
            # Media móvil
            df_new[f'{column}_rolling_mean_{window}'] = df_new[column].rolling(window=window).mean()
            # Desviación estándar móvil
            df_new[f'{column}_rolling_std_{window}'] = df_new[column].rolling(window=window).std()
            # Máximo móvil
            df_new[f'{column}_rolling_max_{window}'] = df_new[column].rolling(window=window).max()
            # Mínimo móvil
            df_new[f'{column}_rolling_min_{window}'] = df_new[column].rolling(window=window).min()
            
            self.created_features.extend([
                f'{column}_rolling_mean_{window}',
                f'{column}_rolling_std_{window}',
                f'{column}_rolling_max_{window}',
                f'{column}_rolling_min_{window}'
            ])
        
        print(f" Creados {len(windows) * 4} rolling features")
        return df_new
    
    def create_aggregation_features(self, df, group_column, agg_column, agg_funcs=['mean', 'sum', 'count']):
        """
        Crea características de agregación.
        
        Args:
            df (pd.DataFrame): Dataset
            group_column (str): Columna para agrupar
            agg_column (str): Columna a agregar
            agg_funcs (list): Funciones de agregación
            
        Returns:
            pd.DataFrame: Dataset con características agregadas
        """
        df_new = df.copy()
        
        print(f"\n Creando características de agregación: {group_column} -> {agg_column}")
        
        for func in agg_funcs:
            agg_data = df_new.groupby(group_column)[agg_column].transform(func)
            feature_name = f'{group_column}_{agg_column}_{func}'
            df_new[feature_name] = agg_data
            self.created_features.append(feature_name)
        
        print(f" Creadas {len(agg_funcs)} características de agregación")
        return df_new
    
    def create_interaction_features(self, df, columns):
        """
        Crea características de interacción entre variables.
        
        Args:
            df (pd.DataFrame): Dataset
            columns (list): Lista de columnas para interacciones
            
        Returns:
            pd.DataFrame: Dataset con interacciones
        """
        df_new = df.copy()
        
        print(f"\n Creando características de interacción")
        
        for i in range(len(columns)):
            for j in range(i+1, len(columns)):
                col1, col2 = columns[i], columns[j]
                
                # Producto
                feature_name = f'{col1}_x_{col2}'
                df_new[feature_name] = df_new[col1] * df_new[col2]
                self.created_features.append(feature_name)
                
                # Ratio (evitar división por cero)
                if (df_new[col2] != 0).all():
                    feature_name = f'{col1}_div_{col2}'
                    df_new[feature_name] = df_new[col1] / df_new[col2]
                    self.created_features.append(feature_name)
        
        print(f" Creadas {len(self.created_features)} características de interacción")
        return df_new
    
    def create_polynomial_features(self, df, columns, degree=2):
        """
        Crea características polinómicas.
        
        Args:
            df (pd.DataFrame): Dataset
            columns (list): Columnas para transformación polinómica
            degree (int): Grado del polinomio
            
        Returns:
            pd.DataFrame: Dataset con características polinómicas
        """
        df_new = df.copy()
        
        print(f"\n Creando características polinómicas (grado {degree})")
        
        for col in columns:
            for d in range(2, degree + 1):
                feature_name = f'{col}_pow_{d}'
                df_new[feature_name] = df_new[col] ** d
                self.created_features.append(feature_name)
        
        print(f" Creadas {len(columns) * (degree - 1)} características polinómicas")
        return df_new
    
    def create_binning_features(self, df, column, bins=5, labels=None):
        """
        Crea características mediante binning (discretización).
        
        Args:
            df (pd.DataFrame): Dataset
            column (str): Columna a discretizar
            bins (int): Número de bins
            labels (list): Etiquetas para los bins
            
        Returns:
            pd.DataFrame: Dataset con variable discretizada
        """
        df_new = df.copy()
        
        print(f"\n Creando bins para: {column}")
        
        feature_name = f'{column}_binned'
        df_new[feature_name] = pd.cut(df_new[column], bins=bins, labels=labels)
        self.created_features.append(feature_name)
        
        print(f" Variable discretizada en {bins} bins")
        return df_new
    
    def get_feature_summary(self):
        """
        Muestra un resumen de las características creadas.
        """
        print("\n" + "="*50)
        print(" RESUMEN DE FEATURE ENGINEERING")
        print("="*50)
        print(f"\n Total de características creadas: {len(self.created_features)}")
        print(f"\n Lista de características:")
        for i, feature in enumerate(self.created_features, 1):
            print(f"  {i}. {feature}")
        print("="*50 + "\n")


# Ejemplo de uso
if __name__ == "__main__":
    print(" Módulo feature_engineering.py listo para usar")
