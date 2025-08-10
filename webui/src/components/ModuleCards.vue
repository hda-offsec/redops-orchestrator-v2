<script setup>
const modules = [
  { key: 'nmap', title: 'Nmap', desc: 'TCP/UDP, services, NSE', to: '/nmap' },
  { key: 'webrecon', title: 'WebRecon', desc: 'Headers, cookies, CORS', to: '/webrecon' },
  { key: 'vuln', title: 'Vuln', desc: 'Nuclei + Searchsploit', to: '/vuln' },
  { key: 'orchestrator', title: 'Orchestrator', desc: 'Profils multi-modules', to: '/orchestrator' }
]
</script>

<template>
  <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
    <RouterLink v-for="m in modules" :key="m.key" :to="m.to"
      class="bg-redops-card p-5 rounded-xl border border-gray-800 hover:border-red-600 transition">
      <div class="text-lg font-semibold text-red-400">[[ m.title ]]</div>
      <div class="text-sm text-gray-400 mt-1">[[ m.desc ]]</div>
    </RouterLink>
  </div>
</template>
