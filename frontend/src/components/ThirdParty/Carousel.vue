<template>
  <v-carousel v-bind:height="height">
    <v-carousel-item
      v-for="(item,i) in itemsImages"
      :key="i"
      :src="item.src"
      reverse-transition="fade-transition"
      transition="fade-transition"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: 'Carousel',
  props: ['itemsImages', 'height']
}
</script>

<style scoped>

</style>
