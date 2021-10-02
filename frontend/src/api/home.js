import { session, setAuthHeader } from '@/api/session'

export default {
  getMainSliderImages () {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/slider/main/images/`, setAuthHeader())
  },
  getNoveltyProducts () {
    setAuthHeader()
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/novelties/`, setAuthHeader())
  }
}
