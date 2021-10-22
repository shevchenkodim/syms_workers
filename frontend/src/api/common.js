import { session, setAuthHeader } from '@/api/session'

export default {
  getAllCategories () {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/categories/`, setAuthHeader())
  },
  getCategoryByCode (code = '') {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/categories/${code}`, setAuthHeader())
  },
  getCategoryProducts (category, limit, offset, priceFrom = '', priceTo = '', brand = '', ordering = '') {
    return session.get(
      `${process.env.VUE_APP_BACKEND_API_URL}/products?${category ? `category_id=${category}&` : ''}limit=${limit}
      &offset=${offset}&price_from=${priceFrom}&price_to=${priceTo}&brand=${brand}&ordering=${ordering}`,
      setAuthHeader())
  },
  getProductByCode (code = '') {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/products/${code}`, setAuthHeader())
  },
  getSellerByCode (code = '') {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/sellers/${code}`, setAuthHeader())
  },
  getCartDetail () {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/carts/`, setAuthHeader())
  },
  addCartItem (data) {
    return session.post(`${process.env.VUE_APP_BACKEND_API_URL}/carts/`, data, setAuthHeader())
  }
}
