from Accounts.models import Account, Salon
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import permissions

from .serializers import (RegistrationSerializer, SalonDetailSerializer,
                          SalonSerializer, SalonUpdateSerializer)
from .permissions import SalonUserPermission


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


class GetSalonView(viewsets.ReadOnlyModelViewSet):
    queryset = Salon.objects.all()
    lookup_field = 'slug'
    permission_classes = []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SalonDetailSerializer
        return SalonSerializer


class UpdateSalonView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = Salon.objects.all()
    serializer_class = SalonUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated, SalonUserPermission]
