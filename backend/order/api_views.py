from .models import Cart, CartItem, Order, Coupon, Shipping
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (OrderSerializer, CartSerializer,
                          ShippingSerializer)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ShippingAPIView(APIView):
    serializer_class = ShippingSerializer

    def get(self, request, order_id):
        shipping = Shipping.objects.filter(order=order_id)
        if shipping:
            serializer = ShippingSerializer(shipping, many=True)
            return Response(serializer.data)
