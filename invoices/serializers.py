from rest_framework import serializers
from invoices.models import Invoice, Item


class InvoiceSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id','code','order_id','invoice_date','terms','due_date',
                  'notes','conditions','date_created','date_updated','status',
                  'items')

    def get_items(self, obj):
        serializer = ItemSerializer(Item.objects.filter(invoice=obj), many=True)
        return serializer.data


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id','invoice','details','quantity','rate')