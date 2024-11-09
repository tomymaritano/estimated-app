import pandas as pd

def get_frontend_data():
    data = {
        'technology': ['flutter', 'svelte', 'react_native'],
        'uiFramework': ['tailwindcss', 'mui', 'chakra_ui'],
        'database': ['firebase', 'sql', 'mongodb'],
        'devops': ['docker', 'kubernetes', 'jenkins'],
        'platforms': ['mobile', 'desktop', 'web'],
        'stateManagement': ['redux', 'context_api', 'vuex'],
        'numberOfDevelopers': [2, 4, 3],
        'developerLevel': ['ssr', 'senior', 'junior'],
        'pluginsLibraries': ['flutter_bloc', 'vue_router', 'react_navigation'],
        'uiType': ['mobile', 'desktop', 'responsive'],
        'estimated_time': [25, 18, 22]  # Días de estimación para cada proyecto
    }
    return pd.DataFrame(data)