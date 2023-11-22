from .models import Category, SubCategory
from .serializers import (CategorySerializer, SubCategorySerializer,
                          ProductSerializer, DashboardSerializer)
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class DashboardAPIView(APIView):
    serializer_class = DashboardSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"data": serializer.data})

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()


class SubCategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        category = self.kwargs['id']
        return SubCategory.objects.all().filter(category__id=category)
