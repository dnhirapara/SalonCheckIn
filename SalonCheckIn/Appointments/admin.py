from django.contrib import admin
from .models import Appointment, dummy
# Register your models here.

admin.site.register(Appointment)
admin.site.register(dummy)
