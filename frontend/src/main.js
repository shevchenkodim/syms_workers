import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSpinners from 'vue-spinners'
import VueMask from 'v-mask'
import VueToastr from '@deveodk/vue-toastr'
import '@deveodk/vue-toastr/dist/@deveodk/vue-toastr.css'

Vue.use(VueMask)
Vue.use(VueSpinners)
Vue.use(VueAxios, axios)
Vue.use(VueToastr, {
  defaultPosition: 'toast-top-right',
  defaultTimeout: 3000
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
