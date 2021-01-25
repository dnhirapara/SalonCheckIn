from django.db import models
from Accounts.models import Salon
# Create your models here.


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    price = models.IntegerField()
    tags = models.ManyToManyField(Tag, null=True)
    durations = models.DurationField()

    def __str__(self):
        return self.salon.display_name+" "+self.name


# class WorkingHours(models.Model):
#     day = models.choices()
