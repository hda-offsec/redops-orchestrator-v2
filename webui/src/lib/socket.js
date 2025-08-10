import { io } from 'socket.io-client'

// Backend Socket.IO (optionnel). Si pas dispo, on ne crash pas.
export function makeSocket(url) {
  try {
    const s = io(url, { transports: ['websocket'], autoConnect: true })
    return s
  } catch {
    return null
  }
}
