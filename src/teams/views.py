from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        #filtering
        
        #ordering
        # order = self.request.query_params.get('order_by', None)
        # if order is not None:
        #     queryset = queryset.order_by(order)

        return queryset

    #create new team
    def create(self, request):
        permission_classes = (IsAuthenticated,)
        authentication_classes = (TokenAuthentication,)
        user = request.user.id
        # soccer = request.data.get('soccer', False)
        data = {
            'user': user,
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'bio': request.data.get('bio', None),
            'created_at': request.data.get('created_at', None),
            'updated_at': request.data.get('updated_at', None),
        }
        serializer = TeamSerializer(data=data)
        # Check is user exists before creating a team
        print(request.user)
        if serializer.is_valid() and data['user'] is not None:
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # used for updating 
    def put(self, request):
        user = request.user.id
        team = Team.objects.get(id=request.data.get('id',None))
        data = {
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'bio': request.data.get('bio', None),
            'created_at': request.data.get('created_at', None),
            'updated_at': request.data.get('updated_at', None),
        }
        serializer = TeamSerializer(data=data)
        if serializer.is_valid() and user is not None:
            serializer.update(team, serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)