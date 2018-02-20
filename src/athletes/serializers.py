from rest_framework import serializers
from .models import *

class AthleteSerializer(serializers.ModelSerializer):
    # account fields
    username = serializers.CharField(source='id.username', required=False)
    first_name = serializers.CharField(source='id.first_name', required=False)
    last_name = serializers.CharField(source='id.last_name', required=False)

    class Meta:
        model = Athlete
        fields = ('username', 'first_name', 'last_name','bio', 'soccer')

    def create(self, validated_data):
        data = validated_data
        register = Athlete.objects.create(**data)