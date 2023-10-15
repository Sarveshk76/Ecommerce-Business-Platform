from django.urls import path
from .api_views import CategoryListView, SubCategoryListView


urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:id>/',
         SubCategoryListView.as_view()),
]
