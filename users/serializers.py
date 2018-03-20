from rest_framework import serializers

from users.models import User


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
