<template>
  <div class="grid md:grid-cols-3 gap-4">
    <Card><template #title>[[ m.title ]]</template>[[ m.desc ]]</Card>
    <Card><template #title>[[ m.title ]]</template>[[ m.desc ]]</Card>
    <Card><template #title>[[ m.title ]]</template>[[ m.desc ]]</Card>
  </div>
</template>
<script setup>
import Card from '@/components/ui/Card.vue'
</script>
