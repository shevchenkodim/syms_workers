<template>
  <v-container>
    <v-form v-on:submit="signIn()">
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
        v-if="authForm.phone.show"
        class="d-flex justify-center"
      >
        <v-col
          lg="4"
          md="6"
          sm="6"
          cols="12"
        >
          <!--clearable-->
          <v-text-field
            dark
            dense
            outlined
            label="Mobile phone"
            placeholder="Mobile phone"
            prepend-icon="mdi-cellphone-iphone"
            v-model="authForm.phone.value"
            v-mask="'+38(0##)###-##-##'"
            :disabled="!authForm.phone.editable"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        v-if="authForm.otpCode.show"
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
            v-model="authForm.otpCode.value"
            v-mask="'####'"
            :disabled="!authForm.otpCode.editable"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        v-if="authForm.firstName.show"
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
            v-model="authForm.firstName.value"
            :disabled="!authForm.firstName.editable"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        v-if="authForm.lastName.show"
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
            v-model="authForm.lastName.value"
            :disabled="!authForm.lastName.editable"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        v-if="authForm.email.show"
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
            v-model="authForm.email.value"
            :disabled="!authForm.email.editable"
            type="email"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        v-if="authForm.password.show"
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
            type="password"
            v-model="authForm.password.value"
            :disabled="!authForm.password.editable"
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
          <v-btn
            type="submit"
            @click.prevent="signIn()"
          >
            Sign in
          </v-btn>
        </v-col>
      </v-row>

      <AuthOverlay :isLoading="isAuthLoading"></AuthOverlay>

    </v-form>
  </v-container>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import AuthOverlay from '@/components/ThirdParty/LoaderOverlay'

export default {
  name: 'Auth',
  components: { AuthOverlay },
  data: () => ({
    authForm: {
      step: 'FIRST',
      phone: {
        value: null,
        show: true,
        editable: true
      },
      email: {
        value: null,
        show: false,
        editable: false
      },
      lastName: {
        value: null,
        show: false,
        editable: false
      },
      firstName: {
        value: null,
        show: false,
        editable: false
      },
      otpCode: {
        value: null,
        show: false,
        editable: false
      },
      password: {
        value: null,
        show: false,
        editable: false
      }
    }
  }),
  computed: {
    ...mapGetters('auth', ['isAuthLoading']),
    ...mapMutations('auth', ['initSuccess', 'initEnd', 'authenticationError'])
  },
  methods: {
    signIn () {
      this.$store.dispatch('auth/signIn', { ...this.authForm })
        .then(({ data }) => {
          if (!data.success) {
          } else if (data.response.access && data.response.refresh) {
            this.$store.commit('auth/initSuccess', data.response)
            this.$router.push({ name: 'Home' })
          } else {
            this.updateFormData(data.response)
          }
        })
        .catch(() => {
        })
        .finally(() => {
          this.$store.commit('auth/initEnd')
        })
    },
    updateFormData (data) {
      for (const i in data) {
        this.authForm[i] = data[i]
      }
    }
  }
}
</script>

<style scoped>
</style>
