from django.db import models
from django.contrib.auth import get_user_model
from inventory.models import Product

User = get_user_model()

ORDER_TYPE = (
    ('pickup', 'pickup'),
    ('delivery', 'delivery'),
)

CART_TYPE = (
    ('wishlist', 'wishlist'),
    ('cart', 'cart'),
)

ORDER_STATUS = ( 
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled'),
)

SHIPPING_STATUS = (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('shipped', 'shipped'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled'),
)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_type = models.CharField(choices=CART_TYPE, max_length=20)
    discount = models.IntegerField(null=True, blank=True)
    coupon = models.ManyToManyField('Coupon', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_type = models.CharField(choices=ORDER_TYPE, max_length=20)
    address = models.ForeignKey('common.Address', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_on = models.DateField(auto_now=True)
    payment = models.ForeignKey('common.Payment', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cart)


class Coupon(models.Model):
    code = models.CharField(max_length=10)
    discount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_till = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.valid_from} - {self.valid_till}"

class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(choices=SHIPPING_STATUS, max_length=20)
    from_address = models.ForeignKey('common.Address', on_delete=models.CASCADE, related_name='from_address')
    to_address = models.ForeignKey('common.Address', on_delete=models.CASCADE, related_name='to_address')
    shipped_on = models.DateField(auto_now=True)
    delivered_on = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.order} - {self.product} - {self.status}"
