# from django.contrib.postgres.fields import JSONField
from django.db import models
# from teams.models import Team
# from athletes.models import Sport

# Core league data structure
class League(models.Model):
    # sport_instance = models.ForeignKey(
    #     Sport, 
    #     on_delete=models.CASCADE,
    #     related_name='sports'
    # )
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)
    bio = models.CharField(max_length=125, blank=True, null=True)
    # locations = JSONField(default=dict, blank=True, null=True)

    league_start = models.DateTimeField(blank=True, null=True)
    league_end = models.DateTimeField(blank=True, null=True)
    playoff_start = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class LeagueOwnerPermissions(models.Model):
    league_instance = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    permission = models.CharField(max_length=20)

class LeagueDivision(models.Model):
    leagues = models.ManyToManyField(
        League,
        related_name='league_divisions'
    )
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)

#Should be populated on the end of a season
class LeagueHistory(models.Model):
    league_instance = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    # league_mvp = models.ForeignKey(
    #     User,
    #     related_name='leagueMVP',
    #     on_delete=models.CASCADE,
    # )
    champion = models.CharField(max_length=30, blank=False, null=False)
    # finals_mvp = models.ForeignKey(
    #     User,
    #     related_name='finalsMVP',
    #     on_delete=models.CASCADE,
    # )
    league_start = models.DateTimeField(blank=True, null=True)
    league_end = models.DateTimeField(blank=True, null=True)
