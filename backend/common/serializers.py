from .models import *
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['id',"user"]


class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        exclude = ['id',"user"]


class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        exclude = ['id',"user"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class CommonSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    kyc = serializers.SerializerMethodField()
    bank_detail = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        request = self.context.get('request', None)
        if request:
            return {"id": request.user.id, "email": request.user.email}
        
    def get_address(self, obj):
        address = Address.objects.filter(user=self.get_user(obj)["id"]).first()
        if address:
            return AddressSerializer(address).data
        return None
    
    def get_kyc(self, obj):
        kyc = KYC.objects.filter(user=self.get_user(obj)["id"]).first()
        if kyc:
            return KYCSerializer(kyc).data
        return None
    
    def get_bank_detail(self, obj):
        bank_detail = BankDetail.objects.filter(user=self.get_user(obj)["id"]).first()
        if bank_detail:
            return BankDetailSerializer(bank_detail).data
        return None
    
    