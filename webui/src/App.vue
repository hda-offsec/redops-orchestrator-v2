<template>
  <div class="min-h-screen flex">
    <aside class="w-64 bg-redops-card border-r border-gray-800 hidden md:block">
      <div class="p-4 text-xl font-bold text-red-400">RedOps</div>
      <nav class="p-2 space-y-1">
        <RouterLink class="block px-3 py-2 rounded hover:bg-gray-800" to="/">Dashboard</RouterLink>
        <RouterLink class="block px-3 py-2 rounded hover:bg-gray-800" to="/nmap">Nmap</RouterLink>
        <RouterLink class="block px-3 py-2 rounded hover:bg-gray-800" to="/webrecon">WebRecon</RouterLink>
        <RouterLink class="block px-3 py-2 rounded hover:bg-gray-800" to="/vuln">Vuln</RouterLink>
        <RouterLink class="block px-3 py-2 rounded hover:bg-gray-800" to="/orchestrator">Orchestrator</RouterLink>
        <RouterLink class="block px-3 py-2 rounded hover:bg-gray-800" to="/settings">Settings</RouterLink>
      </nav>
    </aside>
    <main class="flex-1">
      <header class="sticky top-0 z-10 bg-redops-card/80 backdrop-blur border-b border-gray-800">
        <div class="max-w-6xl mx-auto p-3 flex items-center justify-between">
          <div class="font-semibold">RedOps Orchestrator</div>
          <div class="text-xs text-gray-400">Dark • Live • OSCP-safe</div>
        </div>
      </header>
      <section class="max-w-6xl mx-auto p-4">
        <RouterView />
      </section>
    </main>
  </div>
</template>
