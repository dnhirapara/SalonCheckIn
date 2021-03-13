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
    salon = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('id', 'salon', 'name', 'price', 'tags', 'duration')

    def get_salon(self, obj):
        return obj.salon.display_name

    def get_tags(self, obj):
        return TagSerializer(obj.tags).data
