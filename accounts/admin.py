from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account


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

admin.site.register(Account, AccountAdmin)

# Register your models here.
