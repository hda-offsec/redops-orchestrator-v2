import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'node:path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
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
