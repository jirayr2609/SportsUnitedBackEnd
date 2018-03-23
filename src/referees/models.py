from django.db import models
from accounts.models import User
from games.models import Game
from leagues.models import League

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=15)

class Referee(models.Model):
    user_instance= models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_referee'
    )
    league_instance=models.ManyToManyField(
        League,
        blank = True,
        related_name='league_referee'

    )
    game_instance=models.ManyToManyField(
        Game,
        blank = True,
        related_name='game_referee'

    )
    bio = models.CharField(max_length=125)
