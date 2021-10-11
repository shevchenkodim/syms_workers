<template>
  <div class="product">
    <ProductComponent :product_code="product_code"></ProductComponent>
  </div>
</template>

<script>
import ProductComponent from '@/components/ProductComponent'
export default {
  name: 'Product',
  components: { ProductComponent },
  props: ['product_code']
}
</script>

<style scoped>

</style>
