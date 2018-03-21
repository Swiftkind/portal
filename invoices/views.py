from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from invoices.models import Invoice
from invoices.mixins import PaginationMixin 
from invoices.serializers import InvoiceSerializer


class InvoicesViewset(LoginRequiredMixin, PaginationMixin, ViewSet):
    """ View for adding new invoice and gets the list of all invoices
    """

    def list(self, *args, **kwargs):
        """ Response invoices
        """
        queryset = Invoice.objects.all()
        if queryset:
            page = self.paginate_queryset(queryset, self.request)
            serializer = InvoiceSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return Response(status=200)

