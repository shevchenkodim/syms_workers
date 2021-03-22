<template>
  <v-container>
    <div>
      <div class="d-flex justify-center p-t-10 p-b-10" style="color: #FFFFFF">
        <v-icon color="white">mdi-cart</v-icon>
        <h2 class="pl-2"><b>S Y M S</b></h2>
      </div>
      <div class="d-flex justify-center m-t-10">
        <div class="col-lg-4 col-md-6 col-sm-12 text-center p-b-20">
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
            <input type="passwowasdrd"
                   class="form-control form-control-lg"
                   placeholder="Passwasdord"
                   aria-label="Paasdssword"
                   aria-describedby="basic-addon1"
            >
          </div>
        </div>
      </div>
      <div class="d-flex justify-center">
        <div class="col-lg-4 col-md-6 col-sm-12 text-center">
          <div class="input-group p-t-20 mr-2">
            <button class="btn btn-success"
                    type="button">
              Вхід
            </button>
           <button class="btn btn-success"
                   type="button">
              Регистрация
            </button>
          </div>
        </div>
      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'Auth',
  data: () => ({})
}
</script>

<style scoped>

</style>
