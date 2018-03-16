from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    """ Manage user
    """
    def create_user(self, email, password, **kwargs):
        """ Set default for user
        """
        user = self.model(email=email, is_active=True, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        """ Set default for superuser
        """
        return self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):
    """ User information
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    image = models.ImageField('Profile picture', upload_to='profiles', blank=True, null=True)

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
