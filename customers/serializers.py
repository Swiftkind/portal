from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('first_name','last_name','company','email','billing_address',)
