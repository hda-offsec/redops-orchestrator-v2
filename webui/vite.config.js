import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Proxy dev → backend FastAPI (port 5000)
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://127.0.0.1:5000',
      '/metrics': 'http://127.0.0.1:5000',
      '/health': 'http://127.0.0.1:5000'
    }
  },
  build: { outDir: 'dist' }
})
