import { defineNuxtPlugin } from '#app'
import { createVuetify } from 'vuetify'
import '@mdi/font/css/materialdesignicons.css'
// make sure to also import the coresponding css


// Import everything
// import * as components from 'vuetify/components'

export default defineNuxtPlugin((nuxtApp) => {
   const vuetify = createVuetify({
    icons: {
      defaultSet: 'mdi',
      
    },
   })
   nuxtApp.vueApp.use(vuetify)
})