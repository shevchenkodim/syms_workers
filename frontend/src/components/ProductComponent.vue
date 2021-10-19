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
                :items-images="productDetail.images"
                :media_url="getBackendUrl"
                :height="productDetail.image_height"
              ></Carousel>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <h2>Короткі характеристики</h2>
              <p>{{ productDetail.short_character }}</p>
            </v-col>
            <v-col cols="12">
              <h2>Опис товару</h2>
            </v-col>
            <v-col
              cols="12"
              class="pt-0"
              v-for="(block, index) in productDetail.product_descriptions"
              :key="index"
            >
              <h3>{{ block.title }}</h3>
              <p>{{ block.description }}</p>
            </v-col>
            <v-col cols="12">
              <h2>Характеристики</h2>
              <v-list dense light>
                <v-list-item-group>
                  <template v-for="(character, index) in productDetail.characteristic_list">
                    <v-list-item :key="index">
                      <v-list-item-content>
                        <v-list-item-title class="d-flex justify-space-between">
                          <span>{{ character.attribute }}</span>
                          <span>
                            <span v-for="(char, index) in character.values" :key="index">
                              {{ char.value }} {{ char.unit }}
                            </span>
                          </span>
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>

                    <v-divider :key="index"></v-divider>
                  </template>
                </v-list-item-group>
              </v-list>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <h2>Відгуки</h2>
            </v-col>
            <v-col cols="12">
              <v-list three-line>
                <template v-for="(v, i) in [1, 2, 3]">
                  <v-divider :key="i"></v-divider>

                  <v-subheader :key="i">
                    <v-row>
                      <v-col cols="12" class="d-flex justify-space-between pb-0 pt-0">
                        <span><b>Dmytro Shevchenko</b></span>
                        <span>
                          <v-rating
                            :value="4"
                            color="amber"
                            dense
                            half-increments
                            readonly
                            size="14"
                          ></v-rating>
                        </span>
                      </v-col>
                    </v-row>
                  </v-subheader>

                  <v-list-item :key="i">
                    <v-list-item-avatar>
                      <v-img src="https://cdn-icons-png.flaticon.com/512/149/149071.png"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>
                        Some comment, some comment, some comment, some comment
                      </v-list-item-title>
                      <v-list-item-subtitle class="d-flex align-center justify-space-between">
                        <span>
                          <v-btn
                            icon
                            color="green"
                            class="mr-1"
                          >
                            <v-icon>mdi-thumb-up</v-icon>
                            4
                          </v-btn>
                          <v-btn
                            icon
                            color="error"
                            class="ml-1"
                          >
                            <v-icon>mdi-thumb-down</v-icon>
                            7
                          </v-btn>
                        </span>
                        <span class="text-muted">
                          27.09.2021 15.05
                        </span>
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </template>
              </v-list>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-row>
            <v-col cols="12">
              <h4>Код: {{ productDetail.product_id }}</h4>
            </v-col>
            <v-col cols="12 pt-0 pb-0 d-flex justify-content-start align-items-center">
              <v-rating
                :value="productDetail.average_star_rating"
                color="amber"
                dense
                half-increments
                readonly
                size="20"
              ></v-rating>
              <div class="grey--text ml-4">
                {{ productDetail.comment_count }} відгуків
              </div>
            </v-col>
            <v-col cols="12">
              <v-chip
                :class="{'green': productDetail.is_available, 'danger': !productDetail.is_available}"
                dark
              >
                <v-icon>
                  mdi-check-bold
                </v-icon>
                {{ productDetail.is_available ? 'Є в наявності' : 'Немає' }}
              </v-chip>
            </v-col>
            <v-col cols="12">
              <v-row>
                <v-col cols="6">
                  <b class="black--text" v-if="productDetail.old_price">
                    <strike>
                      {{productDetail.old_price}} грн.
                    </strike>
                  </b>
                  <b :class="{'red--text': productDetail.old_price, 'black--text': !productDetail.old_price}">
                    <h3>{{productDetail.price}} грн.</h3>
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
                  Інтернет-магазин "{{ sellerDetail.name }}"
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
                            Місце знаходження: {{ sellerDetail.address }}
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-phone</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            {{ sellerDetail.phone }}
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-email-fast</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            {{ sellerDetail.email }}
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col
              cols="12"
              v-for="(block, index) in sellerDetail.blocks"
              :key="index"
            >
              <v-card :class="block.bg_class" dark>
                <v-card-title class="text-h6">
                  {{ block.title }}
                </v-card-title>
                <v-card-text class="white mb-0 pb-0">
                  <v-list dense light>
                    <v-list-item-group>
                      <v-list-item
                        v-for="(item, index) in block.items"
                        :key="index"
                      >
                        <v-list-item-icon>
                          <v-icon>{{ item.icons }}</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            {{ item.value }}
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
import { mapGetters } from 'vuex'
export default {
  name: 'ProductComponent',
  components: { Carousel },
  props: ['product_code'],
  computed: {
    ...mapGetters('product', ['getBackendUrl']),
    ...mapGetters({
      productDetail: 'product/getProductData',
      sellerDetail: 'product/getSellerData'
    })
  },
  data: () => ({}),
  methods: {
    doInit () {
      this.doLoadProductDetail()
    },
    doLoadProductDetail () {
      this.$store.dispatch('product/loadProductData', this.product_code)
    }
  },
  mounted () {
    this.doInit()
  }
}
</script>

<style scoped>

</style>
