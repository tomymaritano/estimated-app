from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Cargar el modelo entrenado
try:
    model = joblib.load("estimator_model.pkl")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    model = None

# Definir un endpoint para realizar predicciones
@app.post("/predict")
def predict(data: dict):
    try:
        if not model:
            return {"error": "Modelo no disponible"}
        # Convertir los datos de entrada en un formato adecuado para el modelo
        features = np.array([data['feature1'], data['feature2']]).reshape(1, -1)
        # Realizar la predicción
        prediction = model.predict(features)
        return {"estimated_time": prediction[0]}
    except KeyError as e:
        return {"error": f"Falta un parámetro: {e}"}
    except Exception as e:
        return {"error": f"Error al realizar la predicción: {e}"}