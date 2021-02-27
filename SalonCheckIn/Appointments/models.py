from django.db import models
from Accounts.models import Customer, Salon
from SalonServices.models import Service, Tag
from django.utils.translation import ugettext_lazy as _
# Create your models here.

STATUS = [
    (1, _("Waiting")),
    (2, _("OnChair")),
    (3, _("Completed")),
]


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.service.price
        # for ser in self.service.objects.all():
        #     total += ser.price
        return total
