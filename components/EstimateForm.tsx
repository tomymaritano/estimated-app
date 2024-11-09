import { useState } from 'react';

function EstimateForm() {
  const [features, setFeatures] = useState({ feature1: '', feature2: '' });
  const [estimatedTime, setEstimatedTime] = useState(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFeatures({ ...features, [name]: value });
  };

  const handleEstimate = async () => {
    try {
      const response = await fetch('/api/estimate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(features),
      });
      const data = await response.json();
      setEstimatedTime(data.estimatedTime);
    } catch (error) {
      console.error('Error al obtener la estimación:', error);
    }
  };

  return (
    <div className="max-w-md mx-auto my-10 p-8 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">Estimador de Tiempo de Desarrollo</h2>
      <div className="mb-4">
        <input
          type="text"
          name="feature1"
          placeholder="Feature 1"
          value={features.feature1}
          onChange={handleInputChange}
          className="w-full p-2 border border-gray-300 rounded-lg"
        />
      </div>
      <div className="mb-4">
        <input
          type="text"
          name="feature2"
          placeholder="Feature 2"
          value={features.feature2}
          onChange={handleInputChange}
          className="w-full p-2 border border-gray-300 rounded-lg"
        />
      </div>
      <button
        onClick={handleEstimate}
        className="w-full p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-200"
      >
        Obtener Estimación
      </button>
      {estimatedTime && (
        <p className="mt-4 text-center text-xl font-semibold">
          Tiempo estimado: {estimatedTime} días
        </p>
      )}
    </div>
  );
}

export default EstimateForm;