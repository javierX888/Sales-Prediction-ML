class DataLoader:
    def __init__(self, base_path):
        self.base_path = base_path

    def load_from_local(self, filename):
        try:
            file_path = f"{self.base_path}/raw/{filename}"
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no se encontró en {self.base_path}/raw/")
            return None

    def get_dataset_info(self, df):
        print("Información del Dataset:")
        print(f"Dimensiones: {df.shape[0]:,} filas x {df.shape[1]} columnas")
        print("Columnas:")
        print(df.columns.tolist())
        print("\nTipos de Datos:")
        print(df.dtypes)
        print("\nValores Faltantes:")
        print(df.isnull().sum())