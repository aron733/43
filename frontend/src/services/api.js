import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    'Content-Type': 'application/json'
  }
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const trading = {
  getPositions: () => api.get('/trading/positions'),
  getTrades: () => api.get('/trading/trades'),
  createOrder: (data) => api.post('/trading/order', data)
};

export const market = {
  getQuote: (symbol) => api.get(`/market/quote/${symbol}`),
  getIntraday: (symbol, interval) => api.get(`/market/intraday/${symbol}?interval=${interval}`)
};

export const sentiment = {
  getMarket: () => api.get('/sentiment/market'),
  getCrypto: () => api.get('/sentiment/crypto')
};

export const myfxbook = {
  getAccounts: () => api.get('/myfxbook/accounts'),
  getStats: (accountId) => api.get(`/myfxbook/account/${accountId}/stats`)
};

export default api;