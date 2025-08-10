<template>
  <RouterLink :to="to"
    class="rounded-xl border border-zinc-800 bg-zinc-900/50 p-4 hover:border-brand-700 hover:bg-zinc-900 transition flex items-start gap-3">
    <component :is="icon" class="w-6 h-6 text-brand-400 mt-1" />
    <div><div class="font-semibold text-zinc-100">{{ title }}</div>
      <div class="text-sm text-zinc-400 mt-1">{{ subtitle }}</div></div>
  </RouterLink>
</template>
<script setup lang="ts">
defineProps<{ title:string; subtitle?:string; icon:any; to:string }>()
</script>
