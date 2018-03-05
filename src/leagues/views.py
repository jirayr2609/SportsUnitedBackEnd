from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework import status

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

    def get_queryset(self):
        queryset = League.objects.all()

        return queryset

    #create new league
    def create(self, request):
        user = request.user
        if serializer.is_valid():
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer)
            return Response(status=status.HTTP_400_BAD_REQUEST)
