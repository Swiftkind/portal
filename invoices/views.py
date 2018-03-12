from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from invoices.models import Invoice


class InvoiceView(LoginRequiredMixin, TemplateView):
    """ View for invoice model
    """
    template_name = 'invoices/invoice_list.html'

    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        return render(self.request, self.template_name, {'invoices':invoices})
