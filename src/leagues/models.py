from django.db import models
from accounts.models import User
from teams.models import Team

# Core league data structure
class League(models.Model):
    leagueID = models.AutoField(primary_key=True)
    sportID = 0 # we need to make a sport table to hold all of the sport names and sport properties
    captain = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)
    bio = models.CharField(max_length=125, blank=True, null=True)
    leagueStart = models.DateTimeField(blank=True, null=True)
    leagueEnd = models.DateTimeField(blank=True, null=True)
    playoffStart = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

#Stores all locations for a league
class LeagueLocations(models.Model):
    leagueID = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    location = models.CharField(max_length=50, blank=True, null=True)

class LeagueOwnerPermissions(models.Model):
    permissionID = models.AutoField(primary_key=True)
    permission = models.CharField(max_length=20)

#Keeps track of the different owners of a league
class LeagueOwner(models.Model):
    leagueID = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    ownerID = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    permission = models.ForeignKey(
        LeagueOwnerPermissions,
        on_delete=models.CASCADE,
    )

#Keeps a track of all the leagues in a league
class LeagueTeams(models.Model):
    leagueID = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    teamID = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

#Should be populated on the end of a season
class LeagueHistory(models.Model):
    leagueID = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    leagueMVP = models.ForeignKey(
        User,
        related_name='leagueMVP',
        on_delete=models.CASCADE,
    )
    champion = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    finalsMVP = models.ForeignKey(
        User,
        related_name='finalsMVP',
        on_delete=models.CASCADE,
    )
    leagueStart = models.DateTimeField(blank=True, null=True)
    leagueEnd = models.DateTimeField(blank=True, null=True)
