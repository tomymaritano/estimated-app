import pandas as pd

def get_ux_data():
    data = {
        'ux_complexity': ['baja', 'media', 'alta', 'media', 'alta'],
        'accessibility': ['alta', 'media', 'baja', 'media', 'alta'],
        'estimated_time': [7, 14, 21, 14, 18]
    }
    df = pd.DataFrame(data)
    return df

# Función para preprocesar los datos UX
def preprocess_ux_data(df):
    # Preprocesamiento específico para datos UX
    return df