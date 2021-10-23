<template>
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <h2>{{ productDetail.name }}</h2>
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
              :key="index + '_block_description'"
            >
              <h3>{{ block.title }}</h3>
              <p>{{ block.description }}</p>
            </v-col>
            <v-col cols="12">
              <h2>Характеристики</h2>
              <v-list dense light>
                <v-list-item-group>
                  <template v-for="(character, index) in productDetail.characteristic_list">
                    <v-list-item :key="index + 1 + '_block_character'">
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

                    <v-divider :key="index + 1 + '_d_block_character'"></v-divider>
                  </template>
                </v-list-item-group>
              </v-list>
            </v-col>
          </v-row>
          <v-row v-if="productComments.length > 0">
            <v-col cols="12">
              <h2>Відгуки[{{productComments.length}}]</h2>
            </v-col>
            <v-col cols="12">
              <v-list three-line>
                <template v-for="(comment, i) in productComments">
                  <Comment
                    :comment="comment"
                    :key="i + '_comment_p'"
                  ></Comment>
                </template>
              </v-list>
            </v-col>
            <v-col cols="12">
              <v-row v-if="productComments.length > 0" class="d-flex justify-center">
                <div class="text-center">
                  <v-pagination
                    v-model="pagination_current"
                    :length="parseInt(Math.ceil(pagination.count / pagination.limit))"
                    :total-visible="7"
                  ></v-pagination>
                </div>
              </v-row>
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
                  <v-btn
                    @click="doAddCartItem(productDetail.id)"
                    v-if="!productDetail.exists_in_cart"
                    class="green"
                    dark
                  >
                    <v-icon>mdi-cart-outline</v-icon>
                    Купити
                  </v-btn>
                  <v-btn
                    v-else
                    class="green"
                    dark
                    @click="doGoToCart"
                  >
                    <v-icon>mdi-cart-outline</v-icon>
                    Оформити
                  </v-btn>
                  <v-btn
                    icon
                    class="ml-5"
                    @click="doAddCartItem()"
                  >
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
<!--                      <v-list-item>-->
<!--                        <v-list-item-icon>-->
<!--                          <v-icon>mdi-link-variant</v-icon>-->
<!--                        </v-list-item-icon>-->
<!--                        <v-list-item-content>-->
<!--                          <v-list-item-title>-->
<!--                            Сторінка продавця-->
<!--                          </v-list-item-title>-->
<!--                        </v-list-item-content>-->
<!--                      </v-list-item>-->

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
import Comment from '@/components/Products/Comment'
import { mapGetters } from 'vuex'
export default {
  name: 'ProductComponent',
  components: { Carousel, Comment },
  props: ['product_code'],
  computed: {
    ...mapGetters('product', ['getBackendUrl']),
    ...mapGetters({
      productDetail: 'product/getProductData',
      sellerDetail: 'product/getSellerData'
    })
  },
  data: () => ({
    productComments: [],
    pagination_current: 1,
    pagination: {
      limit: 4,
      count: 0
    }
  }),
  methods: {
    doInit () {
      this.doLoadProductDetail()
    },
    doLoadComments (sleep = 200) {
      this.productComments = []
      if (!this.productDetail.product_id) { return }
      setTimeout(() => {
        this.$store.dispatch('product/loadProductComments', {
          productId: this.productDetail.product_id,
          ...this.pagination,
          ...{ current: this.pagination_current }
        })
          .then(({ data }) => {
            this.productComments = data.rows
            this.pagination.count = data.params.count
          })
      }, sleep)
    },
    doLoadProductDetail () {
      this.$store.dispatch('product/loadProductData', this.product_code)
      this.$forceUpdate()
      // this.doLoadComments(1000)
    },
    doGoToCart () {
      window.location.replace('/cart')
    },
    doAddCartItem () {
      this.$store.dispatch('cart/doAddCartItemPromise', { product_id: this.productDetail.product_id })
        .then(resp => {
          if (resp.status === 201) {
            this.$store.dispatch('cart/loadCartItems')
            this.$store.commit('product/setIsExistsCartItem', { product_id: this.productDetail.product_id, value: true })
            this.$forceUpdate()
          }
        })
    }
  },
  mounted () {
    this.doInit()
    this.$store.dispatch('cart/loadCartItems')
  },
  watch: {
    pagination_current: function (val) {
      this.pagination_current = val
      // this.doLoadComments(1000)
    }
  }
}
</script>

<style scoped>

</style>
