from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import *

class SportaRegistrationSerializer(serializers.Serializer):
	class meta:
		model = User
	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		return user