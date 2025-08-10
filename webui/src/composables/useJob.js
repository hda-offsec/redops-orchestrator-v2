import { ref } from 'vue'
import api from '@/api'
import { pushToast } from '@/components/ui/Toast.vue'

export function useJob(module){
  const jobId = ref('')
  const status = ref('idle')
  const result = ref(null)
  const error = ref(null)

  async function start(payload){
    const { data } = await api.post(`/api/v1/${module}/scans`, payload)
    jobId.value = data.job_id
    status.value = 'queued'
    pushToast({title:'Scan créé', msg:`Job ${jobId.value}`})
    poll()
  }
  async function poll(){
    let delay=1000
    while(true){
      const { data } = await api.get(`/api/v1/${module}/scans/${jobId.value}`)
      status.value = data.status
      if (data.result) result.value = data.result
      if (status.value==='finished'){ pushToast({title:'Terminé',msg:`${module} ok`}); break }
      if (status.value==='failed'){ error.value=data.error||'failed'; pushToast({title:'Échec',msg:error.value}); break }
      await new Promise(r=>setTimeout(r, delay)); delay=Math.min(delay*1.5, 2000)
    }
  }
  return { jobId, status, result, error, start }
}
