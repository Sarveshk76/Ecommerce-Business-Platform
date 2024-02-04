from django.contrib import admin
from .models import (Address, BankDetail,
                    Payment, KYC)

admin.site.register(Address)
admin.site.register(BankDetail)
admin.site.register(Payment)
admin.site.register(KYC)
