from .models import (DeliveryVenture)
from rest_framework.serializers import ModelSerializer


class DeliveryVentureSerializer(ModelSerializer):
    class Meta:
        model = DeliveryVenture
        fields = "__all__"
