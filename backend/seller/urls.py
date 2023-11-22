from django.urls import path
from .api_views import SellerViewSet

urlpatterns = [
    path('', SellerViewSet.as_view({'get': 'list', 'post': 'create'}), name='seller'),
]