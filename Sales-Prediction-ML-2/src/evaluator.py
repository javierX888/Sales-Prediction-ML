# Importar librerías necesarias
import pickle
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score

class Evaluator:
    def __init__(self, model_path, scaler_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        with open(scaler_path, 'rb') as scaler_file:
            self.scaler = pickle.load(scaler_file)

    def evaluate(self, X_test, y_test):
        # Escalar las características de prueba
        X_test_scaled = self.scaler.transform(X_test)
        
        # Realizar predicciones
        y_pred = self.model.predict(X_test_scaled)
        
        # Calcular métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }