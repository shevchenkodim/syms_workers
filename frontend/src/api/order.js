import { session, setAuthHeader } from '@/api/session'

export default {
  createOrder () {
    return session.post(`${process.env.VUE_APP_BACKEND_API_URL}/orders/`, {}, setAuthHeader())
  },
  loadHistoryOrder () {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/orders/`, setAuthHeader())
  }
}
