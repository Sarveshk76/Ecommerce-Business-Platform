from django.contrib import admin
from .models import (Order, Coupon, Cart,)

admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Cart)
