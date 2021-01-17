from .models import Salon, Account, Customer
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=Salon)
def save_salon(sender, instance, **kwargs):
    if(instance.user.is_salon == False):
        instance.user.is_salon = True
        instance.user.save()


@receiver(post_save, sender=Customer)
def save_customer(sender, instance, **kwargs):
    if(instance.user.is_customer == False):
        instance.user.is_customer = True
        instance.user.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
