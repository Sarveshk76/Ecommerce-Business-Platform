<template>
    <div class="ma-5">
        <p class="text-h6">Shopping Cart</p>
        <v-row class="ma-3">
            <v-col class="border border-primary h-100"  cols="9">
                <v-card style="height: 100%;">
                    <v-card-text>
                        <v-row v-for="(item, index) in items"
                        :key="index"
                        :value="index">
                            <v-col cols="2">
                                <v-img src="https://cdn.vuetifyjs.com/images/cards/cooking.png"></v-img>
                            </v-col>
                            <v-col cols="10">
                                <p class="text-h6">{{ item.name }}</p>
                                <p>Price: $100</p>
                                <p>Quantity: 1</p>
                            </v-col>
                            <v-divider></v-divider>
                        </v-row>
                        <p>Subtotal: $100</p>
                        
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col class="border border-primary h-30" cols="3">
                <v-card class="pa-3 text-center">
                    <p>Eligible for FREE delivery</p>
                    <v-btn color="yellow">Proceed to Checkout</v-btn>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
<script>
export default {
    data: () => ({
        items: [
            { name: 'Item 1' },
            { name: 'Item 2' },
            { name: 'Item 3' },
            { name: 'Item 4' },
    ]
    })
}
</script>