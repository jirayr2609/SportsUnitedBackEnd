from django.db import models
from accounts.models import User
from teams.models import Team
from leagues.models import League

class Sport(models.Model):
    name = models.CharField(max_length=15)

class Athlete(models.Model):
    def __str__(self):
        return self.user_instance.email

    user_instance = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_athlete'
    )
    # should show what team they are apart of
    team_instance = models.ManyToManyField(
        Team,
        through='AthleteTeamInstance',
        blank=True,
        related_name='team_athletes'
    )
    # in a league, need to be assigned a team
    league_instance = models.ManyToManyField(
        League,
        blank=True,
        related_name='league_athletes'
    )
    bio = models.CharField(max_length=140,blank=True, null=True)
    #sports interested in for recruiting, convert this section to JSON when postgres is involved
    # soccer = models.BooleanField(default=False)
    #etc...

class AthleteTeamInstance(models.Model):
    def __str__(self):
        return self.athlete.user_instance.email + ' | Team: ' + self.team.name
    athlete = models.ForeignKey(
        Athlete,
        on_delete=models.CASCADE
        )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
        )
    is_suspended = models.BooleanField(default=False)

# Can pull stats history for a player by pulling all stats with their athlete id
class SoccerStats(models.Model):

    athlete_instance = models.ManyToManyField(
        Athlete, 
        blank=False,
        related_name='athlete_soccer_stats'
    )
    # JSON field?
    athlete_league = models.ForeignKey(
        League,
        on_delete=models.CASCADE
    )
    # JSON field?
    athlete_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    #Game instance to be added...

    #should sport stats be JSON or regular fields?
    goals = models.IntegerField(blank=True, null=True)
#add new classes for when we add more sports