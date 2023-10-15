from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()

class RegisterAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, user_type, format=None):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        if email is None or password is None:
            return Response(
                {"error": "Please provide both email and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if user_type == "customer":
            user = User.objects.create_customer(email, password)
            token = Token.objects.create(user=user)
            return Response({"user":user.email, "token": token.key}, status=status.HTTP_201_CREATED)
        elif user_type == "seller":
            user = User.objects.create_seller(email, password)
            token = Token.objects.create(user=user)
            return Response({"user":user.email, "token": token.key}, status=status.HTTP_201_CREATED)
        elif user_type == "delivery_partner":
            user = User.objects.create_delivery_partner(email, password)
            token = Token.objects.create(user=user)
            return Response({"user":user.email, "token": token.key}, status=status.HTTP_201_CREATED)
        

class LoginAPIView(APIView):

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        if email is None or password is None:
            return Response(
                {"error": "Please provide both email and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.filter(email=email).first()
        if user is None:
            return Response(
                {"error": "No user with given email"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if not user.check_password(password):
            return Response(
                {"error": "Incorrect password"},
                status=status.HTTP_404_NOT_FOUND,
            )
        token = Token.objects.get(user=user)
        return Response({"user":user.email, "token": token.key}, status=status.HTTP_200_OK)