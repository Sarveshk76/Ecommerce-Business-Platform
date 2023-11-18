<template>
  <div>
    <v-img class="mt-10" height="60" src="~/assets/logo.png"></v-img>

    <div class="h-100 d-flex align-items-center justify-content-center">
      <v-progress-circular
      v-if="isLoading"
      indeterminate
      color="teal"></v-progress-circular>
        <v-card v-else elevation="3" align="center" style="width: 350px;" color="teal" variant="outlined">
          <v-card-title>
            Login {{ $route.params.role }}
          </v-card-title>
          <div class="d-flex justify-content-start mx-3">
            <v-btn icon="mdi-arrow-left" color="teal" v-if="isEmail" @click="isEmail = false"></v-btn>
          </div>
          <v-card-item v-if="isEmail == false">
            <v-text-field
              label="Email"
              varient="outlined"
              v-model="email"
            ></v-text-field>
          </v-card-item>
          <v-card-item v-if="isEmail == true">
            <v-text-field
              label="Password"
              varient="outlined"
              v-model="password"
            ></v-text-field>
          </v-card-item>

          <v-card-actions class="d-flex align-items-center justify-content-center">
            <v-btn v-if="isEmail == false" @click="isEmail = !isEmail" variant="outlined">
              Continue
            </v-btn>
            <v-btn v-if="isEmail == true" @click="loginCustomer" variant="outlined">
              Login
            </v-btn>
          </v-card-actions>
          <div class="ma-3">
            <p class="text-subtitle-2">
                By continuing, you agree to our <a href="#" style="text-decoration: none;">Terms of Service</a> and <a href="#" style="text-decoration: none;">Privacy Policy</a>.
            </p>
            <v-divider></v-divider>
            <p class="mx-3 text-subtitle-2">New here? <v-btn variant="outlined" color="teal" @click="navigateTo('/register/customer')" style="text-decoration: none;">Register</v-btn></p>
          </div>

        </v-card>
    </div>
    <v-snackbar
      v-model="snackbar"
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="teal"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>
<script setup>
definePageMeta({
  layout: 'auth',
})
import { ref } from 'vue'
import axios from 'axios'
import { useTokenStore } from '@/stores/token';
const email = ref('')
const password = ref('')
const isEmail = useState('isEmail',()=> false)
const isLoading = useState('isLoading',()=> true)
const snackbar = useState('snackbar',()=> false)
const text = useState('text',()=> '')
setTimeout(() => {
  isLoading.value = false
}, 1000);
const token = useTokenStore()

const loginCustomer = async ()=>{
  axios.post('http://localhost:8001/accounts/api/v1/login/', {
  email: email.value,
  password: password.value
}).then((response) => {
  
  if (response.data.error){
    snackbar.value = true
    text.value = response.data.error
  }
  if (response.data.access){
    snackbar.value = true
    text.value = "Logged in successfully!!"
  }
  // navigateTo('/', {'token': response.data.access})
}).catch((error) => {
  console.log(error)
})
}
</script>
