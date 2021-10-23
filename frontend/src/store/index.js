import Vue from 'vue'
import Vuex from 'vuex'
import auth from '@/store/auth'
import user from '@/store/user'
import home from '@/store/home'
import cart from '@/store/cart'
import search from '@/store/search'
import common from '@/store/common'
import product from '@/store/product'
import category from '@/store/category'
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
    cart,
    search,
    common,
    category,
    product
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
