<template>
  <v-app>
    <component :is="layout">
      <router-view />
    </component>
  </v-app>
</template>

<script>
import AuthLayout from '@/layouts/AuthLayout'
import MainLayout from '@/layouts/MainLayout'
export default {
  name: 'App',
  computed: {
    layout () {
      return (this.$route.meta.layout || 'auth') + '-layout'
    }
  },
  components: {
    AuthLayout,
    MainLayout
  }
}
</script>

<style>
</style>
