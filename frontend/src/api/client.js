import { session } from '@/api/session'

export default {
  test (payload) {
    return session.post('api/v1/auth/test', payload)
  }
}
