from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import *
from athletes.models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import detail_route

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
            'primary_color': request.data.get('primary_color', None),
            'secondary_color': request.data.get('secondary_color', None),
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
            'primary_color': request.data.get('primary_color', None),
            'secondary_color': request.data.get('secondary_color', None),
            'created_at': request.data.get('created_at', None),
            'updated_at': request.data.get('updated_at', None),
        }
        serializer = TeamSerializer(data=data)
        if serializer.is_valid() and user is not None:
            serializer.update(team, serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Team owner permission functions 
    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='add_athlete')
    def add_athlete(self, request, pk=None):
        team = Team.objects.get(id=pk)
        athlete = Athlete.objects.get(user_instance_id=request.data.get('user_id'))
        # Check if team exists 
        if team is not None:
            # Check if athlete exists
            if athlete is not None:
                permission_id = TeamOwnerPermissionList.objects.get(permission='add_athlete')
                # Check if owner has permission
                owner_permission = TeamOwnerPermissions.objects.filter(owner_instance=request.user.id,team_instance=team,permission=permission_id)
                if owner_permission.exists() is False:
                    print(owner_permission)
                    return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    athlete.team_instance.add(team)
                    return Response({'detail':'Adding athlete...'},status=status.HTTP_200_OK)

                return Response(status=status.HTTP_200_OK)

            else:
                return Response({'detail':'Athlete does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'detail':'Team does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='remove_athlete')
    def remove_athlete(self, request, pk=None):
        team = Team.objects.get(id=pk)
        athlete = Athlete.objects.get(user_instance_id=request.data.get('user_id'))
        # Check if team exists 
        if team is not None:
            # Check if athlete exists
            if athlete is not None:
                permission_id = TeamOwnerPermissionList.objects.get(permission='delete_athlete')
                # Check if owner has permission
                owner_permission = TeamOwnerPermissions.objects.filter(owner_instance=request.user.id,team_instance=team,permission=permission_id)
                if owner_permission.exists() is False:
                    print(owner_permission)
                    return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    athlete.team_instance.remove(team)
                    return Response({'detail':'Removing athlete...'},status=status.HTTP_200_OK)

                return Response(status=status.HTTP_200_OK)

            else:
                return Response({'detail':'Athlete does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'detail':'Team does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='suspend_athlete')
    def suspend_athlete(self, request, pk=None):
        team = Team.objects.get(id=pk)
        athlete = Athlete.objects.get(user_instance_id=request.data.get('user_id'))
        # Check if team exists 
        if team is not None:
            # Check if athlete exists
            if athlete is not None:
                permission_id = TeamOwnerPermissionList.objects.get(permission='suspend_athlete')
                # Check if owner has permission
                owner_permission = TeamOwnerPermissions.objects.filter(owner_instance=request.user.id,team_instance=team,permission=permission_id)
                if owner_permission.exists() is False:
                    return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    team_athlete = AthleteTeamInstance.objects.get(team=team,athlete=athlete)
                    if team_athlete.is_suspended is False:
                        team_athlete.is_suspended = True
                        team_athlete.save()
                        return Response({'detail':'Suspended athlete...'},status=status.HTTP_200_OK)
                    else:
                        team_athlete.is_suspended = False
                        team_athlete.save()
                        return Response({'detail':'Unsuspended athlete...'},status=status.HTTP_200_OK)
                return Response(status=status.HTTP_200_OK)

            else:
                return Response({'detail':'Athlete does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'detail':'Team does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='change_name')
    def change_name(self, request, pk=None):
        team = Team.objects.get(id=pk)
        new_name = request.data.get('name')
        # Check if team exists 
        if team is not None:
            permission_id = TeamOwnerPermissionList.objects.get(permission='change_name')
            # Check if owner has permission
            owner_permission = TeamOwnerPermissions.objects.filter(owner_instance=request.user.id,team_instance=team,permission=permission_id)
            if owner_permission.exists() is False:
                return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
            else:
                team.name = new_name
                team.save()
                return Response({'detail':'Name changed...'},status=status.HTTP_200_OK)
        else:
            return Response({'detail':'Team does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='change_colors')
    def change_colors(self, request, pk=None):
        team = Team.objects.get(id=pk)
        p_color = request.data.get('primary_color')
        s_color = request.data.get('secondary_color')
        # Check if team exists 
        if team is not None:
            permission_id = TeamOwnerPermissionList.objects.get(permission='change_color')
            # Check if owner has permission
            owner_permission = TeamOwnerPermissions.objects.filter(owner_instance=request.user.id,team_instance=team,permission=permission_id)
            print(owner_permission)
            if owner_permission.exists() is False:
                return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
            else:
                if p_color is not None:
                    team.primary_color = p_color
                if s_color is not None:
                    team.secondary_color = s_color
                team.save()
                return Response({'detail':'Colors changed...'},status=status.HTTP_200_OK)
        else:
            return Response({'detail':'Team does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)