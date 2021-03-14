from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core import validators
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Address(models.Model):
    address_line = models.CharField(
        max_length=150, default="Enter Address Line")
    city = models.CharField(max_length=50, default="Enter city")
    state = models.CharField(max_length=50, default="Enter state")
    pincode = models.CharField(max_length=10, default="Enter Pin Code")


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.address = Address.objects.get(id=1)
        user.is_superuser = True
        print(user)
        user.save(using=self._db)
        return user


username_validator = validators.RegexValidator(
    "^[a-z0-9-_]{4,20}$", "Username Must contains 4-20 characters. Allowed Characters: small (a-z),(0-9), (-) and (_). Whitespaces not allowed.")


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(
        max_length=30, unique=True, validators=[username_validator])
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    profile_image = models.ImageField(
        default='profiles/man.png', upload_to='profiles')
    phone = models.CharField(max_length=10, default='1234567891')
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    is_customer = models.BooleanField(default=False)
    is_salon = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


def no_future_date(date_value):
    """
    checks whether date is less than currunt date. If date greater than currnt date then it will raise validation error.
    """
    if date_value > date.today():
        raise ValidationError("Future date not allowed!!")


class Customer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    birth_date = models.DateField(
        verbose_name="Birth Date", null=True, blank=True)

    def __str__(self):
        return self.user.username


class Salon(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE)
    display_name = models.CharField(
        max_length=64, null=False, default="Salon Name")
    display_image = models.ImageField(
        default='salon_display_pics/default.jpg', upload_to='salon_display_pics')
    description = models.CharField(max_length=1024, default="Descriptin")
    slug = models.SlugField(default='', editable=False,
                            max_length=200, null=False, unique=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        value = self.user.username + " "+self.display_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
