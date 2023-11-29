from django.urls import path
from .api_views import RegisterAPIView, LoginAPIView, ProfileAPIView

urlpatterns = [
    path("api/v1/register/<str:user_type>/", RegisterAPIView.as_view(), name="register"),
    path("api/v1/login/", LoginAPIView.as_view(), name="login"),
    path("api/v1/profile/", ProfileAPIView.as_view(), name="profile"),
]