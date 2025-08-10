import axios from 'axios'
const api = axios.create({
  baseURL: localStorage.getItem('apiBase') || import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000'
})
api.interceptors.request.use(cfg=>{
  const token = localStorage.getItem('apiToken') || import.meta.env.VITE_DEFAULT_TOKEN || ''
  if (token) cfg.headers['X-RedOps-Token'] = token
  return cfg
})
export default api
