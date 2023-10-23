from .models import (Category, Product, SubCategory,)
from rest_framework.serializers import ModelSerializer


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
