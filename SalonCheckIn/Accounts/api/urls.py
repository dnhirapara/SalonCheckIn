from django.urls import path
from .views import (
    registration_view,
    getSalonView,
    getSalonDetailView
)
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = format_suffix_patterns([
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('getsalons', getSalonView.as_view(), name="getsalons"),
    path('getsalon/<slug>',
         getSalonDetailView.as_view(), name="getsalondetail"),
])
