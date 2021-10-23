<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h2>Корзина</h2>
      </v-col>
    </v-row>

    <v-row v-if="cartItems.length > 0">
      <v-col
        cols="12"
        v-for="(item, index) in cartItems"
        :key="index + '_cart_item'"
      >
        <v-row>
          <v-col cols="1 d-flex align-center justify-center">
            <b>№{{ index + 1 }}</b>
          </v-col>
          <v-col cols="3">
            <b>Продукт:</b>
            <a :href="'/product/' + item.product.code" target="_blank">
              {{ item.product.name }}
            </a>
            <b>Ціна:</b> {{ item.product.price }}
          </v-col>
          <v-col cols="2" class="d-flex align-center justify-center">
            <v-text-field
              label="Кількість"
              type="number"
              dense
              outlined
              clearable
              hide-details="auto"
              placeholder="1"
              v-model="item.quantity"
              @change="doCheckQuantityValue(item)"
            ></v-text-field>
          </v-col>
          <v-col cols="2" class="d-flex align-center">
            <b class="pr-2">Сума:</b> {{ parseFloat(item.quantity) * parseFloat(item.product.price) }} грн.
          </v-col>
          <v-col cols="3" class="d-flex align-center">
            <v-select class=""
              label="Спосіб доставки"
              v-model="item.delivery_method"
              :hint="`${item.delivery_method.id}, ${item.delivery_method.value}`"
              :items="item.delivery_methods"
              item-text="value"
              item-value="id"
              dense
              outlined
              hide-details="false"
            ></v-select>
          </v-col>
          <v-col cols="1" class="d-flex align-center justify-center">
            <v-btn icon @click="doRemoveCartItem(item.id)">
              <v-icon>mdi-trash-can-outline</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <hr v-if="cartItems.length > index" class="mt-2">
      </v-col>

      <v-col cols="12" class="d-flex justify-space-between align-center">
        <span>
          <h3><b>Загальна сума:</b> <span>{{ totalAmount }}</span> грн.</h3>
        </span>
        <div>
          <v-btn
            class="primary"
            @click="doCreateOrder"
          >
            <v-icon>mdi-cart-check</v-icon>
            Оформити
          </v-btn>
          <v-btn
            @click="doSaveCartItems"
            class="green ml-3"
            dark
          >
            <v-icon>mdi-check-all</v-icon>
            Зберегти
          </v-btn>
        </div>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col cols="12">
        Товарів не знайдено
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'CartComponent',
  computed: {
    ...mapGetters('cart', ['getCartCount'])
  },
  data: function () {
    return {
      totalAmount: 0,
      cartItems: []
    }
  },
  methods: {
    doInitAll () {
      this.doLoadCartItems()
      this.$store.dispatch('cart/loadCartItems')
    },
    doGetTotalPrice () {
      // eslint-disable-next-line no-return-assign
      this.totalAmount = this.cartItems.reduce((total, item) => total += (item.product.price * item.quantity), 0)
    },
    doCheckQuantityValue (item) {
      let value = parseInt(item.quantity)

      if (!value || value < 1) {
        value = 1
      }

      item.quantity = value

      this.doGetTotalPrice()
    },
    doLoadCartItems () {
      this.$store.dispatch('cart/loadCartItemsPromise')
        .then(resp => {
          this.cartItems = resp.data.items
          this.doGetTotalPrice()
          this.$forceUpdate()
        })
    },
    doSaveCartItems () {
      this.$store.dispatch('cart/doSaveCartItemsPromise', { cart_items: this.cartItems })
        .then(resp => {
          if (resp.status === 200) {
            this.doInitAll()
          }
        })
    },
    doCreateOrder () {
      this.$store.dispatch('cart/doCreateOrderPromise')
        .then(resp => {
          if (resp.status === 201) {
            this.doInitAll()
          }
        })
    },
    doRemoveCartItem (id) {
      this.$store.dispatch('cart/doRemoveCartItemPromise', { id: id })
        .then(resp => {
          if (resp.status === 200) {
            this.doInitAll()
          }
        })
    }
  },
  mounted () {
    this.doInitAll()
  }
}
</script>

<style scoped>

</style>
