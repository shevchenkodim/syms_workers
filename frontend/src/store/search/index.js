import search from '@/api/search'

const getDefaultSearchState = () => ({
  isSearchLoading: false,
  SearchError: false,
  SearchErrors: undefined,
  searchProducts: []
})

export default {
  namespaced: true,
  state: getDefaultSearchState(),
  getters: {
    isSearchLoading (state) {
      return state.isSearchLoading
    },
    getSearchProducts (state) {
      return state.searchProducts
    },
    getBackendUrl (state) {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  mutations: {
    initStart (state) {
      state.isSearchLoading = true
      state.SearchError = false
      state.SearchErrors = undefined
    },
    initEnd (state) {
      state.isSearchLoading = false
      state.SearchError = false
      state.SearchErrors = undefined
    },
    setSearchProducts (state, data) {
      state.searchProducts = data
    }
  },
  actions: {
    async loadSearchProducts ({ commit, state }, data) {
      commit('initStart')
      return await search.getSearchProducts(data.searchValue, data.limit, data.current * data.limit - data.limit)
    }
  }
}
