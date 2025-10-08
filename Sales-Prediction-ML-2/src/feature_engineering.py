# Importar librerías necesarias
import pandas as pd
import numpy as np

def create_features(df):
    """
    Función para crear nuevas características a partir del dataset existente.
    
    Args:
        df (DataFrame): DataFrame de entrada con datos de ventas.
        
    Returns:
        DataFrame: DataFrame con nuevas características añadidas.
    """
    # Crear características temporales
    df['Order Month'] = df['date'].dt.month
    df['Order Year'] = df['date'].dt.year
    df['Order Day'] = df['date'].dt.day
    df['Order DayOfWeek'] = df['date'].dt.dayofweek
    df['Order Quarter'] = df['date'].dt.quarter
    
    # Crear características de ventas
    df['Sales per Day'] = df['sales'] / df['Order Day']
    df['Sales per Month'] = df['sales'] / df['Order Month']
    
    # Crear características categóricas
    df['High Sales'] = np.where(df['sales'] > df['sales'].mean(), 1, 0)
    
    return df

def feature_selection(df):
    """
    Función para seleccionar características relevantes para el modelo.
    
    Args:
        df (DataFrame): DataFrame de entrada con datos de ventas.
        
    Returns:
        DataFrame: DataFrame con características seleccionadas.
    """
    selected_features = df[['sales', 'Order Month', 'Order Year', 'Order Day', 
                             'Order DayOfWeek', 'Order Quarter', 
                             'Sales per Day', 'Sales per Month', 'High Sales']]
    
    return selected_features