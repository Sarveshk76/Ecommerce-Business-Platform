from django.contrib import admin
from .models import (Order, Coupon, Cart,
                     CartItem, Shipping)

admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Shipping)
