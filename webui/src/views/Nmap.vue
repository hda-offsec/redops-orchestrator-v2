<template>
  <div class="space-y-4">
    <h1 class="text-xl font-bold">Nmap</h1>

    <Card>
      <template #title>Lancer un scan</template>
      <form class="grid md:grid-cols-3 gap-3" @submit.prevent="onStart">
        <div class="md:col-span-2">
          <label class="text-sm">Cible (FQDN/IP)</label>
          <input v-model="target" placeholder="scanme.nmap.org"
            class="w-full mt-1 px-3 py-2 bg-black/20 border border-redops-line rounded-lg"/>
        </div>
        <div>
          <label class="text-sm">Profil</label>
          <select v-model="profile"
            class="w-full mt-1 px-3 py-2 bg-black/20 border border-redops-line rounded-lg">
            <option v-for="p in profiles" :key="p" :value="p">{{ p }}</option>
          </select>
        </div>
        <div class="md:col-span-3">
          <Button :disabled="!target" @click="onStart">Lancer</Button>
        </div>
      </form>
    </Card>

    <Card v-if="jobId || status!=='idle'">
      <template #title>Statut</template>
      <div class="text-sm">Job: <code>{{ jobId||'-' }}</code></div>
      <div class="mt-1">
        <Badge :tone="tone(status)">{{ status }}</Badge>
      </div>
    </Card>

    <Card v-if="summary">
      <template #title>Résumé</template>
      <div class="text-sm space-y-2">
        <div class="opacity-75">Host: {{ summary.host }}</div>
        <div class="flex gap-2 flex-wrap">
          <Badge v-for="p in summary.ports" :key="p.port"
                 :tone="p.state==='open'?'bad':'neutral'">
            {{ p.port }}/{{ p.proto }} — {{ p.service }} {{ p.version||'' }}
          </Badge>
        </div>
      </div>
      <div class="mt-3 flex gap-2">
        <Button @click="copy(jsonOut)">Copier JSON</Button>
        <Button @click="copy(textOut)">Copier texte</Button>
      </div>
    </Card>

    <Card v-if="raw">
      <template #title>Raw output</template>
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
const { jobId, status, result, start } = useJob('nmap')

onMounted(async ()=>{
  try{
    const { data } = await api.get('/api/v1/nmap/profiles')
    profiles.value = data
  }catch(e){ pushToast({title:'Erreur',msg:'Chargement des profils Nmap'}) }
})

function onStart(){ start({ target:target.value, profile:profile.value }) }
function tone(s){ return s==='finished'?'ok':s==='failed'?'bad':s==='started'?'warn':'info' }

const raw = computed(()=> result.value?.stdout || '')
const summary = computed(()=>{
  const hosts = result.value?.result?.hosts || []
  if (!hosts.length) return null
  const [h] = hosts
  return {
    host: h.address,
    ports: (h.ports || []).map(p=>({ port:p, proto:'tcp', state:'open', service: '?', version:'' }))
  }
})
const jsonOut = computed(()=> JSON.stringify(result.value?.result || {}, null, 2))
const textOut = computed(()=>{
  if(!summary.value) return ''
  return summary.value.ports.map(p=>`${p.port}/${p.proto} ${p.service}`).join('\n')
})
async function copy(txt){ await navigator.clipboard.writeText(txt); pushToast({title:'Copié',msg:'dans le presse-papiers'}) }
</script>
