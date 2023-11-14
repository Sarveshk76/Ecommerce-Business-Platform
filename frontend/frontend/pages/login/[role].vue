<template>
    <div class="h-100 d-flex align-items-center justify-content-center">
        <v-card elevation="3" align="center" style="width: 350px;" color="teal" variant="outlined">
          <v-card-title>
            Login {{ $route.params.role }}
          </v-card-title>
          <v-card-item v-if="isEmail == false">
            <v-text-field
              label="Email or Mobile Number"
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
            <v-btn @click="isEmail = !isEmail" variant="outlined">
              Continue
            </v-btn>
          </v-card-actions>
          <div class="ma-3">
            <p class="text-subtitle-2">
                By continuing, you agree to our <a href="#" style="text-decoration: none;">Terms of Service</a> and <a href="#" style="text-decoration: none;">Privacy Policy</a>.
            </p>
            <v-divider></v-divider>
            <p class="mx-3 text-subtitle-2">New here? <a href="#" style="text-decoration: none;">Register</a></p>
          </div>

        </v-card>
    </div>
</template>
<script setup>
definePageMeta({
  layout: 'auth',
})
import { ref } from 'vue'
const email = ref('')
const isEmail = useState('isEmail',()=> false)

</script>
