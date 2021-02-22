from django.urls import path
from .views import (
    registration_view,
    GetSalonView,
    # UpdateSalonView,
)
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework.reverse import reverse

app_name = 'api'

router = routers.SimpleRouter()
router.register('getsalons', GetSalonView)
# router.register('update-salon', UpdateSalonView)

urlpatterns = format_suffix_patterns([
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
])


urlpatterns += router.urls
