# Importar librerías necesarias
import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(df):
    """
    Limpia el DataFrame eliminando filas con valores faltantes.
    
    Args:
        df (pd.DataFrame): DataFrame a limpiar.
        
    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    df_cleaned = df.dropna()
    return df_cleaned

def normalize_data(df):
    """
    Normaliza los datos numéricos en el DataFrame utilizando StandardScaler.
    
    Args:
        df (pd.DataFrame): DataFrame a normalizar.
        
    Returns:
        pd.DataFrame: DataFrame con datos normalizados.
    """
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df, scaler

def preprocess_data(df):
    """
    Función principal para la limpieza y normalización de datos.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar.
        
    Returns:
        pd.DataFrame: DataFrame procesado.
        StandardScaler: Objeto scaler utilizado para normalización.
    """
    df_cleaned = clean_data(df)
    df_normalized, scaler = normalize_data(df_cleaned)
    return df_normalized, scaler