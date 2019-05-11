# django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

# project imports
from tweety_utils.model_utils import RowInformation

# app imports
from users.managers import UserManager


class User(RowInformation, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=140, null=False, blank=False)
    last_name = models.CharField(max_length=140, null=False, blank=False)
    username = models.CharField(max_length=140, null=False, blank=False, unique=True, validators=[UnicodeUsernameValidator])
    email = models.CharField(max_length=140, null=False, blank=False, unique=True)
    profile_pic = models.URLField(null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    objects = UserManager()

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
