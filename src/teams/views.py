from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework import status

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        #filtering
        
        #ordering
        order = self.request.query_params.get('order_by', None)
        if order is not None:
            queryset = queryset.order_by(order)

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

    #update athlete info --need to test
    def update(self,request):
        instance = self.get_object()
        # instance.soccer = request.get('soccer', False)
        instance.save()

        serializer = self.get_serializer(instance)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(status=status.HTTP_200_OK)
        else:
            # print(serializer)
            return Response(status=status.HTTP_400_BAD_REQUEST)
