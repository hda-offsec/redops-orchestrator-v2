<script setup>
import { ref } from 'vue'
import ScanForm from '../components/ScanForm.vue'
import JobStatus from '../components/JobStatus.vue'
const jobId = ref('')
function onCreated(id){ jobId.value = id }
</script>

<template>
  <h1 class="text-2xl font-bold mb-4">Nmap</h1>
  <ScanForm module="nmap" @created="onCreated"/>
  <JobStatus v-if="jobId" module="nmap" :job-id="jobId"/>
</template>
