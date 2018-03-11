from django.contrib import admin
from .models import *

admin.site.register(League)
# admin.site.register(LeagueOwner)
admin.site.register(LeagueOwnerPermissions)
# admin.site.register(LeagueTeams)
admin.site.register(LeagueHistory)
admin.site.register(LeagueDivision)