from django.urls import path
from .api_views import CategoryListView, SubCategoryListView, DashboardAPIView


urlpatterns = [
    path('dashboard/', DashboardAPIView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:id>/',
         SubCategoryListView.as_view()),
]
