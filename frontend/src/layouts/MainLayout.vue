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

        <v-form @submit.prevent="doSearchProduct">
          <v-text-field
            v-if="showSearch"
            flat
            dense
            rounded
            hide-details
            label="..."
            prepend-inner-icon="mdi-magnify"
            solo-inverted
            v-model="searchValue"
          ></v-text-field>
        </v-form>

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
                  <v-col cols="auto" class="pl-0">
                    <v-dialog
                      transition="dialog-top-transition"
                      max-width="600"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          class="mx-2"
                          fab
                          dark
                          small
                          color="info"
                          @click="doOpenClientSettings"
                          v-bind="attrs"
                          v-on="on"
                        >
                          <v-icon>mdi-tools</v-icon>
                        </v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar
                            color="primary"
                            dark
                          >
                            Налаштування профілю
                          </v-toolbar>
                          <v-card-text>
                            <form @submit.prevent="doSaveClientDetail">
                              <input type="submit" hidden>
                              <v-row class="mt-3">
                                <v-col cols="6">
                                  <v-text-field
                                    label="Email"
                                    type="email"
                                    disabled
                                    dense
                                    outlined
                                    clearable
                                    hide-details="auto"
                                    placeholder="..."
                                    v-model="clientDetailForm.email"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="6">
                                  <v-text-field
                                    label="Номер телефону"
                                    type="text"
                                    disabled
                                    dense
                                    outlined
                                    clearable
                                    hide-details="auto"
                                    placeholder="..."
                                    v-model="clientDetailForm.phone"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="6">
                                  <v-text-field
                                    label="Прізвище"
                                    type="text"
                                    dense
                                    outlined
                                    clearable
                                    hide-details="auto"
                                    placeholder="..."
                                    v-model="clientDetailForm.last_name"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="6">
                                  <v-text-field
                                    label="Ім'я"
                                    type="text"
                                    dense
                                    outlined
                                    clearable
                                    hide-details="auto"
                                    placeholder="..."
                                    v-model="clientDetailForm.first_name"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="12">
                                  <v-checkbox
                                    v-model="clientDetailForm.need_update_password"
                                    label="Встановити новий пароль"
                                  ></v-checkbox>
                                  <v-text-field
                                    label="Пароль"
                                    type="password"
                                    autocomplete="on"
                                    :disabled="!clientDetailForm.need_update_password"
                                    dense
                                    outlined
                                    clearable
                                    hide-details="auto"
                                    placeholder="*******"
                                    v-model="clientDetailForm.password"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="12">
                                  <v-file-input
                                    label="Фото"
                                    truncate-length="15"
                                    v-model="clientDetailForm.file"
                                  ></v-file-input>
                                </v-col>
                              </v-row>
                            </form>
                          </v-card-text>
                          <v-card-actions class="justify-space-between">
                            <v-btn
                              text
                              @click="dialog.value = false"
                            >
                              Вийти
                            </v-btn>
                            <v-btn
                              @click="doSaveClientDetail"
                              class="primary"
                            >
                              <v-icon>mdi-check-all</v-icon>
                              Зберегти
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
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
                  <v-list-item-title>
                    <v-col cols="auto" class="pl-0">
                      <v-dialog
                        transition="dialog-top-transition"
                        max-width="600"
                        scrollable
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <span
                            @click="doOpenHistoryOrders"
                            v-bind="attrs"
                            v-on="on"
                          >
                            Історія замовленнь
                          </span>
                        </template>
                        <template v-slot:default="dialogHistory">
                          <v-card>
                            <v-toolbar
                              color="primary"
                              dark
                            >
                              Історія замовленнь
                            </v-toolbar>
                            <v-card-text style="height: 450px; padding-top: 20px">
                              <v-row v-for="(h, index) in orderHistory" :key="index + '_hist_ord'">
                                <v-col cols="1 d-flex align-center justify-center">
                                  <b>№{{ index + 1 }}</b>
                                </v-col>
                                <v-col cols="11">
                                  <v-row>
                                    <v-col cols="12 pb-1" class="d-flex justify-space-between">
                                     <span><b>Сума:</b> {{ h.total_amount }} грн.</span>
                                     <span><b>Дата:</b> {{ h.created_at }}</span>
                                    </v-col>
                                    <v-col cols="12 pt-1">
                                      <span v-for="(p, ind) in h.products" :key="index + '_y_' + ind">
                                        {{ p }}
                                        <span v-if="ind + 1 < h.products.length">, </span>
                                      </span>
                                    </v-col>
                                  </v-row>
                                </v-col>
                              </v-row>
                            </v-card-text>
                            <v-card-actions class="justify-end">
                              <v-btn
                                text
                                @click="dialogHistory.value = false"
                              >
                                Вийти
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </template>
                      </v-dialog>
                    </v-col>
                  </v-list-item-title>
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
    dialog: false,
    dialogHistory: false,
    drawer: false,
    showSearch: true,
    searchValue: '',
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
    ],
    orderHistory: [],
    clientDetailForm: {
      first_name: '',
      last_name: '',
      phone: '',
      email: '',
      image: '',
      file: null,
      need_update_password: false,
      password: ''
    }
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
      // this.$router.push('/cart')
      window.location.replace('/cart')
    },
    doOpenHistoryOrders () {
      this.orderHistory = []
      this.$store.dispatch('common/loadOrderHistory')
        .then(resp => {
          this.orderHistory = resp.data
        })
    },
    doOpenClientSettings () {},
    doLoadClientDetailInfo () {
      this.$store.dispatch('user/loadUserDetail')
        .then(({ data }) => {
          this.$store.commit('user/setUserDetail', data)
          this.clientDetailForm = Object.assign(this.clientDetailForm, data)
        })
        .catch(() => {})
        .finally(() => {
          this.$store.commit('user/getUserDetailInitEnd')
        })
    },
    doSaveClientDetail () {
      var fData = new FormData()

      fData.append('first_name', this.clientDetailForm.first_name)
      fData.append('last_name', this.clientDetailForm.last_name)
      fData.append('need_update_password', this.clientDetailForm.need_update_password)
      fData.append('password', this.clientDetailForm.password)
      fData.append('file', this.clientDetailForm.file)

      this.$store.dispatch('user/saveUserDetail', fData)
        .then(resp => {
          if (resp.status === 200) {
            console.log(resp.data)
            if (resp.data.error) {
              this.$toastr('error', resp.data.error)
            } else {
              this.doLoadClientDetailInfo()
              this.$forceUpdate()
            }
          }
        })
        .catch(() => {})
        .finally(() => {
          this.$store.commit('user/getUserDetailInitEnd')
        })
    },
    doSearchProduct () {
      // this.$router.push(`/search/${this.searchValue}`)
      window.location.replace(`/search/${this.searchValue}`)
    }
  },
  created () {
    this.doCheckShowSearchInput()
    this.$store.dispatch('common/loadCategories')
    this.doLoadClientDetailInfo()
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
