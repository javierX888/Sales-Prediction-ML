from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Cargar modelos pre-entrenados
with open('../../models/random_forest.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('../../models/xgboost.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

with open('../../models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convertir los datos a un DataFrame
    input_data = pd.DataFrame(data, index=[0])

    # Escalar los datos
    scaled_data = scaler.transform(input_data)

    # Realizar predicciones
    rf_prediction = rf_model.predict(scaled_data)
    xgb_prediction = xgb_model.predict(scaled_data)

    # Devolver las predicciones
    return jsonify({
        'random_forest_prediction': rf_prediction.tolist(),
        'xgboost_prediction': xgb_prediction.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)