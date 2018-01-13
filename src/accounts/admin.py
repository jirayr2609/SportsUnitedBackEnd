from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# class UserAdmin(BaseUserAdmin):
#     search_fields = ('email', 'first_name')
#     ordering = ('email',)
#     list_display = ('id', 'email', 'first_name')

#     fieldsets = (
#         (None, {'fields': ('email', 'phone', 'password')}),
#         (('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (('Permissions'), {'fields': ('is_active', 'is_staff')}),
#         (('Important dates'), {'fields': ('last_login')}),
#     )


# admin.site.register(User, UserAdmin)

class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)