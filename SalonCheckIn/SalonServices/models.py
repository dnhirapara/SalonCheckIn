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


class Setting(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    is_take_appointments = models.BooleanField(default=True)


def time_validator(from_time, to_time):
    if from_time <= to_time:
        return True
    else:
        return False


class WorkingHour(models.Model):
    # class Meta:
    #     unique_together = ('weekday'),
    # salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    # weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
    # is_open = models.BooleanField(default=True)
    # form = models.TimeField(null=True, blank=True)
    # to = models.TimeField(null=True, blank=True)
    id = models.AutoField(primary_key=True)
    # default_form = models.TimeField(default=time.time())
    # default_to = models.TimeField(default=time.time())

    mon_is_open = models.BooleanField(default=True)
    mon_form = models.TimeField(null=True, blank=True)
    mon_to = models.TimeField(null=True, blank=True)

    tue_is_open = models.BooleanField(default=True)
    tue_form = models.TimeField(null=True, blank=True)
    tue_to = models.TimeField(null=True, blank=True)

    wed_is_open = models.BooleanField(default=True)
    wed_form = models.TimeField(null=True, blank=True)
    wed_to = models.TimeField(null=True, blank=True)

    thu_is_open = models.BooleanField(default=True)
    thu_form = models.TimeField(null=True, blank=True)
    thu_to = models.TimeField(null=True, blank=True)

    fri_is_open = models.BooleanField(default=True)
    fri_form = models.TimeField(null=True, blank=True)
    fri_to = models.TimeField(null=True, blank=True)

    sat_is_open = models.BooleanField(default=True)
    sat_form = models.TimeField(null=True, blank=True)
    sat_to = models.TimeField(null=True, blank=True)

    sun_is_open = models.BooleanField(default=True)
    sun_form = models.TimeField(null=True, blank=True)
    sun_to = models.TimeField(null=True, blank=True)
