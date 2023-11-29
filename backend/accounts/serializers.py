from rest_framework import serializers
from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(User)

    class Meta:
        model = User
        exclude = ("password",)
