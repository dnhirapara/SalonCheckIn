from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from SalonServices.models import Service, Tag
from Accounts.models import Account, Salon
from .serializers import ServiceSerializer, TagSerializer
from rest_framework import permissions
from Accounts.api import permissions as custom_permissions
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from utils import custom_mixins


class GetTagsView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated,
                          custom_permissions.SalonUser]
    permission_action_classes = {
        "list": [permissions.AllowAny],
        "retrieve": [permissions.AllowAny],
    }

    def get_permissions(self):
        print(self.action)
        try:
            for permission in self.permission_action_classes[self.action]:
                print(permission)
            return [
                permission()
                for permission in self.permission_action_classes[self.action]
            ]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, "kwargs", {})
                permission_classes = action_func_kwargs.get(
                    "permission_classes"
                )
            else:
                permission_classes = None
            return [
                permission()
                for permission in (
                    permission_classes or self.permission_classes
                )
            ]


class GetServiceView(custom_mixins.PermissionForMethodMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated,
                          custom_permissions.SalonUserService]
    permission_action_classes = {
        "list": [permissions.AllowAny],
        "retrieve": [permissions.AllowAny],
    }

    def perform_create(self, serializer):
        print(self.request.data)
        # print(self.request.salon)
        user = self.request.user
        # raise serializers.ValidationError("Anonymous User")
        if type(user) is AnonymousUser:
            raise serializers.ValidationError(
                "Anonymous User", code=HTTP_404_NOT_FOUND)
        salon = Salon.objects.get(user=user)
        return serializer.save(salon=salon)
        # return super().perform_create(serializer)
