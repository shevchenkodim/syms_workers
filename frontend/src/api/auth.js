import { session } from '@/api/session'

export default {
  verify (payload) {
    return session.post(`${process.env.VUE_APP_BACKEND_API_URL}/auth/verify`, payload)
  },
  signIn (payload) {
    return session.post(`${process.env.VUE_APP_BACKEND_API_URL}/auth/login`, payload)
  },
  refresh (payload) {
    return session.post(`${process.env.VUE_APP_BACKEND_API_URL}/auth/refresh`, payload)
  }
}
