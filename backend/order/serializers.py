from .models import (Order, CartItem, Cart, Coupon, Shipping)
from common.serializers import AddressSerializer, PaymentSerializer
from accounts.serializers import UserSerializer
from inventory.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import serializers
from common.models import Address, Payment


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = "__all__"

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    coupon = CouponSerializer(many=True)
    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_type', 'discount', 'coupon', 'is_active', 'items')

    def get_items(self, obj):
        cart_items = CartItem.objects.filter(cart=obj)
        serializer = CartItemSerializer(cart_items, many=True)
        return serializer.data


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    address = AddressSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = Order
        fields = "__all__"
    
    def create(self, validated_data):
        cart_data = validated_data.pop('cart')
        address_data = validated_data.pop('address')
        payment_data = validated_data.pop('payment')
        cart = Cart.objects.create(**cart_data)
        address = Address.objects.create(**address_data)
        payment = Payment.objects.create(**payment_data)
        order = Order.objects.create(cart=cart, address=address, payment=payment, **validated_data)
        return order 


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"

    