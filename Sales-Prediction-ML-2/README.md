# Sales Prediction Machine Learning Project

Este proyecto tiene como objetivo predecir las ventas utilizando técnicas de machine learning. A través de un análisis exhaustivo de datos, ingeniería de características y entrenamiento de modelos, se busca desarrollar un sistema que pueda realizar predicciones precisas basadas en datos históricos.

## Estructura del Proyecto

El proyecto está organizado en varias carpetas y archivos, cada uno con una función específica:

- **src/**: Contiene los scripts de Python para la carga de datos, preprocesamiento, ingeniería de características, entrenamiento de modelos y evaluación.
  - `data_loader.py`: Clase para cargar y gestionar datasets.
  - `preprocessing.py`: Funciones para limpiar y preparar datos.
  - `feature_engineering.py`: Funciones para crear nuevas características.
  - `model_trainer.py`: Clase para entrenar modelos de machine learning.
  - `evaluator.py`: Funciones para evaluar el rendimiento de los modelos.

- **notebooks/**: Incluye cuadernos Jupyter para realizar análisis exploratorio de datos, ingeniería de características, entrenamiento de modelos y evaluación.
  - `01_EDA.ipynb`: Análisis exploratorio de datos.
  - `02_Feature_Engineering.ipynb`: Ingeniería de características.
  - `03_Model_Training.ipynb`: Entrenamiento de modelos.
  - `04_Evaluation.ipynb`: Evaluación de modelos.

- **models/**: Contiene los modelos pre-entrenados guardados en formato pickle.
  - `random_forest.pkl`: Modelo de Random Forest.
  - `xgboost.pkl`: Modelo de XGBoost.
  - `scaler.pkl`: Objeto de escalado para normalizar datos.

- **data/**: Almacena los datasets utilizados en el proyecto.
  - `raw/train.csv`: Dataset original.
  - `processed/sales_clean.csv`: Dataset procesado y limpio.
  - `sample/demo_data.csv`: Conjunto de datos de muestra.

- **demo/**: Contiene la aplicación demo que permite realizar predicciones a través de una API.
  - `api/predict.py`: Lógica para la API de predicciones.
  - `public/favicon.ico`: Icono de la aplicación.
  - `app.py`: Punto de entrada de la aplicación.
  - `requirements.txt`: Dependencias necesarias para la aplicación demo.
  - `vercel.json`: Configuración para desplegar en Vercel.

- **.gitignore**: Archivos y directorios que deben ser ignorados por Git.
- **requirements.txt**: Dependencias necesarias para el proyecto en general.
- **README.md**: Documentación del proyecto.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd Sales-Prediction-ML
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el cuaderno de análisis exploratorio de datos para comprender la estructura de los datos:
   ```
   jupyter notebook notebooks/01_EDA.ipynb
   ```

2. Realiza la ingeniería de características:
   ```
   jupyter notebook notebooks/02_Feature_Engineering.ipynb
   ```

3. Entrena los modelos:
   ```
   jupyter notebook notebooks/03_Model_Training.ipynb
   ```

4. Evalúa los modelos:
   ```
   jupyter notebook notebooks/04_Evaluation.ipynb
   ```

5. Para ejecutar la aplicación demo, utiliza:
   ```
   python demo/app.py
   ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.