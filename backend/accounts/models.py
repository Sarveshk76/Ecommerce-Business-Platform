from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_seller', False)
        extra_fields.setdefault('is_delivery_partner', False)
        extra_fields.setdefault('is_customer', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_customer(self, email, password=None, **extra_fields):
        """Create and save a Patient with the given email and password."""
        extra_fields.setdefault('is_customer', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_seller(self, email, password=None, **extra_fields):
        """
        Create and save a Doctor with the given email and password.
        """
        extra_fields.setdefault('is_seller', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_delivery_partner(self, email, password=None, **extra_fields):
        """Create and save a reception with the given email and password."""
        extra_fields.setdefault('is_delivery_partner', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ custom user model that supports using emails instead user names"""
    username = None
    email = models.EmailField(max_length=255, unique=True)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_delivery_partner = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    pic = models.ImageField(default="static/profiles/default.png",
                            upload_to="static/profiles")
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"User: {self.user.id}, Customer: {self.user.is_customer},\
              Delivery_partner: {self.user.is_delivery_partner}"
