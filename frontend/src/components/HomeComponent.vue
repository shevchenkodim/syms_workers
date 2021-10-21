<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <Carousel :itemsImages="getMainSliderImages" :height="350" :media_url="getBackendUrl" />
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <h3>Новинки</h3>
      </v-col>
      <v-col
        v-for="product in noveltyProducts"
        :key="product.product_id"
        cols="3"
      >
        <Product
          :mainPath="getBackendUrl"
          :product="product"
        ></Product>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Carousel from '@/components/ThirdParty/Carousel'
import Product from '@/components/Products/Product'
import { mapGetters } from 'vuex'

export default {
  name: 'HomeComponent',
  components: { Carousel, Product },
  computed: {
    ...mapGetters('home', ['isHomeLoading', 'getMainSliderImages', 'getBackendUrl']),
    ...mapGetters({
      noveltyProducts: 'home/getNoveltyProducts'
    })
  },
  data: () => ({}),
  mounted: function () {
    this.$store.dispatch('home/loadMainSliderImages')
    this.$store.dispatch('home/loadNoveltyProducts')
    this.$store.dispatch('cart/loadCartItems')
  }
}
</script>

<style scoped>

</style>
