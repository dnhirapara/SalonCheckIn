from Appointments.models import Appointment
from rest_framework import serializers
from Accounts.models import Salon, Customer


class AppointmentSerializer(serializers.ModelSerializer):
    # total = serializers.CharField(source='get_total')
    # customer = serializers.HiddenField(
    #     default=Customer.objects.get(user=serializers.CurrentUserDefault()),
    # )

    class Meta:
        model = Appointment
        fields = ['id', 'service', ]

    # def save(self, **kwargs):
    #     appo = Appointment(
    #         customer=self.validated_data['user'],
    #         service=self.validated_data['service']
    #     )
    #     appo.save()
    #     return appo


class AppointmentDetailSerializer(serializers.ModelSerializer):
    total = serializers.CharField(source='get_total')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Appointment
        fields = ['customer', 'service', 'total', 'status', 'date']
