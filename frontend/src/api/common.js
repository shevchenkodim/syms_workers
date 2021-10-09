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
  }
}
