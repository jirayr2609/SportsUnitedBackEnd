from rest_framework import serializers

from athletes.serializers import AthleteSerializer
from accounts.serializers import BaseUserInfoSerializer
from .models import *

class TeamOwnerPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOwnerPermissionList
        fields = ('permission',)

class TeamOwnerSerializer(serializers.ModelSerializer):
    owner_instance = BaseUserInfoSerializer(required=False)
    permission = TeamOwnerPermissionSerializer(many=True,required=False)
    title = serializers.CharField(source='title.title', required=False)
    class Meta:
        model = TeamOwnerPermissions
        fields = ('owner_instance', 'title','permission')

class TeamSerializer(serializers.ModelSerializer):
    team_athletes = AthleteSerializer(many=True, required=False)
    team_owners = TeamOwnerSerializer(many=True, required=False)
    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = Team.objects.create(**data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if value is not None:
                setattr(instance, key, value)

        instance.save()