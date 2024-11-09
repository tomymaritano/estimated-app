import { useState } from 'react';

// Definir el tipo para las tecnologías
type FeaturesType = {
  react: boolean;
  svelte: boolean;
  flutter: boolean;
  react_native: boolean;
  chakra_ui: boolean;
  mui: boolean;
  skeleton: boolean;
  tailwind: boolean;
};

function EstimateForm() {
  // Estado para los datos del formulario y el resultado
  const [features, setFeatures] = useState<FeaturesType>({
    react: false,
    svelte: false,
    flutter: false,
    react_native: false,
    chakra_ui: false,
    mui: false,
    skeleton: false,
    tailwind: false,
  });
  const [estimatedTime, setEstimatedTime] = useState<number | null>(null);

  // Manejar cambios en los inputs del formulario
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, checked } = e.target;
    // Asegurarse de que 'name' es una clave válida para el objeto 'features'
    setFeatures((prevFeatures) => ({
      ...prevFeatures,
      [name]: checked,
    }));
  };

  // Enviar solicitud a la API
  const handleEstimate = async () => {
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          react: features.react ? 1 : 0,
          svelte: features.svelte ? 1 : 0,
          flutter: features.flutter ? 1 : 0,
          react_native: features.react_native ? 1 : 0,
          chakra_ui: features.chakra_ui ? 1 : 0,
          mui: features.mui ? 1 : 0,
          skeleton: features.skeleton ? 1 : 0,
          tailwind: features.tailwind ? 1 : 0,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setEstimatedTime(data.estimated_time); // Actualiza el estado con la estimación
      } else {
        console.error('Error al obtener la estimación:', response.status);
      }
    } catch (error) {
      console.error('Error al obtener la estimación:', error);
    }
  };

  // Renderizar el formulario y el resultado
  return (
    <div className="max-w-md mx-auto my-10 p-8 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">Estimador de Tiempo de Desarrollo</h2>
      <div className="mb-4">
        {Object.keys(features).map((feature) => (
          <div key={feature} className="mb-2">
            <label className="flex items-center">
              <input
                type="checkbox"
                name={feature}
                checked={features[feature as keyof FeaturesType]} // Asegurar el tipo correcto
                onChange={handleInputChange}
                className="mr-2"
              />
              {feature.replace('_', ' ').toUpperCase()}
            </label>
          </div>
        ))}
      </div>
      <button
        onClick={handleEstimate}
        className="w-full p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-200"
      >
        Obtener Estimación
      </button>
      {/* Mostrar la estimación si está disponible */}
      {estimatedTime !== null && (
        <p className="mt-4 text-center text-xl font-semibold">
          Tiempo estimado: {estimatedTime} días
        </p>
      )}
    </div>
  );
}

export default EstimateForm;