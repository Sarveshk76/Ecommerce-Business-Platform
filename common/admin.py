from django.contrib import admin
from .models import (Address, BankDetail,
                     Rating, Payment, KYC)

admin.site.register(Address)
admin.site.register(BankDetail)
admin.site.register(Rating)
admin.site.register(Payment)
admin.site.register(KYC)
