from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
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
        print("-----",email, password, user_type)
        if email is None or password is None:
            return Response(
                {"error": "Please provide both email and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is not None:
            return Response(
                {"error": "User already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            if user_type == "customer":
                user = User.objects.create_customer(email, password)
                return Response({"user":user.email, "mesage": "Customer created successfully!!"}, status=status.HTTP_201_CREATED)
            elif user_type == "seller":
                user = User.objects.create_seller(email, password)
                return Response({"user":user.email, "message": "Seller created successfully!!"}, status=status.HTTP_201_CREATED)
            elif user_type == "delivery_partner":
                user = User.objects.create_delivery_partner(email, password)
                return Response({"user":user.email, "message":"Delivery partner created successfully!!"}, status=status.HTTP_201_CREATED)
        

class LoginAPIView(APIView):

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        user = authenticate(email = email, password = password)

        if email is None or password is None:
            return Response(
                {"error": "Please provide both email and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if user is None:
            return Response(
                {"error": "No user with given email"},
                status=status.HTTP_200_OK,
            )
        if not user.check_password(password):
            return Response(
                {"error": "Incorrect password"},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            refresh = RefreshToken.for_user(user)

            return Response({"user":user.email, 'refresh': str(refresh),
                'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        

class ProfileAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = UserSerializer

    def get(self, request):
        user = self.request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response({"user":request.user}, status=status.HTTP_200_OK)
    
    