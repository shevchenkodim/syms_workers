import user from '@/api/user'

const getDefaultState = () => ({
  userLoading: false,
  userError: false,
  userErrors: undefined,
  userData: {
    email: '',
    last_name: '',
    first_name: '',
    image: ''
  }
})

export default {
  namespaced: true,
  state: getDefaultState(),
  getters: {
    getUserData (state) {
      return state.userData
    }
  },
  mutations: {
    getUserDetailInitStart (state) {
      state.userLoading = true
      state.userError = false
      state.userErrors = undefined
    },
    getUserDetailInitEnd (state) {
      state.userLoading = false
      state.userError = false
    },
    setUserDetail (state, data) {
      state.userData = data
    }
  },
  actions: {
    async loadUserDetail ({ commit }) {
      commit('getUserDetailInitStart')
      await user.getUserDetail()
        .then(({ data }) => {
          commit('setUserDetail', data)
        })
        .catch(() => {})
        .finally(() => {
          commit('getUserDetailInitEnd')
        })
    }
  }
}
