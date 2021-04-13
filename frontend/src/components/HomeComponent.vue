<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        Test block
      </v-col>
      <v-col cols="8">
        <Carousel :itemsImages="itemsImages" :height="350" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Carousel from '@/components/ThirdParty/Carousel'
export default {
  name: 'HomeComponent',
  components: { Carousel },
  data: () => ({
    itemsImages: [
      {
        src: 'https://content1.rozetka.com.ua/banner_main/image/original/170837155.jpg'
      },
      {
        src: 'https://content1.rozetka.com.ua/banner_main/image/original/171744989.jpg'
      },
      {
        src: 'https://content.rozetka.com.ua/banner_main/image/original/171736584.jpg'
      },
      {
        src: 'https://content1.rozetka.com.ua/banner_main/image/original/170593288.jpg'
      }
    ]
  })
}
</script>

<style scoped>

</style>
