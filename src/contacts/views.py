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

from .models import *
from .serializers import *


# Create your views here.

class ContactRegistrationViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	serializer_class = ContactRegistrationSerializer
	def create(self, request):
		credential = request.data.get('credential', None)
		name = request.data.get('name', None)
		email = request.data.get('email',None)
		message = request.data.get('message', None)
		datesent = request.data.get('datesent',None)
		registerData = {
            'name': name,
			'credential': credential,
            'email': email,
            'message': message,
            'datesent': datesent
        }

		serializer = ContactRegistrationSerializer(data=registerData)
		if serializer.is_valid():

			new_data = serializer.create(serializer.validated_data)
			return Response(status = status.HTTP_201_CREATED)
		else:

			return Response(status = status.HTTP_400_BAD_REQUEST)
