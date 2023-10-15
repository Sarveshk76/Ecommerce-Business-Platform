from django.db import models
from seller.models import Seller


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="category/images/", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="subcategory/images/", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "subcategories"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products_category+",
                                 on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,
                                    related_name="products_category+",
                                    on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product/images/", blank=True)
    status = models.CharField(max_length=20)
    rating = models.IntegerField()
    review = models.TextField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
