import axios from 'axios';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { feature1, feature2 } = req.body;

    try {
      // Realiza la solicitud al servidor de FastAPI
      const response = await axios.post('http://localhost:8000/predict', {
        feature1,
        feature2,
      });

      res.status(200).json({ estimatedTime: response.data.estimated_time });
    } catch (error) {
      console.error('Error al obtener la predicción:', error);
      res.status(500).json({ error: 'Error al obtener la predicción' });
    }
  } else {
    res.status(405).json({ error: 'Método no permitido' });
  }
}