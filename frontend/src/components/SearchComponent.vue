<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h2>Пошук на сайті</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="10" class="pl-1">
        <form @submit.prevent="doApplySearch" class="p-0 m-0">
          <input type="submit" hidden>
          <v-text-field
            class="ml-2"
            label="Текст пошуку"
            dense
            outlined
            clearable
            hide-details="auto"
            :class="{'is-invalid': !search_frm.value}"
            v-model="search_frm.value"
          ></v-text-field>
        </form>
      </v-col>
      <v-col cols="2">
        <v-btn
          block
          color="success"
          @click="doApplySearch"
        >
          <v-icon>
            mdi-magnify
          </v-icon>
          Знайти
        </v-btn>
      </v-col>
    </v-row>

    <v-row v-if="searchProducts.length > 0">
      <v-col
        v-for="product in searchProducts"
        :key="product.product_id"
        cols="3"
      >
        <Product
          @add_product_to_cart="doApplySearch"
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

    <v-row v-if="searchProducts.length > 0">
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
import { mapGetters } from 'vuex'
import Product from '@/components/Products/Product'

export default {
  name: 'SearchComponent',
  props: {
    search_value: {
      type: String,
      default: ''
    }
  },
  components: { Product },
  computed: {
    ...mapGetters('search', ['getBackendUrl', 'getSearchProducts']),
    ...mapGetters({
      searchProducts: 'search/getSearchProducts'
    })
  },
  data: () => {
    return {
      search_frm: {
        value: ''
      },
      pagination_current: 1,
      pagination: {
        limit: 4,
        count: 0
      }
    }
  },
  methods: {
    doApplySearch () {
      this.$store.dispatch('search/loadSearchProducts', {
        searchValue: this.search_frm.value ? this.search_frm.value : '',
        ...this.pagination,
        ...{ current: this.pagination_current }
      })
        .then(({ data }) => {
          this.$store.commit('search/setSearchProducts', data.rows)
          this.pagination.count = data.params.count
        })
        .catch(() => {})
        .finally(() => {
          this.$store.commit('search/initEnd')
        })
      this.$forceUpdate()
    }
  },
  mounted () {
    this.search_frm.value = this.search_value
    this.doApplySearch()
  },
  watch: {
    pagination_current: function (val) {
      this.pagination_current = val
      this.doApplySearch()
    }
  }
}
</script>

<style scoped>

</style>
