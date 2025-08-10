import axios from 'axios'
const api = axios.create({ baseURL: import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000' })
api.interceptors.request.use((config) => {
  const token = import.meta.env.VITE_DEFAULT_TOKEN || ''
  if (token) config.headers['X-RedOps-Token'] = token
  return config
})
export default api
