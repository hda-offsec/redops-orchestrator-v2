<!-- webui/src/views/Nmap.vue -->
<template>
  <div class="space-y-4">
    <h1 class="text-xl font-bold">Nmap</h1>

    <!-- Carte : lancement -->
    <Card>
      <template #title>Lancer un scan</template>

      <form class="grid md:grid-cols-3 gap-3" @submit.prevent="onStart">
        <div class="md:col-span-2">
          <label class="text-sm">Cible (FQDN/IP)</label>
          <input
            v-model="target"
            placeholder="scanme.nmap.org"
            class="w-full mt-1 px-3 py-2 bg-black/20 border border-redops-line rounded-lg outline-none focus:border-rose-500"
          />
        </div>

        <div>
          <label class="text-sm">Profil</label>
          <select
            v-model="profile"
            class="w-full mt-1 px-3 py-2 bg-black/20 border border-redops-line rounded-lg outline-none focus:border-rose-500"
          >
            <option v-for="p in profiles" :key="p" :value="p">{{ p }}</option>
          </select>
        </div>

        <div class="md:col-span-3 flex gap-2">
          <Button :disabled="!target || starting" @click="onStart">
            <span v-if="starting">Lancement…</span>
            <span v-else>Lancer</span>
          </Button>
        </div>
      </form>
    </Card>

    <!-- Carte : statut -->
    <Card v-if="jobId || status!=='idle'">
      <template #title>Statut</template>
      <div class="text-sm">Job&nbsp;: <code>{{ jobId || '-' }}</code></div>
      <div class="mt-1">
        <Badge :tone="tone(status)">{{ status }}</Badge>
      </div>
    </Card>

    <!-- Carte : résumé -->
    <Card v-if="summary">
      <template #title>Résumé</template>
      <div class="text-sm space-y-2">
        <div class="opacity-75">Host: {{ summary.host }}</div>
        <div class="flex gap-2 flex-wrap">
          <Badge
            v-for="p in summary.ports"
            :key="p.port"
            :tone="p.state==='open' ? 'bad' : 'neutral'"
          >
            {{ p.port }}/{{ p.proto }} — {{ p.service }} {{ p.version || '' }}
          </Badge>
        </div>
      </div>

      <div class="mt-3 flex gap-2">
        <Button @click="copy(jsonOut)">Copier JSON</Button>
        <Button @click="copy(textOut)">Copier texte</Button>
      </div>
    </Card>

    <!-- Carte : sortie brute -->
    <Card v-if="raw">
      <template #title>Sortie brute</template>
      <pre class="text-xs overflow-auto max-h-96 whitespace-pre-wrap">{{ raw }}</pre>
    </Card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Card from '@/components/ui/Card.vue'
import Button from '@/components/ui/Button.vue'
import Badge from '@/components/ui/Badge.vue'
import api from '@/api'
import { useJob } from '@/composables/useJob'
import { pushToast } from '@/components/ui/Toast.vue'

const target = ref('scanme.nmap.org')
const profile = ref('normal')
const profiles = ref(['normal'])
const starting = ref(false)

// hook générique pour la gestion de job (queue nmap)
const { jobId, status, result, start } = useJob('nmap')

// charge la liste des profils depuis l’API
onMounted(async () => {
  try {
    const { data } = await api.get('/api/v1/nmap/profiles')
    // selon l’API, data peut être une liste ou un dict de profils → on normalise
    profiles.value = Array.isArray(data) ? data : Object.keys(data || { normal: true })
  } catch (e) {
    pushToast({ title: 'Erreur', msg: 'Chargement des profils Nmap' })
  }
})

async function onStart () {
  if (!target.value) return
  starting.value = true
  try {
    await start({ target: target.value, profile: profile.value })
  } catch (e) {
    pushToast({ title: 'Erreur', msg: 'Lancement du scan' })
  } finally {
    starting.value = false
  }
}

// map statut → tonalité badge
function tone (s) {
  if (s === 'finished') return 'ok'
  if (s === 'failed' || s === 'error') return 'bad'
  if (s === 'started' || s === 'running') return 'warn'
  if (!s || s === 'idle') return 'neutral'
  return 'info'
}

const raw = computed(() => result.value?.stdout || '')

// construit un petit résumé depuis le JSON parsé
const summary = computed(() => {
  const hosts = result.value?.result?.hosts || []
  if (!hosts.length) return null
  const [h] = hosts
  const ports = (h.ports || []).map(p => ({
    port: p,
    proto: 'tcp',
    state: 'open',
    service: '?',
    version: ''
  }))
  return { host: h.address, ports }
})

const jsonOut = computed(() => JSON.stringify(result.value?.result || {}, null, 2))
const textOut = computed(() => {
  if (!summary.value) return ''
  return summary.value.ports.map(p => `${p.port}/${p.proto} ${p.service}`).join('\n')
})

async function copy (txt) {
  try {
    await navigator.clipboard.writeText(txt || '')
    pushToast({ title: 'Copié', msg: 'dans le presse-papiers' })
  } catch {
    pushToast({ title: 'Erreur', msg: 'Impossible de copier' })
  }
}
</script>
