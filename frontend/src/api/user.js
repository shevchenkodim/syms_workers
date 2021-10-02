import { session, setAuthHeader } from '@/api/session'

export default {
  getUserDetail (id = 'self') {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/users/${id}`, setAuthHeader())
  }
}
