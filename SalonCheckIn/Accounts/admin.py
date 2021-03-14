from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Salon, Customer, Address


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff', 'is_salon', 'is_customer')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Salon)
admin.site.register(Customer)
admin.site.register(Address)
