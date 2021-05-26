import { session } from '@/api/session'

export default {
  getMainSliderImages () {
    return session.get(`${process.env.VUE_APP_BACKEND_URL}/slider/main/images`)
  },
}
