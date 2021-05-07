"""SalonCheckIn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # REF: https://youtu.be/ABuljoh0cig?list=PLLz6Bi1mIXhEXEnfAgUJXB0vLjHkyee6q&t=654 ( namespace )
    # path('accounts/', include('Accounts.urls', namespace="accounts")),
    path('accounts/', include('Accounts.urls')),
    # path('api/accounts/', include('Accounts.api.urls', namespace='api')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/accounts/', include('Accounts.api.urls', namespace='accounts-api')),
    path('api/service/', include('SalonServices.api.urls', namespace='services-api')),
    path('api/appointment/', include('Appointments.api.urls',
                                     namespace='appointment-api'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
