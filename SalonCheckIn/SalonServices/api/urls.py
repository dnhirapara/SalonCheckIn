from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework.reverse import reverse
from .views import GetServiceView, GetTagsView

app_name = 'services'

router = routers.SimpleRouter()
router.register('getservices', GetServiceView)
router.register('gettags', GetTagsView)

urlpatterns = [
    # path('/getservices',)
]

print(repr(router.urls))
urlpatterns += router.urls
