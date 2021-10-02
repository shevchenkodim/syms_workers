<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h2>Смартфони</h2>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
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
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-select class="mb-0 pb-0"
                  label="Виробник"
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
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'CategoryComponent',
  data: () => {
    return {
      sortByItem: 'За рейтингом',
      sortByItems: ['Від дешевших', 'Від дорогих', 'За рейтингом', 'Новинки'],
      producerItem: 'SYMS',
      producerItems: ['SYMS', 'Інші']
    }
  }
}
</script>

<style scoped>

</style>
