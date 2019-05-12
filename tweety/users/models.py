# django imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

# project imports
from tweety_utils.model_utils import RowInformation

# app imports
from users.managers import UserManager


class User(RowInformation, AbstractUser):
    first_name = models.CharField(max_length=140, null=False, blank=False)
    last_name = models.CharField(max_length=140, null=False, blank=False)
    username = models.CharField(max_length=140, null=False, blank=False, unique=True, validators=[UnicodeUsernameValidator])
    email = models.CharField(max_length=140, null=False, blank=False, unique=True)
    profile_pic = models.URLField(null=True, blank=True)
    following = models.ManyToManyField(to='User', related_name='followed_by')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    objects = UserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Tweet(RowInformation):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='tweet')
    text = models.CharField(max_length=140, blank=False, null=False)

    def save(self, *args, **kwargs):
        super(Tweet, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.text)
