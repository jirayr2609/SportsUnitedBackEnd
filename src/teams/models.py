from django.db import models
from accounts.models import User
from athletes.models import Sport

# Core team model
class Team(models.Model):
    sport_id = models.ForeignKey(
        Sport, 
        on_delete=models.CASCADE,
    )
    captain = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)
    bio = models.CharField(max_length=125, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class TeamOwnerPermissions(models.Model):
    permission = models.CharField(max_length=20)

# Keeps track of all team owners
class TeamOwner(models.Model):
    team_id = models.ForeignKey(
        Team, 
        on_delete=models.CASCADE,
        )
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        )
    permission = models.ForeignKey(
        TeamOwnerPermissions, 
        on_delete=models.CASCADE,
        )

# Keeps track of all team players
class TeamPlayers(models.Model):
    team_id = models.ForeignKey(
        Team, 
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )
    suspended = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)

# Keeps track of all team accolades
class TeamAccolades(models.Model):
    team_id = models.ForeignKey(
        Team, 
        on_delete=models.CASCADE,
    )
    league_id = models.IntegerField()
    accolade =  models.CharField(max_length=50)