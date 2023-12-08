from .models import (Category, Product, SubCategory,)
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


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DashboardSerializer(Serializer):
    carousel = serializers.SerializerMethodField()
    todays_offers = serializers.SerializerMethodField()
    new_arrivals = serializers.SerializerMethodField()
    recently_viewed_products = serializers.SerializerMethodField()

    def get_carousel(self, obj):
        obj = ["https://drive.google.com/uc?id=1lkz6JI7dYWVoEv0R8YUe7X4uvHcerke4",
               "https://drive.google.com/uc?id=1w0W83N55Kn2Cb_sAZdugP7YVI_Js7ZAo",
               "https://drive.google.com/uc?id=1iLHAdFzJz9sZ_xiavbvKc1x8skdnrcGB"]
        return obj

    def get_todays_offers(self, obj):
        obj = Product.objects.all().order_by('-id')[:5]
        serializer = ProductSerializer(obj, many=True)
        return serializer.data
    
    def get_recently_viewed_products(self, obj):
        obj = Product.objects.all().order_by('-id')[5:11]
        serializer = ProductSerializer(obj, many=True)
        return serializer.data
    
    def get_new_arrivals(self, obj):
        obj = Product.objects.all().order_by('-id')[10:16]
        serializer = ProductSerializer(obj, many=True)
        return serializer.data