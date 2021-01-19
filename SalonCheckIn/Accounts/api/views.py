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
    # lookup_field = 'slug'


class getSalonDetailView(generics.RetrieveAPIView):
    serializer_class = SalonDetailSerializer
    queryset = Salon.objects.all()
    lookup_field = 'slug'

    # def get_object(self):
    #     username = self.kwargs["pk"]
    #     print("username: "+username)
    #     obj = get_object_or_404(Account, username=username)
    #     print("obj: ")
    #     print(obj)
    #     salon = get_object_or_404(Salon, user=obj)
    #     print("Salon: ")
    #     print(salon.address)
    #     return salon
    # def get_queryset(self):
    #     user = Account.objects.filter(username=self.kwargs['username'])
    #     print(user[0])
    #     salon = Salon.objects.filter(user=user[0])
    #     # for i in salon:
    #     #     print(i[0])
    #     print(salon)
    #     return salon
