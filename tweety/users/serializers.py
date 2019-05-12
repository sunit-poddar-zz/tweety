# Third party imports

# Django imports
from rest_framework import serializers

# Project level imports

# App level imports
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'profile_pic', 'id')
