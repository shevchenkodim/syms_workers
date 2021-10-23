import { session, setAuthHeader } from '@/api/session'

export default {
  getSearchProducts (searchValue, limit, offset) {
    return session.get(
      `${process.env.VUE_APP_BACKEND_API_URL}/search?value=${searchValue}&limit=${limit}&offset=${offset}`,
      setAuthHeader())
  }
}
