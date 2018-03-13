from django.urls import path
from invoices.api import InvoiceDetailView


urlpatterns = [
    path('invoices/<int:id>/', InvoiceDetailView.as_view(), name='invoice_detail')
]