# from django.contrib.postgres.fields import JSONField
from django.db import models 
# from teams.models import Team
# from athletes.models import Sport
from accounts.models import User

# Core league data structure
class League(models.Model):
    def __str__(self):
        return self.name
    # sport_instance = models.ForeignKey(
    #     Sport, 
    #     on_delete=models.CASCADE,
    #     related_name='sports'
    # )

    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)
    bio = models.CharField(max_length=125, blank=True, null=True)
    primary_color = models.CharField(max_length=16, null=True, blank=True)
    secondary_color = models.CharField(max_length=16, null=True, blank=True)
    # locations = JSONField(default=dict, blank=True, null=True)

    league_start = models.DateField(blank=True, null=True)
    league_end = models.DateField(blank=True, null=True)
    playoff_start = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

class LeagueMemberTitles(models.Model):
    def __str__(self):
        return self.title

    title_list = (
        ('Owner', 'Owner'),
        ('Co-Owner', 'Co-Owner')
        )
    title = models.CharField(max_length=200, choices=title_list, null=True, blank=True)


class LeagueOwnerPermissionList(models.Model):
    def __str__(self):
        return self.permissions

    # Add change schedule in the future
    permission_list = (
        ('add_athlete','Add Athlete'),
        ('delete_athlete','Delete Athlete'),
        ('suspend_athlete','Suspend Athlete'),
        ('change_name','Change League Name'),
        ('change_color','Change League Colors'),
    )
    permissions = models.CharField(max_length=200, choices=permission_list, null=True,blank=True, verbose_name="Permission")


class LeagueOwnerPermission(models.Model):
    def __str__(self):
        return self.user_instance.email + ' | League: ' + self.league_instance.name 
    
    user_instance = models.ForeignKey(
        User,
        related_name='league_owner_instance',
        on_delete=models.CASCADE
    )
    league_instance = models.ForeignKey(
        League,
        related_name='owner_instance',
        on_delete=models.CASCADE
    )
    permission = models.ManyToManyField(
        LeagueOwnerPermissionList,
        blank=True,
        related_name='permission_list'
        )
    title = models.ForeignKey(
        LeagueMemberTitles,
        on_delete=models.CASCADE
        )

class LeagueDivision(models.Model):
    def __str__(self):
        return 'League: ' + self.leagues.name + ' | Division: ' + self.name 
    
    leagues = models.ForeignKey(
        League,
        related_name='league_divisions',
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)

#Should be populated on the end of a season
class LeagueHistory(models.Model):
    def __str__(self):
        return self.league_instance + ' | Start: ' + self.league_start + ' | End: '+ self.league_end
    
    league_instance = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    league_start = models.DateField(blank=True, null=True)
    league_end = models.DateField(blank=True, null=True)
    # Store everything at the end of season in the form of a JSON
