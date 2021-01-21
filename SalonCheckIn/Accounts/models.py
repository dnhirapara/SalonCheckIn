from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


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
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_customer = models.BooleanField(default=False)
    is_salon = models.BooleanField(default=False)
    # phone_number = models.CharField(max_lengeth=10, unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.email

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
        verbose_name="Birth Date", validators=[no_future_date], default=timezone.now())
    address = models.CharField(max_length=512, default="Address")

    def __str__(self):
        return self.user.username


class Salon(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE)
    display_name = models.CharField(
        max_length=64, null=False, default="Salon Name")
    description = models.CharField(max_length=1024, default="Descriptin")
    address = models.CharField(max_length=512, null=False, default="Address")
    slug = models.SlugField(default='', editable=False,
                            max_length=200, null=False, unique=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        value = self.user.username + " "+self.display_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('getsalons', args=[str(self.slug)])
    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('getsalon', kwargs={'slug': self.slug})
