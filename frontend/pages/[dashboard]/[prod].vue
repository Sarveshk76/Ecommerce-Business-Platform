<template>
    <div>
        <!-- product page -->
        <v-container>
            <v-row>
                <v-col cols="12" md="6">
                    <v-img class="border" src="/images/no_product_image.jpg" height="300px"></v-img>
                </v-col>
                <v-col cols="12" md="6">
                    <v-card-title class="pa-2">{{ name }}</v-card-title>
                    <v-card-subtitle class="pa-2">{{ desc }}</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Price: ₹{{ price }}</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Seller: {{ seller }}</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Units: {{ stock }}</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Rating: {{ rating }}</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Reviews: {{ reviews }}</v-card-subtitle>
                    <v-btn color="teal"  @click="addToCart">Add to Cart</v-btn>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <v-card-title class="pa-2">Product Details</v-card-title>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                </v-col>
                <v-col cols="12" md="6">
                    <v-card-title class="pa-2">Product Details</v-card-title>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                    <v-card-subtitle class="pa-2">Product Details</v-card-subtitle>
                </v-col>
            </v-row>
        </v-container>

    </div>
</template>
<script>
export default {
    name: 'Dashboard',
    data() {
        return {
            dashboard: this.$route.params.dashboard,
            prod: this.$route.params.prod,
            id: this.$route.query.id,
            name: this.$route.query.name,
            desc: this.$route.query.desc,
            price: this.$route.query.price,
            seller: this.$route.query.seller,
            rating: this.$route.query.rating,
            reviews: this.$route.query.reviews,
            stock: this.$route.query.stock,
        }
    },
    
}
</script>