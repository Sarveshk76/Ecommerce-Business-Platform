from django.urls import path
from .apiviews import RegisterAPIView, LoginAPIView

urlpatterns = [
    path("api/v1/register/<str:user_type>/", RegisterAPIView.as_view(), name="register"),
    path("api/v1/login/", LoginAPIView.as_view(), name="login"),
]