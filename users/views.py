from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from users.serializers import LoginSerializer
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


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

