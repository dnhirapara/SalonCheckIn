from Appointments.models import Appointment
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    total = serializers.CharField(source='get_total')

    class Meta:
        model = Appointment
        fields = ['customer', 'service', 'total']
