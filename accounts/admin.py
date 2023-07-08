from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account, UserProfile
from django.utils.html import format_html



class AccountAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    #convert the following fields to links to edit page
    list_display_links = ('email', 'first_name','last_name')
    readonly_fields = ('last_login', 'date_joined')
    #- means descending
    ordering = ('-date_joined',)


#through this, we're converting password on the Accounts page, read-only
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail' ,'user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

# Register your models here.
