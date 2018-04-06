from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = Contact.objects.create(**data)
