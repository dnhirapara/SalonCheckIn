from Appointments.models import Appointment
from .serializers import AppointmentSerializer
from rest_framework import viewsets


class ManageAppointment(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        return AppointmentSerializer
