from rest_framework import serializers
from .models import *
from teams.serializers import TeamSerializer
from accounts.serializers import UserInfoserializer
from athletes.serializers import AthleteSerializer

class LeagueSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    league_athletes = AthleteSerializer(many=True)
    class Meta:
        model = League
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = League.objects.create(**data)
