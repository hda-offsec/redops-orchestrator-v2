<template>
  <AppLayout @toggleTheme="toggle">
    <h1 class="text-xl font-bold mb-4">Settings</h1>
    <div class="space-y-2 text-sm">
      <div class="text-zinc-400">API Base: <span class="text-zinc-200">{{ apiBase }}</span></div>
      <div class="text-zinc-400">Token: <span class="text-zinc-200">{{ token || '-' }}</span></div>
    </div>
  </AppLayout>
</template>
<script setup lang="ts">
import AppLayout from '@/layouts/AppLayout.vue'
const apiBase = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000'
const token = import.meta.env.VITE_DEFAULT_TOKEN || ''
const toggle = () => document.documentElement.classList.toggle('dark')
</script>
