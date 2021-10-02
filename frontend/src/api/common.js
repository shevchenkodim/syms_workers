import { session, setAuthHeader } from '@/api/session'

export default {
  getAllCategories () {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/categories/`, setAuthHeader())
  }
}
