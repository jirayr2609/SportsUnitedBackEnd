from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import *

# This Serializer is invoked for requests on rest-auth/user. It returns basic information about user
class UserSerializer(serializers.ModelSerializer):
	request_login = serializers.SerializerMethodField()
	request_load = serializers.SerializerMethodField()
	
	def get_request_login(self, obj):
		if self.context['request'].method == 'POST':
			return True
		else:
			return False

	def get_request_load(self, obj):
		if self.context['request'].method == 'POST':
			return False
		else:
			return True

	class Meta:
		model = User
		fields = ('id', 'request_load', 'request_login', 'email', 'username', 'first_name', 'last_name', 'joined', 'date_of_birth', 'is_active', 'is_admin', 'is_staff', 'credential', 'created_at', 'updated_at')


class SportaRegistrationSerializer(serializers.Serializer):
	class meta:
		model = User		
	# def create(self, validated_data):
	# 	user = User.objects.create(**validated_data)
	# 	return user

