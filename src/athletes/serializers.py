from rest_framework import serializers

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
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if value is not None:
                setattr(instance, key, value)

        instance.save()

class SoccerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerStats
        fields = '__all__'

class AthleteInfoSerializer(serializers.ModelSerializer):
    athlete_soccer_stats = SoccerStatsSerializer(many=True)
    class Meta:
        model = Athlete
        fields = '__all__'