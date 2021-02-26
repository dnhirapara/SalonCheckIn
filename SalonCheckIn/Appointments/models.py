from django.db import models
from Accounts.models import Customer, Salon
from SalonServices.models import Service, Tag
# Create your models here.


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ManyToManyField(Service)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = 0
        for ser in self.service.all():
            total += ser.price
        return total
