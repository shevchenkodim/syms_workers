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
    name: 'Home',
    meta: { layout: 'main' },
    component: () => import('../views/Home.vue'),
    beforeEnter: requireAuthenticated
  },
  {
    props: true,
    path: '/category/:category_code',
    name: 'Category',
    meta: { layout: 'main' },
    component: () => import('../views/Category.vue'),
    beforeEnter: requireAuthenticated
  },
  {
    props: true,
    path: '/product/:product_code',
    name: 'Product',
    meta: { layout: 'main' },
    component: () => import('../views/Product.vue'),
    beforeEnter: requireAuthenticated
  },
  {
    path: '/login',
    name: 'Login',
    meta: { layout: 'auth' },
    component: () => import('../views/Auth.vue'),
    beforeEnter: requireUnauthenticated
  },
  {
    path: '/*',
    name: 'Page404',
    meta: { layout: 'main' },
    component: () => import('../views/Page404.vue'),
    beforeEnter: requireUnauthenticated
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
