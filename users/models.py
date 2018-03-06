from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    """ Manage user
    """
    def _create_user(self, email, password, **extra_fields):
        """ save user account using email and password
        """
        if not email:
            raise ValueError('The given Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        """ sets the defaults for user account
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **kwargs):
        """ Set default for superuser
        """
        return self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):
    """ User information
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ('first_name', 'last_name')
    USERNAME_FIELD = 'email'

    def __str__(self):
        """ String  representation of the user model
        """
        return f"{self.email}"

    def get_full_name(self):
        """ User full name
        """
        return f"{self.first_name} {self.last_name}"
