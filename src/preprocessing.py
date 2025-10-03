"""
Preprocessing Module
====================
Módulo para limpieza y transformación de datos.
"""

import pandas as pd
import numpy as np
from slearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder


class DataPreprocessor:
    """Clase para preprocesamiento de datos."""
    
    def __init__(self):
        """Inicializa el preprocesador."""
        self.scaler = None
        self.label_encoders = {}
    
    def handle_missing_values(self, df, strategy='auto'):
        """
        Maneja valores faltantes en el dataset.
        
        Args:
            df (pd.DataFrame): Dataset a procesar
            strategy (str): Estrategia para manejar nulos
                - 'auto': Automático según tipo de columna
                - 'drop': Eliminar filas con nulos
                - 'mean': Rellenar con media (numéricos)
                - 'median': Rellenar con mediana (numéricos)
                - 'mode': Rellenar con moda
        
        Returns:
            pd.DataFrame: Dataset sin valores faltantes
        """
        df_clean = df.copy()
        
        print("\n Analizando valores faltantes...")
        missing = df_clean.isnull().sum()
        missing_pct = (missing / len(df_clean)) * 100
        
        if missing.sum() == 0:
            print(" No hay valores faltantes")
            return df_clean
        
        print(f"\n Valores faltantes encontrados:")
        for col in missing[missing > 0].index:
            print(f"  - {col}: {missing[col]} ({missing_pct[col]:.2f}%)")
        
        if strategy == 'auto':
            for col in df_clean.columns:
                if df_clean[col].isnull().sum() > 0:
                    if df_clean[col].dtype in ['int64', 'float64']:
                        # Numéricos: rellenar con mediana
                        df_clean[col].fillna(df_clean[col].median(), inplace=True)
                    else:
                        # Categóricos: rellenar con moda
                        df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
        
        elif strategy == 'drop':
            df_clean.dropna(inplace=True)
            print(f" {len(df) - len(df_clean)} filas eliminadas")
        
        elif strategy == 'mean':
            for col in df_clean.select_dtypes(include=[np.number]).columns:
                df_clean[col].fillna(df_clean[col].mean(), inplace=True)
        
        elif strategy == 'median':
            for col in df_clean.select_dtypes(include=[np.number]).columns:
                df_clean[col].fillna(df_clean[col].median(), inplace=True)
        
        elif strategy == 'mode':
            for col in df_clean.columns:
                if df_clean[col].isnull().sum() > 0:
                    df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
        
        print(f" Valores faltantes tratados con estrategia: {strategy}")
        return df_clean
    
    def remove_duplicates(self, df):
        """
        Elimina filas duplicadas.
        
        Args:
            df (pd.DataFrame): Dataset a procesar
            
        Returns:
            pd.DataFrame: Dataset sin duplicados
        """
        df_clean = df.copy()
        duplicates = df_clean.duplicated().sum()
        
        if duplicates > 0:
            df_clean.drop_duplicates(inplace=True)
            print(f" {duplicates} filas duplicadas eliminadas")
        else:
            print(" No hay duplicados")
        
        return df_clean
    
    def handle_outliers(self, df, columns=None, method='iqr', threshold=1.5):
        """
        Detecta y maneja outliers.
        
        Args:
            df (pd.DataFrame): Dataset a procesar
            columns (list): Columnas a analizar (None = todas numéricas)
            method (str): 'iqr' o 'zscore'
            threshold (float): Umbral para detección (1.5 para IQR, 3 para zscore)
            
        Returns:
            pd.DataFrame: Dataset con outliers tratados
        """
        df_clean = df.copy()
        
        if columns is None:
            columns = df_clean.select_dtypes(include=[np.number]).columns
        
        print(f"\n Detectando outliers con método: {method}")
        
        for col in columns:
            if method == 'iqr':
                Q1 = df_clean[col].quantile(0.25)
                Q3 = df_clean[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                
                outliers = df_clean[(df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)]
                
                if len(outliers) > 0:
                    print(f"  - {col}: {len(outliers)} outliers detectados")
                    # Reemplazar outliers con límites
                    df_clean[col] = df_clean[col].clip(lower_bound, upper_bound)
            
            elif method == 'zscore':
                z_scores = np.abs((df_clean[col] - df_clean[col].mean()) / df_clean[col].std())
                outliers = df_clean[z_scores > threshold]
                
                if len(outliers) > 0:
                    print(f"  - {col}: {len(outliers)} outliers detectados")
        
        print(" Outliers tratados")
        return df_clean
    
    def encode_categorical(self, df, columns=None, method='label'):
        """
        Codifica variables categóricas.
        
        Args:
            df (pd.DataFrame): Dataset a procesar
            columns (list): Columnas a codificar (None = todas categóricas)
            method (str): 'label' o 'onehot'
            
        Returns:
            pd.DataFrame: Dataset con variables codificadas
        """
        df_encoded = df.copy()
        
        if columns is None:
            columns = df_encoded.select_dtypes(include=['object']).columns
        
        print(f"\n Codificando variables categóricas con método: {method}")
        
        if method == 'label':
            for col in columns:
                le = LabelEncoder()
                df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
                self.label_encoders[col] = le
                print(f"  - {col}: {len(le.classes_)} categorías")
        
        elif method == 'onehot':
            df_encoded = pd.get_dummies(df_encoded, columns=columns, drop_first=True)
            print(f"  - {len(columns)} columnas codificadas con One-Hot Encoding")
        
        print(" Variables categóricas codificadas")
        return df_encoded
    
    def scale_features(self, df, columns=None, method='standard'):
        """
        Escala variables numéricas.
        
        Args:
            df (pd.DataFrame): Dataset a procesar
            columns (list): Columnas a escalar (None = todas numéricas)
            method (str): 'standard' o 'minmax'
            
        Returns:
            pd.DataFrame: Dataset con variables escaladas
        """
        df_scaled = df.copy()
        
        if columns is None:
            columns = df_scaled.select_dtypes(include=[np.number]).columns
        
        print(f"\n Escalando variables con método: {method}")
        
        if method == 'standard':
            self.scaler = StandardScaler()
        elif method == 'minmax':
            self.scaler = MinMaxScaler()
        
        df_scaled[columns] = self.scaler.fit_transform(df_scaled[columns])
        print(f"  - {len(columns)} columnas escaladas")
        print(" Variables escaladas correctamente")
        
        return df_scaled
    
    def get_preprocessing_summary(self, df_original, df_processed):
        """
        Muestra un resumen del preprocesamiento.
        
        Args:
            df_original (pd.DataFrame): Dataset original
            df_processed (pd.DataFrame): Dataset procesado
        """
        print("\n" + "="*50)
        print(" RESUMEN DEL PREPROCESAMIENTO")
        print("="*50)
        print(f"\n Filas:")
        print(f"  - Original: {len(df_original):,}")
        print(f"  - Procesado: {len(df_processed):,}")
        print(f"  - Diferencia: {len(df_original) - len(df_processed):,}")
        
        print(f"\n Columnas:")
        print(f"  - Original: {len(df_original.columns)}")
        print(f"  - Procesado: {len(df_processed.columns)}")
        print(f"  - Diferencia: {len(df_processed.columns) - len(df_original.columns)}")
        
        print(f"\n Valores faltantes:")
        print(f"  - Original: {df_original.isnull().sum().sum():,}")
        print(f"  - Procesado: {df_processed.isnull().sum().sum():,}")
        
        print(f"\n Memoria:")
        print(f"  - Original: {df_original.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        print(f"  - Procesado: {df_processed.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        print("="*50 + "\n")


# Ejemplo de uso
if __name__ == "__main__":
    print(" Módulo preprocessing.py listo para usar")
