# django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# project imports
from tweety_utils.admin_utils import AbstractModelAdmin

# app imports
from users.models import User, Tweet, Follows
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)


# admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Follows)
