from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import traceback

# Crear una instancia de FastAPI
app = FastAPI()

# Añadir el middleware CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes de origen. Puedes restringirlo en producción.
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados HTTP
)

# Cargar el modelo entrenado
try:
    model = joblib.load("estimator_model.pkl")
    print("Modelo cargado con éxito.")
except FileNotFoundError:
    print("Error: El archivo 'estimator_model.pkl' no se encuentra en la carpeta actual.")
    model = None
except Exception as e:
    print("Error inesperado al cargar el modelo:")
    traceback.print_exc()  # Esto imprimirá la traza del error para más detalles
    model = None

# Endpoint para predicción
@app.post("/predict")
def predict(data: dict):
    try:
        if not model:
            raise HTTPException(status_code=500, detail="Modelo no disponible")

        # Crear el array de características basado en los datos recibidos
        features = np.array([
            data.get('react', 0),
            data.get('svelte', 0),
            data.get('flutter', 0),
            data.get('react_native', 0),
            data.get('chakra_ui', 0),
            data.get('mui', 0),
            data.get('skeleton', 0),
            data.get('tailwind', 0),
        ]).reshape(1, -1)

        prediction = model.predict(features)
        return {"estimated_time": prediction[0]}
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Falta un parámetro: {e}")
    except Exception as e:
        print("Error inesperado al realizar la predicción:")
        traceback.print_exc()  # Imprimir la traza del error
        raise HTTPException(status_code=500, detail=f"Error al realizar la predicción: {e}")