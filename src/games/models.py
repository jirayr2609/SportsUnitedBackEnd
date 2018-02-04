from django.db import models
from teams.models import Team
from leagues.models import LeagueLocations
from accounts.models import User

class Sport(models.Model):
    sportID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    homeTeam = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    awayTeam = models.ForeignKey(
        Team,
        related_name='awayTeam',
        on_delete=models.CASCADE
    )
    day = models.DateField()
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    location = models.ForeignKey(
        LeagueLocations,
        related_name='homeTeam',
        on_delete=models.CASCADE
    )

class SoccerGame(models.Model):
    gameID = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE
    )
    # fields with unique soccer game stats

#create a new model for each new sport added to the platform...

class Referee(models.Model):
    userID = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    gameID = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )