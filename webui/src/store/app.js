import { reactive } from 'vue'
export const app = reactive({
  apiBase: localStorage.getItem('apiBase') || import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000',
  apiToken: localStorage.getItem('apiToken') || import.meta.env.VITE_DEFAULT_TOKEN || '',
  oscpSafe: localStorage.getItem('oscpSafe') === 'true',
})
export function saveApp(){
  localStorage.setItem('apiBase', app.apiBase)
  localStorage.setItem('apiToken', app.apiToken)
  localStorage.setItem('oscpSafe', app.oscpSafe ? 'true' : 'false')
}
