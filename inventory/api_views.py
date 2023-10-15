from .models import Category, SubCategory
from .serializers import (CategorySerializer, SubCategorySerializer,
                          ProductSerializer,)
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()


class SubCategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        category = self.kwargs['id']
        return SubCategory.objects.all().filter(category__id=category)
