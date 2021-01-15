from .models import Salon, Account, Customer
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


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
