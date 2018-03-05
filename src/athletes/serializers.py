from rest_framework import serializers

from accounts.serializers import UserInfoserializer
from .models import *

class AthleteSerializer(serializers.ModelSerializer):# account fields
    # account fields
    username = serializers.CharField(source='user_instance.username', required=False)
    first_name = serializers.CharField(source='user_instance.first_name', required=False)
    last_name = serializers.CharField(source='user_instance.last_name', required=False)
    
    class Meta:
        model = Athlete
        fields = ('username', 'first_name', 'last_name', 'bio',)

    def create(self, validated_data):
        data = validated_data
        register = Athlete.objects.create(**data)
    