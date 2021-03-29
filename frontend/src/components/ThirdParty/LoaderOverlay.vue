<template>
  <v-overlay v-if="isLoading">
    <Loader :isLoading="isLoading"></Loader>
  </v-overlay>
</template>

<script>
import Loader from '@/components/ThirdParty/Loader'

export default {
  name: 'LoaderOverlay',
  components: { Loader },
  props: ['isLoading']
}
</script>

<style scoped>

</style>
