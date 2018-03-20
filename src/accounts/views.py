from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from allauth.account import app_settings as allauth_settings

from rest_auth.views import UserDetailsView
from rest_auth.registration.views import RegisterView
from rest_auth.app_settings import (TokenSerializer)
from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import LogoutView
from rest_framework.response import Response

from athletes.models import *
from .models import *
from .serializers import *

from django.db import connection

class VerifyEmailViewSet(viewsets.GenericViewSet):
	permission_classes = (AllowAny,) # user making a request to this view is anonymous
	def create(self, request):
		query_param = self.request.query_params.get('token', None)

		if EmailConfirmation.objects.filter(token=query_param).exists():
			email_confirm_instance = EmailConfirmation.objects.get(token=query_param)
			user_id = email_confirm_instance.user.id
			email_confirm_instance.delete()
			user_instance = User.objects.get(id=user_id)
			user_instance.is_active = True
			user_instance.save()

			user_quick_info = {
				'id': user_instance.id,
				'email': user_instance.email,
				'is_active': True,
				'new_register': True
			}

			return Response(user_quick_info, status=status.HTTP_201_CREATED)
		else:
			return Response({'error': 'token invalid'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(LogoutView):
	permission_classes = (AllowAny,)
	authentication_classes = (TokenAuthentication,)

class CustomLoadUserView(UserDetailsView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

class VerifyUsernameViewSet(viewsets.GenericViewSet):
	permission_classes = (AllowAny,)
	def create(self, request):
		check_user = request.data['username']
		queryset = User.objects.all().filter(username=check_user)
		# print(queryset)
		if queryset.exists():
			return Response({'available': 'false'})
		else:
			return Response({'available': 'true'})

class SportaRegistrationViewSet(viewsets.ModelViewSet):

	#permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = SportaRegistrationSerializer

		#def put(self):
		#print ("REQUEST")
		#print (request.user)
		#user = request.user
		#return Response(status=status.HTTP_201_CREATED)"""
	def put(self, request, format=None):
		user = request.user
		credential = request.data.get('credential', None)
		first_name = request.data.get('firstName', None)
		last_name = request.data.get('lastName', None)
		username = request.data.get('username',None)

		print(request.data)

		if User.objects.filter(email=user.email).exists():
			user_instance = User.objects.get(email=user.email)
		else:
			error = "Unable to Verify"
			return Response(error, status=status.HTTP_400_BAD_REQUEST)

		registerData = {
            'first_name': first_name,
            'last_name': last_name,
            'credential': credential,
            'username': username,
        }
		registerData = dict(filter(lambda x: x[1] != "", registerData.items()))



		serializer = SportaRegistrationSerializer(data=registerData)
		if serializer.is_valid():
			serializer.update(user_instance, registerData )
			return Response(status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class UserInfoViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = (AllowAny,)
	serializer_class = UserInfoserializer
	def get_queryset(self):
		print(self.request.query_params.get('id',None))
		queryset = User.objects.select_related().filter(id=1)
		return queryset