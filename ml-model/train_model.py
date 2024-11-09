import joblib
from sklearn.linear_model import LinearRegression

# Datos de ejemplo para entrenamiento
X = [[1, 2], [2, 3], [3, 4]]  # Características de entrada (puedes cambiarlas con datos reales)
y = [5, 7, 9]  # Tiempos de desarrollo (objetivo)

# Entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Guardar el modelo entrenado en un archivo
joblib.dump(model, 'estimator_model.pkl')

print("Modelo entrenado y guardado como 'estimator_model.pkl'")