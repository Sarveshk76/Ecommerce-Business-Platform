<template>
    <div>
      <v-img class="mt-10" height="60" src="~/assets/logo.png"></v-img>
    
    <div class="h-100 d-flex align-items-center justify-content-center">
      <v-progress-circular
      v-if="isLoading"
      indeterminate
      color="teal"
    ></v-progress-circular>
        <v-card elevation="3" v-else align="center" style="width: 350px;" color="teal" variant="outlined">
          <v-card-title>
            Register
          </v-card-title>
          
          <v-card-item>
            <v-text-field
              label="Email"
              varient="outlined"
              v-model="email"
            ></v-text-field>
            <v-text-field
              label="Password"
              varient="outlined"
              v-model="password"
              :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
              @click:append-inner="visible = !visible"
              :type="visible ? 'text' : 'password'"
            ></v-text-field>
          </v-card-item>

          <v-card-actions class="d-flex align-items-center justify-content-center">
            <v-btn @click="registerCustomer" variant="outlined">
              Register
            </v-btn>
          </v-card-actions>
          <div class="ma-3">
            <p class="text-subtitle-2">
                By continuing, you agree to our <a href="#" style="text-decoration: none;">Terms of Service</a> and <a href="#" style="text-decoration: none;">Privacy Policy</a>.
            </p>
            <v-divider></v-divider>
            <p class="mx-3 text-subtitle-2">New here?
              <v-btn variant="outlined" color="teal" @click="navigateTo('/login/customer')" >Login</v-btn>
            </p>
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
const email = ref('')
const password = ref('')
const visible = useState('false', ()=>false)
const isLoading = useState('isLoading',()=> true)
const snackbar = useState('snackbar',()=> false)
const text = useState('text',()=> '')
setTimeout(() => {
  isLoading.value = false
}, 1000);

  const registerCustomer = async () => {
    await axios.post('http://localhost:8001/accounts/api/v1/register/customer/', {
      email: email.value,
      password: password.value,
    }).then((response) => {
      console.log(response)
      snackbar.value = true
      text.value = 'Registered Successfully'
      navigateTo('/login/customer')
    }).catch((error) => {
      console.log(error)
      snackbar.value = true
      text.value = 'Something went wrong'
    })
  } 

</script>
