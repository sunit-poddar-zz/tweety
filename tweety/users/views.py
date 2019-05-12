# django imports
from django.db.models import Subquery
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated


# app imports
from users.models import User, Tweet
from users.serializers import UserSerializer, TweetSerializer


class CustomUserViewset(ModelViewSet):
    """
    Custom viewset for 'user' model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering_fields = ['modified_at', 'created_at']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class TweetViewset(ModelViewSet):
    """

    """

    queryset = Tweet.objects.all().prefetch_related('user')
    serializer_class = TweetSerializer

    permission_classes = [IsAuthenticated]

    search_fields = ['user', 'text']


def user_profile_timeline(request, id):
    print(id)
    if request.user.is_authenticated:
        return User.objects.get(id=id).tweet.all().order_by('-created_at')
    else:
        raise PermissionDenied("Authentication not provided")


def user_home_timeline(request, id):
    if request.user.is_authenticated:
        if request.user.id == id:
            user = User.objects.get(id=id).following.annotate()
        else:
            raise PermissionDenied("Can't see someone else's home")
    else:
        raise PermissionDenied("Authentication not provided")
