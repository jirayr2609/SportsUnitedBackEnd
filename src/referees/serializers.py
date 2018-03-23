from rest_framework import serializers

from .models import *


class RefereeSerializer(serializers.ModelSerializer):# account fields
    # account fields
    username = serializers.CharField(source='user_instance.username', required=False)
    first_name = serializers.CharField(source='user_instance.first_name', required=False)
    last_name = serializers.CharField(source='user_instance.last_name', required=False)

    class Meta:
        model = Referee
        fields = ('username', 'first_name', 'last_name', 'bio',)

    def create(self, validated_data):
        data = validated_data
        register = Referee.objects.create(**data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if value is not None:
                setattr(instance, key, value)

        instance.save()
