from rest_framework import serializers

from athletes.serializers import AthleteSerializer
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    team_athletes = AthleteSerializer(many=True)

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = Team.objects.create(**data)