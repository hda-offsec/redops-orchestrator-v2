<script setup>
import { useAppStore } from '../store/app'
const app = useAppStore()
</script>
<template>
  <h1 class="text-2xl font-bold mb-4">Settings</h1>
  <div class="bg-redops-card p-4 rounded-xl border border-gray-800 space-y-3">
    <div class="text-sm text-gray-400">Ces champs lisent les variables Vite (rebuild nécessaire pour changer).</div>
    <div class="grid md:grid-cols-2 gap-3">
      <div><label class="text-xs">API Base</label><input disabled :value="app.apiBase" class="w-full bg-black/40 border-gray-700 rounded"/></div>
      <div><label class="text-xs">Token</label><input disabled :value="app.token" class="w-full bg-black/40 border-gray-700 rounded"/></div>
    </div>
  </div>
</template>
