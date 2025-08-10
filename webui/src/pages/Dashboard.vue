<template>
  <AppLayout @toggleTheme="toggle">
    <h1 class="text-xl font-bold mb-4">Dashboard</h1>
    <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-4">
      <ModuleCard to="/nmap" title="Nmap" subtitle="Scan r\u00e9seau rapide" :icon="CommandLineIcon" />
      <ModuleCard to="/webrecon" title="Web Recon" subtitle="D\u00e9couverte surface web" :icon="GlobeAltIcon" />
      <ModuleCard to="/vuln" title="Vuln" subtitle="Enrichissement & d\u00e9tection" :icon="ShieldExclamationIcon" />
      <ModuleCard to="/settings" title="Settings" subtitle="API, tokens, limites" :icon="Cog6ToothIcon" />
    </div>
  </AppLayout>
</template>
<script setup lang="ts">
import AppLayout from '@/layouts/AppLayout.vue'
import ModuleCard from '@/components/ModuleCard.vue'
import { CommandLineIcon, GlobeAltIcon, ShieldExclamationIcon, Cog6ToothIcon } from '@heroicons/vue/24/outline'
const toggle = () => document.documentElement.classList.toggle('dark')
</script>
