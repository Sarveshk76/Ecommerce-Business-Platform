from django.db import models
from seller.models import Seller
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "subcategories"


class Images(models.Model):
    url = models.URLField(max_length=2048)

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,
                                    related_name="products_category",
                                    on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ManyToManyField(Images)
    rating = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    todays_offer = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    recently_viewed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
