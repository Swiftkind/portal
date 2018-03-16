from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from invoices.models import Invoice
from customers.models import Customer
from invoices.serializers import InvoiceSerializer


class InvoiceAPI(LoginRequiredMixin, APIView):
    """ Show the detail of selected invoice and for editing invoice
    """
    def get(self, request, id, format=None):
        invoice = get_object_or_404(Invoice, id=id)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        invoice = get_object_or_404(Invoice, id=id)
        serializer = InvoiceSerializer(invoice, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoicesAPI(LoginRequiredMixin, APIView):
    """ View for adding new invoice and gets the list of all invoices
    """
    def get(self, request, format=None):
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
