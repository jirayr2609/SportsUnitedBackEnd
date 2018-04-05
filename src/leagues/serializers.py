from rest_framework import serializers
from .models import *
from teams.serializers import TeamSerializer
from accounts.serializers import BaseUserInfoSerializer
from athletes.serializers import AthleteSerializer

class LeagueOwnerPermissionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeagueOwnerPermissionList
        fields = ('permissions',)

class LeagueOwnerPermissionSerializer(serializers.ModelSerializer):
    permission = LeagueOwnerPermissionListSerializer(many=True, required=False)
    user_instance = BaseUserInfoSerializer(required=False)
    title = serializers.CharField(source='title.title', required=False)
    class Meta:
        model = LeagueOwnerPermission 
        exclude = ('id', 'league_instance',)

class LeagueDivisionSerializer(serializers.ModelSerializer):
    division_teams = TeamSerializer(many=True, required=False)

    class Meta:
        model = LeagueDivision
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = LeagueDivision.objects.create(**data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if value is not None:
                setattr(instance, key, value)
        instance.save()

class BasicDivisionSerializer(serializers.ModelSerializer):
    division_teams = TeamSerializer(many=True, required=False)

    class Meta:
        model = LeagueDivision
        exclude = ('leagues',)

class LeagueSerializer(serializers.ModelSerializer):
    league_divisions = BasicDivisionSerializer(many=True, required=False)
    league_athletes = AthleteSerializer(many=True, required=False)
    owner_instance = LeagueOwnerPermissionSerializer(many=True, required=False)
    
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
