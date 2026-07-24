import { useState, useEffect } from 'react';
import axios from 'axios';

const useSentiment = () => {
  const [sentiment, setSentiment] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSentiment = async () => {
      try {
        const response = await axios.get('/api/sentiment/market');
        setSentiment(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching sentiment:', error);
      }
    };

    fetchSentiment();
    const interval = setInterval(fetchSentiment, 10000);
    return () => clearInterval(interval);
  }, []);

  return { sentiment, loading };
};

export default useSentiment;