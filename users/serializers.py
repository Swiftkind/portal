from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer
    """
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'image',
        )
    read_only_fields = ('image', 'last_name')


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}
        )

    def validate(self, *args):
        email = self.initial_data.get('email')
        password = self.initial_data.get('password')


        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid Email or Password.')
        return self.initial_data

