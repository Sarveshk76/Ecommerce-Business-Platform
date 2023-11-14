import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: [
    'bootstrap/dist/css/bootstrap.min.css',
    'vuetify/lib/styles/main.sass',
    "@mdi/font/css/materialdesignicons.css",
  ],
  modules: [
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
    '@pinia/nuxt',
    //...
  ],
  build: {
    transpile: ['vuetify']
},
  vite: {
    define: {
      "process.env.DEBUG": false,
    },
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
});
