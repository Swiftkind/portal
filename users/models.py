from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Manage user
    """
    def _create_user(self, email, first_name, last_name, password, **kwargs):
        # Create usera
        if not email:
            raise ValueError('The given Email must be set')
        email = self.normalize_email(email)
        first_name = first_name
        last_name = last_name
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            **kwargs,
        )
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, first_name, last_name, password, **kwargs):
        # Set default for user
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', False)

        return self._create_user(email, first_name, last_name, password, **kwargs)

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        # Set default for superuser
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        return self._create_user(email, first_name, last_name, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """ User information
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    is_active = models.BooleanField(_('activate'), default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        # String  representation of the user model

        return f"{self.email}"

    def get_full_name(self):
        # User full name

        return f"{self.first_name} {self.last_name}"
