import React, { useState } from 'react';

const EstimateForm = () => {
  const [formData, setFormData] = useState({
    technology: '',
    uiFramework: '',
    database: '',
    devops: '',
    platforms: '',
    stateManagement: '',
    numberOfDevelopers: 1,
    developerLevel: '',
    pluginsLibraries: '',
    uiType: '',  // Nuevo campo para UI
  });

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement | HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      alert(`Estimated time: ${data.estimated_time} days`);
    } catch (error) {
      console.error('Error fetching the estimate:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-md">
      {/* Campo de selección de UI */}
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">UI Type</label>
        <select
          name="uiType"
          value={formData.uiType}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="web">Web UI</option>
          <option value="mobile">Mobile UI</option>
          <option value="desktop">Desktop UI</option>
          <option value="responsive">Responsive UI</option>
          <option value="custom_design">Custom Design</option>
        </select>
      </div>

      {/* Resto de los campos */}
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Technology</label>
        <select
          name="technology"
          value={formData.technology}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="react">React</option>
          <option value="svelte">Svelte</option>
          <option value="flutter">Flutter</option>
          <option value="react_native">React Native</option>
          <option value="vue">Vue</option>
          <option value="vite">Vite</option>
          <option value="angular">Angular</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">UI Framework</label>
        <select
          name="uiFramework"
          value={formData.uiFramework}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="chakra_ui">Chakra UI</option>
          <option value="skeleton_ui">Skeleton UI</option>
          <option value="tailwindcss">TailwindCSS</option>
          <option value="mui">Material UI (MUI)</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Database</label>
        <select
          name="database"
          value={formData.database}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="mongodb">MongoDB</option>
          <option value="postgresql">PostgreSQL</option>
          <option value="sql">SQL</option>
          <option value="firebase">Firebase</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">DevOps</label>
        <select
          name="devops"
          value={formData.devops}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="docker">Docker</option>
          <option value="kubernetes">Kubernetes</option>
          <option value="jenkins">Jenkins</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Platforms</label>
        <select
          name="platforms"
          value={formData.platforms}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="web">Web</option>
          <option value="webapp">WebApp</option>
          <option value="mobile">Mobile</option>
          <option value="desktop">Desktop</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">State Management</label>
        <select
          name="stateManagement"
          value={formData.stateManagement}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="redux">Redux</option>
          <option value="vuex">Vuex</option>
          <option value="ngrx">NgRx</option>
          <option value="context_api">Context API</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Number of Developers</label>
        <input
          type="number"
          name="numberOfDevelopers"
          value={formData.numberOfDevelopers}
          min="1"
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Developer Level</label>
        <select
          name="developerLevel"
          value={formData.developerLevel}
          onChange={handleChange}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">None</option>
          <option value="junior">Junior</option>
          <option value="ssr">Semi-Senior (SSR)</option>
          <option value="senior">Senior</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Plugins or Libraries</label>
        <textarea
          name="pluginsLibraries"
          value={formData.pluginsLibraries}
          onChange={handleChange}
          placeholder="Enter the list of plugins or libraries used"
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>

      <button
        type="submit"
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Get Estimate
      </button>
    </form>
  );
};

export default EstimateForm;