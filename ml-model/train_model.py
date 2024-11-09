import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Importar datos de los módulos
from backend_model import get_backend_data
from frontend_model import get_frontend_data

# Unir los datos de backend y frontend
backend_df = get_backend_data()
frontend_df = get_frontend_data()

# Asegurarse de que todas las columnas existen en ambos DataFrames
required_columns = ['technology', 'uiFramework', 'database', 'devops', 'platforms', 'stateManagement', 'numberOfDevelopers', 'developerLevel', 'pluginsLibraries', 'uiType', 'estimated_time']

for df in [backend_df, frontend_df]:
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0 if col == 'numberOfDevelopers' else 'unknown'

# Unir los DataFrames asegurando que tienen las mismas columnas
all_data = pd.concat([backend_df, frontend_df], axis=0)

# Reemplazar valores NaN
all_data.fillna('unknown', inplace=True)

# Separar las características (X) y el objetivo (y)
X = all_data.drop('estimated_time', axis=1)
y = all_data['estimated_time']

# Definir transformadores para cada tipo de característica
numeric_features = ['numberOfDevelopers']
categorical_features = ['technology', 'uiFramework', 'database', 'devops', 'platforms', 'stateManagement', 'developerLevel', 'uiType']
text_features = 'pluginsLibraries'

numeric_transformer = StandardScaler()

# Definir todas las categorías posibles para `OneHotEncoder`
technology_categories = ['react', 'svelte', 'flutter', 'react_native', 'vue', 'vite', 'angular']
ui_framework_categories = ['chakra_ui', 'skeleton_ui', 'tailwindcss', 'mui']
database_categories = ['mongodb', 'postgresql', 'sql', 'firebase']
devops_categories = ['docker', 'kubernetes', 'jenkins']
platform_categories = ['web', 'webapp', 'mobile', 'desktop']
state_management_categories = ['redux', 'vuex', 'ngrx', 'context_api']
developer_level_categories = ['junior', 'ssr', 'senior']
ui_type_categories = ['web', 'mobile', 'desktop', 'responsive', 'custom_design']

# Preprocesamiento de columnas categóricas: OneHotEncoder con categorías definidas y manejo de valores desconocidos
categorical_transformer = OneHotEncoder(categories=[
    technology_categories,
    ui_framework_categories,
    database_categories,
    devops_categories,
    platform_categories,
    state_management_categories,
    developer_level_categories,
    ui_type_categories
], handle_unknown='ignore')

text_transformer = TfidfVectorizer(min_df=1)

# Crear el preprocesador usando ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features),
        ('text', text_transformer, text_features)
    ]
)

# Crear el modelo de regresión (Random Forest)
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Crear el pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(pipeline, 'estimator_model_professional.pkl')

print("Modelo entrenado y guardado como 'estimator_model_professional.pkl'")