<template>
  <div>
    <v-container>
      <v-row>
        <v-carousel>
          <v-carousel-item
            v-for="(item,i) in carousels"
            :key="i"
            src="item.src"
            cover
          ></v-carousel-item>

        </v-carousel>
      </v-row>
      <v-row>
        <p>Todays' Offers</p>
      </v-row>
      <v-row class="border border-primary mt-5">
        <v-col v-for="n in 4"
        :key="n"
        align="center"
        >
          <v-card border class="ma-2 pa-2" style="width: 250px; height: 300px;">
            One of four columns
          </v-card>
        </v-col>
      </v-row>

      <v-row>
        <p>New Arrivals</p>
      </v-row>
      <v-row>
        <v-col v-for="n in 4"
        :key="n"
        align="center"
        >
          <v-card border class="ma-2 pa-2" style="width: 250px; height: 300px;">
            One of four columns
          </v-card>
        </v-col>
      </v-row>

      <v-row>
        <p>Recently Viewed Products</p>
      </v-row>
      <v-row>
        <v-col v-for="n in 4"
        :key="n"
        align="center"
        >
          <v-card border class="ma-2 pa-2" style="width: 250px; height: 300px;">
            One of four columns
          </v-card>
        </v-col>
      </v-row>
      
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
        var token = localStorage.getItem('token')
        // localStorage.setItem('token', "")
      }
  
    await axios.get('http://localhost:8001/inventory/dashboard/', {headers: {
      'Authorization': `JWT ${token}`
    }}).
    
  then((response) => {
    // console.log(response.data);
    // carousels.value = response.data.carousels
    // todays_offers.value = response.data.todays_offers
    // new_arrivals.value = response.data.new_arrivals
    // recently_viewed_products.value = response.data.recently_viewed_products
    console.log(typeof(carousels))
    console.log(typeof(todays_offers))
    console.log(typeof(new_arrivals))
    console.log(typeof(recently_viewed_products))
  }).catch((error) => {
    console.log(error);
  });
    }
    getDashcoard();


</script>