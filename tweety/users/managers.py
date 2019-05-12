from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom model manager for User model
    """

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
