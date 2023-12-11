<template>
    <div>
        <v-card class="mx-5 my-5"  variant="outlined">
          <v-card-text>
            Category:
          </v-card-text>
        </v-card>
        <v-container class="bg-surface-variant">
    <v-row v-for="n in 3"
        :key="n" no-gutters>
      <v-col
        v-for="n in 3"
        :key="n"
        cols="12"
        sm="4"
      >
        <v-sheet class="ma-2 pa-2">
          One of three columns
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
    </div>
</template>
<script>
</script>