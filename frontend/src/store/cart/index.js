import common from '@/api/common'

const getDefaultCartState = () => ({
  isCartLoading: false,
  cartError: false,
  cartErrors: undefined,
  cartCount: 0,
  cartItems: []
})

export default {
  namespaced: true,
  state: getDefaultCartState(),
  getters: {
    isCartLoading (state) {
      return state.isCartLoading
    },
    getCartCount (state) {
      return state.cartCount
    },
    getCartItems (state) {
      return state.cartItems
    }
  },
  mutations: {
    initStart (state) {
      state.isCartLoading = true
      state.cartError = false
      state.cartErrors = undefined
    },
    initEnd (state) {
      state.isCartLoading = false
      state.cartError = false
      state.cartErrors = undefined
    },
    setCartCount (state, data) {
      state.cartCount = data
    },
    setCartItems (state, data) {
      state.cartItems = data
    }
  },
  actions: {
    async loadCartItems ({ commit }) {
      commit('initStart')
      await common.getCartDetail()
        .then(({ data }) => {
          commit('setCartCount', data.count)
          commit('setCartItems', data.items)
        })
        .catch(() => {
          this.$router.push({ name: 'Home' })
        })
        .finally(() => {
          commit('initEnd')
        })
    },
    async loadCartItemsPromise ({ commit }) {
      return await common.getCartDetail()
    }
  }
}
