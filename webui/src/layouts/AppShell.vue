<template>
  <div class="flex min-h-screen">
    <aside class="w-60 bg-[#0e141b] border-r border-redops-line">
      <div class="px-4 py-3 font-bold text-lg">RedOps</div>
      <nav class="px-2 space-y-1">
        <SidebarItem to="/">Dashboard</SidebarItem>
        <SidebarItem to="/nmap">Nmap</SidebarItem>
        <SidebarItem to="/webrecon">WebRecon</SidebarItem>
        <SidebarItem to="/vuln">Vuln</SidebarItem>
        <SidebarItem to="/orchestrator">Orchestrator</SidebarItem>
        <SidebarItem to="/settings">Settings</SidebarItem>
      </nav>
    </aside>
    <div class="flex-1">
      <TopBar />
      <main class="p-6"><slot /></main>
    </div>
  </div>
</template>
<script setup>
import SidebarItem from '@/components/SidebarItem.vue'
import TopBar from '@/components/TopBar.vue'
</script>
