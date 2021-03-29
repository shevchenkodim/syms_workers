<template>
  <square
    color="#FFFFFF"
    v-if="isLoading"
    v-bind:loading=isLoading
  ></square>
</template>

<script>
export default {
  name: 'Loader',
  props: ['isLoading']
}
</script>

<style scoped>

</style>
