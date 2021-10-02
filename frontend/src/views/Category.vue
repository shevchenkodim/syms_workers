<template>
  <div class="category">
    <CategoryComponent />
  </div>
</template>

<script>
import CategoryComponent from '@/components/CategoryComponent'

export default {
  name: 'Category',
  props: ['category_code'],
  components: {
    CategoryComponent
  }
}
</script>

<style scoped>

</style>
