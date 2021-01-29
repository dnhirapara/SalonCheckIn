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
        """Return the permission classes based on action.

        Look for permission classes in a dict mapping action to
        permission classes array, ie.:

        class MyViewSet(ViewSetActionPermissionMixin, ViewSet):
            ...
            permission_classes = [AllowAny]
            permission_action_classes = {
                'list': [IsAuthenticated]
                'create': [IsAdminUser]
                'my_action': [MyCustomPermission]
            }

            @action(...)
            def my_action:
                ...

        If there is no action in the dict mapping, then the default
        permission_classes is returned. If a custom action has its
        permission_classes defined in the action decorator, then that
        supercedes the value defined in the dict mapping.
        """
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
            # for permission in self.permission_classes:
            #     print(permission)
            return [
                permission()
                for permission in (
                    permission_classes or self.permission_classes
                )
            ]


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
