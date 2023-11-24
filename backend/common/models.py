from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

DOC_TYPE = (
    ('aadhar', 'aadhar'),
    ('pan', 'pan'),
    ('passport', 'passport'),
    ('driving_license', 'driving_license'),
)


class Address(models.Model):
    user = models.ManyToManyField(User, related_name='address')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return str(self.address)


class KYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kyc_status = models.BooleanField(default=False)
    doc_type = models.CharField(choices=DOC_TYPE, max_length=20)
    document = models.FileField(upload_to="documents/")
    uploaded_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.doc_type


class BankDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)

    def __str__(self):
        return self.account_holder_name


class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.rating


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = (
        ('paid', 'paid'),
        ('unpaid', 'unpaid'),
    )
    status = models.CharField(choices=STATUS, max_length=20)
    payment_on = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.amount)
