<template>
  <div id="search_component_id">
    <SearchComponent :search_value="search_value"></SearchComponent>
  </div>
</template>

<script>
import SearchComponent from '@/components/SearchComponent'
export default {
  name: 'Search',
  components: { SearchComponent },
  props: ['search_value']
}
</script>

<style scoped>

</style>
