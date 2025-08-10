<template>
  <button
    class="inline-flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium
           bg-neutral-100 text-black hover:bg-white/90 active:translate-y-[1px]"
    :class="variant==='danger' && 'bg-redops-accent text-white hover:opacity-90'"
    v-bind="$attrs"><slot /></button>
</template>
<script setup>
defineProps({ variant:{type:String,default:'default'} })
</script>
