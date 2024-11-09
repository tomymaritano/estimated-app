import pandas as pd

def get_backend_data():
    data = {
        'technology': ['react', 'vue', 'angular'],
        'uiFramework': ['tailwindcss', 'mui', 'chakra_ui'],
        'database': ['mongodb', 'sql', 'postgresql'],
        'devops': ['docker', 'kubernetes', 'jenkins'],
        'platforms': ['web', 'webapp', 'mobile'],
        'stateManagement': ['redux', 'context_api', 'ngrx'],
        'numberOfDevelopers': [3, 5, 2],
        'developerLevel': ['senior', 'junior', 'ssr'],
        'pluginsLibraries': ['redux-thunk', 'axios', 'formik'],
        'uiType': ['responsive', 'web', 'mobile'],
        'estimated_time': [20, 30, 15]  # Días de estimación para cada proyecto
    }
    return pd.DataFrame(data)