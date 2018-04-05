from django.contrib import admin
from .models import *

admin.site.register(League)
admin.site.register(LeagueOwnerPermission)
admin.site.register(LeagueOwnerPermissionList)
admin.site.register(LeagueHistory)
admin.site.register(LeagueDivision)
admin.site.register(LeagueMemberTitles)