from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import *
from athletes.serializers import *

# This Serializer is invoked for requests on rest-auth/user. It returns basic information about user
class UserSerializer(serializers.ModelSerializer):
	request_login = serializers.SerializerMethodField()
	request_load = serializers.SerializerMethodField()

	def get_request_login(self, obj):
		returned_value = False
		try:
			if self.context['request'].method == 'POST':
				returned_value =  True
			else:
				returned_value = False
		except:
			returned_value = False

		return returned_value

	def get_request_load(self, obj):
		returned_value = False
		try:
			if self.context['request'].method == 'POST':
				returned_value =  False
			else:
				returned_value = True
		except:
			returned_value = False

		return returned_value

	class Meta:
		model = User
		fields = ('id', 'request_load', 'request_login', 'email', 'username', 'first_name', 'last_name', 'joined', 'date_of_birth', 'is_active', 'is_admin', 'is_staff', 'credential', 'created_at', 'updated_at')

class SportaRegistrationSerializer(serializers.Serializer):
	class meta:
		model = User
		fields = ('first_name', 'last_name', 'credential', 'username')

	def update(self, instance, validated_data):
		print ("here")
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.credential = validated_data.get('credential', instance.credential)
		instance.username = validated_data.get('username', instance.username)
		instance.save()
		return instance

class UserInfoserializer(serializers.ModelSerializer):
	user_athlete = AthleteInfoSerializer(many=False)
	class Meta:
		model = User
		exclude = ('password',)

class BaseUserInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('email', 'username', 'first_name', 'last_name')