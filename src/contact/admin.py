from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'credential', 'email', 'beta_registration', 'datesent']

admin.site.register(Contact, ContactAdmin)

# Register your models here.
