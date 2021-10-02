import Vue from 'vue'
import Vuex from 'vuex'
import auth from '@/store/auth'
import user from '@/store/user'
import home from '@/store/home'
import common from '@/store/common'
import createLogger from 'vuex/dist/logger'

const debug = process.env.NODE_ENV !== 'production'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
    user,
    home,
    common
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
