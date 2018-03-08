from django.urls import path
from invoices.api import InvoiceDetailView


urlpatterns = [
    path('invoice/<int:id>/', InvoiceDetailView.as_view(), name='invoice-detail')
]