<template>
    <div class="Header">
      <v-overlay :value="drawer" z-index="4">
    </v-overlay>
        <v-app-bar color="teal" title="Ecom Biz Platform" :elevation="1" app clipped-left flat dark>
            

        <template v-slot:prepend>
          <v-app-bar-nav-icon  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        </template>


        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-cart-outline</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-account-outline</v-icon>
        </v-btn>
        </v-app-bar>
        <v-navigation-drawer v-model="drawer" app clipped flat dark expand-on-hover>
          <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
          <v-divider></v-divider>
          <v-list-item link title="List Item 1"></v-list-item>
          <v-list-item link title="List Item 2"></v-list-item>
          <v-list-item link title="List Item 3"></v-list-item>
        </v-navigation-drawer>
    </div>
</template>
<script>
export default{
  data: () => ({
    drawer: false
  })
}
</script>