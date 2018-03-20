from django.db import models
# from athletes.models import Sport
from leagues.models import LeagueDivision
# Core team model
class Team(models.Model):
    # sport_instance = models.ManyToManyField(
    #     Sport, 
    #     blank=True,
    # )
    # Can be apart of multiple leagues
    division_instance = models.ManyToManyField(
        LeagueDivision,
        blank=True,
        related_name='division_teams',
    )
    
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)
    bio = models.CharField(max_length=125, blank=True, null=True)
    # Accolade as JSON field
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class TeamOwnerPermissions(models.Model):
    permission = models.CharField(max_length=20)