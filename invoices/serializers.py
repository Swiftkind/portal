from rest_framework import serializers
from invoices.models import Invoice, Item
from customers.serializers import CustomerSerializer
from customers.models import Customer


class InvoiceSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id','code','order_id','invoice_date','terms','due_date',
                  'notes','conditions','status','items','total_amount','customer')

    def get_items(self, obj):
        serializer = ItemSerializer(Item.objects.filter(invoice=obj), many=True)
        return serializer.data

    def get_customer(self, obj):
        serializer = CustomerSerializer(Customer.objects.get(email=obj.customer.email))
        return serializer.data


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id','invoice','details','quantity','rate','amount')
