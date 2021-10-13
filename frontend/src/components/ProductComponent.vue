<template>
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <h2>Apple iPhone 12 Pro</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-row class="d-flex justify-center">
            <v-col cols="12">
              <Carousel
                :items-images="productImages"
                :media_url="mediaBase"
                :height="600"
              ></Carousel>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <h2>Короткі характеристики</h2>
              <p>
                Экран (6.1", OLED (Super Retina XDR), 2532x1170) /
                Apple A15 Bionic / тройная основная камера: 12 Мп + 12 Мп + 12 Мп,
                фронтальная камера: 12 Мп / 1 ТБ встроенной памяти / 3G / LTE / 5G / GPS / Nano-SIM / iOS 15
              </p>
            </v-col>
            <v-col cols="12">
              <h2>Опис товару</h2>
            </v-col>
            <v-col cols="12" class="pt-0">
              <h3>Потрясающий экран и плавный просмотр контента</h3>
              <p>
                Насладитесь детальным изображением на Super AMOLED 6.4'' Infinity-U экране с разрешением FHD+ и
                яркостью до 800 нит, которое отлично видно даже при ярком дневном свете. Функция защиты глаз Eye
                Comfort Shield снижает уровень синего свечения, а сверхплавная прокрутка обеспечивает комфортный
                просмотр во время игрового сеанса или скроллинга изображения на экране.
              </p>
            </v-col>
            <v-col cols="12" class="pt-0">
              <h3>Минималистичный и элегантный дизайн</h3>
              <p>
                Galaxy A32 отлично выглядит и его комфортно держать в руке.
                Необычный дизайн камеры и блестящая текстура задней панели выделяют этот смартфон среди других.
                Смартфон выполнен в трех цветах: черный, лавандовый и синий.
              </p>
            </v-col>
            <v-col cols="12" class="pt-0">
              <h3>Потрясающая камера</h3>
              <p>
                Четыре AI камеры Galaxy A32 поднимают уровень качества фото на новую высоту.
                Делайте сверхчёткие снимки на 64 мегапиксельную основную камеру.
                Расширьте поле зрения камеры с помощью сверхширокоугольной камеры.
                Управляйте резкостью камеры с датчиком глубины или снимите детали объекта съемки с помощью макрокамеры.
              </p>
            </v-col>
            <v-col cols="12">
              <h2>Характеристики</h2>
              <v-list dense light>
                <v-list-item-group>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title class="d-flex justify-space-between">
                        <span>Разрешение дисплея</span>
                        <span>2400 x 1080</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>

                  <v-divider></v-divider>

                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title class="d-flex justify-space-between">
                        <span>Оперативная память</span>
                        <span>4 ГБ</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>

                  <v-divider></v-divider>

                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title class="d-flex justify-space-between">
                        <span>Встроенная память</span>
                        <span>64 ГБ</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <h2>Відгуки</h2>
            </v-col>
            <v-col cols="12">
              <v-list three-line>
                <template v-for="(v, i) in [1, 2, 3]">
                  <v-divider :key="i"></v-divider>

                  <v-subheader :key="i">
                    <v-row>
                      <v-col cols="12" class="d-flex justify-space-between pb-0 pt-0">
                        <span><b>Dmytro Shevchenko</b></span>
                        <span>
                          <v-rating
                            :value="4"
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

                  <v-list-item :key="i">
                    <v-list-item-avatar>
                      <v-img src="https://cdn-icons-png.flaticon.com/512/149/149071.png"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>
                        Some comment, some comment, some comment, some comment
                      </v-list-item-title>
                      <v-list-item-subtitle class="d-flex align-center justify-space-between">
                        <span>
                          <v-btn
                            icon
                            color="green"
                            class="mr-1"
                          >
                            <v-icon>mdi-thumb-up</v-icon>
                            4
                          </v-btn>
                          <v-btn
                            icon
                            color="error"
                            class="ml-1"
                          >
                            <v-icon>mdi-thumb-down</v-icon>
                            7
                          </v-btn>
                        </span>
                        <span class="text-muted">
                          27.09.2021 15.05
                        </span>
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </template>
              </v-list>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-row>
            <v-col cols="12">
              <h4>Код: 0000000001</h4>
            </v-col>
            <v-col cols="12 pt-0 pb-0 d-flex justify-content-start align-items-center">
              <v-rating
                :value="3"
                color="amber"
                dense
                half-increments
                readonly
                size="20"
              ></v-rating>
              <div class="grey--text ml-4">
                8 відгуків
              </div>
            </v-col>
            <v-col cols="12">
              <v-chip
                class="green"
                dark
              >
                <v-icon>
                  mdi-check-bold
                </v-icon>
                Є в наявності
              </v-chip>
            </v-col>
            <v-col cols="12">
              <v-row>
                <v-col cols="6">
                  <b style="color: black;">
                    <strike>
                      19500 грн.
                    </strike>
                  </b>
                  <b class="text-muted"
                     style="color: red;"
                  >
                    <h3>18500 грн.</h3>
                  </b>
                </v-col>
                <v-col cols="6" class="d-flex align-center justify-center">
                  <v-btn class="green" dark>
                    <v-icon>mdi-cart-outline</v-icon>
                    Купити
                  </v-btn>
                  <v-btn icon class="ml-5">
                    <v-icon>mdi-heart-outline</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="12">
              <v-card class="secondary" dark>
                <v-img
                  src="https://picsum.photos/350/165?random"
                  height="170"
                  class="grey darken-4"
                ></v-img>
                <v-card-title class="text-h6 d-flex justify-center">
                  Інтернет-магазин "Active life"
                </v-card-title>
                <v-card-text class="white mb-0 pb-0">
                  <v-list dense light>
                    <v-list-item-group>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-link-variant</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Сторінка продавця
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-google-maps</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Місце знаходження: м.Київ, Зочих 28
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-phone</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            +380000000000
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-email-fast</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            activelife@gmail.com
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card class="green" dark>
                <v-card-title class="text-h6">
                  Доступні способи доставки
                </v-card-title>
                <v-card-text class="white mb-0 pb-0">
                  <v-list dense light>
                    <v-list-item-group>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-hoop-house</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Самовивіз з магазину
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-map-marker-distance</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Самовивіз з Нової Пошти
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-google-maps</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Самовивіз з УкрПошти
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-shopping-outline</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Самовивіз з Justin
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-truck-delivery-outline</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Доставка від продавця
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card class="warning" dark>
                <v-card-title class="text-h6">
                  Гарантія
                </v-card-title>
                <v-card-text class="white mb-0 pb-0">
                  <v-list dense light>
                    <v-list-item-group>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-security</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            12 місяців
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-update</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Обмін/повернення товару впродовж 14 днів
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card class="info" dark>
                <v-card-title class="text-h6">
                  Способи оплати
                </v-card-title>
                <v-card-text class="white mb-0 pb-0">
                  <v-list dense light>
                    <v-list-item-group>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-cash</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Готівкою
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-credit-card-multiple</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Оплата картою Visa
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-credit-card-multiple-outline</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            Оплата картою MasterCard
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                    </v-list-item-group>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import Carousel from '@/components/ThirdParty/Carousel'
export default {
  name: 'ProductComponent',
  components: { Carousel },
  props: ['product_code'],
  data: () => ({
    mediaBase: 'https://content1.rozetka.com.ua/',
    productImages: [
      { item_image: 'goods/images/big/221250977.jpg' },
      { item_image: 'goods/images/big/221250974.jpg' },
      { item_image: 'goods/images/big/221022193.jpg' },
      { item_image: 'goods/images/big/221250972.jpg' }
    ]
  })
}
</script>

<style scoped>

</style>
