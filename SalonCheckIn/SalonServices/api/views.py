from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from SalonServices.models import Service, Tag
from Accounts.models import Account, Salon
from .serializers import ServiceSerializer
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED


class GetServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        # print(self.request.salon)
        user = self.request.user
        print(user)
        # raise serializers.ValidationError("Anonymous User")
        if type(user) is AnonymousUser:
            raise serializers.ValidationError(
                "Anonymous User", code=HTTP_404_NOT_FOUND)
        salon = Salon.objects.get(user=user)
        return serializer.save(salon=salon)
        # return super().perform_create(serializer)
