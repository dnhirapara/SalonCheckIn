from rest_framework import serializers
from django.core.exceptions import (
    ValidationError
)
from SalonServices.models import Service, Tag


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'price', 'tags', 'duration')
