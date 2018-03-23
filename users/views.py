from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from users.serializers import LoginSerializer, UserSerializer



class UserAPI(LoginRequiredMixin, ViewSet):
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


class LoginAPI(ViewSet):
    """ Login viewset. 
    """
    def post(self, *args, **kwargs):
        serializer = LoginSerializer(data=self.request.data)

        if serializer.is_valid(raise_exception=True):
            return Response(token, status=200)

        return Response(serializer.errors, status=400)