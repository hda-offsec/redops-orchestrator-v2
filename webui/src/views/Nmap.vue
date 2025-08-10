<script setup>
import { ref, onBeforeUnmount } from 'vue'

// Base API : en dev Vite utilise le proxy, en prod (servi par FastAPI) on reste en relatif
const API_BASE = import.meta.env.VITE_API_BASE || ''

// Token : settings > localStorage('redops_token') sinon fallback .env (VITE_DEFAULT_TOKEN) sinon 'changeme'
const TOKEN = localStorage.getItem('redops_token') || import.meta.env.VITE_DEFAULT_TOKEN || 'changeme'

const target = ref('scanme.nmap.org')
const profile = ref('normal')
const loading = ref(false)
const jobId = ref('')
const status = ref('')
const result = ref(null)
let pollTimer = null

const PROFILES = [
  { value: 'normal', label: 'Normal' },
  { value: 'quick',  label: 'Quick'  },
  { value: 'full',   label: 'Full'   },
]

// Lancer le scan
async function startScan () {
  if (!target.value) return
  loading.value = true
  result.value = null
  status.value = 'queued'
  jobId.value = ''

  try {
    const res = await fetch(`${API_BASE}/api/v1/nmap/scans`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-RedOps-Token': TOKEN
      },
      body: JSON.stringify({ target: target.value, profile: profile.value })
    })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()
    jobId.value = data.job_id || ''
    // poll
    if (jobId.value) {
      pollStatus(jobId.value)
    } else {
      status.value = 'error'
      loading.value = false
    }
  } catch (e) {
    console.error(e)
    status.value = 'error'
    loading.value = false
  }
}

async function pollStatus (id) {
  clearTimeout(pollTimer)
  try {
    const res = await fetch(`${API_BASE}/api/v1/nmap/scans/${id}`, {
      headers: { 'X-RedOps-Token': TOKEN }
    })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()
    status.value = data.status
    if (data.status === 'finished') {
      result.value = data.result || null
      loading.value = false
      return
    }
    if (data.status === 'failed' || data.status === 'error') {
      loading.value = false
      return
    }
    pollTimer = setTimeout(() => pollStatus(id), 1500)
  } catch (e) {
    console.error(e)
    pollTimer = setTimeout(() => pollStatus(id), 2000)
  }
}

onBeforeUnmount(() => clearTimeout(pollTimer))
</script>

<template>
  <div class="space-y-6">
    <h2 class="text-xl font-semibold">Nmap</h2>

    <!-- Carte formulaire -->
    <div class="rounded-2xl border border-zinc-800 bg-zinc-900/40 p-4">
      <div class="grid gap-3 sm:grid-cols-[1fr_160px_auto]">
        <input
          class="w-full rounded-xl bg-zinc-900/70 border border-zinc-800 px-3 py-2 outline-none focus:border-zinc-600"
          placeholder="cible (FQDN / IP)"
          v-model="target"
        />
        <select
          class="rounded-xl bg-zinc-900/70 border border-zinc-800 px-3 py-2 outline-none focus:border-zinc-600"
          v-model="profile"
        >
          <option v-for="p in PROFILES" :key="p.value" :value="p.value">{{ p.label }}</option>
        </select>
        <button
          class="rounded-xl px-4 py-2 font-medium bg-rose-600 hover:bg-rose-500 disabled:opacity-60"
          :disabled="loading"
          @click="startScan"
        >
          {{ loading ? 'En cours…' : 'Lancer' }}
        </button>
      </div>

      <div class="mt-3 text-sm text-zinc-400 flex items-center gap-4">
        <div>Job ID : <code class="text-zinc-300">{{ jobId || '-' }}</code></div>
        <div>Statut : <span class="text-zinc-200 font-medium">{{ status || '-' }}</span></div>
      </div>
    </div>

    <!-- Résultat -->
    <div v-if="result" class="rounded-2xl border border-zinc-800 bg-zinc-900/40 p-4">
      <h3 class="font-semibold mb-2">Résultats</h3>

      <div v-if="result.stdout" class="mb-4">
        <div class="text-sm text-zinc-400 mb-1">Stdout</div>
        <pre class="text-xs leading-5 whitespace-pre-wrap p-3 rounded-xl bg-black/40 border border-zinc-800 overflow-auto max-h-[420px]">
{{ result.stdout }}
        </pre>
      </div>

      <div v-if="result.result" class="mb-2">
        <div class="text-sm text-zinc-400 mb-1">JSON</div>
        <pre class="text-xs leading-5 whitespace-pre p-3 rounded-xl bg-black/40 border border-zinc-800 overflow-auto max-h-[420px]">
{{ JSON.stringify(result.result, null, 2) }}
        </pre>
      </div>
    </div>
  </div>
</template>
