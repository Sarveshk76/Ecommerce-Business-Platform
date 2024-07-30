<template>
    <div class="Header">
      <v-overlay :value="drawer" location="">
    </v-overlay>
        <v-app-bar :order="1" color="teal" title="Ecom Biz Platform" :elevation="1" app clipped-left flat dark>
            
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
      <v-list v-if="authenticated">
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          :value="index"
        >
          <v-list-item-title @click=item.onClick>{{ item.title }}</v-list-item-title>
        </v-list-item>
        </v-list>
        <v-list v-else>
        <v-list-item  class="text-center"> 
          <v-btn color="yellow">Sign In</v-btn>
          <br>
          <p>new customer?</p>
        </v-list-item>
      </v-list>
    </v-menu>
        </v-app-bar>
        <v-navigation-drawer
        v-model="drawer"
        temporary
        app
      >
          <v-icon v-if="drawer" size="40" color="white" @click="drawer=false" style="position: absolute; right: -50px; top: 10px;">mdi-alpha-x-circle-outline</v-icon>
          
          <v-divider></v-divider>
          <v-card-title class="text-h6">Trending</v-card-title>
          <v-list-item link title="Best Sellers"></v-list-item>
          <v-list-item link title="New Releases"></v-list-item>
          <v-divider></v-divider>
          <v-card-title class="text-h6">Shop By Categories</v-card-title>
          <v-list-item link title="Category 1"></v-list-item>
          <v-list-item link title="Category 2"></v-list-item>
          <v-list-item link title="..more"></v-list-item>
          <v-divider></v-divider>
          <v-card-title class="text-h6">Help & Support</v-card-title>
          <v-list-item link title="Your Account"></v-list-item>
          <v-list-item link title="Customer Service"></v-list-item>
          <v-list-item link title="Sign Out"></v-list-item>
      </v-navigation-drawer>
    </div>
</template>
<script>
import { useTokenStore } from '#imports';
import axios from 'axios';
export default{
  data: () => ({
    authenticated: false,
    drawer: false,
    items: [
      { title: 'Profile', onClick: () => {this.$router.push('/profile')}},
      { title: 'Settings', onClick: () => {this.$router.push('/settings')}},
      { title: 'Logout', onClick: () => {
        if(process.client) {
      localStorage.setItem('token', '')
      // console.log('Token: ',localStorage.getItem('token'))
    }
      navigateTo('/login/customer', { text: 'Logged out!' })
  } },
    ],
  }),
  created() {
    this.getProfile();
    if(process.client) {
      console.log('Token: ',localStorage.getItem('token'))
    }
  },
  methods: {
    async getProfile() {
      if(process.client) {
        var token = localStorage.getItem('token')
      }
      if ( token === "") {
        this.authenticated = false;
      }else{
      this.authenticated = true;
      }
  
    await axios.get('http://localhost:8001/accounts/api/v1/profile/', {headers: {
      'Authorization': `JWT ${token}`
    }}).
    
  then((response) => {
    console.log(response.data);
    this.items[0].title = 'Profile ('+response.data.first_name+' '+response.data.last_name+')';
  }).catch((error) => {
    console.log(error);
  });
    },

  },
  
}
</script>