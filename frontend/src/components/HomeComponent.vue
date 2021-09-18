<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <Carousel :itemsImages="getMainSliderImages" :height="350" />
      </v-col>
    </v-row>

    <v-row>
        <v-col cols="12">
          <h3>Новинки</h3>
        </v-col>
        <v-col cols="3">
          <v-card
            :loading="false"
            max-width="250"
          >
            <template slot="progress">
              <v-progress-linear
                color="deep-purple"
                height="10"
                indeterminate
              ></v-progress-linear>
            </template>

            <v-img
              height="250"
              src="https://i1.rozetka.ua/goods/13545489/112005632_images_13545489308.jpg"
            ></v-img>

            <v-card-title>Apple iPhone 11</v-card-title>

            <v-card-text>
              <v-row
                align="center"
                class="mx-0 pb-2"
              >
                <v-rating
                  :value="2"
                  color="amber"
                  dense
                  half-increments
                  readonly
                  size="14"
                ></v-rating>

                <div class="grey--text ml-4">
                  8 відгуків
                </div>
              </v-row>

              <div class="pt-2 pb-2 subtitle-1 d-flex justify-space-between">
                <b style="color: black;"><strike>23500 грн.</strike></b>
                <b class="text-muted" style="color: red;">18500 грн.</b>
              </div>

              <v-chip class="green" dark>
                <v-icon>mdi-check-bold</v-icon>
                Є в наявності
              </v-chip>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

  </v-container>
</template>

<script>
import Carousel from '@/components/ThirdParty/Carousel'
import { mapGetters } from 'vuex'

export default {
  name: 'HomeComponent',
  components: { Carousel },
  computed: {
    ...mapGetters('home', ['isHomeLoading', 'getMainSliderImages'])
  },
  data: () => ({}),
  mounted: function () {
    this.$store.dispatch('home/loadMainSliderImages')
  }
}
</script>

<style scoped>

</style>
