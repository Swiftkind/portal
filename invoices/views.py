import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from invoices.mixins import Paginate
from invoices.models import Invoice, Item
from invoices.serializers import InvoiceSerializer, ItemSerializer


class InvoiceAPI(LoginRequiredMixin, ViewSet):
    """ Endpoint that manages invoice detail data
    """
    serializer_class = InvoiceSerializer

    def detail(self, *args, **kwargs):
        serializer = self.serializer_class(get_object_or_404(
          self.serializer_class.Meta.model, id=kwargs.get('inv_id')))

        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        invoice = get_object_or_404(Invoice, id=kwargs.get('inv_id'))
        serializer = self.serializer_class(data=self.request.data, instance=invoice)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)

    def delete(self, *args, **kwargs):
        invoice = get_object_or_404(Invoice, id=kwargs.get('inv_id'))
        invoice.delete()

        return Response(status=200)


class InvoicesAPI(LoginRequiredMixin, Paginate ,ViewSet):
    """ Endpoint that manages invoice data
    """
    serializer_class = InvoiceSerializer

    def list(self, *args, **kwargs):
        invoices = self.serializer_class.Meta.model.objects.all()
        data = self.paginate(invoices)

        return Response(data, status=200)

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def terms(self, *args, **kwargs):
        terms = json.dumps(self.serializer_class.Meta.model.TERMS)

        return Response(json.loads(terms))

    def latest(self, *args, **kwargs):
        serializer = self.serializer_class(
                self.serializer_class.Meta.model.objects.order_by('date_created').last())

        return Response(serializer.data)


class ItemsAPI(LoginRequiredMixin, ViewSet):
    """ Add item in invoice
    """
    serializer_class = ItemSerializer

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)


class ItemAPI(LoginRequiredMixin, ViewSet):
    """ Detail of item
    """
    serializer_class = ItemSerializer

    def update(self, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs.get('item_id'))
        serializer = self.serializer_class(data=self.request.data, instance=item)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)
