from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(TeamOwnerPermissions)
admin.site.register(TeamOwnerPermissionList)
admin.site.register(TeamMemberTitles)
admin.site.register(TeamHistory)