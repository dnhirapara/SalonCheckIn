from django.db import models
from django.utils.translation import ugettext_lazy as _
from Accounts.models import Salon
import datetime
# Create your models here.


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    price = models.PositiveIntegerField()
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.name + " - " + self.salon.display_name


WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),
]


class WorkingHour(models.Model):
    id = models.AutoField(primary_key=True)

    mon_is_open = models.BooleanField(default=True)
    mon_form = models.TimeField(null=True, blank=True, default="09:00:00")
    mon_to = models.TimeField(null=True, blank=True, default="20:00:00")

    tue_is_open = models.BooleanField(default=True)
    tue_form = models.TimeField(null=True, blank=True, default="09:00:00")
    tue_to = models.TimeField(null=True, blank=True, default="20:00:00")

    wed_is_open = models.BooleanField(default=True)
    wed_form = models.TimeField(null=True, blank=True, default="09:00:00")
    wed_to = models.TimeField(null=True, blank=True, default="20:00:00")

    thu_is_open = models.BooleanField(default=True)
    thu_form = models.TimeField(null=True, blank=True, default="09:00:00")
    thu_to = models.TimeField(null=True, blank=True, default="20:00:00")

    fri_is_open = models.BooleanField(default=True)
    fri_form = models.TimeField(null=True, blank=True, default="09:00:00")
    fri_to = models.TimeField(null=True, blank=True, default="20:00:00")

    sat_is_open = models.BooleanField(default=True)
    sat_form = models.TimeField(null=True, blank=True, default="09:00:00")
    sat_to = models.TimeField(null=True, blank=True, default="20:00:00")

    sun_is_open = models.BooleanField(default=True)
    sun_form = models.TimeField(null=True, blank=True, default="09:00:00")
    sun_to = models.TimeField(null=True, blank=True, default="20:00:00")


class Setting(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    is_take_appointments = models.BooleanField(default=True)
    workinghour = models.OneToOneField(WorkingHour, on_delete=models.CASCADE)


def time_validator(from_time, to_time):
    if from_time <= to_time:
        return True
    else:
        return False
