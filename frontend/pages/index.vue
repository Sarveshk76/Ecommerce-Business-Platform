<template>
  <div>
    <v-container>
      <v-row class="my-5">
        <v-carousel>
          <v-carousel-item
            v-for="(item,i) in carousels"
            :key="i"
            :src="item"
            cover
          ></v-carousel-item>

        </v-carousel>
        
      </v-row>
      <v-row class="mt-5">
        <p class="text-h6 font-weight-bold">Todays' Offers</p>
      </v-row>
     
      <v-layout class="overflow-x-auto scrollbar-hidden border pa-3">
        
       <div v-if="todays_offers.length != 0">
        <div class="border m-2" align="center" xs12 sm6 md3 v-for="(item,i) in todays_offers" :key="i" >
          <nuxt-link :to="{path:'todays-offers/'+item.name.slice(0,50)+'/', 
                           query:{
                            'id': item.id,
                            'name': item.name,
                            'desc': item.description,
                            'price': item.price,
                            'seller': item.seller.venture,
                            'rating': item.rating,
                            'reviews': item.reviews,
                            'stock': item.stock,}
                           }">
          <v-card height="300" width="220">
            <v-img src="/images/no_product_image.jpg" height="200px"></v-img>
            <p>{{ item.name }}</p>
          </v-card>
          </nuxt-link>
        </div>
      </div>
      <div v-else>
        <p> No Products Available!!</p>
      </div>
      </v-layout>

      <v-row class="mt-5">
        <p class="text-h6 font-weight-bold">New Arrivals</p>
      </v-row>
      <v-layout class="overflow-x-auto scrollbar-hidden border pa-3">
       <div v-if="new_arrivals.length != 0">
        <div class="border m-2" align="center" xs12 sm6 md3 v-for="(item,i) in new_arrivals" :key="i" >
          <v-card height="300" width="220">
            <v-img src="/images/no_product_image.jpg" height="200px"></v-img>
            <p>{{ item.name }}</p>
          </v-card>
        </div>
      </div>
      <div v-else>
        <p>No Products Available!!</p>
      </div>
      </v-layout>

      <v-row class="mt-5">
        <p class="text-h6 font-weight-bold">Recently Viewed Products</p>
      </v-row>
      <v-layout class="overflow-x-auto scrollbar-hidden border pa-3">
        <div v-if="recently_viewed_products.length != 0">
        <div class="border m-2" align="center" xs12 sm6 md3 v-for="(item,i) in recently_viewed_products" :key="i" >
          <v-card height="300" width="220">
            <v-img src="/images/no_product_image.jpg" height="200px"></v-img>
            <p>{{ item.name }}</p>
          </v-card>
        </div>
      </div>
      <div v-else>
        <p>No Products Available!!</p>
      </div>
      </v-layout>
      
    </v-container>
  </div>
</template>

<script setup>
import axios from 'axios'

const carousels = useState("carousels", () => [], {type: Array})
const todays_offers = useState("todays_offers", () => [], {type: Array})
const new_arrivals = useState("new_arrivals", () => [], {type: Array})
const recently_viewed_products = useState("recently_viewed_products", () => [], {type: Array})

async function getDashcoard()  {
      if(process.client) {
        // var token = localStorage.getItem('token')
        // localStorage.setItem('token', "")
      }
  
    await axios.get('http://localhost:8001/inventory/dashboard/').
    
  then((response) => {
    carousels.value = response.data.data.carousel
    todays_offers.value = response.data.data.todays_offers
    new_arrivals.value = response.data.data.new_arrivals
    recently_viewed_products.value = response.data.data.recently_viewed_products
  }).catch((error) => {
    console.log(error);
  });
    }
    getDashcoard();
  


</script>
<style>
.scrollbar-hidden::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge add Firefox */
.scrollbar-hidden {
  -ms-overflow-style: none;
  scrollbar-width: none; /* Firefox */
}
</style>