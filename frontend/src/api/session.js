import axios from 'axios'

// const CSRF_COOKIE_NAME = 'csrftoken'
// const CSRF_HEADER_NAME = 'X-CSRFToken'

export const session = axios.create({
  // xsrfCookieName: CSRF_COOKIE_NAME,
  // xsrfHeaderName: CSRF_HEADER_NAME
})

export function setAuthHeader () {
  return {
    headers: {
      Authorization: `JWT ${
        localStorage.getItem(process.env.VUE_APP_ACCESS_STORAGE_KEY)
      }`
    }
  }
}
