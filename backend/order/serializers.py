from .models import (Order, CartItem, Cart, Coupon, Shipping)
from rest_framework.response import Response
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_type', 'discount', 'coupon', 'is_active', 'items')

    def get_items(self, obj):
        cart_items = CartItem.objects.filter(cart=obj)
        serializer = CartItemSerializer(cart_items, many=True)
        return serializer.data


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"

    