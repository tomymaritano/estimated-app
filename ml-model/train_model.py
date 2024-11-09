import joblib
from sklearn.linear_model import LinearRegression

# Datos de ejemplo para entrenamiento
# Cada fila de X representa un pedido con características binarias (tecnologías incluidas)
# Orden: [React, Svelte, Flutter, React Native, Chakra UI, MUI, Skeleton, Tailwind CSS]
X = [
    [1, 0, 0, 0, 1, 0, 0, 1],  # Proyecto que usa React, Chakra UI, Tailwind CSS
    [0, 1, 0, 0, 0, 1, 0, 0],  # Proyecto que usa Svelte, MUI
    [0, 0, 1, 0, 0, 0, 1, 0],  # Proyecto que usa Flutter, Skeleton
    [1, 0, 0, 1, 0, 0, 0, 1],  # Proyecto que usa React, React Native, Tailwind CSS
    [0, 1, 0, 0, 1, 0, 0, 0],  # Proyecto que usa Svelte, Chakra UI
]

# Tiempo estimado para cada proyecto en días
y = [15, 12, 20, 25, 18]

# Entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Guardar el modelo entrenado en un archivo
joblib.dump(model, 'estimator_model.pkl')

print("Modelo entrenado y guardado como 'estimator_model.pkl'")