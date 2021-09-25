import common from '@/api/common'

const getDefaultCommonState = () => ({
  commonLoading: false,
  commonError: false,
  commonErrors: undefined,
  categories: []
})

export default {
  namespaced: true,
  state: getDefaultCommonState(),
  getters: {
    isCommonLoading (state) {
      return state.commonLoading
    },
    getAllCategories (state) {
      return state.categories
    }
  },
  mutations: {
    initStart (state) {
      state.commonLoading = true
      state.commonError = false
      state.commonErrors = undefined
    },
    initEnd (state) {
      state.commonLoading = false
      state.commonError = false
      state.commonErrors = undefined
    },
    setCategories (state, data) {
      state.categories = data
    }
  },
  actions: {
    async loadCategories ({ commit }) {
      await common.getAllCategories()
        .then(({ data }) => {
          commit('setCategories', data)
        })
        .catch(() => {})
        .finally(() => {
          commit('initEnd')
        })
    }
  }
}
