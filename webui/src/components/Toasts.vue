<template>
  <div class="fixed right-4 bottom-4 space-y-2 z-50">
    <div v-for="t in toasts" :key="t.id" class="px-4 py-3 rounded-lg shadow border flex items-center gap-2"
         :class="cls(t.kind)">
      <span class="font-medium">{{ t.title }}</span>
      <button class="ml-2 text-sm opacity-70 hover:opacity-100" @click="dismiss(t.id)">×</button>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useToasts } from '@/composables/useToasts'
const { toasts, dismiss } = useToasts()
const cls = (k?:string)=>({
  'bg-emerald-900/40 text-emerald-200 border-emerald-800': k==='success',
  'bg-rose-900/40 text-rose-200 border-rose-800': k==='error',
  'bg-zinc-900/60 text-zinc-100 border-zinc-800': !k || k==='info',
})
</script>
