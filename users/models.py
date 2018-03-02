from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    """Manage user
    """
    def create_user(self, email, first_name, last_name, password):
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """ Creates superuser
        """
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_active = True,
            is_staff = True,
            is_superuser = True,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


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

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        """ String  representation of the user model
        """
        return f"{self.email}"

    def get_full_name(self):
        """ User full name
        """
        return f"{self.first_name} {self.last_name}"
