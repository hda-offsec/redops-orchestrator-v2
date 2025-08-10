<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import API from '../api'

const props = defineProps({ module: String, jobId: String })
const status = ref('pending')
const result = ref(null)
let t = null

async function poll() {
  const { data } = await API.get(`/${props.module}/scans/${props.jobId}`)
  status.value = data.status
  if (data.result) result.value = data.result
  if (data.status === 'finished' || data.status === 'failed') clearInterval(t)
}

onMounted(() => { t = setInterval(poll, 1500); poll() })
onUnmounted(() => t && clearInterval(t))
</script>

<template>
  <div class="bg-redops-card p-4 rounded-xl border border-gray-800 mt-3">
    <div class="text-sm">Job [[ jobId ]] – <span :class="status==='finished'?'text-green-400':status==='failed'?'text-red-400':'text-yellow-400'">[[ status ]]</span></div>
    <pre v-if="result?.stdout" class="mt-3 p-3 bg-black/40 rounded overflow-auto text-xs">[[ result.stdout ]]</pre>
    <pre v-if="result?.stderr" class="mt-3 p-3 bg-black/40 rounded overflow-auto text-xs text-red-300">[[ result.stderr ]]</pre>
  </div>
</template>
