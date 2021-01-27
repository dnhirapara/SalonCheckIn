from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import RegistrationSerializer, SalonSerializer, SalonDetailSerializer
from Accounts.models import Salon, Account
from django.shortcuts import get_object_or_404


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


class getSalonView(generics.ListAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer


class getSalonDetailView(generics.RetrieveAPIView):
    serializer_class = SalonDetailSerializer
    lookup_field = 'slug'
