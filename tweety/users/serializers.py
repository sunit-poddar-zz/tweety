# Third party imports

# Django imports
from rest_framework import serializers

# Project level imports

# App level imports
from users.models import User, Tweet


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'profile_pic', 'id', 'following',
                  'followed_by')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
