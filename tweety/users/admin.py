# django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# project imports
from tweety_utils.admin_utils import AbstractModelAdmin

# app imports
from users.models import User, Tweet
from users.forms import CustomUserCreationForm, CustomUserChangeForm


admin.site.register(User)
admin.site.register(Tweet)
# admin.site.register(Follows)
