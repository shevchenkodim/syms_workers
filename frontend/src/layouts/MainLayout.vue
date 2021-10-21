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
            <router-link
              :to="{ path: `/`}"
              style="text-decoration: none; color: white;"
            >
              <b> SYMS</b>
            </router-link>
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-text-field
          v-if="showSearch"
          flat
          dense
          rounded
          hide-details
          label="..."
          prepend-inner-icon="mdi-magnify"
          solo-inverted
        ></v-text-field>

        <v-spacer></v-spacer>

<!--        <v-menu-->
<!--          v-model="notifications"-->
<!--          :close-on-content-click="false"-->
<!--          :nudge-width="200"-->
<!--          offset-x-->
<!--          bottom-->
<!--        >-->
<!--          <template v-slot:activator="{ on, attrs }">-->
<!--            <v-btn-->
<!--              icon-->
<!--              dark-->
<!--              v-bind="attrs"-->
<!--              v-on="on"-->
<!--            >-->
<!--              <v-icon>mdi-bell-outline</v-icon>-->
<!--            </v-btn>-->
<!--          </template>-->

<!--          <v-card>-->
<!--            <v-list>-->
<!--              <v-list-item>-->
<!--                <v-list-item-content>-->
<!--                  View read (5)-->
<!--                </v-list-item-content>-->

<!--                <v-list-item-action>-->
<!--                  <v-btn-->
<!--                    fab-->
<!--                    small-->
<!--                  >-->
<!--                    <v-icon>mdi-email-open</v-icon>-->
<!--                  </v-btn>-->
<!--                </v-list-item-action>-->
<!--              </v-list-item>-->
<!--            </v-list>-->

<!--            <v-divider></v-divider>-->

<!--            <v-list three-line>-->
<!--              <template v-for="(item, index) in notification_items">-->
<!--                <v-subheader-->
<!--                  v-if="item.header"-->
<!--                  :key="item.header"-->
<!--                  v-text="item.header"-->
<!--                ></v-subheader>-->

<!--                <v-divider-->
<!--                  v-else-if="item.divider"-->
<!--                  :key="index"-->
<!--                  :inset="item.inset"-->
<!--                ></v-divider>-->

<!--                <v-list-item-->
<!--                  v-else-->
<!--                  :key="item.title"-->
<!--                >-->
<!--                  <v-list-item-avatar>-->
<!--                    <v-img :src="item.avatar"></v-img>-->
<!--                  </v-list-item-avatar>-->

