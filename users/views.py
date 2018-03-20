from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserAPI(LoginRequiredMixin, viewsets.ViewSet):
    """ User profile viewset
    """
    def detail(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
