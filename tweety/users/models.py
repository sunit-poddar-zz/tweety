# django imports
from django.db import models

# project imports
from tweety.tweety_utils.model_utils import RowInformation


class User(RowInformation):
    first_name = models.CharField(max_length=140, null=False, blank=False)
    last_name = models.CharField(max_length=140, null=False, blank=False)
    username = models.CharField(max_length=140, null=False, blank=False, unique=True)
    email = models.CharField(max_length=140, null=False, blank=False, unique=True)
    profile_pic = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)


class Follows(RowInformation):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='follows')
    followers = models.ManyToManyField(to=User, related_name='followers')

    def save(self, *args, **kwargs):
        super(Follows, self).save(*args, **kwargs)


class Tweet(RowInformation):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='tweet')
    text = models.CharField(max_length=140, blank=False, null=False)

    def save(self, *args, **kwargs):
        super(Tweet, self).save(*args, **kwargs)
