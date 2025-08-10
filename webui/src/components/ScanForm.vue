<script setup>
import { ref, onMounted } from 'vue'
import API from '../api'

const props = defineProps({ module: { type: String, required: true } })
const target = ref('')
const profile = ref('')
const profiles = ref([])
const busy = ref(false)
const emit = defineEmits(['created'])

onMounted(async () => {
  const { data } = await API.get(`/${props.module}/profiles`)
  profiles.value = data
  profile.value = data[0] || 'normal'
})

async function submit() {
  busy.value = true
  try {
    const { data } = await API.post(`/${props.module}/scans`, { target: target.value, profile: profile.value })
    emit('created', data.job_id)
  } finally { busy.value = false }
}
</script>

<template>
  <div class="bg-redops-card p-4 rounded-xl border border-gray-800">
    <div class="grid md:grid-cols-3 gap-3">
      <input v-model="target" type="text" placeholder="Cible (ex: scanme.nmap.org)" class="bg-black/40 border-gray-700 rounded"/>
      <select v-model="profile" class="bg-black/40 border-gray-700 rounded">
        <option v-for="p in profiles" :key="p" :value="p">[[ p ]]</option>
      </select>
      <button :disabled="busy || !target" @click="submit"
        class="bg-redops-accent/20 hover:bg-red-600/30 border border-red-600 rounded px-4">
        Lancer
      </button>
    </div>
  </div>
</template>
