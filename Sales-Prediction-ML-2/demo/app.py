from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Cargar modelos pre-entrenados
with open('../models/random_forest.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('../models/xgboost.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

with open('../models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    
    # Preprocesar los datos
    scaled_data = scaler.transform(df)
    
    # Realizar predicciones
    rf_predictions = rf_model.predict(scaled_data)
    xgb_predictions = xgb_model.predict(scaled_data)
    
    return jsonify({
        'random_forest_predictions': rf_predictions.tolist(),
        'xgboost_predictions': xgb_predictions.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)