<template>
  <span class="inline-flex items-center px-2 py-0.5 rounded-md text-xs font-semibold"
        :class="classes"><slot/></span>
</template>
<script setup>
const props = defineProps({ tone:{type:String,default:'neutral'} })
const map={
  neutral:'bg-slate-700/60 text-slate-200',
  ok:'bg-green-500/20 text-green-300',
  warn:'bg-yellow-500/20 text-yellow-300',
  bad:'bg-red-500/20 text-red-300',
  info:'bg-sky-500/20 text-sky-300'
}
const classes = map[props.tone] || map.neutral
</script>
