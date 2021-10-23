import common from '@/api/common'
import comment from '@/api/comment'

const getDefaultProductState = () => ({
  isProductLoading: false,
  ProductError: false,
  ProductErrors: undefined,
  productData: {},
  sellerData: { code_name: null }
})

export default {
  namespaced: true,
  state: getDefaultProductState(),
  getters: {
    isProductLoading (state) {
      return state.isProductLoading
    },
    getProductData (state) {
      return state.productData
    },
    getSellerData (state) {
      return state.sellerData
    },
    getBackendUrl (state) {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  mutations: {
    initStart (state) {
      state.isProductLoading = true
      state.ProductError = false
      state.ProductErrors = undefined
    },
    initEnd (state) {
      state.isProductLoading = false
      state.ProductError = false
      state.ProductErrors = undefined
    },
    setProductData (state, data) {
      state.productData = data
    },
    setSellerData (state, data) {
      state.sellerData = data
    },
    setIsExistsCartItem (state, value) {
      state.productData.exists_in_cart = value
    }
  },
  actions: {
    async loadProductData ({ commit, dispatch }, code) {
      commit('initStart')
      await common.getProductByCode(code)
        .then(({ data }) => {
          commit('setProductData', data)
          dispatch('loadSellerData')
        })
        .catch(() => {
          this.$router.push({ name: 'Home' })
        })
        .finally(() => {
          commit('initEnd')
        })
    },
    async loadSellerData ({ commit, state }) {
      commit('initStart')
      await common.getSellerByCode(state.productData.seller_code)
        .then(({ data }) => {
          commit('setSellerData', data)
        })
        .catch(() => {
          this.$router.push({ name: 'Home' })
        })
        .finally(() => {
          commit('initEnd')
        })
    },
    async loadProductComments ({ commit, state }, data) {
      return await comment.getProductComments(data.productId, data.limit, data.current * data.limit - data.limit)
    }
  }
}
