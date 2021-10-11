<template>
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <h2>Apple iPhone 12 Pro</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-row class="d-flex justify-center">
            <v-col cols="12">
              <Carousel
                :items-images="productImages"
                :media_url="mediaBase"
                :height="600"
              ></Carousel>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-row>
            <v-col cols="12">
              <h4>Код: 0000000001</h4>
            </v-col>
            <v-col cols="12 pt-0 pb-0 d-flex justify-content-start align-items-center">
              <v-rating
                :value="3"
                color="amber"
                dense
                half-increments
                readonly
                size="20"
              ></v-rating>
              <div class="grey--text ml-4">
                8 відгуків
              </div>
            </v-col>
            <v-col cols="12">
              <v-chip
                class="green"
                dark
              >
                <v-icon>
                  mdi-check-bold
                </v-icon>
                Є в наявності
              </v-chip>
            </v-col>
            <v-col cols="12">
              <v-row>
                <v-col cols="6">
                  <b style="color: black;">
                    <strike>
                      19500 грн.
                    </strike>
                  </b>
                  <b class="text-muted"
                     style="color: red;"
                  >
                    <h3>18500 грн.</h3>
                  </b>
                </v-col>
                <v-col cols="6" class="d-flex align-center justify-center">
                  <v-btn class="green" dark>
                    <v-icon>mdi-cart-outline</v-icon>
                    Купити
                  </v-btn>
                  <v-btn icon class="ml-5">
                    <v-icon>mdi-heart-outline</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="12">
              <v-card class="secondary" dark>
                <v-img
                  src="https://picsum.photos/350/165?random"
                  height="170"
                  class="grey darken-4"
                ></v-img>
                <v-card-title class="text-h6 d-flex justify-center">
                  Інтернет-магазин "Active life"
                </v-card-title>
                <v-card-text class="white mb-0 pb-0">
                  <v-list dense light>
                    <v-list-item-group>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-link-variant</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Сторінка продавця
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-google-maps</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Місце знаходження: м.Київ, Зочих 28
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-phone</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            +380000000000
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-email-fast</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            activelife@gmail.com
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import Carousel from '@/components/ThirdParty/Carousel'
export default {
  name: 'ProductComponent',
  components: { Carousel },
  props: ['product_code'],
  data: () => ({
    mediaBase: 'https://content1.rozetka.com.ua/',
    productImages: [
      { item_image: 'goods/images/big/221250977.jpg' },
      { item_image: 'goods/images/big/221250974.jpg' },
      { item_image: 'goods/images/big/221022193.jpg' },
      { item_image: 'goods/images/big/221250972.jpg' }
    ]
  })
}
</script>

<style scoped>

</style>
