from django.db import models
from leagues.models import LeagueDivision
from accounts.models import User

# Core team model
class Team(models.Model):
    # sport_instance = models.ManyToManyField(
    #     Sport, 
    #     blank=True,
    # )
    # Can be apart of multiple leagues
    def __str__(self):
        return self.name

    division_instance = models.ManyToManyField(
        LeagueDivision,
        blank=True,
        related_name='division_teams',
        )
    
    name = models.CharField(max_length=30, blank=False, null=False)
    abbrev = models.CharField(max_length=4, blank=True, null=True)
    bio = models.CharField(max_length=125, blank=True, null=True)
    primary_color = models.CharField(max_length=16, null=True, blank=True)
    secondary_color = models.CharField(max_length=16, null=True, blank=True)
    # Accolade as JSON field
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class TeamMemberTitles(models.Model):
    def __str__(self):
        return self.title
    title_list = (
        ('Captain', 'Captain'),
        ('Co-Captain', 'Co-Captain')
        )
    title = models.CharField(max_length=200, choices=title_list, null=True, blank=True)

class TeamOwnerPermissionList(models.Model):
    def __str__(self):
        return self.permission
    permission_list = (
        ('add_athlete','Add Athlete'),
        ('delete_athlete','Delete Athlete'),
        ('suspend_athlete','Suspend Athlete'),
        ('change_name','Change Team Name'),
        ('change_color','Change Team Colors'),
        )
    
    permission = models.CharField(max_length=200, choices=permission_list, null=True,blank=True)

class TeamOwnerPermissions(models.Model):
    def __str__(self):
        return 'Owner: ' + self.owner_instance.email + ' | Title: ' + self.title.title + ' | Team: ' + self.team_instance.name
    owner_instance = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_owner_instance'
        )
    team_instance = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team_owners'
        )
    
    permission = models.ManyToManyField(
        TeamOwnerPermissionList,
        blank=True,
        related_name='permission_list'
        )
    title = models.ForeignKey(
        TeamMemberTitles,
        on_delete=models.CASCADE
        )

class TeamHistory(models.Model):
    team_instance = models.ManyToManyField(
        Team,
        related_name='team_history'
        )
    league_instance = models.ManyToManyField(
        LeagueDivision,
        related_name='league_division'
        )
    wins = models.IntegerField(blank=False, null=False)
    losses = models.IntegerField(blank=False, null=False)