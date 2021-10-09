<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h2>{{ getCategoryData.name }}</h2>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-form @submit.prevent="doApplyFilter">
          <input type="submit" hidden>
          <v-card>
            <v-card-text>
              <v-row>
                <v-col cols="4" class="d-flex">
                  <v-text-field
                    class="mr-2"
                    label="Ціна від"
                    value="0"
                    type="number"
                    dense
                    outlined
                    clearable
                    hide-details="auto"
                    v-model="filters.priceFrom"
                  ></v-text-field>
                  <span style="vertical-align: middle;" class="pt-2">
                    <b>-</b>
                  </span>
                  <v-text-field
                    class="ml-2"
                    label="Ціна до"
                    type="number"
                    value="99999"
                    dense
                    outlined
                    clearable
                    hide-details="auto"
                    v-model="filters.priceTo"
                  ></v-text-field>
                </v-col>
                <v-col cols="3">
                  <v-select class="mb-0 pb-0"
                    label="Бренд"
                    v-model="producerItem"
                    :items="producerItems"
                    dense
                    outlined
                    hide-details="auto"
                  ></v-select>
                </v-col>
                <v-col cols="3">
                  <v-select class="mb-0 pb-0"
                    label="Відсортувати"
                    v-model="sortByItem"
                    :items="sortByItems"
                    dense
                    outlined
                    hide-details="auto"
                  ></v-select>
                </v-col>
                <v-col cols="2" class="d-flex">
                  <v-btn
                    block
                    color="success"
                    @click="doApplyFilter"
                  >
                    <v-icon>
                      mdi-filter
                    </v-icon>
                    Знайти
                  </v-btn>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-form>
      </v-col>
    </v-row>

    <v-row v-if="categoryProducts.length > 0">
      <v-col
        v-for="product in categoryProducts"
        :key="product.product_id"
        cols="3"
      >
        <Product
          :mainPath="getBackendUrl"
          :product="product"
        ></Product>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col cols="12">
        Товарів не знайдено
      </v-col>
    </v-row>

    <v-row v-if="categoryProducts.length > 0">
      <v-col cols="12">
        <div class="text-center">
          <v-pagination
            v-model="pagination_current"
            :length="parseInt(Math.ceil(pagination.count / pagination.limit))"
            :total-visible="7"
          ></v-pagination>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Product from '@/components/Products/Product'
import { mapGetters } from 'vuex'

export default {
  name: 'CategoryComponent',
  props: ['category_code'],
  computed: {
    ...mapGetters('category', ['getBackendUrl', 'getCategoryData']),
    ...mapGetters({
      categoryProducts: 'category/getCategoryProducts'
    })
  },
  components: { Product },
  data: () => {
    return {
      filters: {
        priceFrom: 0,
        priceTo: 999999
      },
      sortByItem: 'Новинки',
      sortByItems: ['Від дешевших', 'Від дорогих', 'Новинки'],
      producerItem: '',
      producerItems: ['', 'SYMS', 'Apple', 'Huawei', 'OnePlus', 'Samsung', 'Xiaomi'],
      pagination_current: 1,
      pagination: {
        limit: 4,
        count: 0
      }
    }
  },
  methods: {
    doInit () {
      this.initPagination()
      this.$store.dispatch('category/loadCategoryData', this.category_code)
      setTimeout(() => {
        this.doLoadProducts()
      }, 500)
    },
    doApplyFilter () {
      this.initPagination()
      this.doLoadProducts()
    },
    doLoadProducts () {
      this.$store.dispatch('category/loadCategoryProducts', {
        ...this.pagination,
        ...{ current: this.pagination_current },
        ...{ priceFrom: this.filters.priceFrom, priceTo: this.filters.priceTo, ordering: this.sortByItem, brand: this.producerItem }
      })
        .then(({ data }) => {
          console.log(data)
          this.$store.commit('category/setCategoryProducts', data.rows)
          this.pagination.count = data.params.count
        })
        .catch(() => {})
        .finally(() => {
          this.$store.commit('category/initEnd')
        })
    },
    initPagination () {
      this.pagination_current = 1
      this.pagination = { limit: 4, count: null }
    }
  },
  mounted () {
    this.doInit()
  },
  watch: {
    category_code: function (val) {
      this.category_code = val
      this.doInit()
    },
    pagination_current: function (val) {
      this.pagination_current = val
      this.doLoadProducts()
    }
  }
}
</script>

<style scoped>

</style>
