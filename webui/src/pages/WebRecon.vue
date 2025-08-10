<template>
  <AppLayout @toggleTheme="toggle">
    <h1 class="text-xl font-bold mb-4">Web Recon</h1>
    <p class="text-zinc-400">Module en cours de d\u00e9veloppement.</p>
  </AppLayout>
</template>
<script setup lang="ts">
import AppLayout from '@/layouts/AppLayout.vue'
const toggle = () => document.documentElement.classList.toggle('dark')
</script>
