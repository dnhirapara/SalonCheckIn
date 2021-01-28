from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework.reverse import reverse

app_name = 'services'

router = routers.SimpleRouter()
# router.register('update-salon', UpdateSalonView)

urlpatterns = format_suffix_patterns([
])

print(repr(router.urls))
urlpatterns += router.urls
