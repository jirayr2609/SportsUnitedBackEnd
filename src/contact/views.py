from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	serializer_class = ContactSerializer
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

		serializer = ContactSerializer(data=registerData)
		if serializer.is_valid():

			new_data = serializer.create(serializer.validated_data)
			return Response(status = status.HTTP_201_CREATED)
		else:

			return Response(status = status.HTTP_400_BAD_REQUEST)
