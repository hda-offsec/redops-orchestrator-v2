import { defineStore } from 'pinia'
export const useAppStore = defineStore('app', {
  state: () => ({
    token: import.meta.env.VITE_API_TOKEN || 'changeme',
    apiBase: import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000/api/v1',
    notifications: []
  }),
  actions: {
    notify(kind, msg) {
      this.notifications.push({ id: Date.now(), kind, msg })
      setTimeout(() => this.notifications.shift(), 5000)
    }
  }
})
