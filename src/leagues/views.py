from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from athletes.models import Athlete, AthleteTeamInstance
from teams.models import Team

class LeagueDivisionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LeagueDivisionSerializer

    def get_queryset(self):
        queryset = LeagueDivision.objects.all()
        return queryset
    #create new division
    def create(self, request):
        permission_classes = (IsAuthenticated,)
        authentication_classes = (TokenAuthentication,)
        user = request.user.id
        # soccer = request.data.get('soccer', False)
        data = {
            'user': user,
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'leagues': request.data.get('league_id', None),
        }
        serializer = LeagueDivisionSerializer(data=data)
        print(data)
        # Check is user exists before creating a division
        if serializer.is_valid() and data['user'] is not None:
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # used for updating 
    def put(self, request):
        user = request.user.id
        division = LeagueDivision.objects.get(id=request.data.get('id',None))
        data = {
            'user': user,
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'leagues': request.data.get('league_id', None),
        }
        print(data)
        serializer = LeagueDivisionSerializer(data=data)
        if serializer.is_valid() and user is not None:
            serializer.update(division, serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class LeagueViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LeagueSerializer

    def get_queryset(self):
        permission_classes = (AllowAny,)
        queryset = League.objects.all()
        return queryset

    #create new league
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
            'league_start': request.data.get('league_start', None),
            'league_end': request.data.get('league_end', None),
            'playoff_start': request.data.get('playoff_start', None),
        }
        serializer = LeagueSerializer(data=data)
        # Check is user exists before creating a league
        if serializer.is_valid() and data['user'] is not None:
            new_data = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # used for updating
    def put(self, request):
        user = request.user.id
        league = League.objects.get(id=request.data.get('id',None))
        data = {
            'name': request.data.get('name', None),
            'abbrev': request.data.get('abbrev', None),
            'bio': request.data.get('bio', None),
            'league_start': request.data.get('league_start', None),
            'league_end': request.data.get('league_end', None),
            'playoff_start': request.data.get('playoff_start', None),
        }
        serializer = LeagueSerializer(data=data)
        if serializer.is_valid() and user is not None:
            serializer.update(league, serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # League owner permissions
    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='add_athlete')
    def add_athlete(self, request, pk=None):
        league = League.objects.get(id=pk)
        athlete = Athlete.objects.get(user_instance_id=request.data.get('user_id'))
        # Check if league exists 
        if league is not None:
            # Check if athlete exists
            if athlete is not None:
                permission_id = LeagueOwnerPermissionList.objects.get(permissions='add_athlete')
                # Check if owner has permission
                owner_permission = LeagueOwnerPermission.objects.filter(user_instance=request.user.id,league_instance=league,permission=permission_id)
                if owner_permission.exists() is False:
                    print(owner_permission)
                    return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    athlete.league_instance.add(league)
                    return Response({'detail':'Adding athlete...'},status=status.HTTP_200_OK)

                return Response(status=status.HTTP_200_OK)

            else:
                return Response({'detail':'Athlete does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'detail':'League does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='remove_athlete')
    def remove_athlete(self, request, pk=None):
        league = League.objects.get(id=pk)
        athlete = Athlete.objects.get(user_instance_id=request.data.get('user_id'))
        # Check if league exists 
        if league is not None:
            # Check if athlete exists
            if athlete is not None:
                permission_id = LeagueOwnerPermissionList.objects.get(permissions='delete_athlete')
                # Check if owner has permission
                owner_permission = LeagueOwnerPermission.objects.filter(user_instance=request.user.id,league_instance=league,permission=permission_id)
                if owner_permission.exists() is False:
                    print(owner_permission)
                    return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    athlete.league_instance.remove(league)
                    return Response({'detail':'Deleting athlete...'},status=status.HTTP_200_OK)

                return Response(status=status.HTTP_200_OK)

            else:
                return Response({'detail':'Athlete does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'detail':'League does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)


    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='suspend_athlete')
    def suspend_athlete(self, request, pk=None):
        league = League.objects.get(id=pk)
        team = Team.objects.get(id=request.data.get('team_id'))
        athlete = Athlete.objects.get(user_instance_id=request.data.get('user_id'))
        # Check if team exists 
        if league is not None:
            # Check if athlete exists
            if athlete is not None:
                permission_id = LeagueOwnerPermissionList.objects.get(permissions='suspend_athlete')
                # Check if owner has permission
                owner_permission = LeagueOwnerPermission.objects.filter(user_instance=request.user.id,league_instance=league,permission=permission_id)
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
        league = League.objects.get(id=pk)
        new_name = request.data.get('name')
        # Check if league exists 
        if league is not None:
            permission_id = LeagueOwnerPermissionList.objects.get(permissions='change_name')
            # Check if owner has permission
            owner_permission = LeagueOwnerPermission.objects.filter(user_instance=request.user.id,league_instance=league,permission=permission_id)
            if owner_permission.exists() is False:
                return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
            else:
                league.name = new_name
                league.save()
                return Response({'detail':'Name changed...'},status=status.HTTP_200_OK)
        else:
            return Response({'detail':'League does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_name='change_colors')
    def change_colors(self, request, pk=None):
        league = League.objects.get(id=pk)
        p_color = request.data.get('primary_color')
        s_color = request.data.get('secondary_color')
        # Check if league exists 
        if league is not None:
            permission_id = LeagueOwnerPermissionList.objects.get(permissions='change_color')
            # Check if owner has permission
            owner_permission = LeagueOwnerPermission.objects.filter(user_instance=request.user.id,league_instance=league,permission=permission_id)
            print(owner_permission)
            if owner_permission.exists() is False:
                return Response({'detail':'User does not have required permission.'},status=status.HTTP_400_BAD_REQUEST)
            else:
                if p_color is not None:
                    league.primary_color = p_color
                if s_color is not None:
                    league.secondary_color = s_color
                league.save()
                return Response({'detail':'Colors changed...'},status=status.HTTP_200_OK)
        else:
            return Response({'detail':'League does not exist.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)