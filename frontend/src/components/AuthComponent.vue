<template>
  <v-container>
     <div class="auth-wrapper d-flex justify-content-center align-items-center bg-dark">
        <div class="auth-box bg-dark border-top border-secondary">
            <div id="loginform">
                <div class="text-center p-t-10 p-b-10">
                    <h2 class="text-white">
                        <b class="logo-icon p-l-10">
                            <i class="fab fa-opencart"></i>
                        </b>
                        <b>S Y M S</b>
                    </h2>
                </div>
                <!-- Form -->
                <div class="form-horizontal m-t-10">
                    <div class="row p-b-20">
                        <div class="col-12">
                            <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                    <span class="input-group-text bg-info text-white">
                                        <i class="ti-mobile"></i>
                                    </span>
                                </div>
                                <input type="text"
                                       class="form-control form-control-lg mr-1"
                                       placeholder="Mobile phone"
                                       aria-label="Mobile phone"
                                       aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                    <span class="input-group-text bg-primary text-white">
                                        <i class="fas fa-code"></i>
                                    </span>
                                </div>
                                <input type="text"
                                       class="form-control form-control-lg mr-1"
                                       placeholder="OTP-code"
                                       aria-label="OTP-code"
                                       aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                    <span class="input-group-text bg-success text-white">
                                        <i class="fas fa-user"></i>
                                    </span>
                                </div>
                                <input type="text"
                                       class="form-control form-control-lg mr-1"
                                       placeholder="First Name"
                                       aria-label="First Name"
                                       aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                    <span class="input-group-text bg-success text-white">
                                        <i class="fas fa-user-plus"></i>
                                    </span>
                                </div>
                                <input type="text"
                                       class="form-control form-control-lg mr-1"
                                       placeholder="Last Name"
                                       aria-label="Last Name"
                                       aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                    <span class="input-group-text bg-danger text-white" id="basic-addon1">
                                        <i class="ti-email"></i>
                                    </span>
                                </div>
                                <input type="email"
                                       class="form-control form-control-lg"
                                       placeholder="Email Address"
                                       aria-label="Username"
                                       aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                    <span class="input-group-text bg-warning text-white" id="basic-addon2">
                                        <i class="ti-pencil"></i>
                                    </span>
                                </div>
                                <input type="password"
                                       class="form-control form-control-lg"
                                       placeholder="Password"
                                       aria-label="Password"
                                       aria-describedby="basic-addon1">
                            </div>

<!--                            <div v-if="state.auth.loading"-->
<!--                                 class="overlay text-center text-white">-->
<!--                                <i class="fas fa-2x fa-sync-alt fa-spin"></i>-->
<!--                            </div>-->

                        </div>
                    </div>
                    <div class="row border-top border-secondary">
                        <div class="col-12">
                            <div class="form-group">
                                <div class="p-t-20 d-flex justify-content-end">
                                    <button class="btn btn-success"
                                            type="button">
                                        Вхід
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

  </v-container>
</template>

<script>
// import Vue from 'vue'

export default {
  name: 'Auth',
  data: () => ({
    urls: {
      do_client_auth: "{% url 'client_api:auth' %}",
      do_client_auth_init: "{% url 'client_api:auth_init' %}",
    },
    data: {
      contactCSRF: '',
      data: {
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        phone: '',
        otp_code: ''
      },
      state__: {
        step: 'FIRST',
        otp: false,
        otp_editable: false,
        first_name: false,
        first_name_editable: false,
        last_name: false,
        last_name_editable: false,
        email: false,
        email_editable: false,
        password: false,
        password_editable: false,
        phone: true,
        phone_editable: true
      }
    },
    state: {
      loading: false
    }
  })
  // methods: {
  //   axios_post (_url, _body = {}) {
  //     const headers = {
  //       'X-CSRFToken': this.data.contactCSRF
  //     }
  //     return Vue.axios({
  //       method: 'POST',
  //       url: _url,
  //       data: _body,
  //       headers: headers
  //     })
  //   },
  //   axios_get (_url) {
  //     return Vue.axios({
  //       method: 'GET',
  //       url: _url
  //     })
  //   },
  //   render_star_rating(value) {
  //     let html = ''
  //     const star = '<i class="fas fa-star text-warning"></i>'
  //     const star_empty = '<i class="far fa-star text-warning"></i>'
  //     const list_stars = [1, 2, 3, 4, 5]
  //     for (let item in list_stars) {
  //       if (list_stars[item] <= value) {
  //         html += star
  //       } else {
  //         html += star_empty
  //       }
  //     }
  //     return html
  //   },
  //   do_client_auth () {
  //     this.state.auth.loading = true
  //
  //     this.axios_post(this.urls.do_client_auth, this.data.auth.data)
  //       .then(resp => {
  //         if (resp.status === 200) {
  //           if (resp.data.state) {
  //             this.do_update_auth_state(resp.data.state)
  //           }
  //           if (resp.data.parameters) {
  //             this.do_update_auth_parameters(resp.data.parameters)
  //           }
  //           if (resp.data.errors && resp.data.errors.message) {
  //             toastr.error(resp.data.errors.message)
  //           }
  //           if (resp.data.status === 'ok') {
  //             window.location.replace(resp.data.redirect)
  //           }
  //         }
  //       }).catch(() => {
  //
  //       }).finally(() => {
  //         this.state.auth.loading = false
  //       })
  //   },
  //   do_client_auth_init() {
  //     this.axios_get(this.urls.do_client_auth_init)
  //   },
  //   do_update_auth_state(new_state) {
  //     for(let key in new_state) {
  //       this.data.auth.__state__[key] = new_state[key]
  //     }
  //   },
  //   do_update_auth_parameters(parameters) {
  //     for(let key in parameters) {
  //       this.data.auth.data[key] = parameters[key]
  //     }
  //   }
  // }
}
</script>

<style scoped>

</style>
