<template>
  <div class="fixed bottom-4 right-4 space-y-2 z-50">
    <div v-for="t in toasts" :key="t.id"
      class="bg-redops-card border border-redops-line rounded-lg px-3 py-2 shadow-card">
      <div class="text-sm font-semibold">{{ t.title }}</div>
      <div class="text-xs opacity-80">{{ t.msg }}</div>
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue'
export const toasts = ref([])
export function pushToast(t){
  const id = crypto.randomUUID()
  toasts.value.push({ id, ...t }); setTimeout(()=>removeToast(id), t.timeout||4000)
}
function removeToast(id){ toasts.value = toasts.value.filter(x=>x.id!==id) }
export default { setup(){ onMounted(()=>{}) } }
</script>
