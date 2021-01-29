from rest_framework import serializers
from django.core.exceptions import (
    ValidationError
)
from SalonServices.models import Service, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'tags', 'duration')
