import { session, setAuthHeader } from '@/api/session'

export default {
  getProductComments (productId, limit, offset) {
    return session.get(
      `${process.env.VUE_APP_BACKEND_API_URL}/comments?product_id=${productId}&limit=${limit}&offset=${offset}`,
      setAuthHeader())
  }
}
