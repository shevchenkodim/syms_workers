import home from '@/api/home'

const getDefaultHomeState = () => ({
  homeLoading: false,
  homeError: false,
  homeErrors: undefined,
  homeMainSlider: []
})

export default {
  namespaced: true,
  state: getDefaultHomeState(),
  getters: {
    isHomeLoading (state) {
      return state.homeLoading
    },
    getMainSliderImages (state) {
      return state.homeMainSlider
    },
    getBackendUrl (state) {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  mutations: {
    initStart (state) {
      state.homeLoading = true
      state.homeError = false
      state.homeErrors = undefined
    },
    initEnd (state) {
      state.homeLoading = false
      state.homeError = false
      state.homehErrors = undefined
    },
    setMainSliderImages (state, data) {
      state.homeMainSlider = data
    }
  },
  actions: {
    async loadMainSliderImages ({ commit }) {
      await home.getMainSliderImages()
        .then(({ data }) => {
          commit('setMainSliderImages', data)
        })
        .catch(() => {})
        .finally(() => {
          commit('initEnd')
        })
    }
  }
}
