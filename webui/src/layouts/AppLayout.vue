<template>
  <div class="min-h-dvh flex bg-zinc-950 text-zinc-100">
    <aside class="hidden md:flex w-64 flex-col border-r border-zinc-800 bg-zinc-900/60">
      <div class="p-5 border-b border-zinc-800">
        <div class="text-xl font-extrabold"><span class="text-brand-400">Red</span>Ops<span class="text-zinc-400">2</span></div>
        <div class="text-xs text-zinc-400">Orchestrator</div>
      </div>
      <nav class="flex-1 p-3 space-y-1">
        <RouterLink v-for="item in items" :key="item.to" :to="item.to"
          class="flex items-center gap-3 px-3 py-2 rounded-md text-sm hover:bg-zinc-800/80"
          :class="isActive(item.to) ? 'bg-zinc-800 text-brand-300' : 'text-zinc-300'">
          <component :is="item.icon" class="w-5 h-5" /><span>{{ item.label }}</span>
        </RouterLink>
      </nav>
      <div class="p-3 border-t border-zinc-800">
        <button class="w-full text-left text-zinc-400 text-sm hover:text-zinc-200" @click="$emit('toggleTheme')">
          Toggle theme
        </button>
      </div>
    </aside>
    <div class="flex-1 flex flex-col">
      <header class="h-14 border-b border-zinc-800 bg-zinc-900/60 backdrop-blur flex items-center px-3 md:px-6 gap-3">
        <div class="text-sm text-zinc-400">Environment</div>
        <div class="text-xs px-2 py-1 rounded bg-brand-900/40 text-brand-300">local</div>
        <div class="ml-auto text-xs text-zinc-400">API: <span class="text-zinc-200">{{ apiBase }}</span></div>
      </header>
      <main class="p-4 md:p-6"><slot /></main>
    </div>
  </div>
</template>
<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { HomeIcon, Cog6ToothIcon, GlobeAltIcon, ShieldExclamationIcon, CommandLineIcon } from '@heroicons/vue/24/outline'
const route = useRoute()
const apiBase = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000'
const items = [
  { to: '/', label: 'Dashboard', icon: HomeIcon },
  { to: '/nmap', label: 'Nmap', icon: CommandLineIcon },
  { to: '/webrecon', label: 'Web Recon', icon: GlobeAltIcon },
  { to: '/vuln', label: 'Vuln', icon: ShieldExclamationIcon },
  { to: '/settings', label: 'Settings', icon: Cog6ToothIcon },
]
const isActive = (to:string)=> computed(()=>route.path===to).value
</script>
