import auth from '@/api/auth'

const getDefaultState = () => ({
  authLoading: false,
  authError: false,
  authErrors: undefined,
  tokensSet: false
})

export default {
  namespaced: true,
  state: getDefaultState(),
  getters: {
    isAuthenticated (state) {
      return state.tokensSet === true
    },
    isAuthLoading (state) {
      return state.authLoading
    }
  },
  mutations: {
    initStart (state) {
      state.authLoading = true
      state.authError = false
      state.authErrors = undefined
    },
    initEnd (state) {
      state.authLoading = false
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
    tokenAreSet (state, data) {
      state.tokensSet = true
      localStorage.setItem(process.env.VUE_APP_ACCESS_STORAGE_KEY, data.access)
    }
  },
  actions: {
    async initialize ({ commit }) {
      if (localStorage.getItem(process.env.VUE_APP_REFRESH_STORAGE_KEY)) {
        await auth.refresh({
          refresh: localStorage.getItem(process.env.VUE_APP_REFRESH_STORAGE_KEY)
        })
          .then(({ data }) => {
            commit('tokenAreSet', data)
          })
          .catch(() => {
            commit('logout')
          })
      }
    },
    async signIn ({ commit }, payload) {
      commit('initStart')
      return await auth.signIn({
        step: payload.step,
        phone: payload.phone.value,
        email: payload.email.value,
        lastName: payload.lastName.value,
        firstName: payload.firstName.value,
        otpCode: payload.otpCode.value,
        password: payload.password.value
      })
    },
    logout ({ commit }) {
      commit('logout')
    }
  }
}
