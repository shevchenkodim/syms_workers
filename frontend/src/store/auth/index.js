import auth from '@/api/auth'

const getDefaultState = () => ({
  authLoading: false,
  authError: false,
  authErrors: undefined,
  customerLoading: false,
  customerError: false,
  customerErrors: undefined,
  userData: undefined,
  tokensSet: false
})

export default {
  namespaced: true,
  state: getDefaultState(),
  getters: {
    isAuthenticated (state) {
      return state.tokensSet === true
    }
  },
  mutations: {
    initStart (state) {
      state.authLoading = true
      state.authError = false
      state.authErrors = undefined
    },
    initSuccess (state, { access, refresh }) {
      state.tokensSet = true
      state.authLoading = false
      state.authError = false
      localStorage.setItem(process.env.VUE_APP_ACCESS_STORAGE_KEY, access)
      localStorage.setItem(process.env.VUE_APP_REFRESH_STORAGE_KEY, refresh)
    },
    setCustomerData (state, data) {
      state.userData = data
    },
    logout (state) {
      localStorage.removeItem(process.env.VUE_APP_REFRESH_STORAGE_KEY)
      localStorage.removeItem(process.env.VUE_APP_ACCESS_STORAGE_KEY)
      Object.assign(state, getDefaultState())
    },
    authenticationError (state, { detail = undefined }) {
      state.tokensSet = false
      state.authLoading = false
      state.authError = true
      if (typeof detail === 'object' && detail !== null) {
        state.authErrors = detail[Object.keys(detail)][0]
      } else {
        state.authErrors = detail
      }
    },
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
    },
    tokenAreSet (state, data) {
      state.tokensSet = true
      localStorage.setItem(process.env.VUE_APP_ACCESS_STORAGE_KEY, data.access)
    }
  },
  actions: {
    async initialize ({ commit }) {
      if (
        localStorage.getItem(process.env.VUE_APP_REFRESH_STORAGE_KEY) !== null
      ) {
        await auth.refresh({
          refresh: localStorage.getItem(process.env.VUE_APP_REFRESH_STORAGE_KEY)
        })
          .then(({ data }) => {
            commit('tokenAreSet', data)
          })
      }
    },
    async login ({ commit }, { username, password }) {
      commit('initStart')
      await auth.login({ username, password })
        .then(({ data }) => {
          commit('', data)
        })
        .catch(({ response }) => {
          commit('authenticationError', { detail: response.data.detail })
        })
    },
    async signIn ({ commit }, payload) {
      commit('initSuccess')
      await auth.signIn({
        email: payload.email,
        last_name: payload.lastName,
        password: payload.password,
        username: payload.username,
        first_name: payload.firstName
      })
        .then(({ data }) => {
          commit('initSuccess', data)
          commit('setCustomerData', data)
        })
        .catch(({ response }) => {
          commit('authenticationError', { detail: response.data.detail })
        })
    },
    logout ({ commit }) {
      commit('logout')
    }
  }
}
