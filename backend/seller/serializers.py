from .models import Seller
from rest_framework.serializers import ModelSerializer


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"
