from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework import status

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

    def get_queryset(self):
        queryset = Athlete.objects.all()
        #filtering
        id = self.request.query_params.get('id',None) #can get an individual athlete by passing their id
        if id is not None:
            queryset = queryset.filter(id=id)
        #Discuss implementation of setting preferred locations
        # location = self.request.query_params.get('location',None)
        # if location is not None:
        #     queryset = queryset.filter(preferred_location=location)
        
        #ordering
        order = self.request.query_params.get('order_by', None)
        if order is not None:
            queryset = queryset.order_by(order)

        return queryset

    #create new athlete
    def create(self, request):
        user = request.user.id
        bio = request.data.get('bio', None)
        soccer = request.data.get('soccer', False)
        data = {
            'user': user,
            'bio': bio,
            'soccer': soccer,
        }
        print(data)
        serializer = AthleteSerializer(data=data)
        if serializer.is_valid():
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #update athlete info --need to test
    def update(self,request):
        instance = self.get_object()
        instance.bio = request.get('bio', None)
        instance.soccer = request.get('soccer', False)
        instance.save()

        serializer = self.get_serializer(instance)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(status=status.HTTP_200_OK)
        else:
            print(serializer)
            return Response(status=status.HTTP_400_BAD_REQUEST)
