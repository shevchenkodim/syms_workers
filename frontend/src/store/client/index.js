// import auth from '@/api/auth'

const getDefaultState = () => ({
  clientLoading: false,
  clientError: false,
  clientErrors: undefined,
  clientData: undefined
})

export default {
  namespaced: true,
  state: getDefaultState(),
  getters: {
  },
  mutations: {
    getCustomerInfoStart (state) {
      state.customerLoading = true
      state.customerError = false
      state.customerErrors = undefined
    },
    getCustomerInfoError (state, { detail = undefined }) {
      state.customerLoading = false
      state.customerError = true
      state.authErrors = detail
    },
    getCustomerSuccess (state) {
      state.customerLoading = false
      state.customerError = false
    }
  },
  actions: {
  }
}
