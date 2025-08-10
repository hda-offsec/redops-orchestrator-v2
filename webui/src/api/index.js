import axios from 'axios'

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000/api/v1'
})

API.interceptors.request.use((cfg) => {
  cfg.headers['X-RedOps-Token'] = import.meta.env.VITE_API_TOKEN || 'changeme'
  return cfg
})

export default API
