<template>
  <div>
    <v-container>
      <v-row>
        <v-carousel>
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            cover
          ></v-carousel-item>

          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg"
            cover
          ></v-carousel-item>

          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            cover
          ></v-carousel-item>
        </v-carousel>
      </v-row>
      <v-row>
        <p>offers</p>
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
        <p>Todays offers</p>
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
      
    </v-container>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()

</script>