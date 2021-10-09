import common from '@/api/common'

const getDefaultCategoryState = () => ({
  isCategoryLoading: false,
  CategoryError: false,
  CategoryErrors: undefined,
  categoryData: {},
  categoryProducts: []
})

export default {
  namespaced: true,
  state: getDefaultCategoryState(),
  getters: {
    isCategoryLoading (state) {
      return state.isCategoryLoading
    },
    getCategoryData (state) {
      return state.categoryData
    },
    getCategoryProducts (state) {
      return state.categoryProducts
    },
    getCategoryProductsPaginator (state) {
      return state.categoryProductsPaginator
    },
    getBackendUrl (state) {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  mutations: {
    initStart (state) {
      state.isCategoryLoading = true
      state.CategoryError = false
      state.CategoryErrors = undefined
    },
    initEnd (state) {
      state.isCategoryLoading = false
      state.CategoryError = false
      state.CategoryErrors = undefined
    },
    setCategoryData (state, data) {
      state.categoryData = data
    },
    setCategoryProducts (state, data) {
      state.categoryProducts = data
    }
  },
  actions: {
    async loadCategoryData ({ commit }, code) {
      commit('initStart')
      await common.getCategoryByCode(code)
        .then(({ data }) => {
          commit('setCategoryData', data)
        })
        .catch(() => {
          this.$router.push({ name: 'Home' })
        })
        .finally(() => {
          commit('initEnd')
        })
    },
    async loadCategoryProducts ({ commit, state }, data) {
      commit('initStart')
      return await common.getCategoryProducts(
        state.categoryData.id,
        data.limit,
        data.current * data.limit - data.limit,
        data.priceFrom,
        data.priceTo,
        data.brand,
        data.ordering
      )
    }
  }
}
