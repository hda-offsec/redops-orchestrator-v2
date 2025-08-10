<template>
  <router-link :to="to" class="flex items-center gap-2 px-3 py-2 rounded-md text-sm
     hover:bg-white/5" active-class="bg-white/10">
     <slot />
  </router-link>
</template>
<script setup>
defineProps({ to:{type:[String,Object], required:true} })
</script>
