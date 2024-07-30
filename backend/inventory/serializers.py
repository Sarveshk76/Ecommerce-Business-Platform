from .models import (Category, Product, SubCategory, Images)
from seller.models import Seller
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = "__all__"

class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('url',)

class ProductSerializer(ModelSerializer):
    seller = SellerSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"


class DashboardSerializer(Serializer):
    carousel = serializers.SerializerMethodField()
    todays_offers = serializers.SerializerMethodField()
    new_arrivals = serializers.SerializerMethodField()
    recently_viewed_products = serializers.SerializerMethodField()

    def get_carousel(self, obj):
        obj = ["https://drive.google.com/uc?id=1UZQRgCnEoQW8zyaqlzuj_7cRRA1ILvH7",
               "https://drive.google.com/uc?id=1cyZZpvkvR1luiPO4vHp1D_vTxHsn7XW1",
               "https://drive.google.com/uc?id=1hkBhDqZNbAcrbriHpkK8PJ6so3g9N7-1"]
        return obj

    def get_todays_offers(self, obj):
        obj = Product.objects.filter(todays_offer=True).select_related('seller').order_by('-id')[:5]
        serializer = ProductSerializer(obj, many=True)
        return serializer.data
    
    def get_recently_viewed_products(self, obj):
        obj = Product.objects.filter(recently_viewed=True).order_by('-id')[:5]
        serializer = ProductSerializer(obj, many=True)
        return serializer.data
    
    def get_new_arrivals(self, obj):
        obj = Product.objects.filter(new_arrival=True).order_by('-id')[:5]
        serializer = ProductSerializer(obj, many=True)
        return serializer.data
