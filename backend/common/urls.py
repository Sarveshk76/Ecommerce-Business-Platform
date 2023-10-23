from django.urls import path
from .views import CommonRetrieveUpdateAPIView

urlpatterns = [
    path('api/', CommonRetrieveUpdateAPIView.as_view(), name="common"),
]