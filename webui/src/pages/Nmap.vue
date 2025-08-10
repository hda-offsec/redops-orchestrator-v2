<template>
  <AppLayout @toggleTheme="toggle">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-xl font-bold mb-4">Nmap</h1>
      <div class="rounded-xl border border-zinc-800 bg-zinc-900/50 p-4 space-y-3">
        <div class="flex gap-2">
          <input v-model="target" placeholder="cible (FQDN / IP)"
            class="flex-1 px-3 py-2 rounded-lg bg-zinc-900 border border-zinc-800 text-zinc-100 placeholder-zinc-500 focus:outline-none focus:ring-2 focus:ring-brand-600" />
          <select v-model="profile" class="px-3 py-2 rounded-lg bg-zinc-900 border border-zinc-800 text-zinc-100">
            <option value="normal">normal</option><option value="web_recon">web_recon</option>
          </select>
          <button :disabled="loading" class="px-4 py-2 rounded-lg bg-brand-600 hover:bg-brand-500 disabled:opacity-50" @click="launch">Lancer</button>
        </div>
        <div class="text-sm text-zinc-400">Job ID: <span class="text-zinc-200">{{ jobId || '-' }}</span></div>
        <div class="text-sm text-zinc-400">Statut: <span class="text-zinc-200 font-medium">{{ status || '-' }}</span></div>
      </div>
      <div v-if="stdout" class="mt-4">
        <h2 class="text-sm font-semibold text-zinc-300 mb-2">Sortie Nmap</h2>
        <pre class="text-xs leading-relaxed bg-black/60 border border-zinc-800 rounded-xl p-4 overflow-auto max-h-[40vh]">{{ stdout }}</pre>
      </div>
      <div v-if="result" class="mt-4">
        <h2 class="text-sm font-semibold text-zinc-300 mb-2">R\u00e9sum\u00e9</h2>
        <pre class="text-xs bg-zinc-900 border border-zinc-800 rounded-xl p-4 overflow-auto">{{ jsonPretty }}</pre>
      </div>
    </div>
    <Toasts />
  </AppLayout>
</template>
<script setup lang="ts">
import { ref, computed } from 'vue'
import api from '@/lib/api'
import AppLayout from '@/layouts/AppLayout.vue'
import Toasts from '@/components/Toasts.vue'
import { useToasts } from '@/composables/useToasts'
const target = ref('scanme.nmap.org')
const profile = ref('normal')
const jobId = ref(''); const status = ref(''); const stdout = ref(''); const result = ref<any>(null); const loading = ref(false)
const { push } = useToasts()
const jsonPretty = computed(()=> JSON.stringify(result.value, null, 2))
const poll = async () => {
  if (!jobId.value) return
  try {
    const { data } = await api.get(`/api/v1/nmap/scans/${jobId.value}`)
    status.value = data.status
    if (data.result?.stdout) stdout.value = data.result.stdout
    if (data.status === 'finished') { result.value = data.result?.result || null; push({title:'Scan termin\u00e9',kind:'success'}); loading.value=false; return }
    if (data.status === 'failed') { push({title:'Scan \u00e9chou\u00e9',kind:'error'}); loading.value=false; return }
    setTimeout(poll, 1500)
  } catch(e){ push({title:'Erreur de polling',kind:'error'}); loading.value=false }
}
const launch = async () => {
  loading.value = true; jobId.value=''; status.value='queued'; stdout.value=''; result.value=null
  try {
    const { data } = await api.post('/api/v1/nmap/scans',{ target: target.value, profile: profile.value })
    jobId.value = data.job_id; push({title:`Job ${data.job_id} soumis`,kind:'info'}); poll()
  } catch(e){ push({title:'Erreur de soumission',kind:'error'}); loading.value=false }
}
const toggle = () => document.documentElement.classList.toggle('dark')
</script>
