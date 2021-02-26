from Accounts.models import Account, Salon
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import permissions as custom_permissions
from .serializers import (RegistrationSerializer, SalonDetailSerializer,
                          UserSerializer, SalonSerializer, SalonUpdateSerializer)


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            print(account)
            data['response'] = "Successful"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    user = authenticate(
        username=request.data['username'],
        password=request.data['password']
    )
    if not user:
        return Response({'detail': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)

    user_data = UserSerializer(user)

    return Response({
        'user': user_data.data,
        'token': token.key,
    }, status=HTTP_200_OK)


class GetSalonView(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    lookup_field = 'slug'
    permission_classes = []
    permission_action_classes = {
        "retrive": [permissions.AllowAny],
        "update": [permissions.IsAuthenticated, custom_permissions.SalonUser],
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
        try:
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

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SalonDetailSerializer
        if self.action == 'put':
            return SalonUpdateSerializer
        # return SalonUpdateSerializer
        return SalonSerializer


# class UpdateSalonView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     queryset = Salon.objects.all()
#     serializer_class = SalonUpdateSerializer
#     lookup_field = 'slug'
#     # permission_classes = []
#     permission_action_classes = {
#         "retrive": [permissions.AllowAny],
#         "update": [permissions.IsAuthenticated, custom_permissions.SalonUser],
#     }
#     # def get_permissions(self):
#     #     try:
#     #         return [permission() for permission in self.permission_classes_by_action[self.action]]
#     #     except KeyError:
#     #         if self.action:
#     #             action_func = getattr(self, self.action, {})
#     #             action_func_kwargs = getattr(action_func, 'kwargs', {})
#     #             permission_classes = action_func_kwargs.get(
#     #                 'permission_classes')
#     #         else:
#     #             permission_classes = None

#     #         return [permission() for permission in (permission_classes or self.permission_classes)]

#     def get_permissions(self):
#         """Return the permission classes based on action.

#         Look for permission classes in a dict mapping action to
#         permission classes array, ie.:

#         class MyViewSet(ViewSetActionPermissionMixin, ViewSet):
#             ...
#             permission_classes = [AllowAny]
#             permission_action_classes = {
#                 'list': [IsAuthenticated]
#                 'create': [IsAdminUser]
#                 'my_action': [MyCustomPermission]
#             }

#             @action(...)
#             def my_action:
#                 ...

#         If there is no action in the dict mapping, then the default
#         permission_classes is returned. If a custom action has its
#         permission_classes defined in the action decorator, then that
#         supercedes the value defined in the dict mapping.
#         """
#         try:
#             return [
#                 permission()
#                 for permission in self.permission_action_classes[self.action]
#             ]
#         except KeyError:
#             if self.action:
#                 action_func = getattr(self, self.action, {})
#                 action_func_kwargs = getattr(action_func, "kwargs", {})
#                 permission_classes = action_func_kwargs.get(
#                     "permission_classes"
#                 )
#             else:
#                 permission_classes = None

#             return [
#                 permission()
#                 for permission in (
#                     permission_classes or self.permission_classes
#                 )
#             ]
