<template>
  <v-container>
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

        <v-menu
          v-model="notifications"
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
              <v-icon>mdi-bell-outline</v-icon>
            </v-btn>
          </template>

          <v-card>
            <v-list>
              <v-list-item>
                <v-list-item-content>
                  View read (5)
                </v-list-item-content>

                <v-list-item-action>
                  <v-btn
                    fab
                    small
                  >
                    <v-icon>mdi-email-open</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </v-list>

            <v-divider></v-divider>

            <v-list three-line>
              <template v-for="(item, index) in notification_items">
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
          </v-card>
        </v-menu>

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

              <v-list-item
                v-if="!isAuthenticated"
              >
                <v-list-item-action>
                  <v-icon>mdi-login-variant</v-icon>
                </v-list-item-action>
                <v-list-item-title>Вхід / Реєстрація</v-list-item-title>
              </v-list-item>

              <v-list-item
                v-else
                @click.prevent="logout"
              >
                <v-list-item-action>
                  <v-icon>mdi-logout</v-icon>
                </v-list-item-action>
                <v-list-item-title>Выход</v-list-item-title>
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

    <v-main>
      <v-container>
        <router-view />
      </v-container>

      <v-row>
        <v-col cols="4">
          <div class="d-flex justify-center align-center pb-2">
            <b>Приєднуйтеся до наших соц. мереж</b>
          </div>
          <div class="d-flex justify-center align-center">
            <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/1024px-Facebook_Logo_%282019%29.png" class="mr-1">
            <img width="36" src="https://c7.hotpng.com/preview/145/243/586/logo-computer-icons-clip-art-instagram-layout-thumbnail.jpg" class="ml-1 mr-1">
            <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/600px-Telegram_logo.svg.png" class="ml-1 mr-1">
            <img height="36" src="https://w7.pngwing.com/pngs/928/563/png-transparent-youtube-logo-computer-icons-youtube-angle-company-monochrome.png" class="mr-1">
          </div>
        </v-col>
        <v-col cols="4">
          <div class="d-flex justify-center align-center pb-2">
            <b>Дізнавайтеся про все першими</b>
          </div>
          <v-row>
            <v-col cols="8">
              <v-text-field
                dense
                outlined
                placeholder="Email Address"
                prepend-icon="mdi-email-variant"
                type="email"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-btn
                class="info m-0"
                elevation="2"
              >
                Підписатися
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="4">
          <div class="d-flex justify-center align-center pb-2">
            <b>Звертайтеся з будь-яких питаннь</b>
          </div>
          <div class="d-flex justify-center align-center">
            <img width="36" src="https://w7.pngwing.com/pngs/699/791/png-transparent-facebook-messenger-social-media-logo-computer-icons-facebook-messenger-logo-logo-messenger-logo-blue-angle-triangle.png" class="mr-1">
            <img width="36" src="https://f0.pngfuel.com/png/322/453/viber-application-png-clip-art.png" class="ml-1 mr-1">
            <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/600px-Telegram_logo.svg.png" class="ml-1 mr-1">
          </div>
        </v-col>
      </v-row>

      <v-row class="pb-3">
        <v-col cols="3" v-for="info in infoCards" :key="info">
          <v-card
            outlined
          >
            <v-card-title class="blue-grey lighten-2"
                          v-text="info.title"
            ></v-card-title>
            <v-card-text>
              <v-list>
                <v-item v-for="item in info.items"
                        :key="item"
                >
                  <v-list-item-title
                    v-text="item"
                  ></v-list-item-title>
                </v-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

    </v-main>

    <v-footer
      app
      dark
      class="d-flex justify-center"
    >
      Developed by
      <a href="https://www.instagram.com/dima_shevchenko99/">
        Dmytro Shevchenko
      </a>
    </v-footer>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MainLayout',
  computed: {
    ...mapActions(['auth/logout']),
    ...mapGetters({
      isAuthenticated: 'auth/isAuthenticated'
    })
  },
  data: () => ({
    drawer: false,
    items: [
      { title: 'Home', icon: 'mdi-home-city' },
      { title: 'My Account', icon: 'mdi-account' },
      { title: 'Users', icon: 'mdi-account-group-outline' }
    ],
    mini: true,
    fav: true,
    menu: false,
    message: false,
    hints: true,
    group: null,
    infoCards: [
      {
        title: 'Покупцям',
        items: ['Довідка для покупців', 'Про надійних продавців', 'Як залишити корисний відгук']
      },
      {
        title: 'Продавцям',
        items: ['Довідка для Продавцям', 'Тарифи', 'Угода користувача']
      },
      {
        title: 'Про нас',
        items: ['Про Marketplace', 'Адміністрація', 'Робота в Marketplace']
      },
      {
        title: 'Партнери',
        items: ['Kabanchik.ua', 'Вчасно', 'Zakupki.prom.ua']
      }
    ],
    notifications: false,
    notification_items: [
      { header: 'Today' },
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
        title: 'Brunch this weekend?',
        subtitle: '<span class="text--primary">Ali Connors</span> &mdash; Ill be in your neighborhood doing errands this weekend. Do you want to hang out?'
      },
      { divider: true, inset: true },
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: '<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but Im out of town this weekend.'
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
      },
      { divider: true, inset: true },
      {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
        title: 'Recipe to try',
        subtitle: '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.'
      }
    ]
  }),
  methods: {
    logout () {
      this.$store.dispatch('auth/logout')
      this.$router.push({ name: 'Login' })
    }
  },
  watch: {
    group () {
      this.drawer = false
    }
  }
}
</script>

<style scoped>

</style>
