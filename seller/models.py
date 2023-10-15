from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    venture = models.CharField(max_length=20)
    is_gst_registered = models.BooleanField(default=True)
    gstin_no = models.CharField(max_length=50, blank=True)
    joined_on = models.DateField(auto_now=True)
    status = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.venture

