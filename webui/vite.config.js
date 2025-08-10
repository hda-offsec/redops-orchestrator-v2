import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

// Proxy dev → backend FastAPI (port 5000)
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
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
