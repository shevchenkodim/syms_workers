import { session } from '@/api/session'

export default {
  verify (payload) {
    return session.post(`${process.env.VUE_APP_BACKEND_URL}/api/v1/auth/verify`, payload)
  },
  signIn (payload) {
    return session.post(`${process.env.VUE_APP_BACKEND_URL}/api/v1/auth/login`, payload)
  },
  refresh (payload) {
    return session.post(`${process.env.VUE_APP_BACKEND_URL}/api/v1/auth/refresh`, payload)
  }
}
