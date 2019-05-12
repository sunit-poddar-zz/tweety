from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserQuerySet(models.query.QuerySet):
    """
    Custom querysets for 'User' model
    """

    def get_ordered_tweets(self, user_id):
        return self.get(id=user_id).tweet.all().order_by('-created_at')

    def get_following_user_tweets(self, user_id):
        tweet_ids = list(self.get(id=user_id).following.values_list('tweet', flat=True))
        return tweet_ids


class UserManager(BaseUserManager, models.Manager):
    """
    Custom model manager for User model
    """

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create_user(self, first_name, last_name, username, email, password=None):

        if username is None:
            raise TypeError('Users must have a username.')

        if first_name is None:
            raise TypeError('Users must have a first name.')

        if last_name is None:
            raise TypeError('Users must have a last name.')

        if email is None:
            raise TypeError('Users must have a email address.')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, last_name, username, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(first_name, last_name, username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def get_ordered_tweets(self, user_id):
        return self.get_queryset().get_ordered_tweets(user_id)

    def get_following_user_tweets(self, user_id):
        return self.get_queryset().get_following_user_tweets(user_id)


class TweetQuerySet(models.query.QuerySet):
    """
    Custom querysets for 'Tweet' model
    """

    def get_tweets_in_ids(self, list_of_tweet_ids):
        return self.filter(id__in=list_of_tweet_ids).order_by('-created_at')


class TweetManager(models.Manager):
    """
    Custom model manager for 'Tweet'
    """

    def get_queryset(self):
        return TweetQuerySet(self.model, using=self._db)

    def get_tweets_in_ids(self, list_of_tweet_ids):
        return self.get_queryset().get_tweets_in_ids(list_of_tweet_ids)
