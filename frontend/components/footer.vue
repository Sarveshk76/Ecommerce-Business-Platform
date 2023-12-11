ponent with a Teal color header and columns and rows of links.

<template>
  <v-footer class="d-flex flex-column">
    <!-- <div class="bg-teal d-flex w-100 align-center px-4">
      <strong>Get connected with us on social networks!</strong>

      <v-spacer></v-spacer>

      <v-btn
        v-for="icon in icons"
        :key="icon"
        class="mx-4"
        :icon="icon"
        variant="plain"
        size="small"
      ></v-btn>
      <v-icon icon="home" />
    </div> -->

    <div class="px-4 py-2 bg-black text-center w-100">
        &copy; {{ new Date().getFullYear() }} — <strong>Ecom Biz Platform</strong>
    </div>
  </v-footer>
</template>
<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>