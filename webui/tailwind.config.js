export default {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {
      colors: {
        'redops-bg': '#0b0f14',
        'redops-card': '#121821',
        'redops-line': '#1e293b',
        'redops-accent': '#f43f5e',
        'redops-ok': '#22c55e',
        'redops-warn': '#f59e0b',
        'redops-bad': '#ef4444',
      },
      boxShadow: {
        card: '0 1px 0 0 rgba(255,255,255,0.04) inset, 0 10px 30px rgba(0,0,0,.35)'
      }
    }
  },
  plugins: []
}
