<template>
  <div class="mx-auto overflow-hidden">
    <v-app-bar
      app
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>
        <v-icon>mdi-cart</v-icon>
        <b> SYMS</b>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-text-field
        flat
        dense
        rounded
        hide-details
        label="..."
        prepend-inner-icon="mdi-magnify"
        solo-inverted
      ></v-text-field>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-cart-outline</v-icon>
      </v-btn>

      <v-menu
        v-model="menu"
        :close-on-content-click="false"
        :nudge-width="200"
        offset-x
        bottom
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            dark
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>

        <v-card>
          <v-list>
            <v-list-item>
              <v-list-item-avatar>
                <img
                  src="https://avatars.githubusercontent.com/u/16786985?s=460&u=9f2fe771bbc8bcfcc195fde83ca914b00a98da54&v=4"
                  alt="avatars"
                >
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>Admin Admins</v-list-item-title>
                <v-list-item-subtitle>System administrator</v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action>
                <v-btn
                  class="mx-2"
                  fab
                  dark
                  small
                  color="info"
                >
                  <v-icon>mdi-tools</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>

          <v-divider></v-divider>

          <v-list>
            <v-list-item>
              <v-list-item-action>
                <v-icon>mdi-cart-outline</v-icon>
              </v-list-item-action>
              <v-list-item-title>Кошик</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-action>
                <v-icon>mdi-heart-outline</v-icon>
              </v-list-item-action>
              <v-list-item-title>Список бажаннь</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-action>
                <v-icon>mdi-login-variant</v-icon>
              </v-list-item-action>
              <v-list-item-title>Вхід / Реєстрація</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      dark
    >
      <!-- expand-on-hover-->

      <v-list-item class="px-2 py-1">
        <v-list-item-avatar>
          <v-icon>mdi-view-list-outline</v-icon>
        </v-list-item-avatar>

        <v-list-item-title><b>Категорії товарів</b></v-list-item-title>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-primary--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-camera</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Фото та відео</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-cellphone-iphone</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Смартфони, ТВ</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>

  <v-main class="ml-5 mr-5">
    <v-container fluid>
      <v-row>
        <v-col cols="4">
          <v-list three-line>
            <template v-for="(item, index) in items_lists">
              <v-subheader
                v-if="item.header"
                :key="item.header"
                v-text="item.header"
              ></v-subheader>

              <v-divider
                v-else-if="item.divider"
                :key="index"
                :inset="item.inset"
              ></v-divider>

              <v-list-item
                v-else
                :key="item.title"
              >
                <v-list-item-avatar>
                  <v-img :src="item.avatar"></v-img>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title v-html="item.title"></v-list-item-title>
                  <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
        </v-col>
        <v-col cols="8" >
          <v-carousel height="350">
            <v-carousel-item
              v-for="(item,i) in itemsImages"
              :key="i"
              :src="item.src"
              reverse-transition="fade-transition"
              transition="fade-transition"
            ></v-carousel-item>
          </v-carousel>
        </v-col>
      </v-row>
    </v-container>
  </v-main>

  <v-footer app dark class="d-flex justify-center">
    Developed by
    <a href="https://www.instagram.com/dima_shevchenko99/">
      Dmytro Shevchenko
    </a>
  </v-footer>
</template>

<script>
export default {
  name: 'MainLayout',
  data: () => ({
    drawer: true,
    items: [
      { title: 'Home', icon: 'mdi-home-city' },
      { title: 'My Account', icon: 'mdi-account' },
      { title: 'Users', icon: 'mdi-account-group-outline' }
    ],
    itemsImages: [
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
      }
    ],
    items_lists: [
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
        title: 'Brunch this weekend?',
        subtitle: '<span class="text--primary">Ali Connors</span> &mdash; I\'ll be in your neighborhood doing errands this weekend. Do you want to hang out?'
      },
      { divider: true, inset: true },
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: '<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I\'m out of town this weekend.'
      },
      { divider: true, inset: true },
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
        title: 'Oui oui',
        subtitle: '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?'
      },
      { divider: true, inset: true },
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
        title: 'Birthday gift',
        subtitle: '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?'
      }
    ],
    mini: true,
    fav: true,
    menu: false,
    message: false,
    hints: true,
    group: null
  }),
  watch: {
    group () {
      this.drawer = false
    }
  }
}
</script>

<style scoped>

</style>
