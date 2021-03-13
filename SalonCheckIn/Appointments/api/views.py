from Appointments.models import Appointment
from .serializers import AppointmentSerializer, AppointmentDetailSerializer
from Accounts.models import Salon, Customer
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import *


class ManageAppointment(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        return AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save(customer=Customer.objects.get(user=self.request.user))


class GetAllAppointmentsSalon(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentDetailSerializer

    def get_queryset(self):
        salon_user = Salon.objects.filter(user=self.request.user)[0]
        print(type(salon_user))
        print(salon_user)
        return self.queryset.filter(service__salon=salon_user)


class GetAllAppointmentsCustomer(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentDetailSerializer

    def get_queryset(self):
        customer_user = Customer.objects.filter(user=self.request.user)
        if len(customer_user) == 0:
            raise ValidationError("No Customer Exists.")

        print(type(customer_user))
        print(customer_user)
        return self.queryset.filter(customer=customer_user[0])


@ api_view(['POST', ])
@ permission_classes((IsAuthenticated,))
def change_appointment_status(request, id):
    if(request.user.is_salon == False):
        return Response({'error': "You are not salon user"})
    else:
        data = {}
        appointment = Appointment.objects.get(id=id)
        if appointment.service.salon.user == request.user:
            data['old_status'] = appointment.get_status_display()
            appointment.status = request.data['status']
            appointment.save()
            data['new_status'] = request.data['status']
            data['success'] = 'Your Appointment Status Changed'
            return Response(data, status=HTTP_200_OK)
        else:
            return Response({'error': 'You are not allowed to do this.'})
