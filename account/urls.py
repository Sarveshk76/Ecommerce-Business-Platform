from django.urls import path
from .apiviews import RegisterAPIView, LoginAPIView

urlpatterns = [
    path("register/<str:user_type>/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
]