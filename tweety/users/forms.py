# django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# app imports
from users.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields