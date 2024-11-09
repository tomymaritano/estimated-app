from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import traceback

app = FastAPI()

# Middleware para CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen (en producción debes restringirlo)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados HTTP
)

# Cargar el modelo entrenado
try:
    pipeline = joblib.load("estimator_model_professional.pkl")
    print("Modelo cargado con éxito.")
except FileNotFoundError:
    print("Error: El archivo 'estimator_model_professional.pkl' no se encuentra en la carpeta actual.")
    pipeline = None
except Exception as e:
    print("Error inesperado al cargar el modelo:")
    traceback.print_exc()
    pipeline = None

@app.post("/predict")
def predict(data: dict):
    try:
        if not pipeline:
            raise HTTPException(status_code=500, detail="Modelo no disponible")

        # Convertir los datos de entrada a un DataFrame
        input_df = pd.DataFrame([data])

        # Asegurarse de que las columnas categóricas estén como strings
        categorical_columns = ['technology', 'uiFramework', 'database', 'devops', 'platforms', 'stateManagement', 'developerLevel', 'uiType']
        input_df[categorical_columns] = input_df[categorical_columns].astype(str)

        # Llenar valores faltantes
        input_df.fillna('unknown', inplace=True)

        # Asegurarse de que las columnas categóricas tengan valores esperados
        expected_columns = {
            'technology': ['react', 'svelte', 'flutter', 'react_native', 'vue', 'vite', 'angular'],
            'uiFramework': ['chakra_ui', 'skeleton_ui', 'tailwindcss', 'mui'],
            'database': ['mongodb', 'postgresql', 'sql', 'firebase'],
            'devops': ['docker', 'kubernetes', 'jenkins'],
            'platforms': ['web', 'webapp', 'mobile', 'desktop'],
            'stateManagement': ['redux', 'vuex', 'ngrx', 'context_api'],
            'developerLevel': ['junior', 'ssr', 'senior'],
            'uiType': ['web', 'mobile', 'desktop', 'responsive', 'custom_design']
        }

        # Forzar las categorías a valores conocidos
        for col, expected_values in expected_columns.items():
            input_df[col] = input_df[col].where(input_df[col].isin(expected_values), 'unknown')

        # Depurar el DataFrame para verificar los valores de entrada antes de la predicción
        print("DataFrame de entrada ajustado:")
        print(input_df)

        # Realizar la predicción utilizando el pipeline
        prediction = pipeline.predict(input_df)

        return {"estimated_time": prediction[0]}
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Falta un parámetro: {e}")
    except Exception as e:
        print("Error inesperado al realizar la predicción:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error al realizar la predicción: {e}")