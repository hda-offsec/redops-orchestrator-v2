<script setup>
import { ref } from 'vue'
import ScanForm from '../components/ScanForm.vue'
import JobStatus from '../components/JobStatus.vue'
const jobId = ref('')
</script>
<template>
  <h1 class="text-2xl font-bold mb-4">Vuln</h1>
  <ScanForm module="vuln" @created="id => jobId=id"/>
  <JobStatus v-if="jobId" module="vuln" :job-id="jobId"/>
</template>
