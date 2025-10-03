"""
Data Loader Module for Sales Forecasting Project

This module handles loading data from Kaggle or local files.
Dataset: Sales Forecasting (Kaggle)
URL: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting
"""

import os
import pandas as pd
from pathlib import Path

class DataLoader:
    """Clase para gestionar la descarga y carga de datos"""
    
    def __init__(self, base_path='data'):
        self.base_path = Path(base_path)
        self.raw_path = self.base_path / 'raw'
        self.processed_path = self.base_path / 'processed'
        
        # Crear directorios si no existen
        self.raw_path.mkdir(parents=True, exist_ok=True)
        self.processed_path.mkdir(parents=True, exist_ok=True)
    
    def download_from_kaggle(self):
        """
        Download dataset from Kaggle using kagglehub.
        
        Returns:
            str: Path to downloaded dataset, None if failed
        """
        print("Downloading dataset from Kaggle...")
        try:
            import kagglehub
            path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
            print(f"Dataset downloaded successfully: {path}")
            return path
        except ImportError:
            print("Error: kagglehub is not installed")
            print("Install with: pip install kagglehub")
            return None
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            print("\nKaggle API Configuration:")
            print("  1. Go to https://kaggle.com/settings/account")
            print("  2. Click 'Create New Token' in API section")
            print("  3. Place kaggle.json in:")
            print("     - Windows: C:\\Users\\<username>\\.kaggle\\kaggle.json")
            print("     - Linux/Mac: ~/.kaggle/kaggle.json")
            return None
    
    def load_from_kaggle(self):
        """
        Download and load dataset from Kaggle.
        
        Returns:
            pd.DataFrame: Loaded dataset, None if failed
        """
        kaggle_path = self.download_from_kaggle()
        if kaggle_path is None:
            return None
        
        # Find train.csv
        train_file = Path(kaggle_path) / 'train.csv'
        
        if not train_file.exists():
            train_files = list(Path(kaggle_path).rglob('train.csv'))
            if train_files:
                train_file = train_files[0]
            else:
                print(f"Error: train.csv not found in {kaggle_path}")
                return None
        
        try:
            df = pd.read_csv(train_file)
            print(f"Dataset loaded: {df.shape[0]:,} rows, {df.shape[1]} columns")
            
            # Save copy to data/raw
            output_path = self.raw_path / 'train.csv'
            df.to_csv(output_path, index=False)
            print(f"Copy saved to: {output_path}")
            
            return df
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None
    
    def load_from_local(self, filename='train.csv'):
        """
        Load dataset from local file.
        
        Args:
            filename (str): Name of the file to load
            
        Returns:
            pd.DataFrame: Loaded dataset, None if failed
        """
        file_path = self.raw_path / filename
        
        if not file_path.exists():
            print(f"File not found: {file_path}")
            print(f"Place {filename} in: {self.raw_path}")
            return None
        
        try:
            df = pd.read_csv(file_path)
            print(f"Dataset loaded from local: {df.shape[0]:,} rows, {df.shape[1]} columns")
            return df
        except Exception as e:
            print(f"Error loading file: {e}")
            return None
    
    def load_dataset(self, force_download=False):
        """
        Load dataset (tries local first, then Kaggle).
        
        Args:
            force_download (bool): Force download from Kaggle
            
        Returns:
            pd.DataFrame: Loaded dataset, None if failed
        """
        if force_download:
            print("Forcing download from Kaggle...")
            return self.load_from_kaggle()
        
        # Try loading from local first
        print("Searching for local dataset...")
        df = self.load_from_local()
        
        # If not found locally, try downloading
        if df is None:
            print("\nNot found locally. Attempting to download from Kaggle...")
            df = self.load_from_kaggle()
        
        return df
    
    def get_dataset_info(self, df):
        """
        Display basic dataset information.
        
        Args:
            df (pd.DataFrame): Dataset to analyze
        """
        if df is None:
            print("No dataset available")
            return
        
        print("\n" + "="*60)
        print("SALES FORECASTING DATASET - INFORMATION")
        print("="*60)
        print(f"\nDimensions: {df.shape[0]:,} rows x {df.shape[1]} columns")
        
        print("\nAvailable columns:")
        for i, col in enumerate(df.columns, 1):
            dtype = df[col].dtype
            nulls = df[col].isnull().sum()
            print(f"   {i:2d}. {col:20s} [{dtype}] - {nulls} nulls")
        
        print(f"\nMemory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        print("\nData types:")
        type_counts = df.dtypes.value_counts()
        for dtype, count in type_counts.items():
            print(f"   - {dtype}: {count} columns")
        
        print("\nMissing values:")
        null_counts = df.isnull().sum()
        if null_counts.sum() > 0:
            for col, count in null_counts[null_counts > 0].items():
                pct = (count / len(df)) * 100
                print(f"   - {col}: {count:,} ({pct:.1f}%)")
        else:
            print("   No missing values")
        
        print("\nFirst rows:")
        print(df.head())
        
        print("\n" + "="*60)


def quick_load(force_download=False):
    """
    Quick function to load the dataset.
    
    Args:
        force_download (bool): Force download from Kaggle
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    loader = DataLoader()
    df = loader.load_dataset(force_download=force_download)
    
    if df is not None:
        loader.get_dataset_info(df)
    
    return df


if __name__ == "__main__":
    print("SALES PREDICTION - DATA LOADER")
    print("="*60)
    print("Dataset: Sales Forecasting (Kaggle)")
    print("URL: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting")
    print("="*60)
    
    # Load dataset (automatic: local or Kaggle)
    df = quick_load()
    
    if df is not None:
        print("\nDataset ready for analysis!")
        print("\nNext steps:")
        print("   1. Open Jupyter Lab: http://localhost:8888")
        print("   2. Navigate to notebooks/01_EDA.ipynb")
        print("   3. Run exploratory analysis")
    else:
        print("\nCould not load dataset")
        print("\nOptions:")
        print("   1. Place train.csv in: data/raw/")
        print("   2. Configure Kaggle API and run again")