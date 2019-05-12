# django imports
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer

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
    if request.user.is_authenticated:
        user_tweets = User.objects.get_ordered_tweets(id)
        serialized_tweets = TweetSerializer(user_tweets, many=True)

        return HttpResponse(JSONRenderer().render(serialized_tweets.data))
    else:
        raise PermissionDenied("Authentication not provided")


def user_home_timeline(request, id):
    if request.user.is_authenticated:
        if request.user.id == id:
            # preventing other logged in users from viewing someone else's home
            tweet_ids = User.objects.get_following_user_tweets(id)
            tweets = Tweet.objects.get_tweets_in_ids(tweet_ids)
            serialized_tweets = TweetSerializer(tweets, many=True)

            return HttpResponse(JSONRenderer().render(serialized_tweets.data))
        else:
            raise HttpResponseBadRequest(content="Can't see someone else's home")
    else:
        raise PermissionDenied("Authentication not provided")
