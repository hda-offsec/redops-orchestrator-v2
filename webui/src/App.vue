<template><RouterView /></template>
<script setup lang="ts">
if (!document.documentElement.classList.contains('dark')) {
  document.documentElement.classList.add('dark')
}
</script>
