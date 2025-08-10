<template>
  <Toast/>
  <AppShell><router-view /></AppShell>
</template>
<script setup>
import AppShell from '@/layouts/AppShell.vue'
import Toast from '@/components/ui/Toast.vue'
</script>
