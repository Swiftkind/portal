from rest_framework import serializers
from invoices.models import Invoice, Item


class InvoiceSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id','code','order_id','invoice_date','terms','due_date',
                  'notes','conditions','status','items')

    def get_items(self, obj):
        serializer = ItemSerializer(Item.objects.filter(invoice=obj), many=True)
        return serializer.data


class ItemSerializer(serializers.ModelSerializer):

    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id','invoice','details','quantity','rate','total_amount')

    def get_total_amount(self, obj):
        return obj.quantity * obj.rate