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
        obj = ["Carousel 1", "Carousel 2", "Carousel 3"]
        return obj

    def get_todays_offers(self, obj):
        obj = "Todays Offers"
        return obj
    
    def get_recently_viewed_products(self, obj):
        obj = "Recently Viewed Products"
        return obj
    
    def get_new_arrivals(self, obj):
        obj = "New Arrivals"
        return obj