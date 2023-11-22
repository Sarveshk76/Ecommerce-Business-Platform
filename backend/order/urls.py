from django.urls import path
from .api_views import CartViewSet, OrderViewSet, ShippingAPIView

urlpatterns = [
    path('cart/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart'),
    path('', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order'),
    path('<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='order-detail'),
    path('shipping/<int:order_id>/', ShippingAPIView.as_view(), name='shipping' )
]