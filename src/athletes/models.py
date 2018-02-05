from django.db import models
from accounts.models import User 

class Sport(models.Model):
    name = models.CharField(max_length=15)

class Athlete(models.Model):
    id = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key=True,
    )
    bio = models.CharField(max_length=125)

    #sports interested in for recruiting
    soccer = models.BooleanField(default=False)
    #basketball = models.BooleanField(default=False)
    #baseball = models.BooleanField(default=False)
    #tennis = models.BooleanField(default=False)
    #etc...

class SoccerAthlete(models.Model):
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        )
    #input sport stats below...
#add new classes for when we add more sports