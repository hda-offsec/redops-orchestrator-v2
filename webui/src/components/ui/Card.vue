<template>
  <section class="bg-redops-card rounded-xl border border-redops-line shadow-card">
    <header v-if="$slots.title" class="px-4 pt-4 text-sm font-semibold text-gray-300">
      <slot name="title" />
    </header>
    <div class="p-4">
      <slot />
    </div>
  </section>
</template>
