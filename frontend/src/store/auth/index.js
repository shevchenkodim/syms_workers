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
      if (localStorage.getItem(process.env.VUE_APP_REFRESH_STORAGE_KEY) !== null) {
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
          commit('initSuccess', data)
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
