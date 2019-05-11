# django imports
from django.contrib import admin

# project imports
from tweety_utils.admin_utils import AbstractModelAdmin

# app imports
from users.models import User, Tweet, Follows


admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Follows)
