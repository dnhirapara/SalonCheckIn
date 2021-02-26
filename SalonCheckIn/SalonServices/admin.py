from django.contrib import admin
from .models import Service, Tag, WorkingHour, Setting
# Register your models here.

admin.site.register(Service)
admin.site.register(Tag)
admin.site.register(WorkingHour)
admin.site.register(Setting)
