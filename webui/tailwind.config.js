/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        redops: {
          bg: '#0b0f14',
          card: '#121821',
          accent: '#ff4444',
          ok: '#00ff99',
          warn: '#ffcc00'
        }
      }
    }
  },
  plugins: [require('@tailwindcss/forms')]
}
