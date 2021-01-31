from django.db import models
from Account.models import Customer, Salon
from SalonServices.models import Service, Tag
# Create your models here.


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ManyToManyField(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
