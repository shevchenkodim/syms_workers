import { session, setAuthHeader } from '@/api/session'

export default {
  getUserDetail (id = 'self') {
    return session.get(`${process.env.VUE_APP_BACKEND_API_URL}/users/${id}`, setAuthHeader())
  },
  saveUserDetail (data, id = 'self') {
    var config = setAuthHeader()
    config.headers['Content-Type'] = 'multipart/form-data;'
    return session.put(`${process.env.VUE_APP_BACKEND_API_URL}/users/${id}/`, data, config)
  }
}
