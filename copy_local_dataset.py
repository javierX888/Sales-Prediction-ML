"""
Script to copy the local dataset to the correct project folder

NOTE: This script is useful if:
- You have train.csv in another location
- You want to manually update the dataset
- You downloaded a new version from Kaggle

If you cloned the repo from GitHub, the dataset is already in data/raw/train.csv
"""

import shutil
from pathlib import Path

def copy_dataset():
    """Copy train.csv to the correct location"""
    
    # Paths
    source = Path("train.csv")  # File in project root
    destination = Path("data/raw/train.csv")
    
    print("Dataset Copy Script")
    print("="*60)
    
    # Check if destination already exists
    if destination.exists():
        print(f"Warning: File already exists at: {destination}")
        print(f"Current size: {destination.stat().st_size / 1024 / 1024:.2f} MB")
        
        response = input("\nDo you want to replace it? (y/n): ").lower()
        if response != 'y':
            print("Operation cancelled")
            return False
    
    # Verify source file exists
    if not source.exists():
        print(f"Error: File not found: {source.absolute()}")
        print(f"\nOptions:")
        print(f"   1. Place train.csv in the project root")
        print(f"   2. Download from Kaggle:")
        print(f"      https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting")
        print(f"   3. If you cloned from GitHub, the file should already be at:")
        print(f"      {destination}")
        return False
    
    # Create destination directory if it doesn't exist
    destination.parent.mkdir(parents=True, exist_ok=True)
    
    # Copy file
    try:
        print(f"\nCopying file...")
        shutil.copy2(source, destination)
        print(f"File copied successfully!")
        print(f"From: {source.absolute()}")
        print(f"To: {destination.absolute()}")
        
        # Show file information
        try:
            import pandas as pd
            df = pd.read_csv(destination)
            print(f"\nDataset Information:")
            print(f"   - Rows: {len(df):,}")
            print(f"   - Columns: {len(df.columns)}")
            print(f"   - Size: {destination.stat().st_size / 1024 / 1024:.2f} MB")
            print(f"\nColumns: {', '.join(df.columns[:5])}...")
        except ImportError:
            print(f"\nFile copied (pandas not available for details)")
            print(f"   - Size: {destination.stat().st_size / 1024 / 1024:.2f} MB")
        
        print(f"\nReady! You can now:")
        print(f"   1. Start Jupyter Lab: docker-compose up jupyter -d")
        print(f"   2. Open: http://localhost:8888")
        print(f"   3. Run: notebooks/01_EDA.ipynb")
        
        return True
        
    except Exception as e:
        print(f"Error copying file: {e}")
        return False

if __name__ == "__main__":
    success = copy_dataset()
    exit(0 if success else 1)
