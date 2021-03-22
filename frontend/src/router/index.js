import Vue from 'vue'
import store from '@/store'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const requireAuthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/login')
      } else {
        next()
      }
    })
}

const requireUnauthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (store.getters['auth/isAuthenticated']) {
        next({ name: 'Home' })
      } else {
        next()
      }
    })
}

const routes = [
  {
    path: '/',
    name: 'Main',
    meta: { layout: 'main' },
    component: () => import('../views/Main.vue'),
    beforeEnter: requireAuthenticated
  },
  {
    path: '/login',
    name: 'Login',
    meta: { layout: 'auth' },
    component: () => import('../views/Auth.vue'),
    beforeEnter: requireUnauthenticated
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
