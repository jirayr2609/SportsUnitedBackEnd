from django.db import models
from accounts.models import User
from teams.models import Team
from leagues.models import League

class Sport(models.Model):
    name = models.CharField(max_length=15)

class Athlete(models.Model):
    user_instance = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_athlete'
    )
    team_instance = models.ManyToManyField(
        Team,
        blank=True,
        related_name='team_athletes'
    )
    league_instance = models.ManyToManyField(
        League,
        blank=True,
        related_name='league_athletes'
    )
    bio = models.CharField(max_length=125)
    # league_mvp = models.ManyToManyField(
    #     League,
    #     blank=True
    # )
    #sports interested in for recruiting, convert this section to JSON when postgres is involved
    # soccer = models.BooleanField(default=False)
    #etc...

class SoccerStats(models.Model):
    athlete_instance = models.ManyToManyField(
        Athlete, 
        blank=False,
        related_name='athlete_soccer_stats'
        )

    athlete_league = models.ManyToManyField(
        League,
        blank=False,
        related_name='athlete_league_history',
    )

    athlete_team = models.ManyToManyField(
        Team,
        blank=False,
        related_name='athlete_team_history'
    )
    #Game instance to be added...

    #input sport stats below...
    goals = models.IntegerField(blank=True, null=True)
#add new classes for when we add more sports