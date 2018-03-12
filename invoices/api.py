from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class InvoiceDetailView(LoginRequiredMixin, APIView):
    """ Show the detail of selected invoice
    """
    def get(self, request, id, format=None):
        invoice = get_object_or_404(Invoice, id=id)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
