from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(LoginRequiredMixin, viewsets.ViewSet):
    """ User profile viewset
    """
    def users_detail(self, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update_users(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user, data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
