import { ref } from 'vue'
export type Toast = { id: number; title: string; kind?: 'success'|'error'|'info'; ms?: number }
const toasts = ref<Toast[]>([])
let id = 1
export function useToasts() {
  const push = (t: Omit<Toast,'id'>) => {
    const toast = { id: id++, kind: 'info', ms: 4000, ...t }
    toasts.value.push(toast); setTimeout(()=>dismiss(toast.id), toast.ms)
  }
  const dismiss = (tid:number) => { const i = toasts.value.findIndex(t=>t.id===tid); if(i>=0) toasts.value.splice(i,1) }
  return { toasts, push, dismiss }
}
