from django.db import models
from teams.models import Team
from leagues.models import League
from accounts.models import User
from athletes.models import Sport

class Game(models.Model):
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    away_team = models.ForeignKey(
        Team,
        related_name='away_team',
        on_delete=models.CASCADE
    )
    day = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.ForeignKey( # Pull locations from this when implemented
        League,
        related_name='home_team',
        on_delete=models.CASCADE
    )

class SoccerGame(models.Model):
    game_instance = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )
    # fields with unique soccer game stats

#create a new model for each new sport added to the platform...

class Referee(models.Model):
    user_instance = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    game_instance = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )