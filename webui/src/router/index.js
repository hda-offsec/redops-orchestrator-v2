import { createRouter, createWebHashHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import Nmap from '@/views/Nmap.vue'
import WebRecon from '@/views/WebRecon.vue'
import Vuln from '@/views/Vuln.vue'
import Orchestrator from '@/views/Orchestrator.vue'
import Settings from '@/views/Settings.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', component: Dashboard },
    { path: '/nmap', component: Nmap },
    { path: '/webrecon', component: WebRecon },
    { path: '/vuln', component: Vuln },
    { path: '/orchestrator', component: Orchestrator },
    { path: '/settings', component: Settings },
  ]
})
