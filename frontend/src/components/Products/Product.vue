<template>
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
      class="p-5"
      :height="product.image_height"
      :src="mainPath + product.image"
    ></v-img>

    <v-card-title>
      <router-link
        :to="{ path: `/product/${product.code}`}"
        style="text-decoration: none; color: black;"
      >
        {{product.name}}
      </router-link>
    </v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0 pb-2"
      >
        <v-rating
          :value="product.average_star_rating"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ml-4">
          {{product.comment_count}} відгуків
        </div>
      </v-row>

      <div class="pt-2 pb-2 subtitle-1 d-flex justify-space-between">
        <b class="black--text" v-if="product.old_price">
          <strike>
            {{product.old_price}} грн.
          </strike>
        </b>
        <b :class="{'red--text': product.old_price, 'black--text': !product.old_price}">
          {{product.price}} грн.
        </b>
      </div>

      <div class="d-flex justify-space-between">
        <v-chip
          :class="{'green': product.is_available, 'danger': !product.is_available}"
          dark
        >
          <v-icon>
            mdi-check-bold
          </v-icon>
          {{ product.is_available ? 'Є в наявності' : 'Немає' }}
        </v-chip>
        <v-btn
          icon
          v-if="!product.exists_in_favorites"
        >
          <v-icon>mdi-heart-outline</v-icon>
        </v-btn>
        <v-btn
          icon
          v-if="!product.exists_in_cart"
          @click="doAddCartItem()"
        >
          <v-icon>mdi-cart-outline</v-icon>
        </v-btn>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'NoveltyProduct',
  props: {
    product: {
      type: Object,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: Object({})
    },
    mainPath: {
      type: String,
      default: ''
    }
  },
  methods: {
    doAddCartItem () {
      this.$store.dispatch('cart/doAddCartItemPromise', { product_id: this.product.product_id })
        .then(resp => {
          if (resp.status === 201) {
            this.$store.dispatch('cart/loadCartItems')
            this.$store.commit('home/setIsExistsCartItem', { product_id: this.product.product_id, value: true })
            this.$forceUpdate()
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
