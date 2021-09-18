import Vue from 'vue'
import Vuex from 'vuex'
import auth from '@/store/auth'
import home from '@/store/home'
import createLogger from 'vuex/dist/logger'

const debug = process.env.NODE_ENV !== 'production'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
    home
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
