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

from .models import *
from .serializers import *

# Create your views here.
# class CustomRegisterView(RegisterView):
# 	def get_response_data(self, user):
# 		print("IN CUSTOM REGISTER VIEW")
# 		print (self.request)
# 		if allauth_settings.EMAIL_VERIFICATION == \
# 				allauth_settings.EmailVerificationMethod.OPTIONAL:
# 					return TokenSerializer(user.auth_token).data

class Logout(LogoutView):
	permission_classes = (AllowAny,) 
	authentication_classes = (TokenAuthentication,)

class CustomLoadUserView(UserDetailsView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

class CustomVerifyEmail(VerifyEmailView):
	permission_classes = (AllowAny,) 
	authentication_classes = (TokenAuthentication,)

class SportaRegistrationViewSet(viewsets.ModelViewSet):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializers_class = SportaRegistrationSerializer