<template>
  <div>
    <v-divider></v-divider>
    <v-subheader>
      <v-row>
        <v-col cols="12" class="d-flex justify-space-between pb-0 pt-0">
          <span><b>{{ comment.owner.full_name }}</b></span>
          <span>
            <v-rating
              :value="comment.rating_stars"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
            ></v-rating>
          </span>
        </v-col>
      </v-row>
    </v-subheader>

    <v-list-item>
      <v-list-item-avatar>
        <v-img :src="getBackendUrl + comment.owner.image"></v-img>
      </v-list-item-avatar>

      <v-list-item-content>
        <v-list-item-title>
          {{ comment.text }}
        </v-list-item-title>
        <v-list-item-subtitle class="d-flex align-center justify-space-between">
          <span>
            <v-btn
              icon
              color="green"
              class="mr-1"
            >
              <v-icon>mdi-thumb-up</v-icon>
              {{ comment.likes_count }}
            </v-btn>
            <v-btn
              icon
              color="error"
              class="ml-1"
            >
              <v-icon>mdi-thumb-down</v-icon>
              {{ comment.dislikes_count }}
            </v-btn>
          </span>
          <span class="text-muted">
            {{ comment.date_time_add }}
          </span>
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Comment',
  props: ['comment'],
  computed: {
    ...mapGetters('product', ['getBackendUrl'])
  }
}
</script>

<style scoped>

</style>
