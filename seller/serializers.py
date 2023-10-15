from .models import (Seller, SellerProduct,)
from rest_framework.serializers import ModelSerializer


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"


class SellerProductSerializer(ModelSerializer):
    class Meta:
        model = SellerProduct
        fields = "__all__"
