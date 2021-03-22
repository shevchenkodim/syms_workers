import { session } from '@/api/session'

export default {
  login (payload) {
    return session.post('api/v1/auth/login', payload)
  },
  verify (payload) {
    return session.post('api/v1/auth/verify', payload)
  },
  signIn (payload) {
    return session.post('api/v1/auth/sign-in/', payload)
  },
  refresh (payload) {
    return session.post('api/v1/auth/', payload)
  }
}
