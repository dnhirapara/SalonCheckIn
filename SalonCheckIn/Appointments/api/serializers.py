from Appointments.models import Appointment
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    total = serializers.CharField(source='get_total')

    class Meta:
        model = Appointment
        fields = ['customer', 'service', 'total']


class AppointmentDetailSerializer(serializers.ModelSerializer):
    total = serializers.CharField(source='get_total')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Appointment
        fields = ['customer', 'service', 'total', 'status', 'date']
