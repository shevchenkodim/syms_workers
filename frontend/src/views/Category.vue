<template>
  <div class="category">
    <CategoryComponent :category_code="this.category_code" />
  </div>
</template>

<script>
import CategoryComponent from '@/components/CategoryComponent'

export default {
  name: 'Category',
  props: ['category_code'],
  components: {
    CategoryComponent
  },
  watch: {}
}
</script>

<style scoped>

</style>
