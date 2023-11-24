<template>
    <div class="Header">
      <v-overlay :value="drawer" z-index="4">
    </v-overlay>
        <v-app-bar color="teal" title="Ecom Biz Platform" :elevation="1" app clipped-left flat dark>
            
        <template v-slot:prepend>
          <v-app-bar-nav-icon  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        </template>

        <v-spacer></v-spacer>

        <v-dialog
        transition="dialog-top-transition"
        width="auto"
      >
        <template v-slot:activator="{ props }">
          <v-btn v-bind:="props" icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        </template>
        <template v-slot:default="{ isActive }">
          <v-card width="800" height="400">
            <v-card-title class="text-center">Search Products</v-card-title>
            <v-card-text>
              <v-row align="center">
                <v-text-field
                v-model="search"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
              <v-btn rounded="3" class="mx-2" color="teal" icon>
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
              </v-row>

            </v-card-text>
          </v-card>
        </template>
      </v-dialog>

        <v-btn icon>
          <v-icon>mdi-cart-outline</v-icon>
        </v-btn>

        <v-menu width="200">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" icon>
          <v-icon>mdi-account-outline</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-if="authenticated"
          v-for="(item, index) in items"
          :key="index"
          :value="index"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
        <v-list-item class="text-center"> 
          <v-btn color="yellow">Sign In</v-btn>
          <br>
          <v-list-text>new customer?</v-list-text>
        </v-list-item>
      </v-list>
    </v-menu>
        </v-app-bar>
        <v-navigation-drawer
        v-model="drawer"
        temporary
      >
      <v-divider></v-divider>
          <v-card-title class="text-h6">Trending</v-card-title>
          <v-list-item link title="Best Sellers"></v-list-item>
          <v-list-item link title="New Releases"></v-list-item>
          <v-divider></v-divider>
          <v-card-title class="text-h6">Shop By Categories</v-card-title>
          <v-list-item link title="Category 1"></v-list-item>
          <v-list-item link title="Category 2"></v-list-item>
          <v-divider></v-divider>
      </v-navigation-drawer>
    </div>
</template>
<script>
export default{
  data: () => ({
    authenticated: false,
    drawer: false,
    items: [
      { title: 'Profile' },
      { title: 'Settings' },
      { title: 'Logout' },
    ],
  })
}
</script>