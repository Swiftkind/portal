from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from users.serializers import (
                        LoginSerializer,
                        UserSerializer,
                        UpdateUserSerializer,
                    )
from users.models import User


class UserAPI(LoginRequiredMixin, ViewSet):
    """ User profile viewset.
    """
    def detail(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = UpdateUserSerializer(self.request.user, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class AuthAPI(ViewSet):
    """ Auth API for user
    """
    def login(self, *args, **kwargs):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        login(self.request, serializer.user_cache)
        serializer = UserSerializer(serializer.user_cache)
        return Response(serializer.data, status=200)

    def logout(self, *args, **kwargs):
        logout(self.request)
        return Response(status=200)
