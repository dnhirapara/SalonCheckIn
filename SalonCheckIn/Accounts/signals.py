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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_related_model_objects(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        # print(token)
        if instance.is_customer:
            customer = Customer.objects.create(user=instance)
            # print(customer)
        elif instance.is_salon:
            salon = Salon.objects.create(user=instance)
            # print(salon)


# @receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
# def delete_releted_model_objects(sender, instance, **kwargs):
#     if instance.is_customer:
#         Customer.objects.filter(user=instance).delete()
#     elif instance.is_salon:
#         Salon.objects.filter(user=instance).delete()


# TODO: Need to implement post delete signals for Salon and Customer model so that whenever model deleted boolenfield in Account model updated.
