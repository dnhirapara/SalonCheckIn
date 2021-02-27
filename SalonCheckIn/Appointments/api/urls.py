from django.urls import path
from .views import(
    ManageAppointment,
    GetAllAppointmentsCustomer,
    GetAllAppointmentsSalon,
    change_appointment_status
)


from rest_framework import routers
from rest_framework.reverse import reverse

app_name = 'appointment'

router = routers.SimpleRouter()
router.register('appointment', ManageAppointment)
router.register('getappointmentssalon', GetAllAppointmentsSalon)
router.register('getappointmentscustomer', GetAllAppointmentsCustomer)

urlpatterns = router.urls

urlpatterns += [
    path('chagnestatus/<int:id>', change_appointment_status, name='change-status'),
]
