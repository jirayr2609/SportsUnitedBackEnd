from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class RefereeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AthleteSerializer

    def get_queryset(self):
        queryset = Referee.objects.all()

        return queryset

    #create new athlete
    def create(self, request):
        permission_classes = (IsAuthenticated,)
        authentication_classes = (TokenAuthentication,)
        user = request.user.id
        bio = request.data.get('bio', None)
        # soccer = request.data.get('soccer', False)
        data = {
            'user': user,
            'bio': bio,
        }
        print(data)
        serializer = RefereeSerializer(data=data)
        if serializer.is_valid():
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # used for updating
    def put(self, request):
        user = request.user.id
        user_instance = Referee.objects.get(user_instance_id=user)
        data = {
            'bio': request.data.get('bio',None),
        }
        serializer = RefereeSerializer(data=data)
        if serializer.is_valid() and user is not None:
            serializer.update(user_instance, serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
