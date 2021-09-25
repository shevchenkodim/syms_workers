<template>
  <v-carousel v-bind:height="height">
    <v-carousel-item
      v-for="(item, i) in itemsImages"
      :key="i"
      :src="media_url + item.item_image"
      reverse-transition="fade-transition"
      transition="fade-transition"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: 'Carousel',
  props: ['itemsImages', 'height', 'media_url']
}
</script>

<style scoped>

</style>
