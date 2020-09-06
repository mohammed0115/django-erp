from django.contrib import admin

# Register your models here.
# accounts.admin.py
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)



    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    
    
    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'name', 'last_login')}),
    #     ('Permissions', {'fields': (
    #         'is_active', 
    #         'is_staff', 
    #         'is_superuser',
    #         'groups', 
    #         'user_permissions',
    #     )}),
    # )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    
    )
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             'classes': ('wide',),
    #             'fields': ('email', 'password1', 'password2')
    #         }
    #     ),
    # )

    # list_display = ('email',  'is_staff', 'last_login')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)