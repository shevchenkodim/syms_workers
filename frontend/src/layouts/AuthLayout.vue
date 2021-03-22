<template>
  <div class="bg-color-auth d-flex align-center justify-center">
    <v-container>
      <router-view />
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'AuthLayout'
}
</script>

<style scoped>
  .bg-color-auth {
    background-color: #343a40!important;
    position: relative;
    min-height: 100vh;
  }
</style>
