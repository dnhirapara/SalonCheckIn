from django.urls import path
from .views import(
    ManageAppointment
)


from rest_framework import routers
from rest_framework.reverse import reverse

app_name = 'appointment'

router = routers.SimpleRouter()
router.register('appointment', ManageAppointment)

urlpatterns = router.urls
