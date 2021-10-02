import axios from 'axios'

export const session = axios.create({})

export function setAuthHeader () {
  return {
    headers: {
      Authorization: `Bearer ${
        localStorage.getItem(process.env.VUE_APP_ACCESS_STORAGE_KEY)
      }`
    }
  }
}
