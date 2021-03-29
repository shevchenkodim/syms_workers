<template>
  <v-container>
    <v-form>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
          style="color: #FFFFFF"
          class="d-flex justify-center"
        >
          <v-icon color="white">mdi-cart</v-icon>
          <h2 class="pl-2"><b>S Y M S</b></h2>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <v-text-field
            dark
            dense
            outlined
            label="Mobile phone"
            placeholder="Mobile phone"
            prepend-icon="mdi-cellphone-iphone"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <v-text-field
            dark
            dense
            outlined
            label="OTP-code"
            placeholder="OTP-code"
            prepend-icon="mdi-code-not-equal-variant"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <v-text-field
            dark
            dense
            outlined
            label="First Name"
            placeholder="First Name"
            prepend-icon="mdi-account"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <v-text-field
            dark
            dense
            outlined
            label="Last Name"
            placeholder="Last Name"
            prepend-icon="mdi-account"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <v-text-field
            dark
            dense
            outlined
            label="Email Address"
            placeholder="Email Address"
            prepend-icon="mdi-email-variant"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <v-text-field
            dark
            dense
            outlined
            label="Password"
            placeholder="Password"
            prepend-icon="mdi-pencil"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="d-flex justify-center"
      >
        <v-col
          cols="4"
          class="d-flex justify-end"
        >
          <v-btn>
            Sign in
          </v-btn>
        </v-col>
      </v-row>

      <AuthOverlay :isLoading="isProductsLoading"></AuthOverlay>

    </v-form>
  </v-container>
</template>

<script>
import AuthOverlay from '@/components/ThirdParty/LoaderOverlay'

export default {
  name: 'Auth',
  components: { AuthOverlay },
  data: () => ({
    isProductsLoading: false
  })
}
</script>

<style scoped>

</style>
