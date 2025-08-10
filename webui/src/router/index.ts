import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/pages/Dashboard.vue'
import Nmap from '@/pages/Nmap.vue'
import WebRecon from '@/pages/WebRecon.vue'
import Vuln from '@/pages/Vuln.vue'
import Settings from '@/pages/Settings.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/nmap', name: 'nmap', component: Nmap },
    { path: '/webrecon', name: 'webrecon', component: WebRecon },
    { path: '/vuln', name: 'vuln', component: Vuln },
    { path: '/settings', name: 'settings', component: Settings },
  ]
})
