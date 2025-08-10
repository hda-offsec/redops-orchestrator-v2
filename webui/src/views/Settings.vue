<template>
  <Card>
    <template #title>Paramètres</template>
    <form class="space-y-3" @submit.prevent="save">
      <div>
        <label class="text-sm">API Base</label>
        <input v-model="app.apiBase" class="w-full mt-1 px-3 py-2 bg-black/20 border border-redops-line rounded-lg"/>
      </div>
      <div>
        <label class="text-sm">API Token</label>
        <input v-model="app.apiToken" class="w-full mt-1 px-3 py-2 bg-black/20 border border-redops-line rounded-lg"/>
      </div>
      <label class="inline-flex items-center gap-2">
        <input type="checkbox" v-model="app.oscpSafe" />
        <span>OSCP-safe</span>
      </label>
      <Button @click="save">Sauvegarder</Button>
    </form>
  </Card>
</template>
<script setup>
import Card from '@/components/ui/Card.vue'
import Button from '@/components/ui/Button.vue'
import { app, saveApp } from '@/store/app'
import { pushToast } from '@/components/ui/Toast.vue'
function save(){ saveApp(); pushToast({title:'OK',msg:'Paramètres enregistrés'}) }
</script>
