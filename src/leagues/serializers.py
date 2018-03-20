from rest_framework import serializers
from .models import *
from teams.serializers import TeamSerializer
from accounts.serializers import UserInfoserializer
from athletes.serializers import AthleteSerializer

class LeagueDivisionSerializer(serializers.ModelSerializer):
    division_teams = TeamSerializer(many=True, required=False)

    class Meta:
        model = LeagueDivision
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = League.objects.create(**data)

class LeagueSerializer(serializers.ModelSerializer):
    league_divisions = LeagueDivisionSerializer(many=True, required=False)
    league_athletes = AthleteSerializer(many=True, required=False)

    class Meta:
        model = League
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = League.objects.create(**data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if value is not None:
                setattr(instance, key, value)

        instance.save()