<!--                  <v-list-item-content>-->
<!--                    <v-list-item-title v-html="item.title"></v-list-item-title>-->
<!--                    <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>-->
<!--                  </v-list-item-content>-->
<!--                </v-list-item>-->
<!--              </template>-->
<!--            </v-list>-->
<!--          </v-card>-->
<!--        </v-menu>-->

        <v-btn
          icon
          @click="do_go_to_cart"
        >
          <v-icon>mdi-cart-outline</v-icon>
          <span v-if="cartItemsCount > 0"
                class="green--text"
          >
            {{ cartItemsCount }}
          </span>
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
                    :src="userData.image ? (backendUrl + userData.image) : 'https://avatars.githubusercontent.com/u/16786985?s=460&u=9f2fe771bbc8bcfcc195fde83ca914b00a98da54&v=4'"
                    alt="avatars"
                  >
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>
                    {{userData.last_name}} {{userData.first_name}}
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    {{userData.email}}
                  </v-list-item-subtitle>
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
                <v-list-item-action @click="do_go_to_cart">
                  <v-icon>mdi-cart-outline</v-icon>
                </v-list-item-action>
                <v-list-item-title @click="do_go_to_cart">
                  Кошик ({{ cartItemsCount }})
                </v-list-item-title>
              </v-list-item>

              <v-list-item>
                <v-list-item-action>
                  <v-icon>mdi-heart-outline</v-icon>
                </v-list-item-action>
                <v-list-item-title>Список бажаннь</v-list-item-title>
              </v-list-item>

              <v-list-item>
                <v-list-item-action>
                  <v-icon>mdi-history</v-icon>
                </v-list-item-action>
                <v-list-item-title>Історія замовленнь</v-list-item-title>
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
        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi mdi-format-list-bulleted-square</v-icon>
          </v-list-item-icon>
          <v-list-item-title>
            <b>
              Категорії товарів
            </b>
          </v-list-item-title>
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
            <div
              v-for="category in allCategories"
              :key="category.id"
            >
              <v-list-item
                v-if="!category.children.length"
              >
                <v-list-item-icon>
                  <v-icon>
                    {{category.icon}}
                  </v-icon>
                </v-list-item-icon>
                <v-list-item-title>
                  <router-link
                    :to="{ path: `/category/${category.code_name}`}"
                    style="text-decoration: none; color: white;"
                  >
                    {{category.name}}
                  </router-link>
                </v-list-item-title>
              </v-list-item>

              <v-list-group
                v-else
                :value="true"
                :prepend-icon="category.icon"
              >
                <template v-slot:activator>
                  <v-list-item-title>
                    {{category.name}}
                  </v-list-item-title>
                </template>

                <v-list-item
                  v-for="child in category.children"
                  :key="child.id"
                  class="pl-2"
                >
                  <v-list-item-icon>
                    <v-icon
                      class="pl-1"
                      :small=true
                    >
                      {{child.icon}}
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>
                    <router-link
                      :to="{ path: `/category/${child.code_name}`}"
                      style="text-decoration: none; color: white;"
                    >
                      {{child.name}}
                    </router-link>
                  </v-list-item-title>
                </v-list-item>
              </v-list-group>
              <v-divider></v-divider>
            </div>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </div>

    <v-main>
      <v-container>
        <router-view />
      </v-container>

      <v-container>
        <v-row>
          <v-col cols="4">
            <div class="d-flex justify-center align-center pb-2">
              <b>Приєднуйтеся до наших соц. мереж</b>
            </div>
            <div class="d-flex justify-center align-center">
              <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/1024px-Facebook_Logo_%282019%29.png" class="mr-1">
              <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png" class="ml-1 mr-1">
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
              <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Facebook_Messenger_logo_2020.svg/768px-Facebook_Messenger_logo_2020.svg.png" class="mr-1">
              <img width="36" src="https://f0.pngfuel.com/png/322/453/viber-application-png-clip-art.png" class="ml-1 mr-1">
              <img width="36" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/600px-Telegram_logo.svg.png" class="ml-1 mr-1">
            </div>
          </v-col>
        </v-row>

        <v-row class="pb-3">
          <v-col cols="3" v-for="(info, index) in infoCards" :key="index">
            <v-card
              outlined
            >
              <v-card-title class="blue-grey lighten-2"
                            v-text="info.title"
              ></v-card-title>
              <v-card-text>
                <v-list>
                  <v-item v-for="(item, ind) in info.items"
                          :key="ind"
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
      </v-container>

    </v-main>

    <v-footer
      app
      dark
      class="d-flex justify-center"
    >
      Developed by
      <a href="https://www.instagram.com/dmytro.shevchenko.dev/"
         target="_blank"
         class="pl-2"
      >
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
      isAuthenticated: 'auth/isAuthenticated',
      allCategories: 'common/getAllCategories',
      userData: 'user/getUserData',
      backendUrl: 'home/getBackendUrl',
      cartItemsCount: 'cart/getCartCount'
    })
  },
  data: () => ({
    drawer: true,
    showSearch: true,
    menu: false,
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
    ]
  }),
  methods: {
    doCheckShowSearchInput () {
      this.showSearch = window.innerWidth >= 600
      this.$forceUpdate()
    },
    logout () {
      this.$store.dispatch('auth/logout')
      this.$router.push({ name: 'Login' })
    },
    do_go_to_cart () {
      window.location.replace('/cart')
      // this.$router.push({ name: 'Cart' })
    }
  },
  created () {
    this.doCheckShowSearchInput()
    this.$store.dispatch('common/loadCategories')
    this.$store.dispatch('user/loadUserDetail')
  },
  watch: {
    group () {
      // this.drawer = false
    }
  }
}
</script>

<style scoped>

</style>
