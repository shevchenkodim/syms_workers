import home from '@/api/home'

const getDefaultHomeState = () => ({
  homeLoading: false,
  homeError: false,
  homeErrors: undefined,
  homeMainSlider: [],
  homeNoveltyProducts: []
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
    getNoveltyProducts (state) {
      return state.homeNoveltyProducts
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
    },
    setNoveltyProducts (state, data) {
      state.homeNoveltyProducts = data
    }
  },
  actions: {
    async loadMainSliderImages ({ commit }) {
      commit('initStart')
      await home.getMainSliderImages()
        .then(({ data }) => {
          commit('setMainSliderImages', data)
        })
        .catch(() => {})
        .finally(() => {
          commit('initEnd')
        })
    },
    async loadNoveltyProducts ({ commit }) {
      commit('initStart')
      await home.getNoveltyProducts()
        .then(({ data }) => {
          commit('setNoveltyProducts', data)
        })
        .catch(() => {})
        .finally(() => {
          commit('initEnd')
        })
    }
  }
}
